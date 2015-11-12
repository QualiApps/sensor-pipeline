#!/usr/bin/env python

from sys import exit, argv
from json import loads, dumps
from ipso import IPSO_OBJECTS as ipso
from syslog import syslog, LOG_ERR


class FilterIPSO(object):
    def __init__(self, raw_data):
	self.__data = []
	self.raw_data = raw_data
	self.process(self.raw_data['objectId'])

    def process(self, id):
	'''
	    Data processing
	    :param id - the object id
	'''
	object_info = ipso.get(id)
	if object_info:
	    self.filtering(object_info)

    def filtering(self, obj):
	'''
	    Updates incoming content
	    :param obj - object info
	'''
	requered_res = []
        raw_resources = self.get_resources()
        for resource in raw_resources:
            if resource['id'] in obj['required']:
		res_attribs = self.get_obj_attr(resource['id'], obj['attrib'])
		resource['title'] = res_attribs['description']
		requered_res.append(resource)
	else:
	    if requered_res:
		data = self.set_resources(requered_res)
		data['title'] = obj.get('title')
	    else:
		data = ''
	    self.__data = data

    @staticmethod
    def get_obj_attr(res_id, attrib):
	'''
	    Finds particular resource
	    :param res_id - id resource
	    :param attrib - available resources
	    :return dict
	'''
	response = None
	for attr in attrib:
	    if int(attr['id']) == res_id:
		response = attr
		break

	return response

    def get_resources(self):
	'''
	    Retrieves resources from object
	    :return list
	'''
	return self.raw_data.get('content').get('resources')

    def set_resources(self, res):
	'''
	    Sets new resources
	    :param res - requered resources
	    :return json
	'''
        self.raw_data['content']['resources'] = res
	return self.raw_data

    @property
    def data(self):
	'''
	    Dumps data to json
	'''
	return dumps(self.__data)

    def __str__(self):
	return self.data


if __name__ == '__main__':
    try:
        input_data = loads(raw_input())
        print FilterIPSO(input_data)
    except Exception as error:
	syslog(LOG_ERR, "Resource filtering: " + str(error))

