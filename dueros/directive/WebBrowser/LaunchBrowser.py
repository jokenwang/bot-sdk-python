#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2017/12/31

from dueros.directive.BaseDirective import BaseDirective


class LaunchBrowser(BaseDirective):
    """
        用于调用浏览器指令的类
    """
    def __init__(self, url):

        super(LaunchBrowser, self).__init__('WebBrowser.LaunchBrowser')
        self.data['url'] = url
        self.data['token'] = self.getToken()

if __name__ == '__main__':
    pass
