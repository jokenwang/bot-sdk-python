#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/19

"""
    desc:pass
"""
from dueros.directive.Base.BasePlayerInfoContent import BasePlayerInfoContent
from dueros.directive.AudioPlayer import AudioItemTypeEnum
from dueros import Utils


class AudioPlayerInfoContent(BasePlayerInfoContent):

    def __init__(self):
        super(AudioPlayerInfoContent, self).__init__()
        self.data['audioItemType'] = AudioItemTypeEnum.AUDIO_TYPE_MUSIC

    def set_audio_item_type(self, audio_type):
        if AudioItemTypeEnum.in_enum(audio_type):
            self.data['audioItemType'] = audio_type
        else:
            self.data['audioItemType'] = audio_type

    def set_title(self, title):
        if isinstance(title, str):
            self.data['title'] = title

    def set_title_subtext1(self, title_sub_text1):
        if isinstance(title_sub_text1, str):
            self.data['titleSubtext1'] = title_sub_text1

    def set_title_subtext2(self, title_sub_text2):
        if isinstance(title_sub_text2, str):
            self.data['titleSubtext2'] = title_sub_text2

    def set_lyric(self, url):

        if isinstance(url, str):
            if not Utils.check_key_in_dict(self.data, 'lyric'):
                self.data['lyric'] = {}
            self.data['lyric']['url'] = url
            self.data['lyric']['format'] = AudioItemTypeEnum.FORMAT_LRC

    def set_media_length_in_ms(self, media_length_in_ms):

        media_length_in_ms = Utils.convert_number(media_length_in_ms)
        self.data['mediaLengthInMilliseconds'] = media_length_in_ms

    def set_art(self, src):

        if not Utils.check_key_in_dict(self.data, 'art'):
            self.data['art'] = {}
        self.data['art']['src'] = src

    def set_provider(self, name, logo):

        if not Utils.check_key_in_dict(self.data, 'provider'):
            self.data['provider'] = {}
        self.data['provider']['name'] = name

        if not Utils.check_key_in_dict(self.data['provider'], 'logo'):
            self.data['provider']['logo'] = {}
        self.data['provider']['logo']['src'] = logo

    pass


if __name__ == '__main__':
    pass