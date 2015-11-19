#!/usr/bin/env python

from json import loads, dumps
from requests import get, codes
from os import sep, path
from urlparse import urlunparse
from ipso import IPSO_OBJECTS as ipso
import time


class LeshanPoller(object):
    '''
	Retrieves an information from lwm2m server
	and applies some filtering
    '''
    __slots__ = ["_LeshanPoller__data", "ignore_obj", "device"]

    scheme = "http"
    api_url = "api/clients"
    cfg = "leshan.cfg"

    def __init__(self):
        # ipso device id
        self.device = 3
	self.__data = []
        self.ignore_obj = self.get_except_obj()
	self.get_data()

    def init_urls(self, input):
	"""
	    Init Leshan url
	"""
	url = []
	try:
	    service = loads(input)

	    parts = (self.scheme, ":".join((service["ServiceAddress"], str(service['ServicePort']))), self.api_url, "", "", "")
	    url.append(urlunparse(parts))
	except:
	    pass

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
		        values = object_values(url, device['endpoint'], object)
			if values:
                            self.update_metadata(values, device, object)
	                    self.__data.append(values)

    @staticmethod
    def get_ipso(obj_id):
	'''
	    Gets an IPSO object
	'''
	ipso_obj = ipso.get(obj_id)
	return ipso_obj if ipso_obj else ()

    @staticmethod
    def get_res_attr(res_id, attrib):
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

    def get_object_values(self, url, endpoint, obj):
	'''
	    Retrieves resources from lwm2m server
	    :param url - lwm2m url
	    :param endpoint - client name
	    :param obj - resource obj
	    :return json
	'''
	object_values = {}
	resources = []
        device_time = []
        dtime = None

        ipso_obj = self.get_ipso(obj['objectId'])
	if ipso_obj:
            instance_path = url + sep + endpoint + obj['url'] + sep

	    for res_id in ipso_obj['required']:
                # get device time
                if not dtime:
                    dtime = self._get_device_time(url + sep + endpoint)

	        request_url = instance_path + str(res_id)
                resource = self._get_resource(request_url)
                if resource:
                    res_attribs = self.get_res_attr(res_id, ipso_obj['attrib'])
                    resource['title'] = res_attribs['description']
	            resources.append(resource)
	    else:
	        if resources:
		    object_values['resources'] = resources
		    object_values['title'] = ipso_obj['title']
                    object_values['time'] = dtime


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

    def _get_device_time(self, path):
        '''
            Gets a device time
            If device does not support a time callback
            to get local time
            :param path - url to the time resource
            :return timestamp - int, in nanosec
        '''
        nano = 10**9
        timestamp = None
        # gets device time and utc offset (13 and 14 respectively)
        values = []
        instance_url = '/%s/%s/' % (str(self.device), '0')
        for res_id in ('13', '14'):
            resource = self._get_resource(path + instance_url + res_id)
            if resource:
                values.append(resource.get('value'))
        else:
            if values:
                # device time
                timestamp = self._to_timestamp(values) * nano
            else:
                # local time
                timestamp = int(time()) * nano

        return timestamp

    @staticmethod
    def _to_timestamp(dtime):
        '''
            Converts date to timestamp
            :param dtime - tuple (date, utc_offset)
            :return int
        '''
        date_time, offset = dtime
        sec = int(time.mktime(time.strptime(date_time, '%Y-%m-%dT%H:%M:%SZ')))
        delta = (int(offset[-5:-3]) * 60 + int(offset[-2:])) * 60

        if offset[0] == '-':
            delta = -delta

        return sec + delta

    def _get_resource(self, path):
        '''
            Retrieves particular resource
            by path
            :param path - resource path
            :return json
        '''
        content = None
        try:
            response = get(path)
            if response and response.status_code == codes.ok:
                response = loads(response.text)
                if response:
                    content = response.get('content')
        except:
            pass

        return content

if __name__ == "__main__":
    print LeshanPoller()


