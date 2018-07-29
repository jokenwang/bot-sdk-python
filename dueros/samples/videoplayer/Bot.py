#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/7/28

"""
    desc:pass
"""

from dueros.Bot import Bot
from dueros.directive.VideoPlayer.VideoPlayer import VideoPlayer
from dueros.directive.AudioPlayer.PlayBehaviorEnum import PlayBehaviorEnum
class Bot(Bot):

    def __init__(self, data):
        super(Bot, self).__init__(data)
        self.add_launch_handler(self.launchRequest)
        # 给端下发指令
        self.add_intent_handler('audio_play_intent', self.videoPlayer)

    def launchRequest(self):
        '''
        打开调用名
        '''
        self.wait_answer()
        return {
            'outputSpeech': r'欢迎进入123'
        }


    def videoPlayer(self):

        print('asdfasdf')
        directives = []
        directive = VideoPlayer('http://clips.vorwaerts-gmbh.de/big_buck_bunny.mp4')
        directives.append(directive)
        return {
            'directives': directives,
            'outputSpeech': r'正在为你播放歌曲'
        }

    pass


if __name__ == '__main__':
    pass