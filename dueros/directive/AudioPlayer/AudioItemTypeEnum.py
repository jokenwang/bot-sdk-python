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
class AudioItemTypeEnum(Enum):
    AUDIO_TYPE_MUSIC = 'MUSIC'
    FORMAT_LRC = 'LRC'

    @staticmethod
    def inEnum(item_type):
        return item_type in AudioItemTypeEnum.__members__.values()

    pass


if __name__ == '__main__':
    pass