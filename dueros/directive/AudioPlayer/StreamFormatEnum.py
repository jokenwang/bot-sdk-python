#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/29

"""
    desc:pass
"""


class StreamFormatEnum(object):

    STREAM_FORMAT_MP3 = 'AUDIO_MP3'
    STREAM_FORMAT_M3U8 = 'AUDIO_M3U8'
    STREAM_FORMAT_M4A = 'AUDIO_M4A'

    @staticmethod
    def inEnum(position):
        return position == StreamFormatEnum.STREAM_FORMAT_MP3 or position == StreamFormatEnum.STREAM_FORMAT_M3U8 or position == StreamFormatEnum.STREAM_FORMAT_M4A

    pass


if __name__ == '__main__':
    pass