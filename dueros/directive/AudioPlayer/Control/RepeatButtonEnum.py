#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/28

"""
    desc:pass
"""


class RepeatButtonEnum(object):
    REPEAT_ONE = 'REPEAT_ONE'
    REPEAT_ALL = 'REPEAT_ALL'
    REPEAT_SHUFFLE = 'SHUFFLE'

    @staticmethod
    def inEnum(position):
        return position == RepeatButtonEnum.REPEAT_ONE or position == RepeatButtonEnum.REPEAT_ALL or position == RepeatButtonEnum.REPEAT_SHUFFLE

    pass


if __name__ == '__main__':
    pass