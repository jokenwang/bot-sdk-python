#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/1/2

"""
    desc:pass
"""

from dueros.card.BaseCard import BaseCard

class StandardCard(BaseCard):

    def __init__(self):
        super(StandardCard, self).__init__(['title', 'content', 'image'])
        self.data['type'] = 'standard'


if __name__ == '__main__':
    pass
