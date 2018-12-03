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
from dueros.directive.Display.media.AudioItem import AudioItem


class RenderAudioList(BaseDirective):
    """
    用于渲染音频播放列表,
    注意token, 正在播放音频的token和列表中item的token相同，
    列表会做特殊渲染，来表示某个item正在被播放
    """

    def __init__(self, title, behavior=MediaPlayBehaviorEnum.REPLACE):
        BaseDirective.__init__(self, 'Display.RenderAudioList')

        data = {
            'token': self.gen_token(),
            'title': title,
            'behavior': behavior,
            'size': 0,
            'audioItems': []
        }

        self.data = dict(self.data, **data)

    def add_audio_item(self, audio_item):
        """
        增加audioItem
        :param audio_item:
        :return:
        """
        if audio_item and isinstance(audio_item, AudioItem):
            self.data['audioItems'].append(audio_item.get_data())
            self.data['size'] = self.data['size'] + 1
        else:
            raise ValueError('The audio_item is not AudioItem')


if __name__ == '__main__':


    pass