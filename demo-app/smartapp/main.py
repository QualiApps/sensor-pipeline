#!/usr/bin/python

from os import sep
import argparse
from subprocess import call, Popen, PIPE
import requests
from json import loads, dumps


class Threshold(object):
    '''
        Deploy rules and handlers. Launch all processes.
    '''
    stream_path = "contentListener"
    schema = "http://"
    api_path = "nifi-api"
    group_path = "controller/process-groups/%s"

    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--rules", "-r", type=str, required=True, help="zip archive of rules (a json file)")
        parser.add_argument("--handlers", "-ha", type=str, required=True, help="zip archive of handlers (scripts or app)")
        parser.add_argument("--host", "-ip", type=str, required=True, help="IP address of a stream server")
        parser.add_argument("--port", "-p", type=str, default="8088", help="content listener port")
        parser.add_argument("--group", "-g", type=str, default="Sensor", help="The process group name")
        parser.add_argument("--api-port", "-ap", type=str, default="8090", help="nifi api port")

        self.opt = vars(parser.parse_args())
        self.__resp = ""
        self.upload()

    def upload(self):
        for archive in (self.opt['rules'], self.opt['handlers']):
            self.send(archive)
        else:
            # Run process group
            if self.start():
                self.__resp = "...........All processes were launched!"

    def start(self, run='true'):
        '''
            Start the processes
            :param (str) run - start flag (true|false)
            :return bool
        '''
        response = True
        # get a process group id
        group_id = self._get_group_by_name(self.opt['group'])
        # get last revision
        revision = self._get_revision()

        # run all processes
        # the first revision eq 0, but it's not our case
        if group_id and revision:
            data = {"running": run, "version": revision}
            res = requests.put(
                self._get_url(self.group_path % group_id),
                data=data
            )

            if res.status_code != requests.codes.ok:
                response = False

        return response

    def _get_revision(self):
        '''
            Retrieves a number of last revision
            :return int
        '''
        version = None
        res = requests.get(
            self._get_url('controller/revision')
        )

        if res.status_code == requests.codes.ok:
            revision = loads(res.text)
            version = revision['revision']['version']

        return version

    def _get_group_by_name(self, name):
        '''
            Gets group id by name
            :param name - the name of the group
            :return string
        '''
        group_id = None
        # retrieves all groups
        group_ref_path = "process-group-references"
        res = requests.get(
            self._get_url(sep.join((self.group_path % 'root', group_ref_path)))
        )

        if res.status_code == requests.codes.ok:
            groups = loads(res.text)
            for group in groups['processGroups']:
                if group['name'] == name:
                    group_id = group['id']
                    break

        return group_id

    def _get_url(self, path):
        '''
            Concatenate api url and path
            :param path - part of api
        '''
        return sep.join((self.nifi_api, path))

    def send(self, archive):
        call([
            'curl',
            '-X',
            'POST',
            self.stream,
            '--header',
            '"Content-Type: application/zip"',
            '--data-binary',
            '@' + archive]
        )

    @property
    def stream(self):
        '''
            Stream url, it use for upload archives
        '''
        return self.schema + sep.join((self.opt['host'] + ":" + self.opt['port'], self.stream_path))

    @property
    def nifi_api(self):
        '''
            Api url
        '''
        return self.schema + sep.join((self.opt['host'] + ":" + self.opt['api_port'], self.api_path))

    def __str__(self):
        return self.__resp

def run():
    print Threshold()

if __name__ == "__main__":
    run()
