#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2019-06-13

"""
    desc:pass
"""
from dueros.directive.DPL.Commands.BaseCommand import BaseCommand


class SendEventCommand(BaseCommand):
    """
    SendEventCommand 绑定端触发UserEvent指令
    """

    def __init__(self):
        super(SendEventCommand, self).__init__('SendEvent')


if __name__ == '__main__':
    pass