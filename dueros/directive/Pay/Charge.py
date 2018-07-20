#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/7/20

"""
DuerOS 支付协议
详见：https://dueros.baidu.com/didp/doc/dueros-bot-platform/dbp-pay/pay_markdown
"""
from dueros.directive.BaseDirective import BaseDirective
from dueros.Utils import Utils


class Charge(BaseDirective):

    CODE_CNY = 'CNY'

    def __init__(self, amount, seller_order_id, product_name, description):
        super(Charge, self).__init__('Connections.SendRequest')
        self.data['name'] = 'Charge'
        self.data['token'] = self.gen_token()
        self.data['payload'] = {}
        self.data['payload']['chargeBaiduPay'] = {}
        self.data['payload']['chargeBaiduPay']['authorizeAttributes'] = {}
        self.data['payload']['chargeBaiduPay']['sellerOrderAttributes'] = {}
        self.data['payload']['chargeBaiduPay']['authorizeAttributes']['authorizationAmount'] = {}
        self.set_amount(amount)
        self.set_seller_order_id(seller_order_id)
        self.set_product_name(product_name)
        self.set_description(description)

    def set_token(self, token):
        """
        设置directive的token. 默认在构造时自动生成了token，可以覆盖
        :param token:
        :return:
        """
        if token:
            self.data['token'] = token

    def get_token(self):
        """
        获取directive的token. 默认在构造时自动生成了token
        :return:
        """
        return Utils.getDictDataByKeyss(self.data, ['videoItem', 'stream', 'token'])

    def set_amount(self, amount, currency_code=CODE_CNY):
        """
        设置支付金额
        :param amount:
        :param currency_code:
        :return:
        """
        if Utils.is_numeric(amount) and currency_code and isinstance(currency_code, str):
            self.data['payload']['chargeBaiduPay']['authorizeAttributes']['authorizationAmount'][
                'amount'] = str(amount)
            self.data['payload']['chargeBaiduPay']['authorizeAttributes']['authorizationAmount'][
                'currencyCode'] = currency_code

    def set_seller_authorization_note(self, seller_authorization_note):
        """
        :param seller_authorization_note:
        :return:
        """
        if isinstance(seller_authorization_note, str) and seller_authorization_note:
            self.data['payload']['chargeBaiduPay']['authorizeAttributes']['sellerAuthorizationNote'] \
                = seller_authorization_note

    def set_seller_order_id(self, seller_order_id):
        """
        设置订单ID
        :param seller_order_id:
        :return:
        """
        if isinstance(seller_order_id, str) and seller_order_id:
            self.data['payload']['chargeBaiduPay']['sellerOrderAttributes']['sellerOrderId'] = seller_order_id

    def set_product_name(self, product_name):
        """
        设置商品名称
        :param product_name:
        :return:
        """
        if isinstance(product_name, str) and product_name:
            self.data['payload']['chargeBaiduPay']['sellerOrderAttributes']['productName'] = product_name

    def set_description(self, description):
        """
        设置描述
        :param description:
        :return:
        """
        if isinstance(description, str) and description:
            self.data['payload']['chargeBaiduPay']['sellerOrderAttributes']['description'] = description

    def set_seller_node(self, seller_note):
        """
        设置备注
        :param seller_note:
        :return:
        """
        if isinstance(seller_note, str) and seller_note:
            self.data['payload']['chargeBaiduPay']['sellerOrderAttributes']['sellerNote'] = seller_note


if __name__ == '__main__':
    pass