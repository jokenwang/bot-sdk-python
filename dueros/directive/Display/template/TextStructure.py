#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/26

"""
    desc:pass
"""


class TextStructure(object):

    def __init__(self):
        super(TextStructure, self).__init__()
        self.data = {}
        self.set_type('PlainText')

    def set_type(self, structure_type):

        if structure_type:
            self.data['type'] = structure_type

    def set_text(self, text):

        if text:
            self.data['text'] = text

    def get_data(self):

        return self.data


if __name__ == '__main__':
    pass