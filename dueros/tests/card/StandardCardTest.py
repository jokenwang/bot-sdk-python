#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/7/20

"""
    desc:pass
"""
import unittest
from dueros.card.StandardCard import StandardCard


class StandardCardTest(unittest.TestCase):
    '''
    标准卡片测试
    '''

    def setUp(self):
        self.card = StandardCard()

    def testGetData(self):
        '''
        测试getData方法
        :return:
        '''

        self.card.set_title('title')
        self.card.set_content('这是StandardCard')
        self.card.set_image('www.png')
        card = {
            'type': 'standard',
            'title': 'title',
            'content': '这是StandardCard',
            'image': 'www.png'
        }
        self.assertEqual(self.card.get_data(), card)
    pass


if __name__ == '__main__':
    pass