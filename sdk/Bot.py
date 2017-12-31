#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# description:
# author:jack
# create_time: 2017/12/30

"""
    desc:Bot入口
"""

import json
import re
from lib.Request import Request
from lib.Response import Response

class Bot(object):

    def __init__(self, postData, privateKey = ''):
        '''

        :param postData:
        :param privateKey:
        '''

        #如果第一个参数为字符串，认为是privateKey
        if(postData and isinstance(postData, str)):
            self.privateKey = postData
            self.postData = False
        #TODO

        self.request = Request(postData)
        self.session = self.request.getSession()
        self.nlu = self.request.getNlu()
        self.response = Response(self.request, self.session, self.nlu)
        self.handler = []

    def addLanchHandler(self, func):
        '''
        添加对LaunchRequest的处理函数

        :param func:    回调方法
        :return:
        '''
        return self.__addHandler('LaunchRequest', func)

    def addSessionEndedHandler(self, func):
        '''
        添加对SessionEndedRequest的处理函数
        :param func:    回调方法
        :return:
        '''

        return self.__addHandler('SessionEndedRequest', func)

    def addIntentHandler(self, intentName, func):
        '''
        添加对特定意图的处理函数
        :param intentName:  意图英文标识名
        :param func:    回调方法
        :return:
        '''

        return self.__addHandler('#' + intentName, func)


    def __addHandler(self, mix, func):
        '''
        私有方法
        添加Handler，条件处理顺序相关，优先匹配先添加的条件
            1、如果满足，则执行，有返回值则停止
            2、满足条件，执行返回null,继续寻找下一个满足的条件
        :param mix:     条件，比如意图以'#'开头的'#intentName'或者'LaunchRequest'、'SessionEndedRequest'
        :param func:    处理函数，满足mix条件后执行该函数
        :return:
        '''

        if(isinstance(mix, str) and hasattr(func,'__call__') ):
            arr = {mix: func}
            mix = arr

        if(not isinstance(mix, dict)):
            return

        for key, value in mix.items():

            if (not key or not value):
                return

            self.handler.append({
                'rule': key,
                'func': value
            })

    def addIntercept(self, intercept):
        self.intercept = intercept


    def addEventListener(self, event, func):
        '''
        绑定一个事件的处理回调
        @link http://developer.dueros.baidu.com/doc/dueros-conversational-service/device-interface/audio-player_markdown 具体事件参考

        @example
        <pre>
        $this->addEventListener('AudioPlayer.PlaybackStarted', function($event){
          return [
              'outputSpeech' => '事件处理好啦',
          ];
        });
        </pre>
        :param event:   绑定的事件名称，比如AudioPlayer.PlaybackStarted
        :param func:    处理函数，传入参数为事件的request，返回值做完response给DuerOS
        :return:
        '''

        if(event and func):
            self.event[event] = func

    def addDefaultEventListener(self, event, func):
        '''
        默认兜底事件的处理函数
        :param event:
        :param func:
        :return:
        '''
        if(hasattr(func,'__call__')):
            self.event['__default__'] = func

    def getIntentName(self):
        '''
        获取第一个Intent的名字
        :return:
        '''

        if(self.nlu):
            return self.nlu.getIntentName()

    def getSessionAttribute(self, field, default):
        '''
        获取session某个字段值
        :param field:
        :param default:
        :return:
        '''

        return self.session.getData(field, default)

    def setSessionAttribute(self, field, value, default):
        '''
        设置session某个字段值
        :param field:
        :param value:
        :param default:
        :return:
        '''

        self.session.setData(field, value, default)

    def clearSessionAttribute(self):
        '''
        清空session
        :return:
        '''

        self.session.clear()

    def getSlots(self, field, index = 0):
        '''
        获取槽位值
        :param field:
        :param index:
        :return:
        '''

        if(self.nlu):
            return self.nlu.getSlot(field, index)

    def setSlots(self, field, value, index = 0):
        '''
        设置槽位值
        :param field:
        :param value:
        :param index:
        :return:
        '''

        if(self.nlu):
            self.nlu.setSlot(field, value, index)

    def waitAnswer(self):
        '''
        告诉DuerOS, 在多轮对话中，等待用户回答
        :return:
        '''

        if(self.response != None):
            self.response.setShouldEndSession(False)

    def endDialog(self):
        '''
        告诉DuerOS 需要结束对话
        :return:
        '''

        if(self.response != None):
            self.response.setShouldEndSession(True)

    def run(self, build = True):
        '''
        事件路由添加后，需要执行此函数，对添加的条件、事件进行判断
        将第一个return 非null的结果作为此次的response
        :param build: False:不进行response封装，直接返回handler的result
        :return:
        '''

        #TODO 验证请求签名

        eventHandler = self.__getRegisterEventHandler()

        if(self.request.getType() == 'IntentRequest' and not self.nlu and not eventHandler):
            return self.response.defaultResult()

        #TODO 请求前拦截器

        if(eventHandler):
            #TODO 添加监控
            event = self.request.getEventData()
            ret = self.__callFunc(eventHandler, event)
            #TODO 添加监控
        else:
            #TODO 添加监控
            ret = self.dispatch()
            #TODO 添加监控

        #TODO 返回后拦截器

        if(ret):
            print('====== ret %s' % ret)
            res = self.response.build(ret)
            print('%s' % json.dumps(res))
            #TODO 监控

            if(not build):
                return json.dumps(ret)
            return json.dumps(res)
        else:
            return ret

    def dispatch(self):
        '''
        分发请求并调用回调方法
        :return:
        '''

        if(not self.handler):
            return

        #循环遍历handler 通过正则判断调用哪个handler
        for item in self.handler:
            if(item):
                #获取rule(其实是自己的技能意图的英文标识)
                rule = item['rule']
                #校验handler
                if(self.__checkHandler(rule)):
                    #匹配到handler获取对应的回调方法并立即执行
                    func = item['func']
                    ret = self.__callFunc(func, None)
                    if(ret):
                        return ret


    def __getRegisterEventHandler(self):

        eventData = self.request.getEventData()
        if(eventData and eventData['type']):
            key = eventData['type']
            if(self.event[key]):
                return self.event[key]
            elif (self.event['__default__']):
                return self.event['__default__']

    def __callFunc(self, func, arg):
        '''
        自定义方法调用
        :param func:    可以为方法、字符串，如果是字符串默认调用Bot的方法
        :param arg:     参数
        :return:
        '''

        ret = ''
        if(hasattr(func, '__call__')):
            if(arg == None):
                ret = func()
            else:
                ret = func(arg)
        elif(isinstance(func, str)):
            directive_func = getattr(self, func, None)
            if directive_func:
                ret = directive_func(arg)
        return ret

    # TODO
    def getToken(self, rule):
        '''

        :param rule:
        :return:
        '''

        token = {}
        return self.getSlots(token, rule)
        pass

    #TODO
    def __getToke(self, token, rule):
        '''

        :param token:
        :param rule:
        :return:
        '''

        if(rule == '' or not rule):
            return token
        pass

    def __checkHandler(self, handler):
        '''
        根据意图标识英文名 和 请求类型判断是否是此handler
        :param handler:
        :return:
        '''

        rg = {
            'intent': r'#([\w\.\d_]+)',
            'requestType': r'^(LaunchRequest|SessionEndedRequest)$'
        }

        match = False

        if(re.match(rg['requestType'], handler) and self.request.getType() == handler):
            match = True
            return True

        if(re.match(rg['intent'], handler) and ('#' + self.getIntentName()) == handler):
            match = True
            return True

        if(handler == 'true' or handler == True):
            match = True
            return True

        return False

    #TODO
    def tokenValue(self, str):
        '''

        :param str:
        :return:
        '''
        pass

    def declareEffect(self):
        self.response.setNeedDetermine()

    def effectConfirmed(self):
        self.request.isDetermined()

    def setExpectSpeech(self, expectSpeech):
        '''
        通过控制expectSpeech来控制麦克风开
        :param expectSpeech:
        :return:
        '''

        self.response.setExpectSpeech(expectSpeech)

    def setFallBack(self):
        '''
        标识本次返回的结果是兜底结果
        :return:
        '''

        self.response.setFallBack()

    def ask(self, slot):
        if(self.nlu):
            self.nlu.ask(slot)


if __name__ == '__main__':
    pass