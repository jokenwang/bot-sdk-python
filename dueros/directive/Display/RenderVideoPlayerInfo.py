#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/19

"""
    desc:pass
"""
from dueros.directive.Display.BaseRenderPlayerInfo import BaseRenderPlayerInfo


class RenderVideoPlayerInfo(BaseRenderPlayerInfo):

    def __init__(self, content=None, controls=[]):
        super(RenderVideoPlayerInfo, self).__init__('Display.RenderVideoPlayerInfo', content, controls)


if __name__ == '__main__':
    pass