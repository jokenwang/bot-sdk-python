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
            'stream': {
                'url': url,
                'offsetInMilliseconds': 0,
                'token': self.gen_token()
            }
        }

    def set_token(self, token):
        """
        设置视频token, 注:此token会关联播放列表中每个item的token, 当token相同时item会标记为当前正在播放
        :param token:
        :return:
        """
        if token:
            self.data['videoItem']['stream']['token'] = token

    def get_token(self):
        """
        获取token
        :return:
        """
        return self.data['videoItem']['stream']['token']

    def set_url(self, url):
        """
        设置视频地址
        :param url:
        :return:
        """
        if isinstance(url, str):
            self.data['videoItem']['stream']['url'] = url

    def set_offset_in_milliseconds(self, milliseconds):
        """
        指定从当前offset播放视频
        :param milliseconds:
        :return:
        """
        milliseconds = Utils.convert_number(milliseconds)
        if milliseconds:
            self.data['videoItem']['stream']['offsetInMilliseconds'] = milliseconds

    def set_expiry_time(self, expiry_time):
        """
        ISO8601格式，表示stream过期时间
        :param expiry_time:
        :return:
        """
        if isinstance(expiry_time, str):
            self.data['videoItem']['stream']['expiryTime'] = expiry_time

    def set_report_delay_in_ms(self, report_delay_ms):
        """
        设置directive的属性。如果此字段存在，则设备端在播放该video item时，
        播放到所指定时间之后应该上报ProgressReportDelayElapsed事件；
        如果此字段不存在，则设备端端不需要上报ProgressReportDelayEsapsed事件
        :param report_delay_ms:
        :return:
        """
        report_delay_ms = Utils.convert_number(report_delay_ms)
        if report_delay_ms:
            if 'progressReport' not in self.data['videoItem']['stream']:
                self.data['videoItem']['stream']['progressReport'] = {}

            self.data['videoItem']['stream']['progressReport']['progressReportDelayInMilliseconds'] = int(report_delay_ms)

    def set_report_interval_in_ms(self, interval_ms):
        """
        设置directive的属性。定时上报事件的间隔时间,
        如果此字段存在，则设备端在播放该video item时，每隔指定时间上报ProgressReportIntervalElapsed事件；
        如果此字段不存在，则设备端不需要上报ProgressReportIntervalElapsed事件
        :param interval_ms:
        :return:
        """
        interval_ms = Utils.convert_number(interval_ms)
        if interval_ms:
            if 'progressReport' not in self.data['videoItem']['stream']:
                self.data['videoItem']['stream']['progressReport'] = {}
            self.data['videoItem']['stream']['progressReport']['progressReportIntervalInMilliseconds'] = int(interval_ms)

    def set_expected_previous_token(self, previous_token):
        """
        设置directive的属性。如果此字段存在，则应当匹配前一个video item中的token，如果不匹配则不执行本Play指令
        :param previous_token:
        :return:
        """
        self.data['videoItem']['stream']['expectedPreviousToken'] = previous_token

    def set_title(self, title):
        """
        设置视频标题
        :param title:
        :return:
        """
        if isinstance(title, str):
            self.data['videoItem']['title'] = title


if __name__ == '__main__':
    pass