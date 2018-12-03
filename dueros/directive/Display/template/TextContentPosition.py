#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/28

"""
    desc:pass
"""
from enum import Enum, unique


@unique
class TextContentPosition(Enum):
    TOP_LEFT = 'TOP-LEFT'
    CENTER = 'CENTER'
    BOTTOM_LEFT = 'BOTTOM-LEFT'

    @staticmethod
    def inEnum(position):

        return position in TextContentPosition.__members__.values()

if __name__ == '__main__':

    pass