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
from dueros.Nlu import Nlu
reload(sys)
sys.setdefaultencoding('utf-8')

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
        self.assertEqual(self.request.get_data(), self.data)

    def testGetNlu(self):
        '''
        测试getNlu方法
        :return:
        '''
        nlu = Nlu(self.data['request']['intents'])
        self.assertEqual(self.request.get_nlu().to_directive(), nlu.to_directive())


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

        self.assertEqual(self.request.get_type(), 'IntentRequest')

    def testGetUserId(self):
        '''
        测试getUserId方法
        :return:
        '''

        self.assertEqual(self.request.get_user_id(), 'userId')

    def testGetQuery(self):
        '''
        测试getQuery方法
        :return:
        '''

        self.assertEqual(self.request.get_query(), '所得税查询')

    def testIsLaunchRequest(self):
        '''
        测试isLaunchRequest方法
        :return:
        '''

        self.assertFalse(self.request.is_launch_request())

    def testIsSessionEndRequest(self):
        '''
        测试isSessionEndRequest方法
        :return:
        '''

        self.assertFalse(self.request.is_session_end_request())

    def testIsSessionEndedRequest(self):
        '''
        测试isSessionEndedRequest方法
        :return:
        '''

        self.assertFalse(self.request.is_session_ended_request())


    def testGetBotId(self):
        '''
        测试getBotId方法
        :return:
        '''

        self.assertEquals(self.request.get_bot_id(), 'botId')

    def testIsDialogStateCompleted(self):
        '''
        测试isDialogStateCompleted方法
        :return:
        '''
        self.assertFalse(self.request.is_dialog_state_completed())


    pass


if __name__ == '__main__':
    pass