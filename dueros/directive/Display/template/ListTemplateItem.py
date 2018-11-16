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
from dueros.directive.Display.tag.BaseTag import BaseTag
from dueros.Utils import Utils


class ListTemplateItem(BaseTemplate):

    def __init__(self):
        super(ListTemplateItem, self).__init__(['token'])
        self.image_tags = None

    def set_plain_primary_text(self, primary_text):
        """
        设置一级标题
        :param primary_text:
        :return:
        """

        if not Utils.checkKeyInDict(self.data, 'textContent'):
            self.data['textContent'] = {}
        primary_text_structure = self.create_text_structure(primary_text, TextType.PLAIN_TEXT)
        if primary_text_structure:

           self.data['textContent']['primaryText'] = primary_text_structure.get_data()

    def set_plain_secondary_text(self, secondary_text):
        """
        设置二级标题
        :param secondary_text:
        :return:
        """
        if not Utils.checkKeyInDict(self.data, 'textContent'):
            self.data['textContent'] = {}
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
        if not Utils.checkKeyInDict(self.data, 'textContent'):
            self.data['textContent'] = {}
        tertiary_text_structure = self.create_text_structure(tertiary_text, TextType.PLAIN_TEXT)
        if tertiary_text_structure:
            self.data['textContent']['tertiaryText'] = tertiary_text_structure.get_data()
        pass

    def set_content(self, text):
        text_structure = self.create_text_structure(text)
        if text_structure:
            self.data['content'] = text_structure.get_data()

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

    def set_image_tags(self, tags):
        if not tags:
            return
        if not isinstance(tags, list):
            tags = [tags]
        self.image_tags = list(filter(lambda value: isinstance(value, BaseTag), tags))

    def get_data(self, key=''):
        if Utils.checkKeyInDict(self.data, 'image') and self.image_tags:
            self.data['image']['tags'] = get_image_tag_data(self.image_tags)
        if key:
            return self.data[key]
        return self.data

    def set_anchor_word(self, anchor_word):
        if anchor_word and isinstance(anchor_word, str):
            self.data['anchorWord'] = anchor_word

def get_image_tag_data(tags):
    if not tags or not isinstance(tags, list):
        return []
    return list(map(lambda value: value.get_data(), tags))


if __name__ == '__main__':


    pass
