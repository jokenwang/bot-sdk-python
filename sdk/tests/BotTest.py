#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# description:
# author:jack
# create_time: 2017/12/31 上午12:07

"""
    desc:pass
"""

import json
import logging
from sdk.Bot import Bot
from sdk.card.TextCard import TextCard


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('bot')

class BotTest(Bot):

    def launchRequest(self):
        return {
            'card': TextCard(r'欢迎使用家居控制!请告诉我您要查找什么智能设备，比如查找我的空调'),
            'outputSpeech': r'<speak>欢迎使用家居控制!请告诉我您要查找什么智能设备，比如查找我的空调</speak>'
        }

    def intentRequest(self):

        self.ask('deviceName')

        return {
            'card': TextCard('您要查找什么智能设备呢? 比如"查找我的空调"'),
            'outputSpeech': '<speak>您要查找什么智能设备呢? 比如"查找我的空调"</speak>'
        }

    def controlRequest(self):
        self.ask('deviceName')
        # deviceName = self.getSlots('deviceName')
        # print('deviceName %s' % (deviceName))
        return {
            'card': TextCard('请告诉您的指令，比如调小空调风速、设置温度为30度'),
            'outputSpeech': '请告诉您的指令，比如调小空调风速、设置温度为30度'
        }

    def __init__(self, data):
        super(BotTest, self).__init__(data)

        self.addLanchHandler(self.launchRequest)

        self.addIntentHandler('dueros.device_interface.smart_device.control', self.controlRequest)

        self.addIntentHandler('dueros.device_interface.smart_device.search', self.intentRequest)
    pass

if __name__ == '__main__':

    def launchData():
        with open("./json/launch.json", 'r') as load_f:
            return load_f.read()

    def searchData():
        with open("./json/search2.json", 'r') as load_f:
            return load_f.read()

    def controlData():
        with open("./json/control.json", 'r') as load_f:
            return load_f.read()

    data = searchData()
    bot = BotTest(data)
    bot.run()
    #


    pass