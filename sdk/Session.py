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
        print('data %s' % data)
        self.data = {}
        if('attributes' in data.keys()):
            self.data = data['attributes']

        if('sessionId' in data.keys()):
            self.sessionId = data['sessionId']
        else:
            self.sessionId = None

        if('new' in data.keys()):
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
        if(field in self.data.keys()):
            return self.data[field]

    def setData(self, field, value, default):

        self.data[field] = value


if __name__ == '__main__':
    pass