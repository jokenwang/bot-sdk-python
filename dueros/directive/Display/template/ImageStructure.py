#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/26

"""
    desc:pass
"""


class ImageStructure:

    def __init__(self):
        self.data = {}
        super(ImageStructure, self).__init__()

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