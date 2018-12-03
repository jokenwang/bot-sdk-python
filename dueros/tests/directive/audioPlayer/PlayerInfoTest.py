#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/7/20

"""
    desc:pass
"""
import unittest
from dueros.directive.AudioPlayer.PlayerInfo import PlayerInfo
from dueros.directive.AudioPlayer.Control.FavoriteButton import FavoriteButton
from dueros.directive.AudioPlayer.Control.ShowPlayListButton import ShowPlayListButton
from dueros.directive.AudioPlayer.Control.ShowFavoriteListButton import ShowFavoriteListButton
from dueros.directive.AudioPlayer.Control.RepeatButton import RepeatButton
from dueros.directive.AudioPlayer.Control.RepeatButtonEnum import RepeatButtonEnum
from dueros.directive.AudioPlayer.AudioItemTypeEnum import AudioItemTypeEnum


class PlayerInfoTest(unittest.TestCase):

    def setUp(self):

        self.playerInfo = PlayerInfo()
        self.playerInfo.set_provider('yly', 'http://uri-logo.com')

        self.playerInfo.set_lyric('http://uri-lrc.com')
        self.playerInfo.set_art('art')
        self.playerInfo.set_title('title')
        self.playerInfo.set_title_subtext1('sub text1')
        self.playerInfo.set_title_subtext2('sub text2')
        self.playerInfo.set_audio_item_type(AudioItemTypeEnum.FORMAT_LRC)
        self.playerInfo.set_media_length_in_ms(12321.232)

        favoriteButton = FavoriteButton()
        favoriteButton.set_enabled(False)
        self.playerInfo.add_control(favoriteButton)


        showPlayListButton = ShowPlayListButton()
        showPlayListButton.set_selected(True)
        self.playerInfo.set_controls(showPlayListButton)

        showFavoriteListButton = ShowFavoriteListButton()
        repeatButton = RepeatButton(RepeatButtonEnum.REPEAT_ONE)
        self.playerInfo.set_controls([showFavoriteListButton, repeatButton])

    def testGetData(self):

        ret = {
            'content': {
                'audioItemType': 'LRC',
                'mediaLengthInMilliseconds': 12321,
                'provider': {
                    'name': 'yly',
                    'logo': {
                        'src': 'http://uri-logo.com'
                    }
                },
                'lyric': {
                    'url': 'http://uri-lrc.com',
                    'format': 'LRC'
                },
                'art': {
                    'src': 'art'
                },
                'title': 'title',
                'titleSubtext1': 'sub text1',
                'titleSubtext2': 'sub text2'
            },
            'controls': [
                {
                    'type': 'BUTTON',
                    'name': 'FAVORITE',
                    'enabled': False,
                    'selected': False
                },
                {
                    'type': 'BUTTON',
                    'name': 'SHOW_PLAYLIST',
                    'enabled': True,
                    'selected': True
                },
                {
                    'type': 'BUTTON',
                    'name': 'SHOW_FAVORITE_LIST',
                    'enabled': True,
                    'selected': False
                },
                {
                    'type': 'RADIO_BUTTON',
                    'name': 'REPEAT',
                    'selectedValue': 'REPEAT_ONE'
                }
            ]
        }

        data = self.playerInfo.get_data()
        self.assertEqual(data, ret)
    pass


if __name__ == '__main__':
    pass