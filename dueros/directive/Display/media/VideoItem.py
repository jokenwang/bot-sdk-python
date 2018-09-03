#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/1

"""
    desc:pass
"""

from dueros.directive.Display.media.BaseMediaListItem import BaseMediaListItem
from dueros.Utils import Utils


class VideoItem(BaseMediaListItem):

    def __init__(self, title, title_subtext1):
        super(VideoItem, self).__init__(title, title_subtext1)

    def set_media_length_in_milliseconds(self, milliseconds):
        milliseconds = Utils.convert_number(milliseconds)
        if milliseconds:
            self.data['mediaLengthInMilliseconds'] = milliseconds

if __name__ == '__main__':
    pass