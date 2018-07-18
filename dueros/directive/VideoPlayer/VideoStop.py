#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/7/13

"""
    desc:pass
"""

from dueros.directive.BaseDirective import BaseDirective
from dueros.directive.AudioPlayer.PlayBehaviorEnum import PlayBehaviorEnum
from dueros.Utils import Utils


class VideoStop(BaseDirective):

    def __init__(self):
        super(VideoStop, self).__init__('VideoPlayer.Stop')

    pass


if __name__ == '__main__':
    pass