#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/28

"""
    desc:pass
"""
from dueros.directive.AudioPlayer.Control.BaseButton import BaseButton


class RadioButton(BaseButton):

    def __init__(self, name, selected_value = ''):

        super(RadioButton,self).__init__('RADIO_BUTTON', name)
        self.set_selected_value(selected_value)

    def set_selected_value(self, selected_value):
        self.data['selectedValue'] = selected_value


if __name__ == '__main__':
    pass