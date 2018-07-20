#!/usr/bin/env python3
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

    def __init__(self, selected_value=RepeatButtonEnum.REPEAT_ONE.value):
        super(RepeatButton, self).__init__('REPEAT', selected_value)

    def set_selected_value(self, selected_value=RepeatButtonEnum.REPEAT_ONE):

        if RepeatButtonEnum.inEnum(selected_value):
            self.data['selectedValue'] = selected_value.value
        else:
            self.data['selectedValue'] = RepeatButtonEnum.REPEAT_ONE.value


    pass


if __name__ == '__main__':
    pass