#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/26

"""
    desc:pass
"""

from dueros.directive.Display.template.BaseTemplate import BaseTemplate
from dueros.directive.Display.template.TextType import TextType

class ListTemplateItem(BaseTemplate):

    def __init__(self):
        super(ListTemplateItem, self).__init__(['token', 'image'])
        self.data['textContent'] = {}

    def setPlainPrimaryText(self, primaryText):
        '''
        设置一级标题
        :param primaryText:
        :return:
        '''
        primaryTextStructure = self.createTextStructure(primaryText, TextType.PLAIN_TEXT)
        if primaryTextStructure:
           self.data['textContent']['primaryText'] = primaryTextStructure.getData()

    def setPlainSecondaryText(self, secondaryText):
        '''
        设置二级标题
        :param secondaryText:
        :return:
        '''
        secondaryTextStructure = self.createTextStructure(secondaryText, TextType.PLAIN_TEXT)
        if secondaryTextStructure:
            self.data['textContent']['secondaryText'] = secondaryTextStructure.getData()
        pass

    def setTertiaryText(self, tertiaryText):
        '''
        设置三级标题
        :param tertiaryText:
        :return:
        '''
        tertiaryTextStructure = self.createTextStructure(tertiaryText, TextType.PLAIN_TEXT)
        if tertiaryTextStructure:
            self.data['textContent']['tertiaryText'] = tertiaryTextStructure.getData()
        pass

    def setImage(self, url, widthPixels='', heightPixels = ''):
        '''
        设置
        :param url:
        :param widthPixels:
        :param heightPixels:
        :return:
        '''
        image = self.createImageStructure(url, widthPixels, heightPixels)
        if image:
            self.data['image'] = image.getData()

if __name__ == '__main__':
    pass
