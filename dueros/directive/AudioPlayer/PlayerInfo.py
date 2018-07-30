#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/28

"""
    desc:pass
"""
from dueros.directive.AudioPlayer.Control.BaseButton import BaseButton
from dueros.Utils import Utils
from dueros.directive.AudioPlayer.AudioItemTypeEnum import AudioItemTypeEnum

class PlayerInfo:

    def __init__(self):
        self.data = {'content': {}}
        self.data['content']['audioItemType'] = AudioItemTypeEnum.AUDIO_TYPE_MUSIC.value

    def set_audio_item_type(self, audio_item_type):
        if isinstance(audio_item_type, AudioItemTypeEnum):
            self.data['content']['audioItemType'] = audio_item_type.value

    def set_title(self, title):

        self.data['content']['title'] = title

    def set_title_subtext1(self, title_subtext1):

        self.data['content']['titleSubtext1'] = title_subtext1

    def set_title_subtext2(self, title_subtext2):

        self.data['content']['titleSubtext2'] = title_subtext2

    def set_lyric(self, url):

        if not Utils.checkKeyInDict(self.data['content'], 'lyric'):
            self.data['content']['lyric'] = {}
        self.data['content']['lyric']['url'] = url
        self.data['content']['lyric']['format'] = AudioItemTypeEnum.FORMAT_LRC.value

    def set_media_length_in_ms(self, media_length_in_ms):

        media_length_in_ms = int(media_length_in_ms)
        self.data['content']['mediaLengthInMilliseconds'] = media_length_in_ms

    def set_art(self, src):

        if not Utils.checkKeyInDict(self.data['content'], 'art'):
            self.data['content']['art'] = {}
        self.data['content']['art']['src'] = src

    def set_provider(self, name, logo):

        if not Utils.checkKeyInDict(self.data['content'], 'provider'):
            self.data['content']['provider'] = {}
        self.data['content']['provider']['name'] = name

        if not Utils.checkKeyInDict(self.data['content']['provider'], 'logo'):
            self.data['content']['provider']['logo'] = {}
        self.data['content']['provider']['logo']['src'] = logo

    def set_controls(self, controls):

        if not Utils.checkKeyInDict(self.data, 'controls'):
            self.data['controls'] = []

        if isinstance(controls, BaseButton):
            self.data['controls'].append(controls.get_data())

        if type(controls) == list:
            for control in controls:
                self.data['controls'].append(control.get_data())

    def add_control(self, control):

        if not Utils.checkKeyInDict(self.data, 'controls'):
            self.data['controls'] = []

        if isinstance(control, BaseButton):
            self.data['controls'].append(control.get_data())

    def get_data(self):

        return self.data
    pass


if __name__ == '__main__':
    pass