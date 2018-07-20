#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/28

"""
    desc:pass
"""


class BaseButton:

    def __init__(self, button_type, name):
        self.data = {}
        self.data['type'] = button_type
        self.data['name'] = name

    def get_data(self):

        return self.data

    pass


if __name__ == '__main__':
    pass