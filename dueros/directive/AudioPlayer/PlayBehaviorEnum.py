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
class PlayBehaviorEnum(Enum):
    REPLACE_ALL = 'REPLACE_ALL'
    REPLACE_ENQUEUED = 'REPLACE_ENQUEUED'
    ENQUEUE = 'ENQUEUE'


    @staticmethod
    def inEnum(playBehavior):
        return playBehavior in PlayBehaviorEnum.__members__.values()

    pass


if __name__ == '__main__':

    print(PlayBehaviorEnum.REPLACE_ALL.value)
    pass