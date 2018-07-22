#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/7/2

"""
VideoPlayer.Stop指令
详见文档：https://dueros.baidu.com/didp/doc/dueros-bot-platform/dbp-custom/videoplayer_markdown#VideoPlayer.Stop%E6%8C%87%E4%BB%A4
"""
from dueros.directive.BaseDirective import BaseDirective


class Stop(BaseDirective):
    def __init__(self):
        super(Stop, self).__init__('VideoPlayer.Stop')
    pass


if __name__ == '__main__':
    pass