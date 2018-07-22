#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# description:
# author:jack
# create_time: 2017/12/30

"""
文本卡片
详见文档：https://dueros.baidu.com/didp/doc/dueros-bot-platform/dbp-custom/cards_markdown#%E6%96%87%E6%9C%AC%E5%8D%A1%E7%89%87
"""

from dueros.card.BaseCard import BaseCard


class TextCard(BaseCard):
    """
    卡片形式展示
    """

    def __init__(self, content):
        '''
        文本卡片显示的content
        :param content:
        '''
        super(TextCard, self).__init__(['content'])
        self.data['type'] = "txt"
        self.data['content'] = "%s" % content

if __name__ == '__main__':

    textCard = TextCard('sdfasdfs')
    textCard.set_content('hehe')
    print(textCard.get_data())
    pass
