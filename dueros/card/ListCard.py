#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# description:
# author:jack
# create_time: 2017/12/31

"""
标准列表卡片
详见文档：https://dueros.baidu.com/didp/doc/dueros-bot-platform/dbp-custom/cards_markdown#%E6%A0%87%E5%87%86%E5%88%97%E8%A1%A8%E5%8D%A1%E7%89%87
"""

import json
from dueros.card.BaseCard import BaseCard
from dueros.card.ListCardItem import ListCardItem


class ListCard(BaseCard):

    def __init__(self):
        super(ListCard, self).__init__()
        self.data['type'] = 'list'

    def add_item(self, card_ietm):

        if isinstance(card_ietm, ListCardItem):

            if 'list' not in self.data:
                self.data['list'] = []
            self.data['list'].append(card_ietm.get_data())
        return self


if __name__ == '__main__':

    listCardItem1 = ListCardItem()
    listCardItem1.set_title('baidu')
    listCardItem1.set_url("http://www.baidu.com")
    listCardItem1.set_image("http://www.baidu.com")
    listCardItem1.set_content("http://www.baidu.com")

    print(id(listCardItem1))
    listCardItem2 = ListCardItem()
    listCardItem2.set_title("百度2")
    print(id(listCardItem2))

    listCardItem3 = ListCardItem()
    listCardItem3.set_title("百度3")
    print(id(listCardItem3))

    listCard = ListCard()
    listCard.add_item(listCardItem1)
    listCard.add_item(listCardItem2)
    listCard.add_item(listCardItem3)

    print(json.dumps(listCard.get_data()))

    pass
