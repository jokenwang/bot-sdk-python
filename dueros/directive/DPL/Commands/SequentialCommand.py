#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2019-06-13

"""
    desc:pass
"""
from dueros.directive.DPL.Commands.BaseCommand import BaseCommand
from dueros.Utils import Utils


class SequentialCommand(BaseCommand):
    """
    串行执行指令
    """

    def __init__(self):
        super(SequentialCommand, self).__init__('Sequential')
        self.data['commands'] = list()

    def set_delay_in_milliseconds(self, delay):
        """
        设置延迟执行时间
        :param delay:
        :return:
        """

        if Utils.is_numeric(delay):
            self.data['delayInMilliseconds'] = delay

    def set_repeat_count(self, repeat_count):
        """
        重复执行次数
        :param repeat_count:
        :return:
        """
        if Utils.is_numeric(repeat_count):
            self.data['repeatCount'] = repeat_count

    def set_commands(self, commands):
        """
        添加命令
        :param commands:
        :return:
        """

        if isinstance(commands, BaseCommand):
            self.data['commands'].append(commands.get_data())
        elif isinstance(commands, list):
            self.data['commands'] = list(map(lambda value: value.get_data(), list(filter(lambda value: isinstance(value, BaseCommand), commands))))


if __name__ == '__main__':

    a = '1.3'
    print(a.isdigit())
    pass