#!/usr/bin/env python3
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
from dueros.directive.AudioPlayer.PlayBehaviorEnum import PlayBehaviorEnum
from dueros.directive.Display.template.BodyTemplate2 import BodyTemplate2
from dueros.directive.Display.RenderTemplate import RenderTemplate
import json
class Bot(Bot):
    '''
    自定义的BOT函数
    '''
    def launchRequest(self):
        '''
        打开调用名
        '''
        self.musics = json.loads(self.musicsData())
        self.wait_answer()
        return {
            'directives': [self.getTemplate2(self.musics[self.curIndex])],
            'outputSpeech': '欢迎使用音乐播放器!'
        }

    def audioPlay(self):
        '''
        播放指令
        '''
        self.musics = json.loads(self.musicsData())

        return {
            'directives' : [self.getTemplate2(self.musics[self.curIndex]), self.getDirective("0")],
            'outputSpeech': r'正在为你播放歌曲'
        }

    def getDirective(self, offset = "0"):
        directive = Play(self.musics[self.curIndex]['url'])
        directive.set_token(self.musics[self.curIndex]['token'])
        directive.set_offset_in_milliseconds(offset)
        return directive

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
        directive = Play('http://music.163.com/song/media/outer/url?id=554191055.mp3', PlayBehaviorEnum.ENQUEUE)
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

    def getTemplate2(self, music):
        print(music)
        bodyTemplate = BodyTemplate2()
        bodyTemplate.set_token(music['token'])
        bodyTemplate.set_background_image(self.DEFAULT_IMAGE)
        bodyTemplate.set_title(music['singer'])
        bodyTemplate.set_plain_content(music['name'])
        renderTemplate = RenderTemplate(bodyTemplate)
        return renderTemplate


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

    def musicsData(self):
        with open("./audio_play/musics.json", 'r', encoding='utf-8') as load_f:
            return load_f.read()
    curIndex = 0
    musics = []
    DEFAULT_IMAGE = 'https://skillstore.cdn.bcebos.com/icon/100/c709eed1-c07a-be4a-b242-0b0d8b777041.jpg';

if __name__ == '__main__':
    pass
