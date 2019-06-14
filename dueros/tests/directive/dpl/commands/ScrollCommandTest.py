#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2019-06-14

"""
    desc:pass
"""
import unittest
from dueros.directive.DPL.Commands.ScrollCommand import ScrollCommand


class ScrollCommandTest(unittest.TestCase):

    def testGetData(self):
        scrollCommand = ScrollCommand()
        scrollCommand.set_distance('100dp')
        scrollCommand.set_component_id('componentId')
        self.assertEqual(scrollCommand.get_data(), data)

data = {
    'type': 'Scroll',
    'componentId': 'componentId',
    'distance': '100dp'
}


if __name__ == '__main__':
    pass