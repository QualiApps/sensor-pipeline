#!/usr/bin/env python

from json import loads, dumps
from requests import get, codes
from os import sep, path
from urlparse import urlunparse


class LeshanPoller(object):
    __slots__ = ["_LeshanPoller__data", "ignore_obj"]

    scheme = "http"
    api_url = "api/clients"
    cfg = "leshan.cfg"

    def __init__(self):
	self.__data = []
        self.ignore_obj = self.get_except_obj()
	self.get_data()

    def init_urls(self, input):
	"""
	    Init Leshan url
	"""
	url = []
	service = loads(input)
	
	parts = (self.scheme, ":".join((service["ServiceAddress"], str(service['ServicePort']))), self.api_url, "", "", "")
	url.append(urlunparse(parts))
	
	return url

    def get_data(self):
	'''
	   Retrieves lwm2m resources
	   depends on a config file - leshan.cfg
	'''
	urls = self.init_urls(raw_input())
        leshan_instances = self.get_leshan_instance
	object_values = self.get_object_values
	for url, devices in leshan_instances(urls):
	    for device in devices:
	        for object in device['objectLinks']:
		    if str(object['objectId']) not in self.ignore_obj:
		        values = object_values(url, device['endpoint'], object['url'])
                        self.update_metadata(values, device, object)
	                self.__data.append(values)

    @staticmethod
    def get_leshan_instance(urls):
	'''
	    Retrieves devices from lwm2m server
	    :param urls - lwm2m servers
	    :return json
	'''
	for url in urls:
            response = get(url)
	    if response.status_code == codes.ok:
	        yield url, loads(response.text)

    @staticmethod
    def get_object_values(url, endpoint, obj_url):
	'''
	    Retrieves resources from lwm2m server
	    :param url - lwm2m url
	    :param endpoint - client name
	    :param obj_url - resource path (/object_id/instance_id)
	    :return json
	'''
	object_values = None

	request_url = url + sep + endpoint + obj_url
        response = get(request_url)

        if response.status_code == codes.ok:
            object_values = loads(response.text)

	return object_values

    @staticmethod
    def update_metadata(values, device, object):
	'''
	    Update metadata to the response content
	    :param values - response content
	    :param device - device info
	    :param object - object info
	'''
	values['endpoint'] = device['endpoint']
	values['registrationId'] = device['registrationId']
	values['registrationDate'] = device['registrationDate']
	values['objectId'] = object['objectId']
	values['objectInstanceId'] = object['objectInstanceId']
	del values['status']

    @property
    def data(self):
	return dumps(self.__data)

    def __str__(self):
	return self.data

    def get_except_obj(self):
	'''
	    Retrieves object ids from config file
	    poller must ignore these items
	    :return list
	'''
	ids = []
	import ConfigParser
        config = ConfigParser.ConfigParser()
	script_path = path.dirname(path.realpath(__file__))
        config.read(sep.join((script_path, self.cfg)))
        except_ids = config.get('Except', 'ObjectIds', None)
        if except_ids:
            ids = except_ids.split(',')

	return ids
	

if __name__ == "__main__":
    print LeshanPoller()


