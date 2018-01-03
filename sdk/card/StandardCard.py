#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/1/2 下午11:57

"""
    desc:pass
"""

from sdk.card.BaseCard import BaseCard

class StandardCard(BaseCard):

    def __init__(self):
        super(StandardCard, self).__init__({'title', 'content', 'image'})
        self.data['type'] = 'standard'
    pass

    def setTitle(self, title):
        if(title):
            self.data['title'] = title

    def setContent(self, content):

        if(content):
            self.data['content'] = content

    def setImage(self, image):
        if(image):
            self.data['image'] = image

    def getData(self):
        return self.data


if __name__ == '__main__':
    pass