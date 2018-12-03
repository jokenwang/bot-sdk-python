#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/19

"""
    desc:pass
"""
from dueros.directive.Display.BaseRenderPlayerInfo import BaseRenderPlayerInfo


class RenderAudioPlayerInfo(BaseRenderPlayerInfo):

    def __init__(self, content=None, controls=[]):
        BaseRenderPlayerInfo.__init__(self, 'Display.RenderAudioPlayerInfo', content, controls)


if __name__ == '__main__':
    pass