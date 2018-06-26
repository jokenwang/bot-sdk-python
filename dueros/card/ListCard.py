#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# description:
# author:jack
# create_time: 2017/12/31

import json
from dueros.card.BaseCard import BaseCard
from dueros.card.ListCardItem import ListCardItem


class ListCard(BaseCard):

    def __init__(self):
        super(ListCard, self).__init__()
        self.data['type'] = 'list'

    def addItem(self, listCardIetm):

        if isinstance(listCardIetm, ListCardItem):

            if not 'list' in self.data:
                self.data['list'] = []
            self.data['list'].append(listCardIetm.getData())
        return self


if __name__ == '__main__':

    listCardItem1 = ListCardItem()
    listCardItem1.setTitle('baidu')
    listCardItem1.setUrl("http://www.baidu.com")
    listCardItem1.setImage("http://www.baidu.com")
    listCardItem1.setContent("http://www.baidu.com")

    print(id(listCardItem1))
    listCardItem2 = ListCardItem()
    listCardItem2.setTitle("百度2")
    print(id(listCardItem2))

    listCardItem3 = ListCardItem()
    listCardItem3.setTitle("百度3")
    print(id(listCardItem3))

    listCard = ListCard()
    listCard.addItem(listCardItem1)
    listCard.addItem(listCardItem2)
    listCard.addItem(listCardItem3)

    print(json.dumps(listCard.getData()))

    pass
