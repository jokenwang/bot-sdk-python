#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2019-06-14

"""
    desc:pass
"""
import unittest
from dueros.directive.DPL.Commands.SendEventCommand import SendEventCommand


class SendEventCommandTest(unittest.TestCase):

    def testGetData(self):
        sendEventCommand = SendEventCommand()
        sendEventCommand.set_component_id('componentId')
        self.assertEqual(sendEventCommand.get_data(), data)

data = {
    'type': 'SendEvent',
    'componentId': 'componentId'
}


if __name__ == '__main__':
    pass