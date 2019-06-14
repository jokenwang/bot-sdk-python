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


class ScrollToIndexCommand(BaseCommand):
    """
    滚动到指定index的指令
    example:
        scrollToIndexCommand = ScrollToIndexCommand()
        scrollToIndexCommand.set_index(1);
        scrollToIndexCommand.set_align('center');
        scrollToIndexCommand.set_component_id('componentId');
    """

    def __init__(self):
        super(ScrollToIndexCommand, self).__init__('ScrollToIndex')

    def set_index(self, index):
        """
        设置index索引值
        :param index:
        :return:
        """

        if Utils.is_numeric(index):
            self.data['index'] = index

    def set_align(self, align):
        """
        设置滚动后视图的位置
        :param align:
        :return:
        """

        if isinstance(align, ScrollCommandAlign):
            self.data['align'] = align.value
        elif isinstance(align, str):
            self.data['align'] = align


class ScrollCommandAlign(enum.Enum):
    FIRST = 'first'
    CENTER = 'center'
    LAST = 'last'
    VISIBLE = 'visible'



if __name__ == '__main__':
    pass