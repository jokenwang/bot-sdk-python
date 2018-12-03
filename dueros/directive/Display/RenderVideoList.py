#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/1

"""
    desc:pass
"""
from dueros.directive.BaseDirective import BaseDirective
from dueros.directive.Display.media import MediaPlayBehaviorEnum
from dueros.directive.Display.media.VideoItem import VideoItem


class RenderVideoList(BaseDirective):
    """
    视频播放列表指令
    """

    def __init__(self, title, behavior=MediaPlayBehaviorEnum.REPLACE):
        super(RenderVideoList, self).__init__('Display.RenderVideoList')

        data = {
            'token': self.gen_token(),
            'title': title,
            'behavior': behavior,
            'size': 0,
            'videoItems': []
        }

        self.data = dict(self.data, **data)

    def add_video_item(self, video_item):
        """
        增加VideoItem
        :param video_item:
        :return:
        """
        if video_item and isinstance(video_item, VideoItem):
            self.data['videoItems'].append(video_item.get_data())
            self.data['size'] = self.data['size'] + 1
        else:
            raise ValueError('The video_item is not VideoItem')


if __name__ == '__main__':
    pass