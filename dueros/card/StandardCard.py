#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/1/2

"""
标准卡片
详见文档：https://dueros.baidu.com/didp/doc/dueros-bot-platform/dbp-custom/cards_markdown#%E6%A0%87%E5%87%86%E5%8D%A1%E7%89%87
"""

from dueros.card.BaseCard import BaseCard


class StandardCard(BaseCard):

    def __init__(self):
        super(StandardCard, self).__init__(['title', 'content', 'image'])
        self.data['type'] = 'standard'


if __name__ == '__main__':
    pass
