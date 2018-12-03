#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/17

"""
    desc:pass
"""
from dueros.directive.Display.tag.BaseTag import BaseTag
from dueros.directive.Display.tag import TagTypeEnum


class AuditionTag(BaseTag):

    def __init__(self):
        BaseTag.__init__(self, TagTypeEnum.TAG_TYPE_AUDITION_NEW, '试听')


if __name__ == '__main__':
    pass