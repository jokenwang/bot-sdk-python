#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/28

"""
    desc:pass
"""
from dueros.directive.AudioPlayer.Control.BaseButton import BaseButton

class RadioButton(BaseButton):

    def __init__(self,name, selectedValue = ''):
        super(RadioButton, 'RADIO_BUTTON', name)
        self.setSelectedValue(selectedValue)

    def setSelectedValue(self, selectedValue):
        self.data['selectedValue'] = selectedValue;

    pass


if __name__ == '__main__':
    pass