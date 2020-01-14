#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/28

from enum import Enum, unique

@unique
class RepeatButtonEnum(Enum):
    REPEAT_ONE = 'REPEAT_ONE'
    REPEAT_ALL = 'REPEAT_ALL'
    REPEAT_SHUFFLE = 'SHUFFLE'

    @staticmethod
    def inEnum(repeatButton):
        return repeatButton in RepeatButtonEnum.__members__.values()
