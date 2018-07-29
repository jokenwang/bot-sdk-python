#!/usr/bin/env python2
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
from dueros.directive.AudioPlayer.PlayerInfo import PlayerInfo
from dueros.directive.AudioPlayer.PlayBehaviorEnum import PlayBehaviorEnum
from dueros.directive.AudioPlayer.Control.PlayPauseButton import PlayPauseButton
from dueros.directive.AudioPlayer.Control.PreviousButton import PreviousButton
from dueros.directive.AudioPlayer.Control.NextButton import NextButton
from dueros.directive.AudioPlayer.Control.ShowPlayListButton import ShowPlayListButton

class Bot(Bot):
    '''
    自定义的BOT函数
    '''
    def launchRequest(self):
        '''
        打开调用名
        '''
        self.wait_answer()
        return {
            'outputSpeech': r'欢迎进入'
        }

    def audioPlay(self):
        '''
        播放指令
        '''
        directives = []
        directive1 = Play('http://audio.xmcdn.com/group27/M07/91/30/wKgJW1kVpTTysDS9ABG_opoNMoA008.m4a', PlayBehaviorEnum.REPLACE_ALL)
        playerInfo = PlayerInfo()
        playerInfo.set_title('Python')
        playerInfo.set_title_subtext1('python')
        playerInfo.set_art('https://imagev2.xmcdn.com/group26/M03/94/DD/wKgJWFkVpOyzKhU_AABPh3rraa8772.jpg!op_type=5&upload_type=cover&device_type=ios&name=web_meduim&strip=0&quality=7')

        playpause = PlayPauseButton()
        previous = PreviousButton()
        next = NextButton()
        showPlayList = ShowPlayListButton()
        showPlayList.set_enabled(False)
        controls = [playpause, previous, next, showPlayList]
        # controls = [playpause, previous]
        playerInfo.set_controls(controls)
        # playerInfo.add_control(NextButton())
        directive1.set_player_info(playerInfo)


        # directive2 = Play('http://audio.xmcdn.com/group27/M04/91/28/wKgJW1kVpMfRrzE5AAzyjIkEf9s698.m4a', PlayBehaviorEnum.ENQUEUE)
        # playerInfo = PlayerInfo()
        # playerInfo.set_title('子夜吴歌')
        # playerInfo.set_art(
        #     'https://imagev2.xmcdn.com/group26/M03/94/DD/wKgJWFkVpOyzKhU_AABPh3rraa8772.jpg!op_type=5&upload_type=cover&device_type=ios&name=web_meduim&strip=0&quality=7')
        # playpause = PlayPauseButton()
        # previous = PreviousButton()
        # previous.set_selected(True)
        # controls = [playpause, previous]
        # playerInfo.set_controls(controls)
        # playerInfo.add_control(NextButton())
        # directive2.set_player_info(playerInfo)
        # directive3 = Play('http://audio.xmcdn.com/group27/M04/91/28/wKgJW1kVpMfRrzE5AAzyjIkEf9s698.m4a', PlayBehaviorEnum.ENQUEUE)
        #
        # playerInfo = PlayerInfo()
        # playerInfo.set_title('子夜吴歌')
        # playerInfo.set_art(
        #     'https://imagev2.xmcdn.com/group26/M03/94/DD/wKgJWFkVpOyzKhU_AABPh3rraa8772.jpg!op_type=5&upload_type=cover&device_type=ios&name=web_meduim&strip=0&quality=7')
        # playpause = PlayPauseButton()
        # previous = PreviousButton()
        # previous.set_selected(True)
        # controls = [playpause, previous]
        # playerInfo.set_controls(controls)
        # playerInfo.add_control(NextButton())
        # directive3.set_player_info(playerInfo)
        directives.append(directive1)
        # directives.append(directive2)
        # directives.append(directive3)

        return {
            'directives' : directives,
            'outputSpeech': r'正在为你播放歌曲'
        }

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
        # directives = []
        # directive = Play('http://audio.xmcdn.com/group27/M04/91/28/wKgJW1kVpMfRrzE5AAzyjIkEf9s698.m4a')
        # directives.append(directive)
        pass

    def playBackNearlyFinished(self, event):
        '''
        处理事件上报示例
        '''
        directives = []
        directive = Play('http://audio.xmcdn.com/group27/M07/91/2E/wKgJW1kVpSnwiF91AA7biCK_BT0527.m4a',
                         PlayBehaviorEnum.ENQUEUE)
        directives.append(directive)
        return {
            'directives': directives
        }

    def progressReportIntervalElapsed(self, event):

        pass

    def buttonClicked(self, event):
        print(event)
        pass

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
        self.add_event_listener('AudioPlayer.PlaybackNearlyFinished', self.playBackNearlyFinished)
        self.add_event_listener('AudioPlayer.ProgressReportIntervalElapsed', self.progressReportIntervalElapsed)
        self.add_event_listener('Form.ButtonClicked', self.buttonClicked)
        self.add_event_listener('AudioPlayer.PlaybackStopped', self.progressReportIntervalElapsed)



if __name__ == '__main__':
    pass
