#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/28

"""
    desc:pass
"""
class TextContentPosition(object):
    TOP_LEFT = 'TOP_LEFT'
    CENTER = 'CENTER'
    BOTTOM_LEFT = 'BOTTOM_LEFT'

    @staticmethod
    def inEnum(position):

        return position == TextContentPosition.BOTTOM_LEFT or position == TextContentPosition.BOTTOM_LEFT or position == TextContentPosition.CENTER

if __name__ == '__main__':

    pass