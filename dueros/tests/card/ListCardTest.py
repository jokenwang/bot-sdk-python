#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/7/13

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
        item.setTitle('title1')
        item.setContent('这是ListCardItem1')
        item.setUrl('http://www.baidu.com')
        item.setImage('www.png1')
        item1 = ListCardItem()
        item1.setTitle('title2')
        item1.setContent('这是ListCardItem2')
        item1.setUrl('http://www.baidu.com')
        item1.setImage('www.png2')
        self.listCard.addItem(item)
        self.listCard.addItem(item1)
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
        self.assertEquals(self.listCard.getData(), card)

if __name__ == '__main__':
    pass