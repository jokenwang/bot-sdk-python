#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2017/12/31 上午12:25

"""
用于生成Stop指令的类
详见文档：https://dueros.baidu.com/didp/doc/dueros-bot-platform/dbp-custom/audioplayer_markdown#AudioPlayer.Stop%E6%8C%87%E4%BB%A4
"""
from dueros.directive.BaseDirective import BaseDirective


class Stop(BaseDirective):

    def __init__(self):
        super(Stop, self).__init__('AudioPlayer.Stop')


if __name__ == '__main__':
    pass
