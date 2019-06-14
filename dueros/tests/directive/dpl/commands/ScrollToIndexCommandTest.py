#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2019-06-14

"""
    desc:pass
"""
import unittest
from dueros.directive.DPL.Commands.ScrollToIndexCommand import ScrollToIndexCommand


class ScrollToIndexCommandTest(unittest.TestCase):

    def testGetData(self):
        scrollToIndexCommand = ScrollToIndexCommand()
        scrollToIndexCommand.set_index(1)
        scrollToIndexCommand.set_align('center')
        scrollToIndexCommand.set_component_id('componentId')
        self.assertEqual(scrollToIndexCommand.get_data(), data)

data = {
    'type': 'ScrollToIndex',
    'componentId': 'componentId',
    'index': 1,
    'align': 'center'
}


if __name__ == '__main__':
    pass