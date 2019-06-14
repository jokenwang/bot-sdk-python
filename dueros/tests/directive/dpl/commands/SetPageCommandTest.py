#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2019-06-14

"""
    desc:pass
"""
import unittest
from dueros.directive.DPL.Commands.SetPageCommand import SetPageCommand


class SetPageCommandTest(unittest.TestCase):

    def testGetData(self):
        setPageCommand = SetPageCommand()
        setPageCommand.set_position('relative')
        setPageCommand.set_value(1)
        setPageCommand.set_component_id('componentId')
        self.assertEqual(setPageCommand.get_data(), data)

data = {
    'type': 'SetPage',
    'componentId': 'componentId',
    'position': 'relative',
    'value': 1
}


if __name__ == '__main__':
    pass