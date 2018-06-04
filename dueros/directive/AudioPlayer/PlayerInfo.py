#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/28

"""
    desc:pass
"""
from dueros.directive.AudioPlayer.Control.BaseButton import BaseButton

class PlayerInfo:

    def __init__(self):
        self.data = {}
        self.data['content']={}
        self.data['content']['audioItemType'] = 'AUDIO_TYPE_MUSIC'

    def setAudioItemType(self, type):
        self.data['content']['audioItemType'] = type

    def setTitle(self, title):

        self.data['content']['title'] = title

    def setTitleSubtext1(self, titleSubtext1):
        self.data['content']['titleSubtext1'] = titleSubtext1

    def setTitleSubtext2(self, titleSubtext2):
        self.data['content']['titleSubtext2'] = titleSubtext2

    def setLyric(self, url):
        self.data['content']['lyric']['url'] = url
        self.data['content']['lyric']['format'] = 'FORMAT_LRC'

    def setMediaLengthInMs(self, mediaLengthInMs):
        mediaLengthInMs = int(mediaLengthInMs)
        self.data['content']['mediaLengthInMilliseconds'] = mediaLengthInMs

    def setArt(self, src):
        self.data['content']['art']['src'] = src

    def setProvider(self, name, logo):
        self.data['content']['provider']['name'] = name;
        self.data['content']['provider']['logo']['src'] = logo

    def setControls(self, controls):
        self.data['controls'] = []
        if isinstance(controls, BaseButton):
            self.data['controls'].append(controls.getData())

        if type(controls) == list:
            for control in controls:
                self.data['controls'].append(control.getData())

    def addControl(self, control):
        if isinstance(control, BaseButton):
            self.data['controls'].append(control.getData())

    def getData(self):
        return self.data
    pass


if __name__ == '__main__':
    pass