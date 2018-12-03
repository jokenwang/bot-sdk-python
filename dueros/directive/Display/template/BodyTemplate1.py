#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/26

"""
BodyTemplate1模板
详见文档：https://dueros.baidu.com/didp/doc/dueros-bot-platform/dbp-custom/display-template_markdown#BodyTemplate1%E6%A8%A1%E6%9D%BF
"""

from dueros.directive.Display.template.BaseTemplate import BaseTemplate
from dueros.directive.Display.template import TextType
from dueros.directive.Display.template import TextContentPosition


class BodyTemplate1(BaseTemplate):

    def __init__(self):
        BaseTemplate.__init__(self, ['token', 'title', 'type'])
        self.set_type('BodyTemplate1')

    def set_plain_text_content(self, text, position=TextContentPosition.BOTTOM_LEFT):
        """
        :param text:
        :param position:
        :return:
        """
        text_structure = self.create_text_structure(text, TextType.PLAIN_TEXT)

        if text_structure:
            if 'textContent' not in self.data:
                self.data['textContent'] = {}
            self.data['textContent']['text'] = text_structure.get_data()
            if TextContentPosition.in_enum(position):
                self.data['textContent']['position'] = position
            else:
                self.data['textContent']['position'] = TextContentPosition.BOTTOM_LEFT

            return self


if __name__ == '__main__':
    pass