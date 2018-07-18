#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/27

"""
    desc:pass
"""
from dueros.directive.Display.template.BaseTemplate import BaseTemplate
from dueros.directive.Display.template.TextType import TextType


class TextImageTemplate(BaseTemplate):

    def __init__(self, text_type):
        super(TextImageTemplate, self).__init__(['token', 'title', 'type'])
        self.set_type(text_type)

    def set_image(self, url, width_pixels='', height_pixels=''):
        """
        添加imageStructure
        :param url:
        :param width_pixels:
        :param height_pixels:
        :return:
        """

        image_structure = self.create_imagestructure(url, width_pixels, height_pixels)
        if image_structure:
            self.data['image'] = image_structure.get_data()

    def set_plain_content(self, text):
        """
        设置文本显示
        :param text:
        :return:
        """
        text_structure = self.create_textstructure(text, TextType.PLAIN_TEXT)
        if text_structure:
            self.data['content'] = text_structure.get_data()
        pass


if __name__ == '__main__':


    pass