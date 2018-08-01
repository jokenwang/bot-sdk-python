#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/28

"""
    desc:pass
"""
from dueros.directive.AudioPlayer.Control.RadioButton import RadioButton
from dueros.directive.AudioPlayer.Control.ThumbsUpDownButtonEnum import ThumbsUpDownButtonEnum


class ThumbsUpDownButton(RadioButton):

    def __init__(self, selected_value=ThumbsUpDownButtonEnum.THUMBS_UP):
        super(ThumbsUpDownButton, self).__init__('THUMBS_UP_DOWN', selected_value)

    def set_selected_value(self, selected_value=ThumbsUpDownButtonEnum.THUMBS_UP):
        if ThumbsUpDownButtonEnum.inEnum(selected_value):
            self.data['selectedValue'] = selected_value
        else:
            self.data['selectedValue'] = ThumbsUpDownButtonEnum.THUMBS_UP

    pass


if __name__ == '__main__':
    pass