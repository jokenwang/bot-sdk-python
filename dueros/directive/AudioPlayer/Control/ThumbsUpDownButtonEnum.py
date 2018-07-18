#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/28

"""
    desc:pass
"""


class ThumbsUpDownButtonEnum(object):

    THUMBS_UP = 'THUMBS_UP'
    THUMBS_DOWN = 'THUMBS_DOWN'

    @staticmethod
    def inEnum(position):
        return position == ThumbsUpDownButtonEnum.THUMBS_UP or position == ThumbsUpDownButtonEnum.THUMBS_DOWN


if __name__ == '__main__':
    pass