#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/7/13

"""
    desc:pass
"""

from dueros.directive.BaseDirective import BaseDirective


class VideoStop(BaseDirective):

    def __init__(self):
        super(VideoStop, self).__init__('VideoPlayer.Stop')


if __name__ == '__main__':
    pass