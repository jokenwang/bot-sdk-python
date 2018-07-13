#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/31

"""
    desc:pass
"""
from dueros.directive.BaseDirective import BaseDirective
from dueros.directive.AudioPlayer.PlayBehaviorEnum import PlayBehaviorEnum
from dueros.Utils import Utils

class VideoPlayer(BaseDirective):

    def __init__(self, url, playBehavior = PlayBehaviorEnum.REPLACE_ALL):
        super(VideoPlayer, self).__init__('VideoPlayer.Play')
        self.data['playBehavior'] = playBehavior.value
        self.data['videoItem'] = {
            'videoItemId': self.genToken(),
            'stream':{
                'url': url,
                'offsetInMilliseconds': 0,
                'token': self.genToken()
            }
        }

    def setToken(self, token):
        if token:
            self.data['videoItem']['stream']['token'] = token

    def getToken(self):

        return self.data['videoItem']['stream']['token']

    def setUrl(self, url):

        if url:
            self.data['videoItem']['stream']['url'] = url

    def setOffsetInMilliseconds(self, milliseconds):

        if isinstance(milliseconds, str) and milliseconds.isdigit():
            milliseconds = int(milliseconds)

        if isinstance(milliseconds, int):
            self.data['videoItem']['stream']['offsetInMilliseconds'] = milliseconds

    def setExpiryTime(self, expiryTime):
        self.data['videoItem']['stream']['expiryTime'] = expiryTime

    def setReportDelayInMs(self, reportDelayMs):

        if isinstance(reportDelayMs, str) and reportDelayMs.isdigit():
            reportDelayMs = int(reportDelayMs)

        if isinstance(reportDelayMs, int) or isinstance(reportDelayMs, float):
            if not Utils.checkKeyInDict(self.data['videoItem']['stream'], 'progressReport'):
                self.data['videoItem']['stream']['progressReport'] = {}
            self.data['videoItem']['stream']['progressReport']['progressReportDelayInMilliseconds'] = int(reportDelayMs)

    def setReportIntervalInMs(self, intervalMs):

        if isinstance(intervalMs, str) and intervalMs.isdigit():
            intervalMs = int(intervalMs)

        if isinstance(intervalMs, int) or isinstance(intervalMs, float):

            if not Utils.checkKeyInDict(self.data['videoItem']['stream'], 'progressReport'):
                self.data['videoItem']['stream']['progressReport'] = {}

            self.data['videoItem']['stream']['progressReport']['progressReportIntervalInMilliseconds'] = int(intervalMs)

    def setExpectedPreviousToken(self, previousToken):

        self.data['videoItem']['stream']['expectedPreviousToken'] = previousToken


if __name__ == '__main__':
    pass