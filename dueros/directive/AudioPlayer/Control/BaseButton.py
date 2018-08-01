#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/28

"""
    desc:pass
"""


class BaseButton(object):

    def __init__(self, button_type, name):
        self.data = {'type': button_type, 'name': name}

    def get_data(self):
        return self.data


if __name__ == '__main__':
    pass