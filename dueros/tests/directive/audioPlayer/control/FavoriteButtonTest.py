#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/7/13

"""
    desc:pass
"""

import unittest
from dueros.directive.AudioPlayer.Control.FavoriteButton import FavoriteButton


class FavoriteButtonTest(unittest.TestCase):
    '''

    '''

    def setUp(self):
        self.favoriteButton = FavoriteButton()
        self.favoriteButton.set_enabled(False)
        self.favoriteButton.set_selected(True)

    def testGetData(self):

        ret = {
            'type': 'BUTTON',
            'name': 'FAVORITE',
            'enabled': False,
            'selected': True
        }

        self.assertEqual(self.favoriteButton.get_data(), ret)

    pass


if __name__ == '__main__':
    pass