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
from dueros.directive.Display.template.TextContentPosition import TextContentPosition

class BodyTemplate1(BaseTemplate):

    def __init__(self):
        super(BodyTemplate1, self).__init__(['token','title','type'])
        self.setType('BodyTemplate1')
        pass

    def setPlainTextContent(self, text, position=TextContentPosition.BOTTOM_LEFT ):
        '''

        :param text:
        :param position:
        :return:
        '''
        textStructure = self.createTextStructure(text, TextType.PLAIN_TEXT)

        if textStructure:
            if not 'textContent' in self.data.keys():
                self.data['textContent'] = {}
            self.data['textContent']['text'] = textStructure.getData()
            if TextContentPosition.inEnum(position):
                self.data['textContent']['position'] = position.value
            else:
                self.data['textContent']['position'] = TextContentPosition.BOTTOM_LEFT

            return self

if __name__ == '__main__':

    bodytemplate = BodyTemplate1()
    bodytemplate.setTitle('呵呵')
    bodytemplate.setToken("tttt")
    bodytemplate.setBackGroundImage('htt[://///')
    bodytemplate.setPlainTextContent('bodyTemplate')
    print(bodytemplate.getData())
    pass