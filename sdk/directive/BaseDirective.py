#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2017/12/30

"""
"""


class BaseDirective(object):

    def __init__(self, type):

        self.data['type'] = type

    def getToken(self):

        pass

    def getData(self):
        return self.data;

if __name__ == '__main__':
    pass