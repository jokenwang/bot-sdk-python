#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/7/20

"""
    desc:pass
"""
import unittest
from dueros.directive.Pay.Charge import Charge


class ChargeTest(unittest.TestCase):

    def setUp(self):
        self.charge = Charge('0.01', 'order_id_123', 'product_name', 'test_charge_description');

    def testGetData(self):

        self.charge.set_token('test_token')
        self.charge.set_seller_node('sellerNote')
        self.charge.set_seller_authorization_note('sellerAuthorizationNote')
        data = {
            'type': 'Connections.SendRequest',
            'name': 'Charge',
            'token': 'test_token',
            'payload':{
                'chargeBaiduPay':{
                    'authorizeAttributes':{
                        'authorizationAmount':{
                            'amount': '0.01',
                            'currencyCode': 'CNY'
                        },
                        'sellerAuthorizationNote': 'sellerAuthorizationNote'
                    },
                    'sellerOrderAttributes':{
                        'sellerOrderId': 'order_id_123',
                        'productName': 'product_name',
                        'description': 'test_charge_description',
                        'sellerNote': 'sellerNote'
                    }
                }
            }
        }
        self.assertEqual(self.charge.get_data(), data)


    pass


if __name__ == '__main__':
    pass