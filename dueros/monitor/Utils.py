#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/1/5

"""
    desc:pass
"""
import json

class Utils:

    @staticmethod
    def checkKeyInDict(dicts, key):
        '''
        校验字典中是否存在指定的key
        :param dicts:
        :param key:
        :return:
        '''
        if(isinstance(dicts, dict)):
            return key in dicts
        return False

    @staticmethod
    def checkKeysInDict(dicts, keys):

        if isinstance(dicts, str):
            dicts = json.loads(dicts)
        lastKey = keys[len(keys)-1]
        for key in keys:
            if key in dicts:
                dicts = dicts[key]
                if lastKey == key:
                    return True
                continue
            return False


if __name__ == '__main__':
    pass