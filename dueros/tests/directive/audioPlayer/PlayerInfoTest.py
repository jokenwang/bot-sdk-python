#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/7/13

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
from dueros.directive.AudioPlayer.PlayerInfoAudioItemEnum import PlayerInfoAudioItemEnum
class PlayerInfoTest(unittest.TestCase):

    def setUp(self):

        self.playerInfo = PlayerInfo()
        self.playerInfo.setProvider('yly', 'http://uri-logo.com')
        self.playerInfo.setProviderName('yyy-second');

        self.playerInfo.setLyric('http://uri-lrc.com')
        self.playerInfo.setArt('art')
        self.playerInfo.setTitle('title')
        self.playerInfo.setTitleSubtext1('sub text1')
        self.playerInfo.setTitleSubtext2('sub text2')
        self.playerInfo.setAudioItemType(PlayerInfoAudioItemEnum.FORMAT_LRC)
        self.playerInfo.setMediaLengthInMs(12321.232)

        favoriteButton = FavoriteButton()
        favoriteButton.setEnabled(False)
        self.playerInfo.addControl(favoriteButton)


        showPlayListButton = ShowPlayListButton()
        showPlayListButton.setSelected(True)
        self.playerInfo.setControls(showPlayListButton)

        showFavoriteListButton = ShowFavoriteListButton()
        repeatButton = RepeatButton(RepeatButtonEnum.REPEAT_ONE)
        self.playerInfo.setControls([showFavoriteListButton, repeatButton])

    def testGetData(self):

        ret = {
            'content': {
                'audioItemType': 'LRC',
                'mediaLengthInMilliseconds': 12321,
                'provider': {
                    'name': 'yyy-second',
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

        data = self.playerInfo.getData()
        self.assertEqual(data, ret)
    pass


if __name__ == '__main__':
    pass