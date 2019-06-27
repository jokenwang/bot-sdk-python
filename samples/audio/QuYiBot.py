#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/19

"""
    desc:pass
"""
import requests
import sys
import json
from dueros.Bot import Bot
from dueros.directive.Display.RenderTemplate import RenderTemplate
from dueros.directive.Display.Hint import Hint
from dueros.directive.Display.template.ListTemplate1 import ListTemplate1
from dueros.directive.Display.template.ListTemplateItem import ListTemplateItem
from dueros.directive.Display.template.BodyTemplate1 import BodyTemplate1
from dueros.directive.AudioPlayer.Play import Play
from dueros.directive.AudioPlayer.PlayerInfo import PlayerInfo
from dueros.directive.AudioPlayer.Control.PreviousButton import PreviousButton
from dueros.directive.AudioPlayer.Control.PlayPauseButton import PlayPauseButton
from dueros.directive.AudioPlayer.Control.NextButton import NextButton
from dueros.directive.AudioPlayer.Control.ShowPlayListButton import ShowPlayListButton
from dueros.directive.Display.RenderAudioList import RenderAudioList
from dueros.directive.Display.media.AudioItem import AudioItem
from dueros.directive.AudioPlayer.AudioPlayerInfo import AudioPlayerInfo
from dueros.directive.AudioPlayer.AudioPlayerInfoContent import AudioPlayerInfoContent
from dueros.directive.Display.template.ListTemplate3 import ListTemplate3
from dueros.directive.Display.tag.FreeTag import FreeTag
from dueros.directive.Display.tag.AuditionTag import AuditionTag

