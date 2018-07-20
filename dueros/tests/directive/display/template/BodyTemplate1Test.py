#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/7/20

"""
    desc:pass
"""

import unittest
from dueros.directive.Display.template.BodyTemplate1 import BodyTemplate1


class BodyTemplate1Test(unittest.TestCase):

    '''
    bodyTemplate测试
    '''

    def setUp(self):
        self.template = BodyTemplate1()
        self.template.set_plain_text_content('test')
        self.template.set_background_image('http://www.baidu.com')
        self.template.set_token('0c71de96-15d2-4e79-b97e-e52cec25c254')

    def testGetData(self):
        '''
        测试getData
        :return:
        '''

        data = self.template.get_data()
        ret = {
            'type': 'BodyTemplate1',
            'token': '0c71de96-15d2-4e79-b97e-e52cec25c254',
            'textContent': {
                'text': {
                    'type': 'PlainText',
                    'text': 'test'
                },
                'position': 'BOTTOM-LEFT'
            },
            'backgroundImage': {
                'url': 'http://www.baidu.com'
            }
        }

        self.assertEqual(data, ret)
    pass


if __name__ == '__main__':
    pass