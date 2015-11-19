#!/usr/bin/env python

from sys import argv
from json import loads
from syslog import syslog, LOG_ERR


class InfluxDB(object):
    def __init__(self):
	self.__data = []

    def create(self, in_data):
	raw_resources = in_data.get('resources')
	for resource in raw_resources:
	    tags = {
	        "endpoint": in_data.get('endpoint'),
	        "object_id": in_data.get('objectId'),
	        "instance_id": in_data.get('objectInstanceId'),
	        "resource_id": resource.get('id'),
	        "resource_title": self.convert_name(resource.get('title'))
	    }
	    values = {
	        "value": resource.get('value', 0)
	    }
	    point = self.format_to_line(
	        	self.convert_name(in_data.get('title')),
			tags,
			values,
			in_data.get('time')
		    )

	    self.__data.append(point)

        return self.data

    @property
    def data(self):
	return "\n".join(self.__data)

    def format_to_line(self, measurement, tags, values, timestamp):
	return '%s%s %s %s' % (measurement, ',' + self.dict_to_line(tags) if tags else '', self.dict_to_line(values), timestamp)

    @staticmethod
    def dict_to_line(items):
	return ','.join(['%s=%s' % (k,v) for k,v in items.iteritems()])

    @staticmethod
    def convert_name(name):
	return name.lower().replace(" ", "_")


class OutputStream(object):
    def __init__(self, construct, input_data):
	self.out = construct()
	self.in_data = input_data

    def output(self):
	return self.out.create(self.in_data)

if __name__ == "__main__":
    if len(argv) == 2:
	try:
  	    construct = globals().get(argv[1])
	    if construct:
	        input_data = raw_input()
	        print OutputStream(construct, loads(input_data)).output()
	except Exception as error:
	    syslog(LOG_ERR, "OutputStream processing: " + str(error))

