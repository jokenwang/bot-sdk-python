#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2017/12/31 上午12:25

"""
    用于生成Play指令的类
"""

from dueros.directive.BaseDirective import BaseDirective


class Play(BaseDirective):

    # TODO 常量移走
    REPLACE_ALL = 'REPLACE_ALL'
    REPLACE_ENQUEUED = 'REPLACE_ENQUEUED'
    ENQUEUE = 'ENQUEUE'
    STREAM_FORMAT_MP3 = 'AUDIO_MP3'
    STREAM_FORMAT_M3U8 = 'AUDIO_M3U8'
    STREAM_FORMAT_M4A = 'AUDIO_M4A'

    def __init__(self, url, playBehavior = 'REPLACE_ALL'):
        '''

        :param url:     音频播放地址
        :param playBehavior: REPLACE_ALL: 立即停止当前播放并清除播放队列，立即播放指令中的audio item。
                             ENQUEUE: 将audio item添加到当前队列的尾部。
                             REPLACE_ENQUEUED: 替换播放队列中的所有audio item，但不影响当前正在播放的audio item。
        '''

        super(Play, self).__init__('AudioPlayer.Play')

        self.data['playBehavior'] = playBehavior
        self.data['audioItem'] = {
            'stream': {
                'streamFormat': self.STREAM_FORMAT_MP3,
                'url': url,
                'offsetInMilliSeconds': 0,
                'token': self.genToken()
            }
        }

    def setToken(self, token):
        if token:
            self.data['audioItem']['stream']['token'] = token
        return self

    def getToken(self):
        return self.data['audioItem']['stream']['token']


    def setUrl(self, url):
        if url:
            self.data['audioItem']['stream']['url'] = url
        return self

    def setOffsetInMilliSeconds(self, milliSeconds):
        '''
        设置directive的属性。从指定的offset开始进行播放
        :param milliSeconds:    毫秒数。比如5分钟的歌曲，播放的长度是5*60*1000毫秒，选择起始的播放位置
        :return:
        '''
        if milliSeconds.isdigit():
            milliSeconds = int(milliSeconds)
            self.data['audioItem']['stream']['offsetInMilliSeconds'] = milliSeconds
        return self

    def setProgressReportIntervalMs(self, intervalMs):
        '''
        设置directive的属性。定时上报事件的间隔时间
        :param intervalMs:  毫秒数。
        :return:
        '''
        if intervalMs.isdigit():
            intervalMs = int(intervalMs)
            self.data['audioItem']['stream']['progressReportIntervalMs'] = intervalMs
        return self

    def setStreamFormat(self, streamFormat = 'AUDIO_MP3'):
        '''
        设置directive的属性。音频流格式，streamFormat 默认STREAM_FORMAT_MP3
        :param streamFormat:    取值: STREAM_FORMAT_MP3、STREAM_FORMAT_M3U8、STREAM_FORMAT_M4A
        :return:
        '''
        streamFormatArray = ['AUDIO_MP3', 'AUDIO_M3U8', 'AUDIO_M4A']

        if streamFormat in streamFormatArray:
            self.data['audioItem']['stream']['streamFormat'] = streamFormat
        return self


if __name__ == '__main__':

    play = Play('http://www.baidu.com')
    play.setStreamFormat('AUDIO_M3U8')
    print(play.getData())

