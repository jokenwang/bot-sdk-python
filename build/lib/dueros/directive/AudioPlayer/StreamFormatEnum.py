#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/29

"""
    desc:pass
"""
from enum import Enum, unique

@unique
class StreamFormatEnum(Enum):
    STREAM_FORMAT_MP3 = 'AUDIO_MP3'
    STREAM_FORMAT_M3U8 = 'AUDIO_M3U8'
    STREAM_FORMAT_M4A = 'AUDIO_M4A'

    @staticmethod
    def inEnum(streamFormat):
        return streamFormat in StreamFormatEnum.__members__.values()

    pass


if __name__ == '__main__':
    pass