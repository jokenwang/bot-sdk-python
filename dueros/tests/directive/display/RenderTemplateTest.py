#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/7/13

"""
    desc:pass
"""
import unittest
from dueros.directive.Display.RenderTemplate import RenderTemplate
from dueros.directive.Display.template.BodyTemplate2 import BodyTemplate2


class RenderTemplateTest(unittest.TestCase):
    '''
    测试卡片
    '''

    def setUp(self):
        self.template = BodyTemplate2()
        self.template.set_plain_content('plain context by set')
        self.template.set_image('http://image-uri.com', '123', '234')
        self.renderTemplate = RenderTemplate(self.template)

    def testGetData(self):

        data = self.renderTemplate.get_data()
        print(type(data))
        data['template']['token'] = 'token'
        print(data)
        ret = {
            'type': 'Display.RenderTemplate',
            'template':{
                'type': 'BodyTemplate2',
                'token': 'token',
                'content': {
                    'type': 'PlainText',
                    'text': 'plain context by set'
                },
                'image': {
                    'url': 'http://image-uri.com',
                    'widthPixels': '123',
                    'heightPixels': '234'
                }
            }
        }

        self.assertEqual(data, ret)
    pass


if __name__ == '__main__':
    pass