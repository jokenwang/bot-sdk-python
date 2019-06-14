#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2019-06-14

"""
    desc:pass
"""
import unittest
from dueros.directive.DPL.Commands.ParallelCommand import ParallelCommand
from dueros.directive.DPL.Commands.AutoPageCommand import AutoPageCommand

class ParallelCommandTest(unittest.TestCase):

    def testGetData(self):
        autoPageCommand1 = AutoPageCommand()
        autoPageCommand1.set_duration_in_millisecond(1000)
        autoPageCommand1.set_component_id('componentId1')
        autoPageCommand2 = AutoPageCommand()
        autoPageCommand2.set_duration_in_millisecond(1000)
        autoPageCommand2.set_component_id('componentId2')
        parallelCommand = ParallelCommand()
        parallelCommand.set_delay_in_milliseconds(1000)
        parallelCommand.set_component_id('componentId3')
        parallelCommand.set_commands([autoPageCommand1, autoPageCommand2])

        self.assertEqual(parallelCommand.get_data(), data)

data = {
    'type': 'Parallel',
    'componentId': 'componentId3',
    'delayInMilliseconds': 1000,
    'commands': [
        {
            'type': 'AutoPage',
            'componentId': 'componentId1',
            'durationInMillisecond': 1000
        },
        {
            'type': 'AutoPage',
            'componentId': 'componentId2',
            'durationInMillisecond': 1000
        }
    ]
}



if __name__ == '__main__':
    pass