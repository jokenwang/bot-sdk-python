#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/7/13

"""
    desc:pass
"""

import unittest
from dueros.directive.AudioPlayer.Control.RefreshButton import RefreshButton


class RefreshButtonTest(unittest.TestCase):

    def setUp(self):
        self.refreshButton = RefreshButton()
        self.refreshButton.set_enabled(False)
        self.refreshButton.set_selected(True)

    def testGetData(self):

        ret = {
            'type': 'BUTTON',
            'name': 'REFRESH',
            'enabled': False,
            'selected': True

        }

        self.assertEqual(self.refreshButton.get_data(), ret)
    pass


if __name__ == '__main__':
    pass