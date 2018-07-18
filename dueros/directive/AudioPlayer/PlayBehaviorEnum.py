#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/29

"""
    desc:pass
"""


class PlayBehaviorEnum(object):
    REPLACE_ALL = 'REPLACE_ALL'
    REPLACE_ENQUEUED = 'REPLACE_ENQUEUED'
    ENQUEUE = 'ENQUEUE'

    @staticmethod
    def inEnum(position):
        return position == PlayBehaviorEnum.REPLACE_ALL or position == PlayBehaviorEnum.REPLACE_ENQUEUED or position == PlayBehaviorEnum.ENQUEUE

    pass


if __name__ == '__main__':
    pass