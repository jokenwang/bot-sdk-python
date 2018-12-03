#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/31

"""
VideoPlayer视频播放
详见文档：https://dueros.baidu.com/didp/doc/dueros-bot-platform/dbp-custom/videoplayer_markdown#VideoPlayer.Play%E6%8C%87%E4%BB%A4
"""
from dueros.directive.BaseDirective import BaseDirective
from dueros.directive.AudioPlayer.PlayBehaviorEnum import PlayBehaviorEnum
from dueros.Utils import Utils


class VideoPlayer(BaseDirective):

    def __init__(self, url, play_behavior=PlayBehaviorEnum.REPLACE_ALL):
        super(VideoPlayer, self).__init__('VideoPlayer.Play')
        self.data['playBehavior'] = play_behavior.value
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

        milliseconds = Utils.convert_number(milliseconds)
        if milliseconds:
            self.data['videoItem']['stream']['offsetInMilliseconds'] = milliseconds

    def set_expiry_time(self, expiry_time):
        if isinstance(expiry_time, str):
            self.data['videoItem']['stream']['expiryTime'] = expiry_time

    def set_report_delay_in_ms(self, report_delay_ms):
        report_delay_ms = Utils.convert_number(report_delay_ms)
        if report_delay_ms:
            if 'progressReport' not in self.data['videoItem']['stream']:
                self.data['videoItem']['stream']['progressReport'] = {}

            self.data['videoItem']['stream']['progressReport']['progressReportDelayInMilliseconds'] = int(report_delay_ms)

    def set_report_interval_in_ms(self, interval_ms):
        interval_ms = Utils.convert_number(interval_ms)
        if interval_ms:
            if 'progressReport' not in self.data['videoItem']['stream']:
                self.data['videoItem']['stream']['progressReport'] = {}
            self.data['videoItem']['stream']['progressReport']['progressReportIntervalInMilliseconds'] = int(interval_ms)

    def set_expected_previous_token(self, previous_token):
        self.data['videoItem']['stream']['expectedPreviousToken'] = previous_token


if __name__ == '__main__':
    pass