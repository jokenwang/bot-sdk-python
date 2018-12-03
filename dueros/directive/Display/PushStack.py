#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/30

"""
    用于生成PushStack指令的类
"""

from dueros.directive.BaseDirective import BaseDirective


class PushStack(BaseDirective):
    """
    PushStack指令，用于页面压栈
    """

    def __init__(self):
        BaseDirective.__init__(self, 'Display.PushStack')


if __name__ == '__main__':
    pass