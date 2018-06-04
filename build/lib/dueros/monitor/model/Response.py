#!/usr/bin/env python3
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

    def __init__(self, responseData):
        if isinstance(responseData, str):
            responseData = json.loads(responseData)
        self.data = responseData

    def getOutputSpeech(self):
        if Utils.checkKeysInDict(self.data, ['response', 'outputSpeech']):
            return self.data['response']['outputSpeech']

    def getShouldEndSession(self):
        if Utils.checkKeysInDict(self.data, ['response', 'shouldEndSession']):
            return self.data['response']['shouldEndSession']
        pass


    def getSlotName(self):

        if Utils.checkKeysInDict(self.data, ['response', 'directives']):
            directive = self.data['response']['directives']
            if directive and directive[0]['slotToElicit']:
                return directive[0]['slotToElicit']
        return None


    def getReprompt(self):

        if Utils.checkKeysInDict(self.data, ['response', 'reprompt', 'outputSpeech']):
            return self.data['response']['reprompt']['outputSpeech']
        return None

if __name__ == '__main__':
    pass
