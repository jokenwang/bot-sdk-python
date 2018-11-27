#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/1/5

"""
    desc:pass
"""

import time
import random
import hashlib
import json
import hashlib


class Utils:

    @staticmethod
    def checkKeyInDict(dicts, key):
        '''
        校验字典中是否存在指定的key
        :param dicts:
        :param key:
        :return:
        '''
        if isinstance(dicts, dict):
            return key in dicts
        return False

    @staticmethod
    def checkKeysInDict(dicts, keys):

        if isinstance(dicts, dict):
            for key in keys:
                if key in dicts:
                    dicts = dicts[key]
                    continue
                return False

    @staticmethod
    def getDictDataByKey(dicts, key):
        tmp = dicts
        for k, v in tmp.items():
            if k == key:
                return v
            else:
                if isinstance(v, dict):
                    ret = Utils.getDictDataByKey(v, key)
                    if isinstance(ret, str):
                        return ret
        pass

    @staticmethod
    def get_dict_data_by_keys(dicts, keys):
        if isinstance(dicts, str):
            dicts = json.loads(dicts)
        last_key = keys[len(keys) - 1]
        for key in keys:
            if key in dicts:
                dicts = dicts[key]
                if last_key == key:
                    return dicts
                continue
            return None


    @staticmethod
    def is_numeric(value):
        if isinstance(value, str):
            return type(eval(value)) == int or type(eval(value)) == float
        else:
            return isinstance(value, int) or isinstance(value, float)

    @staticmethod
    def convert_number(value):
        if Utils.is_numeric(value):

            if isinstance(value, str):
                if type(eval(value)) == int:
                    return int(value)
                if type(eval(value)) == float:
                    return int(float(value))

            if isinstance(value, int) or isinstance(value, float):
                return int(value)

    @staticmethod
    def gen_token():
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

    @staticmethod
    def hash_str(key):
        sha1 = hashlib.sha1()
        sha1.update(key.encode('utf-8'))
        return sha1.hexdigest()

if __name__ == '__main__':
    sha1 = hashlib.sha1()
    sha1.update('http://vt1.doubanio.com/201811172131/16f6bbfeaaf6bbe6acba4c04fac2712d/view/movie/M/402380330.mp4'.encode('utf-8'))
    print(sha1.hexdigest())
    pass