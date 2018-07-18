#!/usr/bin/env python2
# -*- encoding=utf-8 -*-
# description:
# author:jack
# create_time: 2018/1/3

"""
    desc:pass
"""

from dueros.Bot import Bot
from dueros.directive.AudioPlayer.Stop import Stop
from dueros.directive.AudioPlayer.Play import Play
class Bot(Bot):
    '''
    自定义的BOT函数
    '''
    def launchRequest(self):
        '''
        打开调用名
        '''
        return {
            'outputSpeech': r'欢迎进入'
        }

    def audioPlay(self):
        '''
        播放指令
        '''
        directives = []
        directive = Play('http://m10.music.126.net/20180308193927/e9ca2860e7923536212ab420aad7b78d/ymusic/e18c/c0a0/ffef/1770e72b9dd1be8f814a566cab863c23.mp3')
        directives.append(directive)
        return {
            'directives' : directives,
            'outputSpeech': r'正在为你播放歌曲'
        }

    def audioStop(self):
        '''
        暂停指令
        '''
        directives = []
        directive = Stop()
        directives.append(directive)
        return {
            'directives' : directives,
            'outputSpeech': r'已经停止播放'
        }

    def playBackStartedEvent(self, event):
        '''
        处理事件上报示例
        '''
        offset = event['offsetInMilliSeconds']
        directives = []
        directive = Play('http://m10.music.126.net/20180308193927/e9ca2860e7923536212ab420aad7b78d/ymusic/e18c/c0a0/ffef/1770e72b9dd1be8f814a566cab863c23.mp3', Play.REPLACE_ALL)
        directives.append(directive)
        return {
            'outputSpeech': r'已处理端上报事件',
            'directives' : directives,
        }

    def playBackNearlyFinished(self, event):
        '''
        处理事件上报示例
        '''
        offset = event['offsetInMilliSeconds']
        return {
            'outputSpeech': r'已处理端上报事件'
        }

    def __init__(self, data):
        '''
        构造函数
        '''
        super(Bot, self).__init__(data)

        self.add_launch_handler(self.launchRequest)
        #给端下发指令
        self.add_intent_handler('audio_play_intent', self.audioPlay)
        self.add_intent_handler('audio_stop_intent', self.audioStop)
        #处理端上报事件
        self.add_event_listener('AudioPlayer.PlaybackStarted', self.playBackStartedEvent)
        self.add_event_listener('AudioPlayer.PlaybackNearlyFinished', self.playBackStartedEvent)


if __name__ == '__main__':
    pass
