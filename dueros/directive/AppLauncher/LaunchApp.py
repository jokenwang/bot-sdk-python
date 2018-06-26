#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/1/2

from dueros.directive.BaseDirective import BaseDirective
import logging

class LaunchApp(BaseDirective):
    """
       用于调用app的指令类
    """

    def __init__(self, appName='', packageName='', deepLink=''):
        '''
        三者必须传一个
        :param appName:     应用名称
        :param packageName: 应用包
        :param deepLink:    打开应用指定功能
        '''

        super(LaunchApp, self).__init__('AppLauncher.LaunchApp')
        if not appName and not packageName and not deepLink:
            print('appName packageName deepLink 必须要有一个')
        else:
            self.data = dict({
                'appName': appName,
                'packageName': packageName,
                'deepLink': deepLink,
                'token': self.genToken()
            },**self.data)

    def setAppName(self, appName):

        if appName:
            self.data['appName'] = appName
        return self

    def setPackageName(self, packageName):

        if packageName:
            self.data['packageName'] = packageName
        return self

    def setDeepLink(self, deepLink):

        if deepLink:
            self.data['deepLink'] = deepLink
        return self

if __name__ == '__main__':

    launchApp = LaunchApp('', '', '2')
    launchApp.setDeepLink('dd')
    print(launchApp.data)

