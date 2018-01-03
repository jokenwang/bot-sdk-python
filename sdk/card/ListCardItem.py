#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/1/3 下午3:29

"""
    desc:pass
"""

from sdk.card.BaseCard import BaseCard

class ListCardItem(BaseCard):

    def setTitle(self, title):
        if(title):
            self.data['title'] = title

    def setContent(self, content):
        if(content):
            self.data['content'] = content

    def setUrl(self, url):
        if(url):
            self.data['url'] = url

    def setImage(self, image):
        if(image):
            self.data['image'] = image

    def getData(self):
        return self.data


if __name__ == '__main__':
    pass