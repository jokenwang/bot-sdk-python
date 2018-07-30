#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2017/12/31

"""
用于生成Play指令的类
详见文档：https://dueros.baidu.com/didp/doc/dueros-bot-platform/dbp-custom/audioplayer_markdown#AudioPlayer.Play%E6%8C%87%E4%BB%A4
"""

from dueros.directive.BaseDirective import BaseDirective
from dueros.directive.AudioPlayer.PlayBehaviorEnum import PlayBehaviorEnum
from dueros.directive.AudioPlayer.StreamFormatEnum import StreamFormatEnum
from dueros.directive.AudioPlayer.PlayerInfo import PlayerInfo
from dueros.directive.AudioPlayer.Control.PlayPauseButton import PlayPauseButton
from dueros.directive.AudioPlayer.Control.PreviousButton import PreviousButton
from dueros.directive.AudioPlayer.Control.NextButton import NextButton
from dueros.Utils import Utils


class Play(BaseDirective):

    def __init__(self, url, play_behavior=PlayBehaviorEnum.REPLACE_ALL):
        '''

        :param url:     音频播放地址
        :param playBehavior: REPLACE_ALL: 立即停止当前播放并清除播放队列，立即播放指令中的audio item。
                             ENQUEUE: 将audio item添加到当前队列的尾部。
                             REPLACE_ENQUEUED: 替换播放队列中的所有audio item，但不影响当前正在播放的audio item。
        '''

        super(Play, self).__init__('AudioPlayer.Play')
        self.data['playBehavior'] = play_behavior.value
        self.data['audioItem'] = {
            'stream': {
                'streamFormat': StreamFormatEnum.STREAM_FORMAT_MP3.value,
                'url': url,
                'offsetInMilliSeconds': 0,
                'token': self.gen_token()
            }
        }

    def set_play_behavior(self, play_behavior):

        if isinstance(play_behavior, PlayBehaviorEnum):
            self.data['playBehavior'] = play_behavior.value

    def set_player_info(self, player_info):

        if isinstance(player_info, PlayerInfo):
            self.data['audioItem']['playerInfo'] = player_info.get_data()

    def set_token(self, token):
        if token:
            self.data['audioItem']['stream']['token'] = token
        return self

    def get_token(self):
        return Utils.get_dict_data_by_keys(self.data,['audioItem','stream','token'])

    def set_url(self, url):
        if url:
            self.data['audioItem']['stream']['url'] = url
        return self

    def set_offset_in_milliseconds(self, milliseconds):
        '''
        设置directive的属性。从指定的offset开始进行播放
        :param milliseconds:    毫秒数。比如5分钟的歌曲，播放的长度是5*60*1000毫秒，选择起始的播放位置
        :return:
        '''
        if milliseconds.isdigit():
            milli_seconds = int(milliseconds)
            self.data['audioItem']['stream']['offsetInMilliSeconds'] = milli_seconds
        return self

    def set_progress_report_interval_ms(self, interval_ms):
        '''
        设置directive的属性。定时上报事件的间隔时间
        :param interval_ms:  毫秒数。
        :return:
        '''
        if interval_ms.isdigit():
            interval_ms = int(interval_ms)
            self.data['audioItem']['stream']['progressReportIntervalMs'] = interval_ms
        return self

    def set_stream_format(self, stream_format=StreamFormatEnum.STREAM_FORMAT_MP3):
        '''
        设置directive的属性。音频流格式，streamFormat 默认STREAM_FORMAT_MP3
        :param stream_format:    取值: STREAM_FORMAT_MP3、STREAM_FORMAT_M3U8、STREAM_FORMAT_M4A
        :return:
        '''
        if StreamFormatEnum.inEnum(stream_format):
            self.data['audioItem']['stream']['streamFormat'] = stream_format.value
        else:
            self.data['audioItem']['stream']['streamFormat'] = StreamFormatEnum.STREAM_FORMAT_MP3.value
        return self


if __name__ == '__main__':
    directive = Play('http://www.baidu.com')
    directive.set_stream_format('AUDIO_M3U8')

    playerInfo = PlayerInfo()

    # 创建暂停按钮
    playpause = PlayPauseButton()
    previous = PreviousButton()
    previous.set_selected(True)
    controls = [playpause, previous]
    playerInfo.set_controls(controls)
    playerInfo.set_controls(NextButton())

    playerInfo.set_title('周杰伦')
    playerInfo.set_title_subtext1('七里香')
    playerInfo.set_art('http://adfadfa')

    # 设置Play指令的PlayerInfo
    directive.set_player_info(playerInfo)
    print(directive.get_data())

