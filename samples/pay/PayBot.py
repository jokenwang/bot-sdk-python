#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/8/18

"""
    desc:pass
"""

from dueros.Bot import Bot
from dueros.directive.Pay.Charge import Charge
from dueros.directive.Display.RenderTemplate import RenderTemplate
class PayBot(Bot):

    def __init__(self, data):
        super(PayBot, self).__init__(data)
        self.add_launch_handler(self.handle_launch)

    def handle_launch(self):

        charge = Charge('0.01', 'order_id_123', 'product_name', 'test_charge_description')

        return {
            'directives': [charge],
            'outputSpeech':'支付测试'
        }

        pass

    pass


if __name__ == '__main__':
    pass