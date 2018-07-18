#!/usr/bin/env python2
# -*- encoding=utf-8 -*-
# description:
# author:jack
# create_time: 2018/1/3

"""
    desc:pass
"""

from dueros.Bot import Bot
class Bot(Bot):
    def launchRequest(self):
        '''
        打开调用名
        '''
        self.wait_answer()
        return {
            'outputSpeech': r'欢迎进入'
        }

    def getTaxSlot(self):
        '''
        获取槽位及逻辑处理
        '''
        num = self.get_slots('sys.number')
        city = self.get_slots('sys.city')
        if num and not city:
            self.nlu.ask('sys.city')
            return {
                'reprompt': r'你所在的城市是那里呢',
                'outputSpeech': r'你所在的城市是那里呢'
            }

        if city and not num:
            self.nlu.ask('sys.number')
            return {
                'reprompt': r'你的税前工资是多少呢',
                'outputSpeech': r'你的税前工资是多少呢'
            }
         
        computeType = self.get_slots('compute_type')
        if not computeType:
            self.nlu.ask('compute_type')
            return {
                'outputSpeech': r'你要查询什么税种呢'
            }
        else:
            taxNum = self.computeType(num, city)
            return {
                'outputSpeech': r'你需要缴纳' + str(taxNum)
            }
    
    def computeType(self, num, city):
        '''
        调用接口计算个税
        '''
        return 100


    def __init__(self, data):
        super(Bot, self).__init__(data)
        self.add_launch_handler(self.launchRequest)
        self.add_intent_handler('personal_income_tax.inquiry', self.getTaxSlot)


if __name__ == '__main__':
    pass
