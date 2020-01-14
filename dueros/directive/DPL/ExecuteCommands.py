#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2019-06-13

from dueros.directive.BaseDirective import BaseDirective
from dueros.directive.DPL.Commands.BaseCommand import BaseCommand


class ExecuteCommands(BaseDirective):

    def __init__(self):
        super(ExecuteCommands, self).__init__('DPL.ExecuteCommands')
        self.data['commands'] = list()
        self.data['token'] = self.gen_token()

    def set_commands(self, commands):
        if isinstance(commands, BaseCommand):
            self.data['commands'].append(commands.get_data())
        elif isinstance(commands, list):
            self.data['commands'] = list(map(lambda value: value.get_data(), list(
                filter(lambda value: isinstance(value, BaseCommand), commands))))
