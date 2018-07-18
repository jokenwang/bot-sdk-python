#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/1/3

"""
    desc:pass
"""


class BotMonitorConfig:

    @staticmethod
    def get_host():
        return 'dueros-api.baidu.com'

    @staticmethod
    def get_upload_url():
        return 'https://dueros-api.baidu.com/uploadmonitordata'
        #return 'http://127.0.0.1:8000'

    @staticmethod
    def get_sdk_version():
        return '1.0.0'

    @staticmethod
    def get_sdk_type():
        return 'python'

    @staticmethod
    def get_upload_port():
        return 443

    @staticmethod
    def get_upload_path():
        return '/uploadmonitordata'


if __name__ == '__main__':
    pass