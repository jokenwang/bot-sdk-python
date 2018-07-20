#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2017/12/30

"""
指令基类
"""

import time
import random
import hashlib
from dueros.Utils import Utils


class BaseDirective(object):

    def __init__(self, directive_type):
        self.data = {}

        self.data['type'] = directive_type

    def gen_token(self):
        """
        生成Token md5(9位随机数+时间戳) 再截取md5后的字符串
        :return: uuid
        """
        #生成随机数
        rand = str(random.randint(0, 9999999999))
        t = str(round(time.time() * 1000))
        md5Str = rand + t
        md5 = hashlib.md5()
        md5.update(md5Str.encode('utf-8'))
        token = md5.hexdigest()
        uuid = token[0:8] + '-'
        uuid = uuid + token[8:12] + '-'
        uuid = uuid + token[12:16] + '-'
        uuid = uuid + token[16:20] + '-'
        uuid = uuid + token[20:]
        return uuid

    def get_data(self):

        return self.data

    def set_token(self, token):
        if token:
            self.data['token'] = token
        return self

    def get_token(self):

        return Utils.get_dict_data_by_keys(self.data, ['token'])


if __name__ == '__main__':

    directive = BaseDirective('TEXT')
    print(directive.get_token())
    pass