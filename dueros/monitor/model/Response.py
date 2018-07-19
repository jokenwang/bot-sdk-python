#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/1/3
"""
    desc:pass
"""

from dueros.monitor.Utils import Utils
import json


class Response:

    def __init__(self, response_data):
        if not isinstance(response_data, dict):
            response_data = json.loads(response_data)
        self.data = response_data

    def get_output_speech(self):
        if Utils.checkKeysInDict(self.data, ['response', 'outputSpeech']):
            return self.data['response']['outputSpeech']

    def get_should_end_session(self):
        if Utils.checkKeysInDict(self.data, ['response', 'shouldEndSession']):
            return self.data['response']['shouldEndSession']
        pass

    def get_slot_name(self):

        if Utils.checkKeysInDict(self.data, ['response', 'directives']):
            directive = self.data['response']['directives']
            if directive and Utils.checkKeysInDict(directive[0], ['slotToElicit']):
                return directive[0]['slotToElicit']
        return None

    def get_reprompt(self):

        if Utils.checkKeysInDict(self.data, ['response', 'reprompt', 'outputSpeech']):
            return self.data['response']['reprompt']['outputSpeech']
        return None

if __name__ == '__main__':
    pass
