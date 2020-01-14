#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/1/3

from dueros.Intercept import Intercept
from dueros.card.TextCard import TextCard


class DuerSessionIntercept(Intercept):
    """
    自定义拦截器
    """

    def __init__(self, tip="非常抱歉，不明白你说的意思，已经取消了本次服务", threshold=2):
        self.tip = tip
        self.threshold = threshold

    def preprocess(self, bot):
        if not self.threshold:
            return

        # NLU尝试slot提取，异常次数
        da_exception = bot.getSlots('da_system_not_understand')
        # bot 自身slot检查，不合法次数
        bot_exception = bot.getSlots('bot_not_understand')
        count = 0
        if da_exception:
            count = count + da_exception

        if bot_exception:
            count = count + bot_exception

        if count >= self.threshold:
            bot.clear_session_attribute()
            bot.end_session()
            card = TextCard(self.tip)
            return {
                'card': card
            }
