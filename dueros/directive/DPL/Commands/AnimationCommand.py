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


class AnimationCommand(BaseCommand):
    """
    动画指令
    example:
        animationCommand = AnimationCommand()
        animationCommand.set_attribute('width');
        animationCommand.set_from('10dp');
        animationCommand.set_to('100dp');
        animationCommand.set_easing('ease-in');
        animationCommand.set_repeat_count('3');
        animationCommand.set_repeat_mode('reverse');
    """

    def __init__(self):
        super(AnimationCommand, self).__init__('Animation')
        self.data['attribute'] = ''
        self.data['from'] = ''
        self.data['to'] = ''
        self.data['easing'] = 'linear'
        self.data['duration'] = 1000
        self.data['repeatCount'] = 'infinite'
        self.data['repeatMode'] = 'restart'
        self.data['onComplete'] = list()

    def set_attribute(self, attribute):
        """
        设置动画属性
        :param attribute: 字符串类型
        :return:
        """

        if isinstance(attribute, str):
            self.data['attribute'] = attribute

    def set_from(self, start):
        """
        设置动画作用属性的起始值
        :param start:
        :return:
        """
        if isinstance(start, str):
            self.data['from'] = start

    def set_to(self, to):
        """
        设置动画作用属性的结束值
        :param to:
        :return:
        """

        if isinstance(to, str):
            self.data['to'] = to

    def set_easing(self, easing):
        """
        设置描述动画执行的速度的类型
        :param easing:
        :return:
        """
        if isinstance(easing, str) and easing.find('cubic-bezier') != -1:
            self.data['easing'] = easing
        if isinstance(easing, AnimationAttrMode):
            self.data['easing'] = easing.value

    def set_duration(self, duration):
        """
        设置动画执行的时间
        :param duration:
        :return:
        """

        if Utils.is_numeric(duration):
            self.data['duration'] = duration

    def set_repeat_count(self, repeat_count):
        """
        设置动画重复的次数
        :param repeat_count:
        :return:
        """

        if isinstance(repeat_count, str):
            self.data['repeatCount'] = repeat_count

    def set_repeat_mode(self, repeat_mode):
        """
        设置动画重复方式
        :param repeat_mode:
        :return:
        """
        if isinstance(repeat_mode, AnimationRepeatMode):
            self.data['repeatMode'] = repeat_mode.value
        elif isinstance(repeat_mode, str):
            self.data['repeatMode'] = repeat_mode

    def add_complete_commands(self, complete_commands):
        """
        设置动画结束后需要触发的commands, 如果repeatCount为infinite，将不会触发onComplete
        :param complete_commands:
        :return:
        """

        if isinstance(complete_commands, BaseCommand):
            self.data['onComplete'].append(complete_commands.get_data())
        elif isinstance(complete_commands, list):
            self.data['onComplete'] = list(map(lambda value: value.get_data(), list(filter(lambda value: isinstance(value, BaseCommand), complete_commands))))


class AnimationAttrMode(enum.Enum):
    SCALEX = 'scaleX'
    SCALEY = 'scaleY'
    ROTATION = 'rotation'


class AnimationEasingMode(enum.Enum):
    LINEAR = 'linear'
    EASE = 'ease'
    EASE_IN = 'ease-in'
    EASE_OUT = 'ease-out'


class AnimationRepeatMode(enum.Enum):
    RESTART = 'restart'
    REVERSE = 'reverse'


if __name__ == '__main__':
    pass
