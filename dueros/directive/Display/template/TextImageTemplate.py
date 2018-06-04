#!/usr/bin/env python3
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

    def __init__(self, type):
        super(TextImageTemplate, self).__init__(['token','title', 'type'])
        self.setType(type)

    def setImage(self, url, widthPixels = '', heightPixels = ''):

        imageStructure = self.createImageStructure(url, widthPixels, heightPixels)
        if imageStructure:
            self.data['image'] = imageStructure.getData()

    def setPlainContent(self, text):
        textStructure = self.createTextStructure(text, TextType.PLAIN_TEXT)
        if textStructure:
            self.data['content'] = textStructure.getData()
        pass


if __name__ == '__main__':


    pass