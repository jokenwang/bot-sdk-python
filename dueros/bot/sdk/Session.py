#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# description:
# author:jack
# create_time: 2017/12/30

"""
Session相关 暂未搞
"""


class Session(object):

    def __init__(self, data):

        self.data = {}

        if 'attributes' in data:
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

    def toResponse(self):

        return {
            'attributes': self.data
        }

    def getData(self, field, default):
        if field in self.data:
            return self.data[field]

    def setData(self, field, value, default):

        self.data[field] = value


if __name__ == '__main__':
    pass