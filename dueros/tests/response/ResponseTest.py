#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/7/16

"""
    desc:pass
"""
import unittest
import json
import sys
from dueros.Request import Request
from dueros.Response import Response
from dueros.card.TextCard import TextCard
reload(sys)
sys.setdefaultencoding('utf-8')


class ResponseTest(unittest.TestCase):

    def setUp(self):
        with open('../json/intent_request.json') as f:
            self.requestData = f.read()
        print(self.requestData)
        self.requestData = json.loads(self.requestData.encode('utf-8'))
        self.request = Request(self.requestData)
        self.session = self.request.getSession()
        self.nlu = self.request.getNlu()
        self.response = Response(self.request, self.session, self.nlu)

    def testSetShouldEndSession(self):
        '''
        测试setShouldEndSession方法
        :return: 
        '''
        self.response.setShouldEndSession(False)
        ret = {}
        result = self.response.build(ret)
        shouldEndSession = result['response']['shouldEndSession']
        self.assertFalse(shouldEndSession)

    def testDefaultResult(self):
        '''
        测试defaultResult方法
        :return:
        '''
        self.assertEquals(self.response.defaultResult(), {"status":0,"msg":''})

    def testBuild(self):
        '''
        测试build方法
        :return:
        '''

        self.response.setShouldEndSession(False)
        card = TextCard("测试服务");
        ret = {
            'card': card,
            'outputSpeech': '测试服务，欢迎光临'
        }
        json = self.response.build(ret)

        rt = {"version":"2.0","context":{"intent":{"name":"intentName","score":100,"confirmationStatus":"NONE","slots":{"city":{"name":"city","value":"北京","score":0,"confirmationStatus":"NONE"}}}},"session":{"attributes":{}},"response":{"directives":[],"shouldEndSession":False,"card":{"type":"txt","content":"测试服务"},"resource":None,"outputSpeech":{"type":"PlainText","text":"测试服务，欢迎光临"},'reprompt': {'outputSpeech': None}}}
        self.assertEquals(json, rt)

    def testFormatSpeech(self):
        '''
        测试formatSpeech方法
        :return:
        '''

        outputSpeech = '测试服务，欢迎光临';
        rt = {
            'type': 'PlainText',
            'text': '测试服务，欢迎光临'
        }
        formatSpeech = self.response.formatSpeech(outputSpeech);
        self.assertEquals(formatSpeech, rt)


    def testSetNeedDetermine(self):
        '''
        测试setNeedDetermine方法
        :return:
        '''

        self.response.setNeedDetermine()
        json = self.response.build({})
        print(json)
        rt = {"version":"2.0","context":{"intent":{"name":"intentName","score":100,"confirmationStatus":"NONE","slots":{"city":{"name":"city","value":"北京","score":0,"confirmationStatus":"NONE"}}}},"session":{"attributes":{}},"response":{"directives":[],"shouldEndSession":True,"card":None,"resource":None,"outputSpeech":None,"reprompt": {"outputSpeech": None},"needDetermine":True}}
        self.assertEquals(json, rt)


    def testSetExpectSpeech(self):
        '''
        测试setFormatSpeech方法
        :return:
        '''

        self.response.setExpectSpeech(False)
        json = self.response.build({})
        rt = {"version":"2.0","context":{"intent":{"name":"intentName","score":100,"confirmationStatus":"NONE","slots":{"city":{"name":"city","value":"北京","score":0,"confirmationStatus":"NONE"}}}},"session":{"attributes":{}},"response":{"directives":[],"shouldEndSession":True,"card":None,"resource":None,"outputSpeech":None,"reprompt": {"outputSpeech": None},"expectSpeech":False}}
        self.assertEquals(json, rt)

        self.response.setExpectSpeech(True)
        json = self.response.build({})
        rt = {"version":"2.0","context":{"intent":{"name":"intentName","score":100,"confirmationStatus":"NONE","slots":{"city":{"name":"city","value":"北京","score":0,"confirmationStatus":"NONE"}}}},"session":{"attributes":{}},"response":{"directives":[],"shouldEndSession":True,"card":None,"resource":None,"outputSpeech":None,"reprompt": {"outputSpeech": None},"expectSpeech":True}}
        self.assertEquals(json, rt)

    def testSetFallBack(self):
        '''
        测试setFallBack方法
        :return:
        '''
        self.response.setFallBack()
        json = self.response.build({})
        rt = {"version":"2.0","context":{"intent":{"name":"intentName","score":100,"confirmationStatus":"NONE","slots":{"city":{"name":"city","value":"北京","score":0,"confirmationStatus":"NONE"}}}},"session":{"attributes":{}},"response":{"directives":[],"shouldEndSession":True,"card":None,"resource":None,"outputSpeech":None,"reprompt": {"outputSpeech": None},"fallBack":True}}
        self.assertEquals(json, rt)

    pass


if __name__ == '__main__':
    pass