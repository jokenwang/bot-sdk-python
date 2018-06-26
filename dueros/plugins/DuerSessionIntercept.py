#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/1/3

"""
    desc:pass
"""
from dueros.Intercept import Intercept
from dueros.card.TextCard import TextCard

class DuerSessionIntercept(Intercept):

    def __init__(self, tip = "非常抱歉，不明白你说的意思，已经取消了本次服务", threshold=2):
        self.tip = tip
        self.threshold = threshold

    def preprocess(self, bot):
        if(not self.threshold):
            return

        #NLU尝试slot提取，异常次数
        daException = bot.getSlots('da_system_not_understand')
        #bot 自身slot检查，不合法次数
        botException = bot.getSlots('bot_not_understand')
        count = 0
        if(daException):
            count = count + daException

        if(botException):
            count = count + botException

        if(count >= self.threshold):
            bot.clearSessionAttribute()
            bot.endDialog()
            card = TextCard(self.tip)
            return {
                'card': card
            }

if __name__ == '__main__':
    pass
