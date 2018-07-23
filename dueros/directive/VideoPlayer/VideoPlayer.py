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

    def __init__(self, url, play_behavior=PlayBehaviorEnum.REPLACE_ALL):

        super(VideoPlayer, self).__init__('VideoPlayer.Play')
        self.data['playBehavior'] = play_behavior
        self.data['videoItem'] = {
            'videoItemId': self.gen_token(),
            'stream': {
                'url': url,
                'offsetInMilliseconds': 0,
                'token': self.gen_token()
            }
        }

    def set_token(self, token):
        if token:
            self.data['videoItem']['stream']['token'] = token

    def get_token(self):

        return self.data['videoItem']['stream']['token']

    def set_url(self, url):

        if url:
            self.data['videoItem']['stream']['url'] = url

    def set_offset_in_milliseconds(self, milliseconds):

        if isinstance(milliseconds, str) and milliseconds.isdigit():
            milliseconds = int(milliseconds)

        if isinstance(milliseconds, int):
            self.data['videoItem']['stream']['offsetInMilliseconds'] = milliseconds

    def set_expiry_time(self, expiry_time):
        self.data['videoItem']['stream']['expiryTime'] = expiry_time

    def set_report_delay_in_ms(self, report_delay_in_ms):

        if isinstance(report_delay_in_ms, str) and report_delay_in_ms.isdigit():
            report_delay_in_ms = int(report_delay_in_ms)

        if isinstance(report_delay_in_ms, int) or isinstance(report_delay_in_ms, float):
            if not Utils.checkKeyInDict(self.data['videoItem']['stream'], 'progressReport'):
                self.data['videoItem']['stream']['progressReport'] = {}
            self.data['videoItem']['stream']['progressReport']['progressReportDelayInMilliseconds'] = int(report_delay_in_ms)

    def set_report_interval_in_ms(self, interval_ms):

        if isinstance(interval_ms, str) and interval_ms.isdigit():
            interval_ms = int(interval_ms)

        if isinstance(interval_ms, int) or isinstance(interval_ms, float):

            if not Utils.checkKeyInDict(self.data['videoItem']['stream'], 'progressReport'):
                self.data['videoItem']['stream']['progressReport'] = {}

            self.data['videoItem']['stream']['progressReport']['progressReportIntervalInMilliseconds'] = int(interval_ms)

    def set_expected_previous_token(self, previous_token):

        self.data['videoItem']['stream']['expectedPreviousToken'] = previous_token


if __name__ == '__main__':
    pass