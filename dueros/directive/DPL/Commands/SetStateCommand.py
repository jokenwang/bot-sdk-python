#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2019-06-13

"""
    desc:pass
"""
from dueros.directive.DPL.Commands.BaseCommand import BaseCommand


class SetStateCommand(BaseCommand):

    def __init__(self):
        super(SetStateCommand, self).__init__('SetState')

    def set_state(self, state):
        if state:
            self.data['state'] = state

    def set_value(self, value):

        if value:
            self.data['value'] = value


if __name__ == '__main__':
    pass