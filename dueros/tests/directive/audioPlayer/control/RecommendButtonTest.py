#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/7/13

"""
    desc:pass
"""

import unittest
from dueros.directive.AudioPlayer.Control.RecommendButton import RecommendButton

class RecommendButtonTest(unittest.TestCase):

    def setUp(self):
        self.recommendButton = RecommendButton()
        self.recommendButton.setEnabled(False)
        self.recommendButton.setSelected(True)

    def testGetData(self):

        ret = {
            'type': 'BUTTON',
            'name': 'RECOMMEND',
            'enabled': False,
            'selected': True

        }

        self.assertEqual(self.recommendButton.getData(), ret)
    pass


if __name__ == '__main__':
    pass