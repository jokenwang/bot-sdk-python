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
        self.refreshButton.setEnabled(False)
        self.refreshButton.setSelected(True)

    def testGetData(self):

        ret = {
            'type': 'BUTTON',
            'name': 'REFRESH',
            'enabled': False,
            'selected': True

        }

        self.assertEqual(self.refreshButton.getData(), ret)
    pass


if __name__ == '__main__':
    pass