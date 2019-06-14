#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2019-06-14

"""
    desc:pass
"""
import unittest
from dueros.directive.DPL.ExecuteCommands import ExecuteCommands
from dueros.directive.DPL.Commands.ScrollCommand import ScrollCommand


class ExecuteCommandsTest(unittest.TestCase):

    def testGetData(self):
        scrollCommand = ScrollCommand()
        scrollCommand.set_distance('100dp')
        scrollCommand.set_component_id('componentId')
        executeCommands = ExecuteCommands()
        executeCommands.set_commands(scrollCommand)
        executeCommands.set_token('test_token')
        self.assertEqual(executeCommands.get_data(), data)

data = {
    'type': 'DPL.ExecuteCommands',
    'commands': [
        {
            'type': 'Scroll',
            'componentId': 'componentId',
            'distance': '100dp'
        }
    ],
    'token': 'test_token'
}


if __name__ == '__main__':
    pass