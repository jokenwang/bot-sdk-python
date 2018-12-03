#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/30

"""
    desc:pass
"""
from dueros.directive.BaseDirective import BaseDirective
from dueros.directive.Permission import PermissionEnum
from dueros import Utils


class AskForPermissionsConsent(BaseDirective):
    """
    申请权限指令
    """

    def __init__(self):
        BaseDirective.__init__(self, 'Permission.AskForPermissionsConsent')
        self.data['token'] = self.gen_token()

    def add_permission(self, permission):
        """
        添加权限
        :param permission:
        :return:
        """
        if permission and PermissionEnum.in_enum(permission):
            if not Utils.check_key_in_dict(self.data, 'permissions'):
                self.data['permissions'] = []
            self.data['permissions'].append({'name': permission})
        else:
            error = 'The permission: "%s" is not support' % permission
            raise ValueError(error)


if __name__ == '__main__':
    pass