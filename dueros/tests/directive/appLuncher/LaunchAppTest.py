#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/7/13

"""
    desc:pass
"""
import unittest
from dueros.directive.AppLauncher.LaunchApp import LaunchApp

class LaunchAppTest(unittest.TestCase):

    '''
    LaunchApp单元测试
    '''

    def setUp(self):
        self.launchApp = LaunchApp('appName', 'packageName', 'deepLink')

        self.launchApp.setAppName('appName by set')
        self.launchApp.setDeepLink('deepLink by set')
        self.launchApp.setPackageName('packageName by set')
        self.launchApp.setToken('token by set')

    def testGetData(self):
        '''
        测试getData方法
        :return:
        '''
        ret = {
            'type': 'AppLauncher.LaunchApp',
            'appName': 'appName by set',
            'packageName': 'packageName by set',
            'deepLink': 'deepLink by set',
            'token': 'token by set'
        }

        data = self.launchApp.getData()

        self.assertEqual(data, ret)

if __name__ == '__main__':
    pass