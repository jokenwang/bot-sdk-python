#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/1/3

"""
    desc:pass
"""

from dueros.Bot import Bot
from dueros.card.TextCard import TextCard
import json
from dueros.directive.Display.template.ListTemplate1 import ListTemplate1
from dueros.directive.Display.template.ListTemplateItem import ListTemplateItem
from dueros.directive.Display.RenderTemplate import RenderTemplate
from dueros.directive.Display.Hint import Hint
from dueros.directive.AudioPlayer.Play import Play as AudioPlay
from dueros.directive.AudioPlayer.Stop import Stop as AudioStop
from dueros.directive.AudioPlayer.PlayBehaviorEnum import PlayBehaviorEnum
from dueros.directive.AudioPlayer.PlayerInfo import PlayerInfo
from dueros.directive.AudioPlayer.Control.PlayPauseButton import PlayPauseButton
from dueros.directive.AudioPlayer.Control.PreviousButton import PreviousButton
from dueros.directive.AudioPlayer.Control.NextButoon import NextButoon
from dueros.directive.AudioPlayer.Control.ShowPlayListButton import ShowPlayListButton
from dueros.directive.VideoPlayer.VideroPlayer import VideroPlayer
import base64

class Bot(Bot):

    def __init__(self, data):

        super(Bot, self).__init__(data)
        self.addLaunchHandler(self.launchRequest)
        self.addIntentHandler('video', self.videoIntent)
        self.addIntentHandler('audio', self.audioIntent)
        self.addIntentHandler('ai.dueros.common.choose_action', self.chooseIntent)
        # 意图6：暂停播放
        self.addIntentHandler('ai.dueros.common.pause_intent', self.pauseIntent)
        # 意图7：继续播放
        self.addIntentHandler('ai.dueros.common.continue_intent', self.continueIntent)
        # 意图8：返回指定界面
        self.addIntentHandler('back', self.backIntent)
        # 事件1：屏幕点击事件
        self.addIntentHandler('Display.ElementSelected', self.screenClickedEvent)
        # 事件2：音频播放结束事件
        self.addEventListener('AudioPlayer.PlaybackFinished', self.audioPlaybackFinished)
        # 事件3：视频播放结束事件
        self.addEventListener('VideoPlayer.PlaybackFinished', self.videoPlaybackFinished)
        # 事件4：音频上报
        self.addEventListener('AudioPlayer.ProgressReportIntervalElapsed', self.defaultEvent)
        # 事件5：视频上报
        self.addEventListener('VideoPlayer.ProgressReportIntervalElapsed', self.defaultEvent)
        # 事件6：兜底
        self.addDefaultEventListener('defaultEvent')
    pass


    def launchRequest(self):

        self.waitAnswer()
        template = self.__getHomeCard()
        speech = '欢迎使用平台样例演示，请试着说'
        reprompt= '没有听懂，可以直接对我想要使用的服务，例如'
        hint = Hint('视频')
        return {
            'outputSpeech': speech,
            'reprompt': reprompt,
            'directives': [hint, template]
        }

    def videoIntent(self):
        self.waitAnswer()
        videoName = self.getSlots('videoname')
        if videoName:
            video = self.getDetailBy('video', 'title', videoName)
            directives = self.getVideoPlay(video['id'])
            if directives:
                return {
                    'directives': directives
                }
            else:
                speech = '没有找到你要播放的视频'
                hint = Hint('第一个','我想看告白气球')
                template = self.getVideoCard()
                return {
                    'outputSpeech': speech,
                    'directives': [hint,template]
                }
        speech = '请选择您要播放的视频'
        reprompt = '没有听懂，请告诉我想要播放的视频'
        template = self.getVideoCard()

        # 定义hint指令
        hint = Hint('第一个', '我想看告白气球')
        return {
            'outputSpeech': speech,
            'reprompt': reprompt,
            'directives': [hint,template]
        }

    def audioIntent(self):

        self.waitAnswer()
        audioName = self.getSlots('audioname')
        if audioName:
            audio = self.getDetailBy('audio', 'title', audioName)
            directives = self.getAudioPlay(audio['id'])
            if directives:
                return {
                    'directives': directives
                }
            else:
                speech = "没有找到你要播放的视频";
                hint = Hint('第一个', '我想听告白气球')
                template = self.getAudioCard()
                return {
                    'outputSpeech': speech,
                    'directives': [hint, template]
                }
        speech = '请选择你想要听的歌曲'
        reprompt = '没有听懂，请告诉我想要听的歌曲'
        template = self.getAudioCard()

        #定义hint指令
        hint = Hint('第一个', '我想听告白')
        return {
            'outputSpeech': speech,
            'reprompt': reprompt,
            'directives': [hint, template]
        }

    def chooseIntent(self):
        self.waitAnswer()
        context = self.request.getScreenContext()
        token = context['template']['token']
        tokenArr = self.decodeToken(token)
        page = tokenArr['page']
        index = self.getSlots('index')

        audioPlayerContext = self.request.getAudioPlayerContext()
        videoPlayerContext = self.request.getVideoPlayerContext()
        audioToken = audioPlayerContext['token']
        videoToken = videoPlayerContext['token']
        audioTokenArr = self.decodeToken(audioToken)
        videoTokenArr = self.decodeToken(videoToken)

        if 'home' == page:
            if '1' == index:
                return self.videoIntent()
            if '2' == index:
                return self.audioIntent()

        if 'video' == page:
            directives = self.getAudioPlay(index)
            return {
                'directives': directives
            }

        if 'audio' == page:

            directives = self.getAudioPlay(index)
            return {
                'directives': directives
            }

    def pauseIntent(self):

        self.waitAnswer()
        self.setExpectSpeech(False)
        audioPlayerContext = self.request.getAudioPlayerContext()
        videoPlayerContext = self.request.getVideoPlayerContext()
        audioToken = audioPlayerContext['token']
        videoToken = videoPlayerContext['token']

        if audioPlayerContext:
            directive = AudioStop()
            return {
                'directives':[directive]
            }

        if videoPlayerContext:
            directive = AudioStop()
            return {
                'directives': [directive]
            }
        return self.defaultRes()

    def continueIntent(self):
        self.waitAnswer()
        audioPlayerContext = self.request.getAudioPlayerContext()
        videoPlayerContext = self.request.getVideoPlayerContext()
        if audioPlayerContext:
            audioToken = audioPlayerContext['token']
            audioTokenArr = self.decodeToken(audioToken)
            id = audioTokenArr['id']
            directives = self.getAudioPlay(id)
            return {
                'directives': directives
            }

        if videoPlayerContext:
            videoToken = videoPlayerContext['token']
            videoTokenArr = self.decodeToken(videoToken)
            id = videoTokenArr['id']
            directives = self.getAudioPlay(id)
            return {
                'directives': directives
            }

        return self.defaultRes()

    def screenClickedEvent(self):

        self.waitAnswer();
        data = self.request.getData();
        url = self.data['request']['token']
        if url:
            self.setExpectSpeech(False);
            return
        token = self.decodeToken(url)
        page = token['page']
        item = token['item']
        if page == 'home' and item == 'video':
            return self.videoIntent()

        if page == 'home' and item == 'audio':
            return self.audioIntent()

        if page == 'video':
            directives = self.getVideoPlay(item)
            return {
                'directives': directives
            }

        if page == 'audio':
            directives = self.getAudioPlay(item)
            return {
                'directives': directives
            }

    def audioPlaybackFinished(self, event):
        self.waitAnswer();
        self.setExpectSpeech(False);
        audioToken = event[0]['token']
        audioTokenArr = self.decodeToken(audioToken)
        if 'id' in audioTokenArr and audioTokenArr['index']:
            id = audioTokenArr['id'];
            id = int(id) +1;
            directives = self.getAudioPlay(id);
            return {
                'directives': directives
            }
        pass

    def videoPlaybackFinished(self, event):
        self.waitAnswer()
        self.setExpectSpeech(False)

        videoToken = event[0]['token']
        videoTokenArr = self.decodeToken(videoToken)

        if 'id' in videoTokenArr and videoTokenArr['index']:
            id = videoTokenArr['id']
            id = int(id) + 1
            directives = self.getVideoPlay(id)
            return {
                'directives': directives
            }


    def defaultEvent(self, event):
        self.waitAnswer()
        self.setExpectSpeech(False)

    def defaultRes(self):
        self.setExpectSpeech(False)
        return {
            'outputSpeech': '样例'
        }

    def getDetailBy(self, datatype, element, value):

        func = lambda data, element, value: data[element] if element in data and data[element] == value else False

        if 'video' == datatype:
            videoList = self.getPlayList(datatype)
            if videoList and type(videoList) == list:

                for video in videoList:
                    return func(video, element, value)

        if 'audio' == datatype:
            audioList = self.getPlayList(datatype)
            if audioList and type(audioList) == list:
                for audio in audioList:
                    return func(audio, element, value)
        return False

    def __loadData(self):
        with open("./data.json", 'r', encoding='utf-8') as load_f:
            return load_f.read()

    def getPlayList(self, type):
        list = json.loads(self.__loadData())
        func = lambda list, element: list[element] if element in list and list[element] else ''

        if type == "video":
            return func(list,"video")

        if type =="audio":
            return func(list, "audio")
        return list

    def getToken(self, token):

        # return str(base64.encodebytes(bytes(str(token), 'utf8')))
        return str(str(token))

    def decodeToken(self, token):

        # return base64.decodebytes(token)
        return str(str(token))

    def __getHomeCard(self):

        token = {'page':'home'}
        videoToken = {'page':'home','item':'video'}
        audioToken = {'page':'home','item':'audio'}
        IMAGE_VIDEO = 'http://dbp-resource.gz.bcebos.com/zhaojing_demo/1.jpg?authorization=bce-auth-v1%2Fbc881876e7a94578935a868716b6cf69%2F2018-05-29T06%3A43%3A48Z%2F-1%2Fhost%2F57cfa880c01aef30b0b2c258231c81f4f887da9db67f424ca22985ef84a69fd1'
        IMAGE_AUDIO = 'http://dbp-resource.gz.bcebos.com/zhaojing_demo/2.jpg?authorization=bce-auth-v1%2Fbc881876e7a94578935a868716b6cf69%2F2018-05-29T06%3A44%3A15Z%2F-1%2Fhost%2F63b930bae44a50b66940fc04ea617448506f690a86db4f90dc6b9d635e2b8ce3'

        listTemplate = ListTemplate1()
        listTemplate.setToken(self.getToken(token))
        listTemplate.setTitle('样例演示')

        listTemplateItem = ListTemplateItem()
        listTemplateItem.setToken(self.getToken(videoToken))
        listTemplateItem.setImage(IMAGE_AUDIO)
        listTemplateItem.setPlainPrimaryText('2aaa')
        listTemplate.addItem(listTemplateItem)
        directive = RenderTemplate(listTemplate)
        return directive

    def getAudioCard(self):

        listTemplate = ListTemplate1()

        tokenArr = {'page':'audio'}
        listTemplate.setToken(self.getToken(tokenArr))
        listTemplate.setTitle('音频实例')
        audioList = self.getPlayList('')
        if audioList and type(audioList)==list:

            func = lambda audio, element: audio[element] if element in audio and audio[element] else ''
            for audio in audioList:
                id = func(audio, 'id')
                title = func(audio, 'title')
                introduction = func(audio, 'intro')
                picUrl = func(audio, 'picurl')
                token = {'page':'audio', 'item':id}
                listTemplateItem = ListTemplateItem()
                listTemplateItem.setToken(self.getToken(token))
                listTemplateItem.setImage(picUrl)
                listTemplateItem.setPlainPrimaryText(title)
                listTemplateItem.setPlainSecondaryText(introduction)
                listTemplate.addItem(listTemplateItem)

        template = RenderTemplate(listTemplate)
        return template

    def getVideoPlay(self, id):

        self.setExpectSpeech(False)
        token = {'type':'video', 'id':id}

        video = self.getDetailBy('video', 'id', id)
        directives = []
        if video and type(video) == dict:
            directive = VideroPlayer(video['url'], PlayBehaviorEnum.REPLACE_ALL)
            directive.setReportIntervalInMs(10000)
            directive.setReportDelayInMs(10000)
            directive.setOffsetInMilliseconds(0)
            directive.setToken(self.__)
            hint = Hint('返回视频模板')
            directives = [directive, hint]
        return directives

    def getAudioPlay(self, id):
        self.setExpectSpeech(False)
        token = {'type':'audio', 'id':id}
        audio = self.getDetailBy('audio','id', id)
        directives = []
        if audio and type(audio)==dict:
            directive = AudioPlay(audio['url', PlayBehaviorEnum.REPLACE_ALL])
            directive.setOffsetInMilliSeconds(0)

            playerInfo = PlayerInfo()
            playpause = PlayPauseButton()
            previous = PreviousButton()
            next = NextButoon()
            showPlayList = ShowPlayListButton()
            showPlayList.setEnabled(False)
            controls = [playpause, previous, next, showPlayList]
            playerInfo.setControls(controls)
            playerInfo.setTitle(audio['title'])
            playerInfo.setTitleSubtext1(audio['intro'])
            directive.setPlayerInfo(playerInfo)
            directive.setToken(self.getToken(token))
            hint = Hint('返回音频模板')
            directives = [directive, hint]

        return directives

    def backIntent(self):
        pass

if __name__ == '__main__':

    bot = Bot()
    bot.getPlayList('video')

    pass
