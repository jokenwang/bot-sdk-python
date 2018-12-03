#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/27

"""
    desc:pass
"""

"""
REPLACE: 清空当前的列表，再渲染，用于首次第一页数据的渲染
APPEND: 当前列表不变，在当前的列表后面渲染，用于往后翻页的渲染
PREPEND:当前列表不变，在当前的列表前面渲染，用于往前翻页的渲染
"""
REPLACE = 'REPLACE'
APPEND = 'APPEND'
PREPEND = 'PREPEND'


def in_enum(play_behavior):
    return play_behavior == REPLACE or play_behavior == APPEND or play_behavior == PREPEND


if __name__ == '__main__':
    pass
