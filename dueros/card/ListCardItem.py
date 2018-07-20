#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/1/3

"""

"""

from dueros.card.BaseCard import BaseCard


class ListCardItem(BaseCard):

    def __init__(self):
        super(ListCardItem, self).__init__(['title', 'content', 'url', 'image'])


if __name__ == '__main__':
    pass
