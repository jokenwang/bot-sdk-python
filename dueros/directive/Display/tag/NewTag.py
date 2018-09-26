#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/17

"""
    desc:pass
"""

from dueros.directive.Display.tag.TagTypeEnum import TagTypeEnum
from dueros.directive.Display.tag.BaseTag import BaseTag


class NewTag(BaseTag):

    def __init__(self):
        super(NewTag, self).__init__(TagTypeEnum.TAG_TYPE_NEW, '最新')


if __name__ == '__main__':
    pass