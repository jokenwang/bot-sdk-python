#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/26

"""
BodyTemplate5模板
详见文档：https://dueros.baidu.com/didp/doc/dueros-bot-platform/dbp-custom/display-template_markdown#BodyTemplate5
"""

from dueros.directive.Display.template.BaseTemplate import BaseTemplate


class BodyTemplate5(BaseTemplate):

    def __init__(self):
        super(BodyTemplate5, self).__init__(['token', 'title', 'type'])
        self.set_type('BodyTemplate5')
        self.data['images'] = []

    def add_images(self, url, width_pixels='', height_pixels=''):

        image_structure = self.create_image_structure(url, width_pixels, height_pixels)
        if image_structure:
            self.data['images'].append(image_structure.get_data())
        return self
    pass


if __name__ == '__main__':
    pass