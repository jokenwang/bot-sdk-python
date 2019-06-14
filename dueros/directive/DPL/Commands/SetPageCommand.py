#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2019-06-13

"""
    desc:pass
"""
import enum
from dueros.Utils import Utils
from dueros.directive.DPL.Commands.BaseCommand import BaseCommand


class SetPageCommand(BaseCommand):
    """
    SetPageCommand 页面切换指令
    """

    def __init__(self):
        super(SetPageCommand, self).__init__('SetPage')

    def set_position(self, position):
        """
        设置属性值
        :param position:相对或者绝对
        :return:
        """

        if isinstance(position, SetPageCommandPositionMode):
            self.data['position'] = position.value
        elif isinstance(position, str):
            self.data['position'] = position

    def set_value(self, value):
        """
        设置切换步长
        :param value:
        :return:
        """

        if Utils.is_numeric(value):
            self.data['value'] = value


class SetPageCommandPositionMode(enum.Enum):
    RELATIVE = 'relative'
    ABSOLUTE = 'absolute'


if __name__ == '__main__':
    pass