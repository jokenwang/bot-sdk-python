#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2019-06-14

"""
    desc:pass
"""
import unittest
from dueros.directive.DPL.Commands.AutoPageCommand import AutoPageCommand


class AutoPageCommandTest(unittest.TestCase):

    def testGetData(self):
        autoPageCommand = AutoPageCommand()
        autoPageCommand.set_duration_in_millisecond(1000)
        autoPageCommand.set_component_id('componentId')
        self.assertEqual(autoPageCommand.get_data(), data)

data = {
    'type': 'AutoPage',
    'componentId': 'componentId',
    'durationInMillisecond': 1000
}

if __name__ == '__main__':
    pass