class QuYiBot(Bot):

    def __init__(self, data):
        super(QuYiBot, self).__init__(data)
        self.add_launch_handler(self.launch_request)

        self.add_intent_handler('com.jack.dbp.quyi.index', self.handle_index)
        self.add_intent_handler('com.jack.dbp.move.help', self.handle_move_help)

        self.add_intent_handler('ai.dueros.common.default_intent', self.handle_default_intent)
        self.add_intent_handler('ai.dueros.common.stop_intent', self.ended)
        self.add_intent_handler('ai.dueros.common.previous_intent', self.handle_common_previous)
        self.add_intent_handler('ai.dueros.common.next_intent', self.handle_common_next)
        # self.add_intent_handler('ai.dueros.common.pause_intent', self.handle_common_pause)
        self.add_intent_handler('ai.dueros.common.continue_intent', self.handle_common_continue)
        self.add_session_ended_handler(self.ended)

        self.add_event_listener('AudioPlayer.Stop', self.handle_audio_stop)
        self.add_event_listener('AudioPlayer.Play', self.handle_audio_start)
        self.add_event_listener('AudioPlayer.PlaybackStarted', self.handle_audio_playback_start)
        self.add_event_listener('AudioPlayer.PlaybackStopped', self.handle_audio_playback_stop)
        self.add_event_listener('AudioPlayer.PlaybackFinished', self.handle_audio_playback_finish)
        self.add_event_listener('AudioPlayer.PlaybackNearlyFinished', self.handle_audio_playback_near_finish)
        self.add_event_listener('Display.ElementSelected', self.handle_display_element_selected)
        self.add_event_listener('Form.ButtonClicked', self.handle_form_button_click)
        self.add_event_listener('Display.ButtonClicked', self.handle_display_button_click)

    def launch_request(self):
        """
        打开调用名
        """
        self.wait_answer()
        self.set_expect_speech(False)
        first_audio = fetch_data()[0]
        self.set_session_attribute('audio_current_list_index', 0, 0)
        # return build_audio_play(0, first_audio)
        return self.build_play_list_by_id_1()

    def handle_index(self):
        self.wait_answer()
        index = self.get_slots('index')
        if not index:
            self.ask('index')
            return {
                'outputSpeech': '请您告诉我要播放第几个。比如:播放第一个'
            }
        else:
            audios = fetch_data()
            index = int(index)
            length = len(audios)
            if index > length:
                self.ask('index')
                return {
                    'outputSpeech': '抱歉，超出了曲艺总数量，请您重新告诉我要播放第几个'
                }
            else:
                item = audios[index - 1]
                self.set_expect_speech(False)
                return self.warp_build_audio_player(index - 1, item)

    def handle_audio_start(self, event):
        self.wait_answer()
        self.set_expect_speech(False)

        print
        'audio start'

    def handle_audio_stop(self, event):
        self.wait_answer()
        self.set_expect_speech(False)

        print
        'audio stop'

    def handle_audio_playback_start(self, event):
        self.wait_answer()
        self.set_expect_speech(False)

        print
        'playback_start'
        pass

    def handle_audio_playback_stop(self, event):
        self.wait_answer()
        self.set_expect_speech(False)

        print
        'playback_stop'
        pass

    def handle_audio_playback_finish(self, event):

        self.wait_answer()
        self.set_expect_speech(False)

        print
        'playback_finish'
        return self.build_prev_next('NEXT')
        pass

    def handle_audio_playback_near_finish(self, event):
        self.wait_answer()
        self.set_expect_speech(False)

        pass

    def handle_common_next(self):
        self.wait_answer()
        self.set_expect_speech(False)
        return self.build_prev_next('NEXT')

    def handle_common_previous(self):
        self.wait_answer()
        self.set_expect_speech(False)
        return self.build_prev_next('PREVIOUS')

    def handle_common_continue(self):
        pass

    def handle_display_button_click(self, event):
        """
        点击事件
        :param event:
        :return:
        """
        self.wait_answer()
        self.set_expect_speech(False)
        print
        '=================handle_display_button_click================'

        print
        event

    def handle_display_element_selected(self, event):
        """
        选择事件
        :param event:
        :return:
        """
        self.wait_answer()
        self.set_expect_speech(False)
        print
        '=================handle_display_element_selected================'
        if event:
            token = event['token']
            datas = token.split(':')
            token_type = datas[0]
            token_data = datas[1]

            if 'playlist' == token_type:
                index = int(token_data)
                return self.warp_build_audio_player(index, fetch_data()[index])

    def warp_build_audio_player(self, index, item):
        self.set_session_attribute('audio', item, '')
        self.set_session_attribute('audio_current_list_index', index, '1')
        return build_audio_play(index, item)

    def handle_form_button_click(self, event):
        """
        播放页面的点击事件
        :param event:
        :return:
        """
        self.wait_answer()
        self.set_expect_speech(False)
        if event:
            button_name = event['name']
            if 'SHOW_PLAYLIST' == button_name:
                return self.build_play_list_by_id_1()
                pass
            elif 'NEXT' == button_name or 'PREVIOUS' == button_name:
                return self.build_prev_next(button_name)

    def build_play_list_by_id(self):
        datas = fetch_data()
        directive = RenderAudioList('aaa')
        index = 0
        for data in datas:
            item = AudioItem(data['audio_name'], data['audio_name'])
            item.set_favorited(False)
            token = 'playlist:%s' % index
            item.set_token(token)
            index = index + 1
            directive.add_audio_item(item)

        return {
            'directives': [directive]
        }

    def build_play_list_by_id_1(self):
        datas = fetch_data()
        template = ListTemplate3()
        template.set_title("sdasdfas")
        template.set_background_image(BG)
        index = 0
        for data in datas:
            item = ListTemplateItem()
            # item.set_plain_primary_text(data['audio_name'])
            item.set_image(BG)
            item.set_content(data['audio_name'])
            # if index % 2 == 0:
            #     tag = AuditionTag()
            #     item.set_image_tags(tag)
            # AudioItem(data['audio_name'], data['audio_name'])
            # item.set_favorited(False)
            token = 'playlist:%s' % index
            item.set_token(token)
            index = index + 1
            # directive.add_audio_item(item)
            template.add_item(item)
        directive = RenderTemplate(template)

        return {
            'directives': [directive]
        }


    def build_prev_next(self, button_name):
        index = self.get_session_attribute('audio_current_list_index', 0)
        datas = fetch_data()
        current_index = int(index)
        if 'NEXT' == button_name:
            current_index = int(index) + 1
            if current_index > len(datas):
                return {
                    'outputSpeech': '已是最后一个了'
                }
        elif 'PREVIOUS' == button_name:
            current_index = int(index) - 1
            if current_index < 0:
                return {
                    'outputSpeech': '已是第一个了'
                }
        item = datas[current_index]
        print
        current_index
        self.set_session_attribute('audio_current_list_index', current_index, 0)
        return build_audio_play(current_index, item)

    def ended(self):
        """
        关闭
        :return:
        """
        self.end_session()
        return {
            'outputSpeech': '欢迎再次使用最新影讯！！'
        }

    def handle_default_intent(self):

        self.wait_answer()
        return {
            'outputSpeech': '抱歉，我没听清，请您再说一次 或 对我说:帮助！！'
        }

    def handle_move_help(self):
        self.wait_answer()
        template = BodyTemplate1()
        template.set_background_image(BG)
        content = '技能帮助如下：\n' \
                  '第一:您要先选择查看哪个城市的影讯,比如:"查看北京的"。\n' \
                  '第二:之后选择查看哪部电影的信息,比如:"查看第一个".\n' \
                  '第三:您可以查看选中电影的主要演员列表和预告片,比如:"查看演员列表或者播放预告片"\n' \
                  '第四:如果您想回到列表页面,可以对我说:"返回列表页"\n'
        template.set_plain_text_content(content)
        directive = RenderTemplate(template)

        hint = Hint(['查看北京的'])
        directives = []
        directives.append(hint)
        directives.append(directive)

        return {
            'directives': directives,
            'outputSpeech': content + '您可以在任何时候对我说:"帮助" 来获取帮助信息。现在请您告诉我要查看哪个城市的影讯'
        }


