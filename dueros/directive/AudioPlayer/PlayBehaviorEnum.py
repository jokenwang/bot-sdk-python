#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/29

"""
    desc:pass
"""

REPLACE_ALL = 'REPLACE_ALL'
REPLACE_ENQUEUED = 'REPLACE_ENQUEUED'
ENQUEUE = 'ENQUEUE'


def in_enum(position):
    return position == REPLACE_ALL or position == REPLACE_ENQUEUED or position == ENQUEUE


if __name__ == '__main__':
    pass
