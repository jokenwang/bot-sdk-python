#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2019-06-25

import enum
from dueros.directive.DPL.Commands.BaseCommand import BaseCommand


class ControlMediaCommand(BaseCommand):

    def __init__(self):
        super(ControlMediaCommand, self).__init__('ControlMedia')
        self.data['command'] = ''

    def set_command(self, command):
        if isinstance(command, ControlMediaCommandType):
            self.data['command'] = command.value
        else:
            self.data['command'] = command


class ControlMediaCommandType(enum.Enum):
    PLAY = 'play'
    PAUSE = 'pause'
    NEXT = 'next'
    PREVIOUS = 'previous'
    SCREEN_BULLET_ON = 'screenBulletOn'
    SCREEN_BULLET_OFF = 'screenBulletOff'
