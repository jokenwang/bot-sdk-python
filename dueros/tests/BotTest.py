#!/usr/bin/env python2
# -*- encoding: UTF-8 -*-

# description:
# author:jack
# create_time: 2017/12/31

"""
    desc:pass
"""

import logging
from dueros.Bot import Bot
from dueros.card.TextCard import TextCard
from dueros.directive.Display.template.BodyTemplate1 import BodyTemplate1
from dueros.directive.Display.RenderTemplate import RenderTemplate
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('bot')
import sys


class BotTest(Bot):

    def launchRequest(self):
        return {
            'card': TextCard(r'欢迎使用家居控制!请告诉我您要查找什么智能设备，比如查找我的空调'),
            'outputSpeech': r'<speak>欢迎使用家居控制!请告诉我您要查找什么智能设备，比如查找我的空调</speak>'
        }

    def searchRequest(self):

        self.ask('deviceName')

        # card = TextCard('您要查找什么智能设备呢? 比如"查找我的空调"')
        # card.addCueWords("百度")
        # card.addCueWords("百度")
        # card.addCueWords("百度")
        # card.setAnchor("http://www.baidu.com", "百度")

        # renderTemplate = RenderTemplate()
        bodyTemplate = BodyTemplate1()
        bodyTemplate.set_token('token')
        bodyTemplate.set_title('托尔斯泰的格言')
        bodyTemplate.set_background_image('https://skillstore.cdn.bcebos.com/icon/100/c709eed1-c07a-be4a-b242-0b0d8b777041.jpg')
        bodyTemplate.set_plaintext_content('拖尔斯泰-理想的书籍是智慧的钥匙')
        renderTemplate = RenderTemplate(bodyTemplate)

        # renderTemplate.setTemplate(bodyTemplate)
        renderTemplate.set_token("renderTemplate")
        return {
            'directives': [renderTemplate],
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

    def inquiry(self):
        return {
            'directives': TextCard('请告诉您的指令，比如调小空调风速、设置温度为30度'),
            'outputSpeech': '请告诉您的指令，比如调小空调风速、设置温度为30度'
        }

    def __init__(self, data):
        super(BotTest, self).__init__(data)

        self.add_launch_handler(self.launchRequest)

        self.add_intent_handler('dueros.device_interface.smart_device.control', self.controlRequest)

        self.add_intent_handler('dueros.device_interface.smart_device.search', self.searchRequest)
        # self.addIntentHandler('inquiry', self.inquiry)
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


    def controlData2():
        with open("./json/a.json", 'r') as load_f:
            return load_f.read()


    def tt(data):
        print(data)
    data = searchData()
    bot = BotTest(data)
    bot.setCallBack(tt)
    bot.run()
    #
    # rand = str(random.randint(0, 9999999999))
    # t = str(round(time.time() * 1000))
    # md5 = hashlib.md5()
    # md5Str = rand + t
    # print("md5Str = %s, encode = %s ", (md5Str,md5Str.encode('utf-8')))
    # md5.update(md5Str.encode('utf-8'))
    # token = md5.hexdigest()
    # uuid = token[0:8] + '-'
    # uuid = uuid + token[8:12] + '-'
    # uuid = uuid + token[12:16] + '-'
    # uuid = uuid + token[16:20] + '-'
    # uuid = uuid + token[20:]
    print(sys.version_info[0])
    #while True:
    #    print("====")
    pass