def build_audio_play(index, audio):
    audio_url = audio['audio_path']
    directive = Play(audio_url)
    audio_content = AudioPlayerInfoContent()
    audio_content.set_title(audio['audio_name'])
    audio_content.set_title_subtext1(audio['audio_name'])
    audio_content.set_art(
        'http://imagev2.xmcdn.com/group10/M0B/85/50/wKgDZ1YgthSi0SHEAACtQo3lZK8096.jpg!op_type=5&upload_type=header&device_type=ios&name=web_x_large&strip=0&quality=7')
    previous = PreviousButton()
    pause = PlayPauseButton()
    next = NextButton()
    play_list = ShowPlayListButton()
    play_info = AudioPlayerInfo(audio_content, [previous, pause, next, play_list])
    directive.set_player_info(play_info)
    token = 'playlist:%s' % index
    directive.set_token(token)
    hint = Hint(['下一个/上一个'])
    return {
        'directives': [hint, directive],
        'outputSpeech': '即将播放:%s' % audio['audio_name']
    }


def fetch_data():
    url = 'http://106.12.27.65/yeting/data.json'
    response = requests.get(url)
    # request = urllib2.Request(url)
    # response = urllib2.urlopen(request).read()
    return json.loads(response.text, encoding='utf-8')['data']


BG = 'http://dbp-resource.gz.bcebos.com/152b61ac-a449-a96b-4b1a-be594d6a4d5a/7a73b9e4dfb6281155df1aca2eac4b17.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-08-31T14%3A42%3A44Z%2F-1%2F%2Fbcf8534aaac8cff3544a25d5f9f557d51a564c557505e8ce4ff86ccdf2adfebb'


if __name__ == '__main__':
    print(fetch_data())
    pass