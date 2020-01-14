#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/28

from enum import Enum, unique


@unique
class ThumbsUpDownButtonEnum(Enum):
    THUMBS_UP = 'THUMBS_UP'
    THUMBS_DOWN = 'THUMBS_DOWN'

    @staticmethod
    def inEnum(thumbsUpDown):
        return thumbsUpDown in ThumbsUpDownButtonEnum.__members__.values()
