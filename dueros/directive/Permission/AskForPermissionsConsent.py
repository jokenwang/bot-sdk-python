#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/30

"""
    desc:pass
"""
from dueros.directive.BaseDirective import BaseDirective
from dueros.directive.Permission.PermissionEnum import PermissionEnum
from dueros.Utils import Utils


class AskForPermissionsConsent(BaseDirective):

    def __init__(self):
        super(AskForPermissionsConsent, self).__init__('Permission.AskForPermissionsConsent')
        self.data['token'] = self.gen_token()

    def set_token(self, token):

        if token and isinstance(token, str):
            self.data['token'] = token

    def add_permission(self, name):
        if name and PermissionEnum.inEnum(name):
            if not Utils.checkKeyInDict(self.data, 'permissions'):
                self.data['permissions'] = []
            self.data['permissions'].append({'name': name.value})


if __name__ == '__main__':


    pass