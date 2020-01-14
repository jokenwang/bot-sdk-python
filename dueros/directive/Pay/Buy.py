#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2019-07-04

from dueros.directive.BaseDirective import BaseDirective


class Buy(BaseDirective):
    """
    用于生成Buy指令的类
    """

    def __init__(self, product_id, token=''):
        super(Buy, self).__init__('Connections.SendRequest.Buy')
        if token:
            self.data['token'] = token
        self.data['payload']['productId'] = product_id
