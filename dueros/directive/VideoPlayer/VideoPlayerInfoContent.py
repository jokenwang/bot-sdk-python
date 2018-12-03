#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/19

"""
    desc:pass
"""
from dueros.directive.Base.BasePlayerInfoContent import BasePlayerInfoContent
from dueros.Utils import Utils


class VideoPlayerInfoContent(BasePlayerInfoContent):

    def __init__(self, title='', media_length_in_milliseconds=0):
        super(VideoPlayerInfoContent, self).__init__()
        self.set_title(title)
        self.set_media_length_in_milliseconds(media_length_in_milliseconds)

    def set_title(self, title):
        if isinstance(title, str):
            self.data['title'] = title

    def set_media_length_in_milliseconds(self, media_length_in_milliseconds):
        milliseconds = Utils.convert_number(media_length_in_milliseconds)
        if milliseconds:
            self.data['mediaLengthInMilliseconds'] = milliseconds
    pass


if __name__ == '__main__':
    pass