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
from dueros.Nlu import Nlu
reload(sys)
sys.setdefaultencoding('utf-8')

class NluTest(unittest.TestCase):

    def setUp(self):

        with open('../json/intent_request.json') as f:
            self.requestData = f.read()
        self.requestData = json.loads(self.requestData.encode('utf-8'))
        self.data = self.requestData['request']['intents']
        self.nlu = Nlu(self.data)

        self.updateIntent = {
            'name': self.nlu.getIntentName(),
            'slots': self.data[0]['slots']
        }

    def testGetSlot(self):
        '''
        测试getSlot方法
        :return:
        '''
        self.assertEqual(self.nlu.getSlot('city'), '北京')


    def testGetSlotConfirmationStatus(self):
        '''
        测试getSlotConfirmationStatus方法
        :return:
        '''
        self.assertEqual(self.nlu.getSlotConfirmationStatus('city'), 'NONE')

    def testGetIntentConfirmationStatus(self):
        '''
        测试getIntentConfirmationStatus方法
        :return:
        '''
        self.assertEqual(self.nlu.getIntentConfirmationStatus(), 'NONE')


    def testGetIntentName(self):
        '''
        测试getIntentName方法
        :return:
        '''
        self.assertEqual(self.nlu.getIntentName(), 'intentName')


    def testGetUpdateIntent(self):
        '''
        测试getUpdateIntent方法
        :return:
        '''
        updateIntent = {
            'name': self.nlu.getIntentName(),
            'slots': self.data[0]['slots']
        }
        self.assertEqual(self.updateIntent, updateIntent)

    def testAsk(self):
        '''
        测试ask方法
        :return:
        '''
        self.nlu.ask('location')
        directive = {
            'type': 'Dialog.ElicitSlot',
            'slotToElicit': 'location',
            'updatedIntent': self.updateIntent
        }
        self.assertEqual(self.nlu.toDirective(), directive)


    def testSetSlot(self):
        '''
        测试setSlot方法
        :return:
        '''
        self.nlu.setSlot('monthsalary', 1212)
        self.assertEqual(self.nlu.getSlot('monthsalary'), 1212)

    def testSetDelegate(self):
        '''
        测试setDelegate方法
        :return:
        '''
        self.nlu.setDelegate()
        directive = {
            'type': 'Dialog.Delegate',
            'updatedIntent': self.updateIntent
        }
        self.assertEqual(self.nlu.toDirective(), directive)



    def testSetConfirmSlot(self):
        '''
        测试setConfirmSlot方法
        :return:
        '''
        self.nlu.setConfirmSlot('city')
        directive = {
            'type': 'Dialog.ConfirmSlot',
            'slotToConfirm': 'city',
            'updatedIntent': self.updateIntent
        }
        self.assertEqual(self.nlu.toDirective(), directive)


    def testSetConfirmIntent(self):
        '''
        测试setConfirmIntent方法
        :return:
        '''

        self.nlu.setConfirmIntent()
        directive = {
            'type': 'Dialog.ConfirmIntent',
            'updatedIntent': self.updateIntent
        }
        self.assertEqual(self.nlu.toDirective(), directive)



    pass



if __name__ == '__main__':
    pass


