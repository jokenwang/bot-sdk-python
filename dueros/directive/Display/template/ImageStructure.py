#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/26

"""
    desc:pass
"""


class ImageStructure(object):

    def __init__(self):
        self.data = {}

    def set_url(self, url):
        if url:
            self.data['url'] = url

    def set_width_pixels(self, width):
        if width:
            self.data['widthPixels'] = width

    def set_height_pixels(self, height):
        if height:
            self.data['heightPixels'] = height

    def get_data(self):
        return self.data

if __name__ == '__main__':
    pass