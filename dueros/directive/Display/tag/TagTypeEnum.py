#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/17

"""
    desc:pass
"""
TAG_TYPE_AMOUNT = 'AMOUNT'
TAG_TYPE_AUDITION_NEW = 'AUDITION'
TAG_TYPE_CUSTOM = 'CUSTOM'
TAG_TYPE_FREE = 'FREE'
TAG_TYPE_HOT = 'HOT'
TAG_TYPE_NEW = 'NEW'
TAG_TYPE_PAY = 'PAY'
TAG_TYPE_PURCHASED = 'PURCHASED'
TAG_TYPE_TIME = 'TIME'
TAG_TYPE_VIP = 'VIP'


def in_enum(tag):
    return tag == TAG_TYPE_AMOUNT \
           or tag == TAG_TYPE_AUDITION_NEW \
           or tag == TAG_TYPE_CUSTOM \
           or tag == TAG_TYPE_FREE \
           or tag == TAG_TYPE_HOT \
           or tag == TAG_TYPE_NEW \
           or tag == TAG_TYPE_PAY \
           or tag == TAG_TYPE_PURCHASED \
           or tag == TAG_TYPE_TIME \
           or tag == TAG_TYPE_VIP

if __name__ == '__main__':
    pass
