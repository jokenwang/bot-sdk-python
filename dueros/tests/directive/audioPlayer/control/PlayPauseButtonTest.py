#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/7/13

"""
    desc:pass
"""

import unittest
from dueros.directive.AudioPlayer.Control.PlayPauseButton import PlayPauseButton

class PlayPauseButtonTest(unittest.TestCase):

    def setUp(self):
        self.playPauseButton = PlayPauseButton()
        self.playPauseButton.setEnabled(False)
        self.playPauseButton.setSelected(True)

    def testGetData(self):

        ret = {
            'type': 'BUTTON',
            'name': 'PLAY_PAUSE',
            'enabled': False,
            'selected': True
        }

        self.assertEqual(self.playPauseButton.getData(), ret)
    pass


if __name__ == '__main__':
    pass