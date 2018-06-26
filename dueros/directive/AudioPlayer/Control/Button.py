#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/28

"""
    desc:pass
"""
from dueros.directive.AudioPlayer.Control.BaseButton import BaseButton

class Button(BaseButton):

    def __init__(self, name):
        super(Button, self).__init__('BUTTON', name)
        self.data['enabled'] = True
        self.data['selected'] = False

    def setEnabled(self, bool):
        self.data['enabled'] = bool

    def setSelected(self, bool):
        self.data['selected'] = bool

    pass


if __name__ == '__main__':
    pass