#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/26

"""
    desc:pass
"""

from dueros.card.BaseCard import BaseCard

class ImageStructure(BaseCard):

    def __init__(self):
        super(ImageStructure, self).__init__()


    def setUrl(self, url):
        if url:
            self.data['url'] = url

    def setWidthPixels(self, width):
        if width:
            self.data['widthPixels'] = width

    def setHeightPixels(self, height):
        if height:
            self.data['heightPixels'] = height
    pass


if __name__ == '__main__':
    pass