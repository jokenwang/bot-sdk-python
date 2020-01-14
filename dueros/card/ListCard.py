#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# description:
# author:jack
# create_time: 2017/12/31

import json
from dueros.card.BaseCard import BaseCard
from dueros.card.ListCardItem import ListCardItem
import dueros.card.CardType as CardType


class ListCard(BaseCard):
    """
    标准列表卡片
    详见文档：https://dueros.baidu.com/didp/doc/dueros-bot-platform/dbp-custom/cards_markdown#%E6%A0%87%E5%87%86%E5%88%97%E8%A1%A8%E5%8D%A1%E7%89%87
    """

    def __init__(self):
        super(ListCard, self).__init__()
        self.data['type'] = CardType.CARD_TYPE_LIST

    def add_item(self, card_item):
        if isinstance(card_item, ListCardItem):
            if 'list' not in self.data:
                self.data['list'] = []
            self.data['list'].append(card_item.get_data())
        return self


if __name__ == '__main__':
    pass
