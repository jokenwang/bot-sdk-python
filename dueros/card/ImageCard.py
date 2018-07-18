#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2017/12/31

from dueros.card.BaseCard import BaseCard


class ImageCard(BaseCard):

    def __init__(self):
        super(ImageCard, self).__init__()
        self.data['type'] = 'image'

    def add_item(self, src, thumbnail=''):
        '''
        添加
        :param src:
        :param thumbnail:
        :return:
        '''

        if not src:
            return self

        if not 'list' in self.data:
            self.data['list'] = []

        item = {}
        item['src'] = src

        if thumbnail:
            item['thumbnail'] = thumbnail
        self.data['list'].append(item)
        return self


if __name__ == '__main__':

    list = []

    dit = {'name':'adfa'}
    list.append(dit)

    print(list)

    pass
