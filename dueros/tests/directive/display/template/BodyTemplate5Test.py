#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/7/20

"""
    desc:pass
"""
import unittest
from dueros.directive.Display.template.BodyTemplate5 import BodyTemplate5


class BodyTemplate5Test(unittest.TestCase):

    '''
    bodyTemplate测试
    '''

    def setUp(self):
        self.template = BodyTemplate5()
        self.template.set_background_image('http://www.baidu.com')
        self.template.set_token('0c71de96-15d2-4e79-b97e-e52cec25c254')
        self.template.add_images('http://uri-img1.com', '1332', '123')
        self.template.add_images('http://uri-img1.com',)
        self.template.add_images('http://uri-img1.com', '32', '123')

    def testGetData(self):
        '''
        测试getData
        :return:
        '''

        data = self.template.get_data()
        ret = {
            'type': 'BodyTemplate5',
            'token': '0c71de96-15d2-4e79-b97e-e52cec25c254',
            'images':[
                {
                    'url':'http://uri-img1.com',
                    'widthPixels': '1332',
                    'heightPixels': '123'
                },{
                    'url':'http://uri-img1.com'
                },{
                    'url': 'http://uri-img1.com',
                    'widthPixels': '32',
                    'heightPixels': '123'
                }
            ],
            'backgroundImage': {
                'url': 'http://www.baidu.com'
            }
        }

        self.assertEqual(data, ret)
    pass


if __name__ == '__main__':
    pass