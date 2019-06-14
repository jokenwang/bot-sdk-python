#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2019-06-13

"""
    desc:pass
"""
from dueros.Utils import Utils
from dueros.directive.DPL.Commands.BaseCommand import BaseCommand


class ParallelCommand(BaseCommand):
    """
    并行执行指令
    example:
        autoPageCommand1 = AutoPageCommand()
        autoPageCommand1.set_duration_in_millisecond(1000);
        autoPageCommand1.set_component_id('componentId1');
        autoPageCommand2 = AutoPageCommand()
        autoPageCommand2.set_duration_in_millisecond(1000);
        autoPageCommand2.set_component_id('componentId2');
        parallelCommand = ParallelCommand();
        parallelCommand.set_delay_in_milliseconds(1000);
        parallelCommand.set_component_id('componentId3');
        parallelCommand.set_commands([autoPageCommand1, autoPageCommand2]);
    """

    def __init__(self):
        super(ParallelCommand, self).__init__('Parallel')
        self.data['commands'] = list()

    def set_delay_in_milliseconds(self, delay):
        """
        设置延迟时间间隔
        :param delay:
        :return:
        """

        if Utils.is_numeric(delay):
            self.data['delayInMilliseconds'] = delay

    def set_commands(self, commands):
        """
        设置并行执行的指令集合
        :param commands:
        :return:
        """

        if isinstance(commands, BaseCommand):
            self.data['commands'].append(commands.get_data())
        elif isinstance(commands, list):
            self.data['commands'] = list(map(lambda value: value.get_data(), list(filter(lambda value: isinstance(value, BaseCommand), commands))))


if __name__ == '__main__':
    pass