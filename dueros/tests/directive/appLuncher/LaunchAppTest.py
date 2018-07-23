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

        self.launchApp.set_app_name('appName by set')
        self.launchApp.set_deep_link('deepLink by set')
        self.launchApp.set_package_name('packageName by set')
        self.launchApp.set_token('token by set')

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

        data = self.launchApp.get_data()
        self.assertEqual(data, ret)


if __name__ == '__main__':
    pass