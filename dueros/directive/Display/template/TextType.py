#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/28

from enum import Enum, unique


@unique
class TextType(Enum):
    PLAIN_TEXT = 'PlainText'
    RICH_TEXT = 'RichText'

    @staticmethod
    def inEnum(position):
        return position in TextType.__members__.values()