#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/7/20

"""
    desc:pass
"""

import unittest
from dueros.directive.AudioPlayer.Control.ShowFavoriteListButton import ShowFavoriteListButton


class ShowFavoriteListButtonTest(unittest.TestCase):

    def setUp(self):
        self.showFavoriteListButton = ShowFavoriteListButton()
        self.showFavoriteListButton.set_enabled(False)
        self.showFavoriteListButton.set_selected(True)

    def testGetData(self):

        ret = {
            'type': 'BUTTON',
            'name': 'SHOW_FAVORITE_LIST',
            'enabled': False,
            'selected': True

        }

        self.assertEqual(self.showFavoriteListButton.get_data(), ret)
    pass


if __name__ == '__main__':
    pass
