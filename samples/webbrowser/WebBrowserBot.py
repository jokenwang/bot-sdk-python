#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/22

"""
    desc:pass
"""
from dueros.Bot import Bot
from dueros.directive.WebBrowser.LaunchBrowser import LaunchBrowser
from dueros.directive.Display.RenderTemplate import RenderTemplate
from dueros.directive.AppLauncher.LaunchApp import LaunchApp

class WebBrowserBot(Bot):

    def __init__(self, request_data):
        super(WebBrowserBot, self).__init__(request_data, '')
        self.add_launch_handler(self.handle_lanuncher)

    def handle_lanuncher(self):

        # template = LaunchBrowser('http://www.baidu.com')
        # directive = RenderTemplate(template)
        launcher = LaunchApp('浏览器','com.android.browser','')
        return {
            'outputSpeech':'欢迎使用',
            'directives': [launcher]

        }

        pass
    pass


if __name__ == '__main__':
    pass