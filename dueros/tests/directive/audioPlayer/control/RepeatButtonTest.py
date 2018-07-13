#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/7/13

"""
    desc:pass
"""

import unittest
from dueros.directive.AudioPlayer.Control.RepeatButton import RepeatButton
from dueros.directive.AudioPlayer.Control.RepeatButtonEnum import RepeatButtonEnum
class RepeatButtonTest(unittest.TestCase):

    def setUp(self):
        self.repeatButton = RepeatButton()
        self.repeatButton.setSelectedValue(RepeatButtonEnum.REPEAT_ONE)

    def testGetData(self):

        ret = {
            'type': 'RADIO_BUTTON',
            'name': 'REPEAT',
            'selectedValue': 'REPEAT_ONE'

        }

        self.assertEqual(self.repeatButton.getData(), ret)
    pass


if __name__ == '__main__':
    pass