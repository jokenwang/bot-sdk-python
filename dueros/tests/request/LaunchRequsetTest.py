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
from dueros.Session import Session
reload(sys)
sys.setdefaultencoding('utf-8')


class LaunchRequsetTest(unittest.TestCase):

    def setUp(self):

        with open('../json/launch.json') as f:
            self.data = f.read()
        self.data = json.loads(self.data)

        self.request = Request(self.data)

    def testGetData(self):
        '''
        测试getData方法
        :return:
        '''
        self.assertEqual(self.request.get_data(), self.data)

    def testGetSession(self):

        session = Session(self.data['session'])
        self.assertEqual(self.request.get_session().to_response(), session.to_response())

    def testGetDeviceId(self):
        '''
        测试getDeviceId方法
        :return:
        '''

        self.assertEqual(self.request.get_device_id(), 'deviceId')

    def testGetUserInfo(self):
        '''
        测试getUserInfo方法
        :return:
        '''

        userInfo = {
            "account": {
                "baidu": {
                    "baiduUid": "baiduUid"
                }
            },
            "location": {
                "geo":{
                    "bd09ll":{
                        "longitude": 12.12,
                        "latitude": 34.12
                    },
                    "wgs84":{
                        "longitude": 12.12,
                        "latitude": 34.12
                    },
                    "bd09mc":{
                        "longitude": 111112.12,
                        "latitude": 322224.12
                    }
                }
            }
        }
        self.assertEqual(self.request.get_user_info(), userInfo)


    def testGetBaiduUid(self):
        '''
        测试getBaiduUid方法
        :return:
        '''

        self.assertEqual(self.request.get_baidu_uid(), 'baiduUid')

    def testGetType(self):
        '''
        测试getType方法
        :return:
        '''

        self.assertEquals(self.request.get_type(), 'LaunchRequest');

    def testGetUserId(self):
        '''
        测试getUserId方法
        :return:
        '''

        self.assertEqual(self.request.get_user_id(), 'userId')

    def testGetCuid(self):
        '''
        测试getCuid方法
        :return:
        '''
        self.assertEqual(self.request.get_cu_id(), 'cuid')

    def testGetAccessToken(self):
        '''

        :return:
        '''
        self.assertEqual(self.request.get_access_token(), 'access_token')
    pass


if __name__ == '__main__':
    pass