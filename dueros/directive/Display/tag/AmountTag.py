#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/17

"""
    desc:pass
"""
from dueros.directive.Display.tag.BaseTag import BaseTag
from dueros.directive.Display.tag.TagTypeEnum import TagTypeEnum


class AmountTag(BaseTag):

    def __init__(self, amount):
        super(AmountTag, self).__init__(TagTypeEnum.TAG_TYPE_AMOUNT, amount)


if __name__ == '__main__':
    pass