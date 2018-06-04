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
        self.supportSetField = field

    def setBackGroundImage(self, url, widthPixels='', heightPixels = ''):
        '''

        :param url:
        :param widthPixels:
        :param heightPixels:
        :return:
        '''
        if url:
            image = self.createImageStructure(url, widthPixels, heightPixels)
            if image:
                self.data['backgroundImage'] = image.getData()

    def createImageStructure(self, url, widthPixels, heightPixels):
        '''

        :param url:
        :param widthPixels:
        :param heightPixels:
        :return:
        '''
        if url:
            image = ImageStructure()
            image.setUrl(url)
            if widthPixels:
                image.setWidthPixels(widthPixels)

            if heightPixels:
                image.setHeightPixels(heightPixels)
            return image

    def createTextStructure(self, content, type=TextType.PLAIN_TEXT):
        '''

        :param content:
        :param type:
        :return:
        '''
        if content:
            textStructure = TextStructure()
            textStructure.setText(content)
            if TextType.inEnum(type):
                textStructure.setType(type.value)
            else:
                textStructure.setType(TextType.PLAIN_TEXT)

            return textStructure

    def getData(self):

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
        field = item[3:]
        if (operation == 'set' and field and (field.lower() in self.supportSetField)):
            def function(*args):
                self.data[field.lower()] = args[0]

            return function
        else:
            def function(*args):
                print('不支持', operation, field)

            return function

if __name__ == '__main__':

    bodytemplate = BaseTemplate(['token'])
    bodytemplate.setToken('a')
    bodytemplate.setBackGroundImage('aaaa')
    print(bodytemplate.getData())
    pass