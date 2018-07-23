#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/2/26

"""
    desc:pass
"""
import unittest

import math


import dueros.Log as log
import logging

class BaseTest(object):

    def test_sqrt(self):
        self.assertEqual(math.sqrt(4) * math.sqrt(4), 4)


if __name__ == "__main__":
    # unittest.main()
    # log.init_log("./log/my_program")  # 日志保存到./log/my_program.log和./log/my_program.log.wf，按天切割，保留7天
    # logging.info("Hello World!!!")

    a = 0
    if a:
        print('aaaa')
    else:
        print('bbb')