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
from dueros.Request import Request
from dueros.Nlu import Nlu
class IntentRequestTest(unittest.TestCase):

    def setUp(self):
        with open('../json/intent_request.json') as f:

            self.data = f.read()
        self.data = json.loads(self.data)
        self.request = Request(self.data)

    def testGetData(self):
        '''
        测试getData方法
        :return:
        '''
        self.assertEqual(self.request.getData(), self.data)

    def testGetNlu(self):
        '''
        测试getNlu方法
        :return:
        '''
        nlu = Nlu(self.data['request']['intents'])
        self.assertEqual(self.request.getNlu(), nlu)


    def testGetAudioPlayerContext(self):
        '''
        测试getAudioPlayerContext方法
        :return:
        '''
        pass

    def testGetType(self):
        '''
        测试getType方法
        :return:
        '''

        self.assertEqual(self.requestgetType(), 'IntentRequest')

    def testGetUserId(self):
        '''
        测试getUserId方法
        :return:
        '''

        self.assertEqual(self.requestgetUserId(), 'userId')

    def testGetQuery(self):
        '''
        测试getQuery方法
        :return:
        '''

        self.assertEqual(self.request.getQuery(), '所得税查询')

    def testIsLaunchRequest(self):
        '''
        测试isLaunchRequest方法
        :return:
        '''

        self.assertFalse(self.request.isLaunchRequest())

    def testIsSessionEndRequest(self):
        '''
        测试isSessionEndRequest方法
        :return:
        '''

        self.assertFalse(self.request.isSessionEndRequest())

    def testIsSessionEndedRequest(self):
        '''
        测试isSessionEndedRequest方法
        :return:
        '''

        self.assertFalse(self.request.isSessionEndedRequest())


    def testGetBotId(self):
        '''
        测试getBotId方法
        :return:
        '''

        self.assertEquals(self.request.getBotId(), 'botId')

    def testIsDialogStateCompleted(self):
        '''
        测试isDialogStateCompleted方法
        :return:
        '''
        self.assertFalse(self.request.isDialogStateCompleted())


    pass


if __name__ == '__main__':
    pass