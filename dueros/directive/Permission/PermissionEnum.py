#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/28

"""
    desc:pass
"""

PERMISSION_USER_INFO = 'USER_INFO'
PERMISSION_LOCATION = 'LOCATION'
PERMISSION_RECORD = 'RECORD'

# 上面的即将废弃 请使用下面的三个新权限
READ_USER_PROFILE = 'READ::USER:PROFILE'
READ_DEVICE_LOCATION = 'READ::DEVICE:LOCATION'
WRITE_SMARTHOME_PRINTER = 'WRITE::SMARTHOME:PRINTER'
RECORD_SPEECH = 'RECORD::SPEECH'


def in_enum(permission):
    return permission == PERMISSION_USER_INFO \
           or permission == PERMISSION_LOCATION \
           or permission == PERMISSION_RECORD \
           or permission == READ_USER_PROFILE \
           or permission == READ_DEVICE_LOCATION \
           or permission == WRITE_SMARTHOME_PRINTER \
           or permission == RECORD_SPEECH


if __name__ == '__main__':

    pass
