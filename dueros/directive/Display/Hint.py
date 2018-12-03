#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/31

"""
    desc:pass
"""
from dueros.directive.BaseDirective import BaseDirective


class Hint(BaseDirective):
    """
    Hint 指令 用于展示提示信息
    """

    def __init__(self, text):
        """

        :param text: 用于显示的文本
        """
        BaseDirective.__init__(self, 'Hint')
        self.data['hints'] = list()
        if not (isinstance(text, str) or isinstance(text, list)):
            raise ValueError('The text must be str or list')

        if isinstance(text, str):
            text = [text]
        if isinstance(text, list):
            for value in text:
                item = dict()
                item['type'] = 'PlainText'
                item['text'] = value
                self.data['hints'].append(item)


if __name__ == '__main__':

    hint = Hint('aaa')
    print(hint.get_data())
    pass