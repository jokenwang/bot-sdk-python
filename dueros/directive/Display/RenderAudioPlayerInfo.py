#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/19

from dueros.directive.Display.BaseRenderPlayerInfo import BaseRenderPlayerInfo


class RenderAudioPlayerInfo(BaseRenderPlayerInfo):

    def __init__(self, content=None, controls=[]):
        super(RenderAudioPlayerInfo, self).__init__('Display.RenderAudioPlayerInfo', content, controls)