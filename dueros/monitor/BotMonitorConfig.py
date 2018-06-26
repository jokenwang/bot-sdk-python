#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/1/3

"""
    desc:pass
"""


class BotMonitorConfig:

    @staticmethod
    def getHost():
        return 'dueros-api.baidu.com'

    @staticmethod
    def getUploadUrl():
        return 'https://dueros-api.baidu.com/uploadmonitordata'

    @staticmethod
    def getSdkVersion():
        return '1.0.0'

    @staticmethod
    def getSdkType():
        return 'python'

    @staticmethod
    def getUploadPort():
        return 443

    @staticmethod
    def getUploadPath():
        return '/uploadmonitordata'


if __name__ == '__main__':
    pass