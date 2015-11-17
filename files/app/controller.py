#!/usr/bin/env python

from json import loads, dumps
from os import sep, path
import operator


class Processor(object):
    '''
	Stream processing
    '''
    conf_path = "conf/threshold.json"
    script_path = path.dirname(path.realpath(__file__))
    status_success = "success"
    status_error = "error"

    def __init__(self):
	'''
	   Init rules
	'''
	self.resp_handlers = []
	self.conf_rules = self.get_config()

    def run(self, in_data):
	'''
	   Processing stream
	   :param in_data - input stream
	'''
	self.process(in_data)

    def process(self, stream):
	'''
	    Evaluate stream and create handlers
	    :param stream - input stream
	    :return None
	'''
	obj_id = stream.get("objectId")
	rules = self.get_obj(self.conf_rules, obj_id)
	try:
	    if rules:
		# if any rules are available
	        for resource in stream['resources']:
		    res_id = resource['id']
		    rule = self.get_obj(rules[str(obj_id)], res_id)
		    if rule:
			# if a particular rule
			rule = rule[str(res_id)]
			if self.threshold(rule, resource['value']):
			    # if an event happened
			    # build response
			    self.resp_handlers.append({
				"status": self.status_success,
				"object": obj_id,
				"instance": stream['objectInstanceId'],
				"resource": res_id,
				"current_value": resource['value'],
				"threshold": rule['value'],
				"handler": rule['handler'],
				"args": rule['args'].split(";") if rule['args'] else []
			    })
	except Exception as error:
	    self.add_error(error.__str__())

    def add_error(self, message):
	'''
	    Init errors
	    :param message - error message		 
	'''
	self.resp_handlers.append({
		"status": self.status_error, 
		"message": message
	})

    @staticmethod
    def get_obj(items, id):
	'''
	    Retrieves object (object | resource)
	    :param items - rules dict
	    :param id - key id (obj | res id)
	    :return list
	'''
	id = str(id) if type(id) is not str else id
	for item in items:
	    if item.get(id):
		break
	else:
	    item = None

	return item
	
    def threshold(self, rule, value):
	'''
	    Applies an operator and invokes action
	    :param rule - threshold
	    :param value - current resource value
	    :return True | False
	'''
	invoke = getattr(operator, rule.get("operator"))
	args = (value, rule.get("value"))
	return invoke(*args)

    def get_config(self):
	'''
	    Gets the rules
	    :return list of rules
	'''	
	config = []
	conf_file = sep.join((self.script_path, self.conf_path))

	if path.isfile(conf_file):
	    with open(conf_file) as conf:
	        config = conf.read()
	        config = loads(config) if config else []
	
	return config

    @property
    def handlers(self):
	'''
	    Process the response
	    :return json dump
	'''
	return dumps(self.resp_handlers)

    def __str__(self):
	return self.handlers


if __name__ == "__main__":
    try	:
	processor = Processor()
        stream = loads(raw_input())
	processor.run(stream)
    except Exception as error:
	processor.add_error(error.__str__())
    finally:
	print processor
