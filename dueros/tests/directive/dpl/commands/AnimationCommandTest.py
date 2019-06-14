#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2019-06-14

"""
    desc:pass
"""
import unittest
from dueros.directive.DPL.Commands.AnimationCommand import AnimationCommand
from dueros.directive.DPL.Commands.AutoPageCommand import AutoPageCommand

class AnimationCommandTest(unittest.TestCase):

    def testAnimation(self):
        animationCommand = AnimationCommand()
        animationCommand.set_attribute('width')
        animationCommand.set_from('10dp')
        animationCommand.set_to('100dp')
        animationCommand.set_easing('ease-in')
        animationCommand.set_repeat_count('3')
        animationCommand.set_repeat_mode('reverse')
        animationCommand.set_component_id('componentId')

        autoPageCommand = AutoPageCommand()
        autoPageCommand.set_duration_in_millisecond(1000)
        autoPageCommand.set_component_id('childComponentId')
        animationCommand.add_complete_commands(autoPageCommand)
        self.assertEqual(animationCommand.get_data(), data)


data = {
    'type': 'Animation',
    'componentId': 'componentId',
    'attribute': 'width',
    'from': '10dp',
    'to': '100dp',
    'easing': 'linear',
    'duration': 1000,
    'repeatCount': '3',
    'repeatMode': 'reverse',
    'onComplete': [
        {
            'type': 'AutoPage',
            'componentId': 'childComponentId',
            'durationInMillisecond': 1000
        }
    ]
}
if __name__ == '__main__':
    pass