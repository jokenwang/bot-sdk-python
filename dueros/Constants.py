#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/4/15

"""
    desc:pass
"""


class _Constants:

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
#授权url
constants.PERMISSION_URL_USER_INFO = 'https://xiaodu.baidu.com/saiya/v1/user/profile'
constants.PERMISSION_PATH_USER_PROFILE = '/saiya/v1/user/profile'
constants.PERMISSION_PATH_RECORD_SPEECH = '/saiya/v1/user/record/speech'
constants.PERMISSION_PATH_DEVICE_LOCATION = '/saiya/v1/devices/location'
constants.PERMISSION_PATH_SMARTHOME_PRINTER = '/saiya/v1/smarthome/printer'
constants.PERMISSION_PATH_MATEAPP_NOTIFICATION = '/saiya/v1/mateapp/notification'

#session key
constants.SESSION_KEY_API_ACCESS_TOKEN = 'session_key_api_access_token'

if __name__ == '__main__':
    print(constants.P)
    pass