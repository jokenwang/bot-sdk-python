#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/7/13

"""
    desc:pass
"""

import unittest
from dueros.directive.AudioPlayer.Control.ShowPlayListButton import ShowPlayListButton


class ShowFavoriteListButtonTest(unittest.TestCase):

    def setUp(self):
        self.showPlayListButton = ShowPlayListButton()
        self.showPlayListButton.set_enabled(False)
        self.showPlayListButton.set_selected(True)

    def testGetData(self):

        ret = {
            'type': 'BUTTON',
            'name': 'SHOW_PLAYLIST',
            'enabled': False,
            'selected': True

        }

        self.assertEqual(self.showPlayListButton.get_data(), ret)
    pass


if __name__ == '__main__':
    pass