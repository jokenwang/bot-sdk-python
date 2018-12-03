#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/19

"""
    desc:pass
"""
import unittest

from dueros.directive.Display.RenderAudioPlayerInfo import RenderAudioPlayerInfo
from dueros.directive.AudioPlayer.AudioPlayerInfoContent import AudioPlayerInfoContent
from dueros.directive.AudioPlayer.Control.PlayPauseButton import PlayPauseButton
from dueros.directive.AudioPlayer.Control.RepeatButton import RepeatButton

import json
class RenderAudioPlayerInfoTest(unittest.TestCase):

    def setUp(self):
        self.renderAudioPlayerInfo = RenderAudioPlayerInfo()
        pass

    def testGetData(self):

        with open('../../json/render_audio.json', encoding='utf-8') as f:
            content = f.read()
            self.data = json.loads(content)

        print(self.data)
        content = AudioPlayerInfoContent()
        content.set_title('title')
        content.set_title_sub_text1('titleSubtext1')
        content.set_title_sub_text2('titleSubtext2')
        content.set_lyric('www.lyric.com')
        content.set_media_length_in_ms(10000)
        content.set_art('www.art.com')
        content.set_provider('provider', 'www.logo.com')

        playPauseButton = PlayPauseButton()
        repeatButton = RepeatButton()
        controls = [playPauseButton,repeatButton]

        self.renderAudioPlayerInfo.set_token('test_token')
        self.renderAudioPlayerInfo.set_content(content)
        self.renderAudioPlayerInfo.set_controls(controls)
        self.assertEqual(self.renderAudioPlayerInfo.get_data(), self.data)
    pass


if __name__ == '__main__':
    pass