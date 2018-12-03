#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/7/20

"""
    desc:pass
"""

import unittest
from dueros.card.ListCardItem import ListCardItem
from dueros.card.ListCard import ListCard


class ListCardTest(unittest.TestCase):
    '''
    '''

    def setUp(self):
        self.listCard = ListCard()


    def testAddItem(self):
        '''
        测试addItem方法
        :return:
        '''
        item = ListCardItem()
        item.set_title('title1')
        item.set_content('这是ListCardItem1')
        item.set_url('http://www.baidu.com')
        item.set_image('www.png1')
        item1 = ListCardItem()
        item1.set_title('title2')
        item1.set_content('这是ListCardItem2')
        item1.set_url('http://www.baidu.com')
        item1.set_image('www.png2')
        self.listCard.add_item(item)
        self.listCard.add_item(item1)
        card = {
            'type': 'list',
            'list': [
                {
                    'title': 'title1',
                    'content': '这是ListCardItem1',
                    'url': 'http://www.baidu.com',
                    'image': 'www.png1'
                },
                {
                    'title': 'title2',
                    'content': '这是ListCardItem2',
                    'url': 'http://www.baidu.com',
                    'image': 'www.png2'
                }
            ]
        }
        self.assertEqual(self.listCard.get_data(), card)


if __name__ == '__main__':
    pass