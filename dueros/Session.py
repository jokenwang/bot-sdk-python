#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# description:
# author:jack
# create_time: 2017/12/30

"""
Session相关
相关文档:https://dueros.baidu.com/didp/doc/dueros-bot-platform/dbp-custom/response_markdown#session%E5%8F%82%E6%95%B0%E8%AF%B4%E6%98%8E
"""
from dueros.Base import Base


class Session(Base):

    def __init__(self, data):

        super(Session, self).__init__()

        self.data = {}

        if 'attributes' in data and isinstance(data['attributes'], list) and len(data['attributes']) > 0:
            self.data = data['attributes']

        if 'attributes' in data and isinstance(data['attributes'], dict):
            self.data = data['attributes']

        if 'sessionId' in data:
            self.sessionId = data['sessionId']
        else:
            self.sessionId = None

        if 'new' in data:
            self.is_new = data['new']
        else:
            self.is_new = False

    def clear(self):
        self.data = {}

    def to_response(self):

        return {
            'attributes': self.data
        }

    def get_data(self, field, default=''):
        """
        获取session中指定key的值
        :param field:   session key
        :param default: 默认值
        :return:
        """
        if field and field in self.data:
            return self.data[field]
        else:
            return default

    def set_data(self, field, value):
        """
        设置session
        :param field:  session key
        :param value:  session value
        :return:
        """
        if value is not None:
            self.data[field] = value


if __name__ == '__main__':

    pass