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

class VideroPlayer(BaseDirective):

    def __init__(self, url, playBehavior = PlayBehaviorEnum.REPLACE_ALL):
        super(VideroPlayer, self).__init__('VideoPlay.Play')
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

        if isinstance(reportDelayMs, int):
            if not Utils.checkKeyInDict(self.data['videoItem']['stream'], 'progressReport'):
                self.data['videoItem']['stream']['progressReport'] = {}
            self.data['videoItem']['stream']['progressReport']['progressReportDelayInMilliseconds'] = reportDelayMs

    def setReportIntervalInMs(self, intervalMs):

        if isinstance(intervalMs, str) and intervalMs.isdigit():
            intervalMs = int(intervalMs)

        if isinstance(intervalMs, int):

            if not Utils.checkKeyInDict(self.data['videoItem']['stream'], 'progressReport'):
                self.data['videoItem']['stream']['progressReport'] = {}

            self.data['videoItem']['stream']['progressReport']['progressReportIntervalInMilliseconds'] = intervalMs

    def setExpectedPreviousToken(self, previousToken):

        self.data['videoItem']['stream']['expectedPreviousToken'] = previousToken


if __name__ == '__main__':
    pass