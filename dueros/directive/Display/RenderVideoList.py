#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/1

"""
    desc:pass
"""
from dueros.directive.BaseDirective import BaseDirective
from dueros.directive.Display.media.MediaPlayBehaviorEnum import MediaPlayBehaviorEnum
from dueros.directive.Display.media.VideoItem import VideoItem

class RenderVideoList(BaseDirective):

    def __init__(self, title, behavior = MediaPlayBehaviorEnum.REPLACE):
        super(RenderVideoList, self).__init__('Display.RenderVideoList')

        data = {
            'token': self.gen_token(),
            'title': title,
            'behavior': behavior.value,
            'size': 0,
            'videoItems': []
        }

        self.data = dict(self.data, **data)

    def set_token(self, token):
        """
        设置directive的token.默认在构造时自动生成了token，可以覆盖
        :param token:
        :return:
        """
        if token:
            self.data['token'] = token

    def add_video_item(self, video_item):
        """
        增加VideoItem
        :param video_item:
        :return:
        """
        if video_item and isinstance(video_item, VideoItem):
            self.data['videoItems'].append(video_item.get_data())
            self.data['size'] = self.data['size'] + 1


if __name__ == '__main__':
    pass