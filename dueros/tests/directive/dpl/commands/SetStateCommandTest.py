#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2019-06-14

"""
    desc:pass
"""
import unittest
from dueros.directive.DPL.Commands.SetStateCommand import SetStateCommand


class SetStateCommandTest(unittest.TestCase):

    def testGetData(self):
        setStateCommand = SetStateCommand()
        setStateCommand.set_state('src')
        setStateCommand.set_value('http://img-url/1.jpg')
        setStateCommand.set_component_id('componentId')
        self.assertEqual(setStateCommand.get_data(), data)

data = {
    'type': 'SetState',
    'componentId': 'componentId',
    'state': 'src',
    'value': 'http://img-url/1.jpg'
}


if __name__ == '__main__':
    pass