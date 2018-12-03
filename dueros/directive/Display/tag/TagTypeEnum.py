#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/17

"""
    desc:pass
"""
from enum import Enum, unique


@unique
class TagTypeEnum(Enum):

    TAG_TYPE_AMOUNT = 'AMOUNT'
    TAG_TYPE_AUDITION_NEW = 'AUDITION'
    TAG_TYPE_CUSTOM = 'CUSTOM'
    TAG_TYPE_FREE = 'FREE'
    TAG_TYPE_HOT = 'HOT'
    TAG_TYPE_NEW = 'NEW'
    TAG_TYPE_PAY = 'PAY'
    TAG_TYPE_PURCHASED = 'PURCHASED'
    TAG_TYPE_TIME = 'TIME'
    TAG_TYPE_VIP = 'VIP'


    @staticmethod
    def inEnum(position):
        return position in TagTypeEnum.__members__.values()


if __name__ == '__main__':
    pass