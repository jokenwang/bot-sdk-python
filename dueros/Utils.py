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
        if isinstance(dicts, dict):
            return key in dicts
        return False

    @staticmethod
    def checkKeysInDict(dicts, keys):

        if isinstance(dicts, str):
            dicts = json.loads(dicts)
        lastKey = keys[len(keys) - 1]
        for key in keys:
            if key in dicts:
                dicts = dicts[key]
                if lastKey == key:
                    return True
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
    def getDictDataByKeys(dicts, keys):
        if isinstance(dicts, dict):
            for key in keys:
                if key in dicts:
                    v = dicts[key]
                    if isinstance(v, dict):
                        dicts = v
                        continue
                    elif isinstance(v, str):
                        return v

    @staticmethod
    def getDictDataByKeyss(dicts, keys):
        if isinstance(dicts, str):
            dicts = json.loads(dicts)
        lastKey = keys[len(keys) - 1]
        for key in keys:
            if key in dicts:
                dicts = dicts[key]
                if lastKey == key:
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

if __name__ == '__main__':

    pass
