#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/7/20

"""
    desc:pass
"""
import unittest
from dueros.directive.Display.Hint import Hint


class HintTest(unittest.TestCase):
    '''
    测试Hint
    '''

    def setUp(self):
        self.hint1 = Hint(['hint1'])
        self.hint2 = Hint(['hint1', 'hint2'])

    def testGetData(self):
        '''
        测试getData
        :return:
        '''
        data1 = {
            'type': 'Hint',
            'hints':[
                {
                    'type':'PlainText',
                    'text': 'hint1'
                }
            ]
        }

        self.assertEqual(self.hint1.get_data(), data1)

        data2 = {
            'type': 'Hint',
            'hints': [
                {
                    'type': 'PlainText',
                    'text': 'hint1'
                },{
                    'type': 'PlainText',
                    'text': 'hint2'
                }
            ]
        }
        self.assertEqual(self.hint2.get_data(), data2)

    pass


if __name__ == '__main__':
    pass