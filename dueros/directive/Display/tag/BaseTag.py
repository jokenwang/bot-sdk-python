#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/17

"""
    tag基类
"""
from dueros.directive.Display.tag.TagTypeEnum import TagTypeEnum


class BaseTag:

    def __init__(self, tag_type, text=''):

        self.data = {}
        self.set_type(tag_type)
        self.set_text(text)

    def set_type(self, tag_type):
        if tag_type and isinstance(tag_type, TagTypeEnum):
            self.data['type'] = tag_type.value

    def set_text(self, text):
        if text and isinstance(text, str):
            self.data['text'] = text

    def set_color(self, color):
        """

        :param color:
        :return:
        """
        if color and isinstance(color, str):
            self.data['color'] = color

    def set_background_color(self, background_color):
        """
        设置backgroundColor
        :param background_color:
        :return:
        """
        if background_color and isinstance(background_color, str):
            self.data['backgroundColor'] = background_color

    def get_data(self):
        return self.data


if __name__ == '__main__':
    pass