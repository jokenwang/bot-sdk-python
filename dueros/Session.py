#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2017/12/30

"""
Session相关 暂未搞
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
            self.isNew = data['new']
        else:
            self.isNew = False

    def clear(self):
        self.data = {}

    def to_response(self):

        return {
            'attributes': self.data
        }

    def get_data(self, field, default=''):
        """

        :param field:
        :param default:
        :return:
        """
        if field is not None and str(field) in self.data:
            field = str(field)
            return self.data[field]
        else:
            return default

    def set_data(self, field, value, default=''):
        """

        :param field:
        :param value:
        :param default:
        :return:
        """
        if field is not None and value is not None:
            field = str(field)
            self.data[field] = value
        else:
            self.data[field] = default


if __name__ == '__main__':
    pass