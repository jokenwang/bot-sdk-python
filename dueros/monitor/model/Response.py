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
        return Utils.getDictDataByKeys(self.data, ['response', 'outputSpeech'])

    def getShouldEndSession(self):
        return Utils.getDictDataByKeys(self.data, ['response', 'shouldEndSession'])


    def getSlotName(self):

        if Utils.checkKeysInDict(self.data, ['response', 'directives']):
            directive = self.data['response']['directives']
            if directive and directive[0]['slotToElicit']:
                return directive[0]['slotToElicit']
        return None


    def getReprompt(self):

        return Utils.getDictDataByKeys(self.data, ['response', 'reprompt', 'outputSpeech'])

if __name__ == '__main__':
    pass
