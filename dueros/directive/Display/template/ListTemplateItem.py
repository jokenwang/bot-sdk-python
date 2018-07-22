#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/26

"""
ListItem
详见文档：https://dueros.baidu.com/didp/doc/dueros-bot-platform/dbp-custom/display-template_markdown#ListItem
"""


from dueros.directive.Display.template.BaseTemplate import BaseTemplate
from dueros.directive.Display.template.TextType import TextType


class ListTemplateItem(BaseTemplate):

    def __init__(self):
        super(ListTemplateItem, self).__init__(['token', 'image'])
        self.data['textContent'] = {}

    def set_plain_primary_text(self, primary_text):
        """
        设置一级标题
        :param primary_text:
        :return:
        """
        primary_text_structure = self.create_text_structure(primary_text, TextType.PLAIN_TEXT)
        if primary_text_structure:
           self.data['textContent']['primaryText'] = primary_text_structure.get_data()

    def set_plain_secondary_text(self, secondary_text):
        """
        设置二级标题
        :param secondary_text:
        :return:
        """
        secondary_text_structure = self.create_text_structure(secondary_text, TextType.PLAIN_TEXT)
        if secondary_text_structure:
            self.data['textContent']['secondaryText'] = secondary_text_structure.get_data()
        pass

    def set_tertiary_text(self, tertiary_text):
        """
        设置三级标题
        :param tertiary_text:
        :return:
        """
        tertiary_text_structure = self.create_text_structure(tertiary_text, TextType.PLAIN_TEXT)
        if tertiary_text_structure:
            self.data['textContent']['tertiaryText'] = tertiary_text_structure.get_data()
        pass

    def set_image(self, url, width_pixels='', height_pixels=''):
        """
        设置
        :param url:
        :param width_pixels:
        :param height_pixels:
        :return:
        """
        image = self.create_image_structure(url, width_pixels, height_pixels)
        if image:
            self.data['image'] = image.get_data()

if __name__ == '__main__':
    pass
