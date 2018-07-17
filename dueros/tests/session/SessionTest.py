#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/7/13

"""
    desc:pass
"""

import unittest
import json
from dueros.Session import Session

class SessionTest(unittest.TestCase):
    '''
    Session单元测试
    '''

    def setUp(self):
        with open('../json/intent_request.json') as f:
            self.data = f.read()
        self.session = Session(json.loads(self.data)['session'])

    def testSetData(self):

        self.session.setData('status', '1')
        ret = {
            'attributes':{
                'status': '1'
            }
        }

        self.assertEquals(self.session.toResponse(), ret)

    def testGetData(self):
        self.session.setData('status', '1')
        self.assertEquals(self.session.getData('status'), '1')
        # self.assertEquals(self.session.getData('status'), '2')
        pass


if __name__ == '__main__':
    pass