#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/26

"""
    desc:pass
"""

from dueros.directive.Display.template.BaseTemplate import BaseTemplate

class BodyTemplate5(BaseTemplate):

    def __init__(self):
        super(BodyTemplate5, self).__init__(['token','title', 'type'])
        self.setType('BaseTemplate')
        self.data['images'] = []

    def addImages(self, url, widthPixels = '', heightPixel = ''):

        imageStructure = self.createImageStructure(url, widthPixels, heightPixel)
        if imageStructure:
            self.data['images'].append(imageStructure.getData())
        return self
    pass


if __name__ == '__main__':
    pass