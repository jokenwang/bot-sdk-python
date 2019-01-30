#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/28

"""
    desc:pass
"""
from enum import Enum, unique


@unique
class PermissionEnum(Enum):

    PERMISSION_USER_INFO = 'USER_INFO'
    PERMISSION_LOCATION = 'LOCATION'
    PERMISSION_RECORD = 'RECORD'

    #上面的即将废弃 请使用下面的三个新权限
    READ_USER_PROFILE = 'READ::USER:PROFILE'
    READ_DEVICE_LOCATION = 'READ::DEVICE:LOCATION'
    WRITE_SMARTHOME_PRINTER = 'WRITE::SMARTHOME:PRINTER'
    RECORD_SPEECH = 'RECORD::SPEECH'

    @staticmethod
    def inEnum(position):
        return position in PermissionEnum.__members__.values()


if __name__ == '__main__':

    # position = TextContentPosition()
    print(PermissionEnum.PLAIN_TEXT.value)
    pass