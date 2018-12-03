#!/usr/bin/env python2
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

    def __init__(self, session_data):

        super(Session, self).__init__()

        self.data = {}

        if 'attributes' in session_data and isinstance(session_data['attributes'], list) and len(session_data['attributes']) > 0:
            self.data = session_data['attributes']

        if 'attributes' in session_data and isinstance(session_data['attributes'], dict):
            self.data = session_data['attributes']

        if 'sessionId' in session_data:
            self.sessionId = session_data['sessionId']
        else:
            self.sessionId = None

        if 'new' in session_data:
            self.is_new = session_data['new']
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
        if field is not None:
            if not isinstance(field, str):
                field = str(field)
            if field in self.data:
                return self.data[field]
            else:
                return default
        else:
            return default

    def set_data(self, field, value):
        """
        设置session
        :param field:  session key
        :param value:  session value
        :return:
        """
        if field is not None:
            if not isinstance(field, str):
                field = str(field)
        if value is not None:
            self.data[field] = value

    def clear_session_field(self, field):
        if field and isinstance(field, str) and field in self.data:
            value = self.data.pop(field)


if __name__ == '__main__':

    pass