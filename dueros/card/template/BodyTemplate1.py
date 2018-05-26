#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/26

"""
    desc:pass
"""

from dueros.card.template.BodyTemplate import BodyTemplate
from dueros.card.template.TextStructure import TextStructure
from dueros.card.template.ImageStructure import ImageStructure

class BodyTemplate1(BodyTemplate):

    def __init__(self):
        super(BodyTemplate1, self).__init__()
        self.textContent.setType('PlainText')
        self.data['template']['textContent'] = {}
        self.setType('BodyTemplate1')
        pass

    def setPosition(self, position):
        '''
        文本垂直方向的位置，支持以下三种情况。
            TOP-LEFT：文本位置置顶，文字左对齐。
            CENTER：文本位置垂直居中，文字居中。
            BOTTOM-LEFT：文本位置置底，文字左对齐
        :param position:
        :return:
        '''
        if position:
            self.data['template']['textContent']['position'] = position

    def setPlainTextContent(self, textContent):
        if textContent:
            self.textContent.setText(textContent)
            self.textContent.setType('PlainText')
            self.data['template']['textContent']['text'] = self.textContent.getData()


    def setTextContent(self, textContent):

        if isinstance(textContent, TextStructure):
            self.textContent = textContent
            self.data['template']['textContent']['text'] = textContent.getData()


    pass


if __name__ == '__main__':
    bodytemplate = BodyTemplate1()
    bodytemplate.setTitle('呵呵')
    bodytemplate.setToken("tttt")
    # bodytemplate.setBackgroundImage('background')
    image = ImageStructure()
    image.setUrl('http://www.baidu.com')
    bodytemplate.setBackgroundImage(image)
    bodytemplate.setPlainTextContent('bodyTemplate')
    bodytemplate.setPosition('LEFT')
    print(bodytemplate.getData())
    pass