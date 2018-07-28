#!/usr/bin/env python2
# -*- encoding=utf-8 -*-
# description:
# author:jack
# create_time: 2018/1/3

"""
    desc:pass
"""

from dueros.Bot import Bot
from dueros.card.TextCard import TextCard

class Bot(Bot):
    def launchRequest(self):
        '''
        打开调用名
        '''
        card = TextCard('欢迎来到猜数字游戏')
        return {
            'card' : card,
            'outputSpeech': r'欢迎来到猜数字游戏'
        }

    def compareNum(self):
        '''
        获取数字槽位值处理
        '''
        rightNum = 10
        num = self.get_slots('sys.number');
        num = int(num)
        if num > rightNum:
            return {
                'outputSpeech' :'您所猜的数字大了'
            }
        elif num < rightNum:
            return {
                'outputSpeech' :'您所猜的数字小了'
            }
        else:
            return {
                'outputSpeech' :'恭喜您猜对了'
            }

    def __init__(self, data):
        super(Bot, self).__init__(data)
        self.add_launch_handler(self.launchRequest)
        self.add_intent_handler('guess_number', self.compareNum)


if __name__ == '__main__':
    pass
