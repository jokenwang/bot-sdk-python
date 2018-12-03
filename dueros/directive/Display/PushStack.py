#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/30

"""
    用于生成PushStack指令的类
"""

from dueros.directive.BaseDirective import BaseDirective


class PushStack(BaseDirective):

    def __init__(self):
        super(PushStack, self).__init__('Display.PushStack')


if __name__ == '__main__':
    pass