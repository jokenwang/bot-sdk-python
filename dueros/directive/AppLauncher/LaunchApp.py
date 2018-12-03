#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/1/2
"""
用于调用app的指令类
"""

from dueros.directive.BaseDirective import BaseDirective
import logging


class LaunchApp(BaseDirective):
    """
    调用App指令
    """

    def __init__(self, app_name='', package_name='', deep_link=''):
        """
        三者必须传一个
        :param app_name:     应用名称
        :param package_name: 应用包
        :param deep_link:    打开应用指定功能
        """

        BaseDirective.__init__(self, 'AppLauncher.LaunchApp')
        if not app_name and not package_name and not deep_link:
            print('appName packageName deepLink 必须要有一个')
        else:
            self.data = dict({
                'appName': app_name,
                'packageName': package_name,
                'deepLink': deep_link,
                'token': self.gen_token()
            }, **self.data)

    def set_app_name(self, app_name):
        """
        设置应用名
        :param app_name:
        :return:
        """
        if app_name:
            self.data['appName'] = app_name
        return self

    def set_package_name(self, package_name):
        """
        设置应用包名
        :param package_name:
        :return:
        """
        if package_name:
            self.data['packageName'] = package_name
        return self

    def set_deep_link(self, deep_link):
        """
        设置功能名
        :param deep_link:
        :return:
        """
        if deep_link:
            self.data['deepLink'] = deep_link
        return self


if __name__ == '__main__':
    pass
