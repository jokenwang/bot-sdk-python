#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/1

"""
    desc:pass
"""
from dueros.Utils import Utils


class BaseMediaListItem:
    """
    BaseListItem类
    """

    def __init__(self, title, title_subtext1):
        self.data = {}
        self.data['title'] = title
        self.data['titleSubtext1'] = title_subtext1
        self.data['token'] = Utils.gen_token()

    def set_token(self, token):
        if token:
            self.data['token'] = token

    def set_favorited(self, favorited=False):
        """
        设置isFavorited
        :param favorited:
        :return:
        """
        if isinstance(favorited, bool):
            self.data['isFavorited'] = favorited

    def set_image(self, image):
        """
        设置image
        :param image:
        :return:
        """
        if image and isinstance(image, str):
            if not Utils.checkKeyInDict(self.data, 'image'):
                self.data['image'] = {}
                self.data['image']['src'] = {}
            self.data['image']['src'] = image

    def set_title_subtext1(self, title_subtext1):
        """
        设置titleSubtext1
        @:param title_subtext1
        :return:
        """
        if title_subtext1 and isinstance(title_subtext1, str):
            self.data['titleSubtext1'] = title_subtext1

    def set_title_subtext2(self, text_subtext2):
        """
        设置titleSubtext2
        :param text_subtext2:
        :return:
        """
        if text_subtext2 and isinstance(text_subtext2, str):
            self.data['titleSubtext2'] = text_subtext2

    def get_data(self):
        return self.data


if __name__ == '__main__':
    pass