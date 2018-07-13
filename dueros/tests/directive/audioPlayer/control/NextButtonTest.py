#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/7/13

"""
    desc:pass
"""

import unittest
from dueros.directive.AudioPlayer.Control.NextButton import NextButton

class NextButtonTest(unittest.TestCase):

    def setUp(self):
        self.nextButton = NextButton()
        self.nextButton.setEnabled(False)
        self.nextButton.setSelected(True)

    def testGetData(self):

        ret = {
            'type': 'BUTTON',
            'name': 'NEXT',
            'enabled': False,
            'selected': True
        }

        self.assertEqual(self.nextButton.getData(), ret)
    pass


if __name__ == '__main__':
    pass