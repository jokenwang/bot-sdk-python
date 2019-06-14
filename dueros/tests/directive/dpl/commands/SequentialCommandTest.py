#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2019-06-14

"""
    desc:pass
"""
import unittest
from dueros.directive.DPL.Commands.SequentialCommand import SequentialCommand
from dueros.directive.DPL.Commands.ScrollCommand import ScrollCommand
from dueros.directive.DPL.Commands.AutoPageCommand import AutoPageCommand

class SequentialCommandTest(unittest.TestCase):

    def testGetData(self):
        autoPageCommand = AutoPageCommand()
        autoPageCommand.set_duration_in_millisecond(1000)
        autoPageCommand.set_component_id('componentId1')
        scrollCommand = ScrollCommand()
        scrollCommand.set_distance('100dp')
        scrollCommand.set_component_id('componentId2')
        sequentialCommand = SequentialCommand()
        sequentialCommand.set_delay_in_milliseconds(1000)
        sequentialCommand.set_repeat_count(2)
        sequentialCommand.set_component_id('componentId3')
        sequentialCommand.set_commands([autoPageCommand, scrollCommand])
        self.assertEqual(sequentialCommand.get_data(), data)

data = {
    'type': 'Sequential',
    'componentId': 'componentId3',
    'delayInMilliseconds': 1000,
    'repeatCount': 2,
    'commands': [
        {
            'type': 'AutoPage',
            'componentId': 'componentId1',
            'durationInMillisecond': 1000
        },
        {
            'type': 'Scroll',
            'componentId': 'componentId2',
            'distance': '100dp'
        }
    ]
}


if __name__ == '__main__':
    pass