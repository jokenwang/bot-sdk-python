#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/11/12

"""
    desc:pass
"""
import unittest
from dueros.directive.Permission.AskForPermissionsConsent import AskForPermissionsConsent
from dueros.directive.Permission.PermissionEnum import PermissionEnum


class AskForPermissionsConsentTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_add_permission(self):
        data = {
            'type': 'Permission.AskForPermissionsConsent',
            'permissions': [
                {
                    'name': 'RECORD::SPEECH'
                }, {
                    'name': 'READ::DEVICE:LOCATION'}
            ],
            'token': 'test_token'
        }

        directive = AskForPermissionsConsent()
        directive.add_permission(PermissionEnum.RECORD_SPEECH)
        directive.add_permission(PermissionEnum.READ_DEVICE_LOCATION)
        directive.set_token('test_token')
        self.assertEqual(directive.get_data(), data)


if __name__ == '__main__':
    pass