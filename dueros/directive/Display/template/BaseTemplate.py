#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/26

"""
    desc:pass
"""

from dueros.directive.Display.template.TextStructure import TextStructure
from dueros.directive.Display.template.ImageStructure import ImageStructure
from dueros.directive.Display.template.TextType import TextType


class BaseTemplate:

    def __init__(self, field):
        super(BaseTemplate, self).__init__()
        self.data = {}
        self.support_set_field = field

    def set_background_image(self, url, width_pixels='', height_pixels=''):
        """
        :param url:
        :param width_pixels:
        :param height_pixels:
        :return:
        """

        if url:
            image = self.create_image_structure(url, width_pixels, height_pixels)
            if image:
                self.data['backgroundImage'] = image.get_data()

    def create_image_structure(self, url, width_pixels, height_pixels):
        """
        :param url:
        :param width_pixels:
        :param height_pixels:
        :return:
        """

        if url:
            image = ImageStructure()
            image.set_url(url)
            if width_pixels and width_pixels != '':
                image.set_width_pixels(width_pixels)

            if height_pixels and height_pixels != '':
                image.set_height_pixels(height_pixels)
            return image

    def create_text_structure(self, content, structure_type=TextType.PLAIN_TEXT):
        """
        :param content:
        :param structure_type:
        :return:
        """

        if content:
            text_structure = TextStructure()
            text_structure.set_text(content)
            if TextType.inEnum(structure_type):
                text_structure.set_type(structure_type.value)
            else:
                text_structure.set_type(TextType.PLAIN_TEXT.value)

            return text_structure

    def get_data(self):

        return self.data

    def __getattr__(self, item):
        '''
        添加魔术方法
        :param item:
        :return:
        '''
        # 获取操作类型 set
        operation = item[0:3]
        # 获取被操作的属性
        field = item[4:]
        if operation == 'set' and field and (field.lower() in self.support_set_field):
            def function(*args):
                self.data[field.lower()] = args[0]

            return function
        else:
            def function(*args):
                print('不支持', operation, field)

            return function

if __name__ == '__main__':

    bodytemplate = BaseTemplate(['token'])
    bodytemplate.set_token('a')
    bodytemplate.set_background_image('aaaa')
    print(bodytemplate.get_data())
    pass