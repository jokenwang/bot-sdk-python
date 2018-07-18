#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/7/13

"""
    desc:pass
"""

import unittest
from dueros.directive.AudioPlayer.Control.RadioButton import RadioButton


class PlayPauseButtonTest(unittest.TestCase):

    def setUp(self):
        self.radioButton = RadioButton('radio')
        self.radioButton.set_selected_value('selected value')

    def testGetData(self):

        ret = {
            'type': 'RADIO_BUTTON',
            'name': 'radio',
            'selectedValue': 'selected value'
        }

        self.assertEqual(self.radioButton.get_data(), ret)
    pass


if __name__ == '__main__':
    pass