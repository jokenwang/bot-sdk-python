#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/4/15

"""
    desc:pass
"""


class _Constants(object):

    class ConstError(TypeError): pass

    class ConstCaseError(ConstError): pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("can't change const %s" % name)
        if not name.isupper():
            raise self.ConstCaseError('const name "%s" is not all uppercase' % name)
        self.__dict__[name] = value


constants = _Constants()

#日志存放地址
constants.LOG_PATH = './apps/log/dueros'

if __name__ == '__main__':
    print(constants.LOG_PATH)
    pass