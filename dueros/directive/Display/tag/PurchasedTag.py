#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/17

"""
    desc:pass
"""
from dueros.directive.Display.tag import TagTypeEnum
from dueros.directive.Display.tag.BaseTag import BaseTag


class PurchasedTag(BaseTag):

    def __init__(self):
        BaseTag.__init__(self, TagTypeEnum.TAG_TYPE_PURCHASED, '已购')


if __name__ == '__main__':
    pass