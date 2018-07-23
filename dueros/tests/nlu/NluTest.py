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
            'name': self.nlu.get_intent_name(),
            'slots': self.data[0]['slots']
        }

    def test_getslot(self):
        '''
        测试getSlot方法
        :return:
        '''
        self.assertEqual(self.nlu.get_slot('city'), '北京')


    def test_getslotconfirmationstatus(self):
        '''
        测试getSlotConfirmationStatus方法
        :return:
        '''
        self.assertEqual(self.nlu.get_slot_confirmation_status('city'), 'NONE')

    def test_getintentconfirmationstatus(self):
        '''
        测试getIntentConfirmationStatus方法
        :return:
        '''
        self.assertEqual(self.nlu.get_intent_confirmation_status(), 'NONE')


    def test_getintentname(self):
        '''
        测试getIntentName方法
        :return:
        '''
        self.assertEqual(self.nlu.get_intent_name(), 'intentName')


    def test_getupdateintent(self):
        '''
        测试getUpdateIntent方法
        :return:
        '''
        updateIntent = {
            'name': self.nlu.get_intent_name(),
            'slots': self.data[0]['slots']
        }
        self.assertEqual(self.updateIntent, updateIntent)

    def test_ask(self):
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
        self.assertEqual(self.nlu.to_directive(), directive)


    def test_setslot(self):
        '''
        测试setSlot方法
        :return:
        '''
        self.nlu.set_slot('monthsalary', 1212)
        self.assertEqual(self.nlu.get_slot('monthsalary'), 1212)

    def test_setdelegate(self):
        '''
        测试setDelegate方法
        :return:
        '''
        self.nlu.set_delegate()
        directive = {
            'type': 'Dialog.Delegate',
            'updatedIntent': self.updateIntent
        }
        self.assertEqual(self.nlu.to_directive(), directive)



    def test_setconfirmslot(self):
        '''
        测试setConfirmSlot方法
        :return:
        '''
        self.nlu.set_confirm_slot('city')
        directive = {
            'type': 'Dialog.ConfirmSlot',
            'slotToConfirm': 'city',
            'updatedIntent': self.updateIntent
        }
        self.assertEqual(self.nlu.to_directive(), directive)


    def testSetConfirmIntent(self):
        '''
        测试setConfirmIntent方法
        :return:
        '''

        self.nlu.set_confirm_intent()
        directive = {
            'type': 'Dialog.ConfirmIntent',
            'updatedIntent': self.updateIntent
        }
        self.assertEqual(self.nlu.to_directive(), directive)



    pass



if __name__ == '__main__':
    pass


