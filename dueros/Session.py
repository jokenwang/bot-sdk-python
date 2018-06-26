#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# description:
# author:jack
# create_time: 2017/12/30

from dueros.Base import Base

class Session(Base):

    def __init__(self, data):

        super(Session, self).__init__()

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

        if field and field in self.data:
            return self.data[field]
        else:
            return default

    def setData(self, field, value, default):
        if value:
            self.data[field] = value
        else:
            self.data[field] = default


if __name__ == '__main__':
    pass