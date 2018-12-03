#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2017/12/30

"""
指令基类
"""
from dueros import Utils


class BaseDirective(object):
    """
    所有展示模板的基类
    """

    def __init__(self, directive_type):
        """

        :param directive_type:
        """

        self.data = dict()
        self.data['type'] = directive_type

    def get_data(self):
        """
        获取data
        :return:
        """

        return self.data

    def set_token(self, token):
        """
        设置directive的token. 默认在构造时自动生成了token，可以覆盖
        :param token:
        :return:
        """

        if token:
            self.data['token'] = token
        return self

    def gen_token(self):
        """
        生成token
        :return:
        """
        return Utils.gen_token()


if __name__ == '__main__':
    pass
