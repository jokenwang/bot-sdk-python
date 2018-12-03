#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/1

"""
    desc:pass
"""
from dueros import Utils


class BaseMediaListItem(object):
    """
    BaseListItem类
    """

    def __init__(self, title, title_subtext1):
        """

        :param title:
        :param title_subtext1:
        """

        self.data = dict()
        self.data['title'] = title
        self.data['titleSubtext1'] = title_subtext1
        self.data['token'] = Utils.gen_token()

    def set_favorited(self, favorited=False):
        """
        设置isFavorited
        :param favorited: True/False
        :return:
        """
        if isinstance(favorited, bool):
            self.data['isFavorited'] = favorited
        else:
            raise ValueError('The Arg favorited is not bool')

    def set_image(self, image):
        """
        设置image
        :param image:
        :return:
        """
        if image:
            if not isinstance(image, str):
                image = str(image)
            if not Utils.check_key_in_dict(self.data, 'image'):
                self.data['image'] = {}
                self.data['image']['src'] = {}
            self.data['image']['src'] = image
        else:
            raise ValueError('The Arg image is null')

    def set_title_subtext1(self, title_subtext1):
        """
        设置titleSubtext1
        @:param title_subtext1
        :return:
        """
        if title_subtext1:
            if not isinstance(title_subtext1, str):
                title_subtext1 = str(title_subtext1)
            self.data['titleSubtext1'] = title_subtext1
        else:
            raise ValueError('The Arg title_subtext1 is null')

    def set_title_subtext2(self, text_subtext2):
        """
        设置titleSubtext2
        :param text_subtext2:
        :return:
        """
        if text_subtext2:
            if not isinstance(text_subtext2, str):
                text_subtext2 = str(text_subtext2)
            self.data['titleSubtext2'] = text_subtext2
        else:
            raise ValueError('The Arg text_subtext2 is null')

    def set_token(self, token):
        if token:
            self.data['token'] = token

    def get_data(self):
        return self.data


if __name__ == '__main__':
    pass