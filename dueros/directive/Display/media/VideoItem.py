#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/1

"""
    desc:pass
"""

from dueros.directive.Display.media.BaseMediaListItem import BaseMediaListItem
from dueros import Utils


class VideoItem(BaseMediaListItem):
    """
    视频Item
    """
    def __init__(self, title, title_subtext1):
        """

        :param title:
        :param title_subtext1:
        """
        BaseMediaListItem.__init__(self, title, title_subtext1)

    def set_media_length_in_milliseconds(self, milliseconds):
        milliseconds = Utils.convert_number(milliseconds)
        if milliseconds:
            self.data['mediaLengthInMilliseconds'] = milliseconds


if __name__ == '__main__':
    pass