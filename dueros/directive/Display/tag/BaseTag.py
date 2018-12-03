#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/17

"""
    tag基类
"""
from dueros.directive.Display.tag import TagTypeEnum


class BaseTag(object):
    """
    标签基类
    """

    def __init__(self, tag_type, text=''):

        self.data = {}
        self.set_type(tag_type)
        self.set_text(text)

    def set_type(self, tag_type):
        """
        设置标签类型
        :param tag_type: 详见TagTypeEnum
        :return:
        """
        if tag_type and TagTypeEnum.in_enum(tag_type):
            self.data['type'] = tag_type
        else:
            raise ValueError('The Arg tag_type is not TagTypeEnum or null')

    def set_text(self, text):
        if text:
            if not isinstance(text, str):
                text = str(text)
            self.data['text'] = text

    def set_color(self, color):
        """
        十六进制二进制码
        :param color: #800080
        :return:
        """
        if color:
            if not isinstance(color, str):
                color = str(color)
            self.data['color'] = color

    def set_background_color(self, background_color):
        """
        设置backgroundColor
        :param background_color: #FFFFFF
        :return:
        """
        if background_color:
            if not isinstance(background_color, str):
                background_color = str(background_color)
            self.data['backgroundColor'] = background_color

    def get_data(self):
        return self.data


if __name__ == '__main__':
    pass