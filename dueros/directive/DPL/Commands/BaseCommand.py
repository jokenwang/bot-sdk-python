#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2019-06-13

"""
    desc:pass
"""


class BaseCommand:
    """
    命令基类
    """

    def __init__(self, command_type):
        self.data = dict()
        self.data['type'] = command_type
        self.data['componentId'] = ''

    def set_component_id(self, command_id):
        """
        设置命令绑定的id
        :param command_id:
        :return:
        """

        if command_id:
            self.data['componentId'] = command_id

    def get_data(self):
        return self.data


if __name__ == '__main__':
    pass