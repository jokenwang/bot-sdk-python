#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/28

"""
    desc:pass
"""
from dueros.directive.AudioPlayer.Control.BaseButton import BaseButton
from dueros.directive.AudioPlayer.PlayerInfoAudioItemEnum import PlayerInfoAudioItemEnum
class PlayerInfo:

    def __init__(self):
        self.data = {}
        self.data['content']={}
        self.data['content']['provider'] = {}
        self.data['content']['lyric'] = {}
        self.data['content']['audioItemType'] = PlayerInfoAudioItemEnum.AUDIO_TYPE_MUSIC
        self.data['controls'] = []
        self.data['content']['provider']['logo'] = {}

    def set_audio_item_type(self, audio_type):
        self.data['content']['audioItemType'] = audio_type

    def set_title(self, title):

        self.data['content']['title'] = title

    def set_title_subtext1(self, title_subtext1):
        self.data['content']['titleSubtext1'] = title_subtext1

    def set_title_subtext2(self, title_subtext2):
        self.data['content']['titleSubtext2'] = title_subtext2

    def set_lyric(self, url):
        self.data['content']['lyric']['url'] = url
        self.data['content']['lyric']['format'] = 'LRC'

    def set_media_length_in_ms(self, media_length_in_ms):
        media_length_in_ms = int(media_length_in_ms)
        self.data['content']['mediaLengthInMilliseconds'] = media_length_in_ms

    def set_art(self, src):
        self.data['content']['art'] = {}
        self.data['content']['art']['src'] = src

    def set_provider(self, name, logo):
        self.data['content']['provider']['name'] = name
        self.data['content']['provider']['logo']['src'] = logo

    def set_provider_name(self, name):
        self.data['content']['provider']['name'] = name

    def set_provider_logo(self, logo):
        self.data['content']['provider']['logo']['src'] = logo

    def set_controls(self, controls):
        if isinstance(controls, BaseButton):
            self.data['controls'].append(controls.get_data())

        if type(controls) == list:
            for control in controls:
                self.data['controls'].append(control.get_data())

    def add_control(self, control):
        if isinstance(control, BaseButton):
            self.data['controls'].append(control.get_data())

    def get_data(self):
        return self.data
    pass


if __name__ == '__main__':
    pass