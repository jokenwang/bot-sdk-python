#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/31

"""
    desc:pass
"""
from dueros.directive.BaseDirective import BaseDirective
from dueros.directive.AudioPlayer.PlayBehaviorEnum import PlayBehaviorEnum

class VideroPlayer(BaseDirective):

    def __init__(self, url, playBehavior = PlayBehaviorEnum.REPLACE_ALL):
        super(VideroPlayer, self).__init__('VideoPlay.Play')
        self.data['playBehavior'] = playBehavior.value
        self.data['videoItem'] = {
            'videoItemId': self.getToken(),
            'stream': {
                'url': url,
                'offsetInMilliseconds': 0,
                'token': self.getToken()
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

        if milliseconds.isdigit():
            milliseconds = int(milliseconds)
            self.data['videoItem']['stream']['offsetInMilliseconds'] = milliseconds

    def setExpiryTime(self, expiryTime):
        self.data['videoItem']['stream']['expiryTime'] = expiryTime

    def setReportDelayInMs(self, reportDelayMs):
        self.data['videoItem']['stream']['progressReport']['progressReportDelayInMilliseconds'] = int(reportDelayMs)

    def setReportIntervalInMs(self, intervalMs):
        self.data['videoItem']['stream']['progressReport']['progressReportIntervalInMilliseconds'] = int(intervalMs)

    def setExpectedPreviousToken(self, previousToken):
        self.data['videoItem']['stream']['expectedPreviousToken'] = previousToken


if __name__ == '__main__':
    pass