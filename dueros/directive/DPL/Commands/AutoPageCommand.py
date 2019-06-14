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


class AutoPageCommand(BaseCommand):
    """
    自动翻页指令
    example:
        autoPageCommand = AutoPageCommand()
        autoPageCommand.set_duration_in_millisecond(1000);
        autoPageCommand.set_component_id('componentId');
    """

    def __init__(self):
        super(AutoPageCommand, self).__init__('AutoPage')

    def set_duration_in_millisecond(self, duration):
        """
        设置切换间隔
        :param duration:
        :return:
        """

        if Utils.is_numeric(duration):
            self.data['durationInMillisecond'] = duration


if __name__ == '__main__':
    pass