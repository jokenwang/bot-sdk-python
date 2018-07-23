#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/28

"""
    desc:pass
"""
from dueros.directive.AudioPlayer.Control.RadioButton import RadioButton
from dueros.directive.AudioPlayer.Control.RepeatButtonEnum import RepeatButtonEnum


class RepeatButton(RadioButton):

    def __init__(self, selectedValue = RepeatButtonEnum.REPEAT_ONE):
        super(RepeatButton, self).__init__('REPEAT', selectedValue)

    def setSelectedValue(self, selectedValue = RepeatButtonEnum.REPEAT_ONE):

        if RepeatButtonEnum.inEnum(selectedValue):
            self.data['selectedValue'] = selectedValue
        else:
            self.data['selectedValue'] = RepeatButtonEnum.REPEAT_ONE


    pass


if __name__ == '__main__':
    pass