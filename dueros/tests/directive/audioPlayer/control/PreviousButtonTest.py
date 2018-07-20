#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/7/20

"""
    desc:pass
"""


import unittest
from dueros.directive.AudioPlayer.Control.PreviousButton import PreviousButton


class PlayPauseButtonTest(unittest.TestCase):

    def setUp(self):
        self.previousButton = PreviousButton()
        self.previousButton.set_enabled(False)
        self.previousButton.set_selected(True)

    def testGetData(self):

        ret = {
            'type': 'BUTTON',
            'name': 'PREVIOUS',
            'enabled': False,
            'selected': True
        }

        self.assertEqual(self.previousButton.get_data(), ret)
    pass


if __name__ == '__main__':
    pass