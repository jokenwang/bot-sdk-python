#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/26

"""
    模板展示基类
"""

from dueros.directive.Display.template.TextStructure import TextStructure
from dueros.directive.Display.template.ImageStructure import ImageStructure
from dueros.directive.Display.template.TextType import TextType


class BaseTemplate(object):

    def __init__(self, field=[]):
        self.data = {}
        self.supportSetField = field

    def set_background_image(self, url, width_pixels='', height_pixels=''):

        """
        设置背景图片
        :param url:
        :param width_pixels:
        :param height_pixels:
        :return:
        """

        if url:
            image = self.create_imagestructure(url, width_pixels, height_pixels)
            if image:
                self.data['backgroundImage'] = image.get_data()

    def create_imagestructure(self, url, width_pixels, height_pixels):

        """
        创建imageStructure
        :param url:
        :param width_pixels:
        :param height_pixels:
        :return:
        """

        if url:
            image = ImageStructure()
            image.set_url(url)
            if width_pixels:
                image.set_width_pixels(width_pixels)

            if height_pixels:
                image.set_height_pixels(height_pixels)
            return image

    def create_textstructure(self, content, text_type=TextType.PLAIN_TEXT):
        """
        创建TextStructure
        :type content: object
        :param content:
        :param text_type:
        :return:
        """

        if content:
            texture = TextStructure()
            texture.set_text(content)
            if TextType.inEnum(text_type):
                texture.set_type(text_type)
            else:
                texture.set_type(TextType.PLAIN_TEXT)

            return texture

    def get_data(self):

        return self.data

    def __getattr__(self, item):
        """
        添加魔术方法
        :param item:
        :return:
        """

        # 获取操作类型 set
        operation = item[0:3]
        # 获取被操作的属性
        field = item[4:]
        if operation == 'set' and field and (field.lower() in self.supportSetField):
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
