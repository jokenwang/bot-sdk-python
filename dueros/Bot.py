#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# description:
# author:jack
# create_time: 2017/12/30

import json
import re
import logging

from dueros.monitor.BotMonitor import BotMonitor
from dueros.Certificate import Certificate
from dueros.Intercept import Intercept
from dueros.Request import Request
from dueros.Response import Response
from dueros.Base import Base

class Bot(Base):
    '''
    Bot入口
    '''

    def __init__(self, postdata, privateKey= ''):
        '''
        构造方法
        :param postData:
        '''
        super(Bot, self).__init__()
        self.postData = postdata
        self.request = Request(postdata)
        self.session = self.request.getSession()
        self.nlu = self.request.getNlu()
        self.response = Response(self.request, self.session, self.nlu)
        self.handler = []
        self.botMonitor = BotMonitor(postdata)
        self.intercept = []
        self.certificate = None
        self.callBackFunc = None
        self.cakkBackData = None
        self.event = {}
        # logging.info('Bot init')

    def initCertificate(self, environ, privateKey=''):
        '''
        创建Certificate
        :param environ:
        :return:
        '''

        self.certificate = Certificate(environ, self.postData, privateKey)
        return self

    def enableVerifyRequestSign(self):
        '''
        开启签名验证
        :return:
        '''

        if self.certificate:
            self.certificate.enableVerifyRequestSign()
        return self

    def disableVerifyRequestSign(self):
        '''
        关闭签名验证
        :return:
        '''

        if self.certificate:
            self.certificate.disableVerifyRequestSign()
        return self

    def setPrivateKey(self, privateKey):

        self.botMonitor.setEnvironmentInfo(privateKey, 0)
        return self

    def addLaunchHandler(self, func):
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

        if isinstance(mix, str) and hasattr(func, '__call__'):
            arr = {mix: func}
            mix = arr

        if not isinstance(mix, dict):
            return

        for key, value in mix.items():

            if not key or not value:
                return

            self.handler.append({
                'rule': key,
                'func': value
            })
        return self

    def addIntercept(self, intercept):
        '''
        添加拦截器
        :param intercept:
        :return:
        '''

        if isinstance(intercept, Intercept):
            self.intercept.append(intercept)

    def addEventListener(self, event, func):
        '''
        绑定一个事件的处理回调
        @link http://developer.dueros.baidu.com/doc/dueros-conversational-service/device-interface/audio-player_markdown 具体事件参考

        @example
        <pre>
        self.addEventListener('AudioPlayer.PlaybackStarted', function(event){
          return {
              'outputSpeech' => '事件处理好啦'
          }
        })
        </pre>
        :param event:   绑定的事件名称，比如AudioPlayer.PlaybackStarted
        :param func:    处理函数，传入参数为事件的request，返回值做完response给DuerOS
        :return:
        '''

        if isinstance(event, str) and hasattr(func, '__call__'):
            self.event[event] = func

    def addDefaultEventListener(self, func):
        '''
        默认兜底事件的处理函数
        :param event:
        :param func:
        :return:
        '''
        if hasattr(func, '__call__'):
            self.event['__default__'] = func

    def getIntentName(self):
        '''
        获取第一个Intent的名字
        :return:
        '''

        return self.nlu.getIntentName() if self.nlu else ''

    def getSessionAttribute(self, field, default=''):
        '''
        获取session某个字段值
        :param field:   属性名
        :param default: 未获取 返回默认值
        :return:
        '''
        if field and isinstance(field, str):
            return self.session.getData(field, default)
        else:
            return default

    def setSessionAttribute(self, field, value, default):
        '''
        设置session某个字段值
        :param field:       属性名
        :param value:       属性值
        :param default:     默认值
        :return:
        '''
        if field and isinstance(field, str):
            self.session.setData(field, value, default)

    def clearSessionAttribute(self):
        '''
        清空session字段所有值
        :return:
        '''

        self.session.clear()

    def getSlots(self, field, index=0):
        '''
        获取槽位值
        :param field:   槽位名
        :param index:   槽位 位置 默认值为0
        :return:
        '''

        if self.nlu and field and isinstance(field, str):
            return self.nlu.getSlot(field, index)

    def setSlots(self, field, value, index=0):
        '''
        设置槽位值
        :param field:   槽位名称(创建技能时的槽位名)
        :param value:   槽位填充的值(通过Dueros处理后放置进来的,为定义的词典值)
        :param index:
        :return:
        '''

        if self.nlu and field and isinstance(field, str):
            self.nlu.setSlot(field, value, index)

    def waitAnswer(self):
        '''
        告诉DuerOS, 在多轮对话中，等待用户回答。用来设置session是否为新的会话
        :return:
        '''

        if self.response:
            self.response.setShouldEndSession(False)

    def __endDialog(self):
        '''
        告诉DuerOS 需要结束对话
        :return:
        '''

        if self.response:
            self.response.setShouldEndSession(True)

    def endSession(self):
        '''
        告诉DuerOS 需要结束对话, 当技能需要关闭的时候在对应的意图中调用此方法
        :return:
        '''
        self.__endDialog()

    def run(self, build=True):
        '''
        Bot SDK 主要逻辑在这里
        1、判断是否校验请求数据的合法性
        2、获取事件的处理器Handler(通过addEventListener添加事件处理器)
        3、判断事件处理器是否存在是否能处理

        事件路由添加后，需要执行此函数，对添加的条件、事件进行判断
        将第一个return 非null的结果作为此次的response
        :param build: False:不进行response封装，直接返回handler的result
        :return:
        '''

        if self.certificate and not self.certificate.verifyRequest():
            return self.response.illegalRequest()

        eventHandler = self.__getRegisterEventHandler()

        if self.request.getType() == 'IntentRequest' and not self.nlu and not eventHandler:
            return self.response.defaultResult()

        ret = {}
        if self.intercept:
            for intercept in self.intercept:
                self.botMonitor.setPreEventStart()
                ret = intercept.preprocess(self)
                self.botMonitor.setPreEventEnd()
                if ret:
                    return

        if not ret:
            if eventHandler:
                self.botMonitor.setDeviceEventStart()
                event = self.request.getEventData()
                ret = self.__callFunc(eventHandler, event)
                self.botMonitor.setDeviceEventEnd()
            else:
                self.botMonitor.setEventStart()
                ret = self.__dispatch()
                self.botMonitor.setEventEnd()
        else:
            for intercept in self.intercept:
                self.botMonitor.setPostEventStart()
                ret = intercept.postprocess(self, ret)
                self.botMonitor.setPostEventEnd()

        res = self.response.build(ret)
        print(json.dumps(res))
        self.botMonitor.setResponseData(res)
        self.botMonitor.updateData()

        if self.cakkBackData:
            return json.dumps(self.cakkBackData)

        if not build:
            return json.dumps(ret)
        else:
            return json.dumps(res)
    
    def __dispatch(self):
        '''
        分发请求并调用回调方法
        1、判断handler是否
        :return:
        '''

        if not self.handler:
            return

        #循环遍历handler 通过正则判断调用哪个handler
        for item in self.handler:
            if item:
                #获取rule(其实是自己的技能意图的英文标识)
                rule = item['rule']
                #校验handler
                if self.__checkHandler(rule):
                    #匹配到handler获取对应的回调方法并立即执行
                    func = item['func']
                    ret = self.__callFunc(func, None)
                    if ret:
                        return ret
        #调用回调
        self.unMatchHandler(self.callBackData)


    def __getRegisterEventHandler(self):
        '''
        根据Dueros传递来的事件，在本地查找是否注册过本事件，如果找到则返回对应的handler方法，否则返回默认的handler
        :see addEventListener
        :return:
        '''
        eventData = self.request.getEventData()
        if eventData and eventData['type']:
            key = eventData['type']
            if self.event[key]:
                return self.event[key]
            elif self.event['__default__']:
                return self.event['__default__']

    def __callFunc(self, func, arg):
        '''
        自定义方法调用
        :param func:    可以为方法、字符串，如果是字符串默认调用Bot的方法
        :param arg:     参数
        :return:
        '''

        ret = ''
        if hasattr(func, '__call__'):
            if not arg:
                ret = func()
            else:
                ret = func(arg)
        elif isinstance(func, str):
            directive_func = getattr(self, func, None)
            if directive_func:
                ret = directive_func(arg)
        return ret

    def getToken(self, rule):
        '''

        :param rule:
        :return:
        '''

        token = {}
        return self.getSlots(token, rule)
        pass

    def __getToke(self, token, rule):
        '''

        :param token:
        :param rule:
        :return:
        '''

        if rule == '' or not rule:
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

        if re.match(rg['requestType'], handler):
            if self.request.getType() == handler:
                self.callBackData = None
                return True
            else:
                self.unMatchHandler({'type': 'requestType', 'message': u'未匹配到:' + self.request.getType()})

        if re.match(rg['intent'], handler):
            if ('#' + self.getIntentName()) == handler:
                self.callBackData = None
                return True
            else:
                self.callBackData = {'type': 'intent', 'message': u'handler未匹配到:' + self.getIntentName()}

        if handler == 'true' or handler == True:
            return True

        return False

    def setCallBack(self, func):
        '''
        设置回调方法
        :param func:
        :return:
        '''
        if hasattr(func, '__call__'):
            self.callBackFunc = func

    def unMatchHandler(self, data):
        '''
        未匹配到Handler回调
        :param func:
        :return:
        '''
        if self.callBackFunc and data:
            self.callBackFunc(data)

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

    def setExpectSpeech(self, expectSpeech=False):
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
        '''
        询问槽位信息
        :param slot:
        :return:
        '''
        if self.nlu and slot:
            self.nlu.ask(slot)


if __name__ == '__main__':
    pass
