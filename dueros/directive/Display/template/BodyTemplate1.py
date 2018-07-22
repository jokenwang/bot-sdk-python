#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/26

"""
BodyTemplate1模板
详见文档：https://dueros.baidu.com/didp/doc/dueros-bot-platform/dbp-custom/display-template_markdown#BodyTemplate1%E6%A8%A1%E6%9D%BF
"""

from dueros.directive.Display.template.BaseTemplate import BaseTemplate
from dueros.directive.Display.template.TextType import TextType
from dueros.directive.Display.template.TextContentPosition import TextContentPosition


class BodyTemplate1(BaseTemplate):

    def __init__(self):
        super(BodyTemplate1, self).__init__(['token', 'title', 'type'])
        self.set_type('BodyTemplate1')
        pass

    def set_plain_text_content(self, text, position=TextContentPosition.BOTTOM_LEFT):
        """
        :param text:
        :param position:
        :return:
        """
        text_structure = self.create_text_structure(text, TextType.PLAIN_TEXT)

        if text_structure:
            if 'textContent' not in self.data.keys():
                self.data['textContent'] = {}
            self.data['textContent']['text'] = text_structure.get_data()
            if TextContentPosition.inEnum(position):
                self.data['textContent']['position'] = position.value
            else:
                self.data['textContent']['position'] = TextContentPosition.BOTTOM_LEFT.value

            return self

if __name__ == '__main__':

    bodytemplate = BodyTemplate1()
    bodytemplate.set_title('呵呵')
    bodytemplate.set_token("tttt")
    bodytemplate.set_background_image('htt[://///')
    bodytemplate.set_plain_text_content('bodyTemplate')
    print(bodytemplate.get_data())
    pass