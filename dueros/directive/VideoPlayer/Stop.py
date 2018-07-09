#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/7/2

"""
    desc:pass
"""
from dueros.directive.BaseDirective import BaseDirective


class Stop(BaseDirective):
    def __init__(self):
        super(Stop, self).__init__('VideoPlay.Stop')
    pass


if __name__ == '__main__':
    pass