#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2017/12/31 上午12:25

"""
    用于生成Stop指令的类
"""
from dueros.directive.BaseDirective import BaseDirective


class Stop(BaseDirective):

    def __init__(self):
        super(Stop, self).__init__('AudioPlayer.Stop')


if __name__ == '__main__':
    pass
