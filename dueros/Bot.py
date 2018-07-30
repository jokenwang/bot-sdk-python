#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

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
from dueros.Utils import Utils

class Bot(Base):
    '''
    Bot入口
    '''

    def __init__(self, post_data):
        '''
        构造方法
        :param post_data:
        '''
        super(Bot, self).__init__()
        self.postData = post_data
        self.request = Request(post_data)
        self.session = self.request.get_session()
        self.nlu = self.request.get_nlu()
        self.response = Response(self.request, self.session, self.nlu)
        self.handler = []
        self.botMonitor = BotMonitor(post_data)
        self.intercept = []
        self.certificate = None
        self.callback_func = None
        self.callback_data = None
        self.event = {}
        logging.info('Bot init')

    def init_certificate(self, environ, private_key=''):
        """
        创建Certificate
        :param environ:
        :param private_key:
        :return:
        """

        self.certificate = Certificate(environ, self.postData, private_key)
        return self

    def enable_verify_request_sign(self):
        """
        开启签名验证
        :return:
        """

        if self.certificate:
            self.certificate.enable_verify_request_sign()
        return self

    def disable_verify_request_sign(self):
        """
        关闭签名验证
        :return:
        """

        if self.certificate:
            self.certificate.disable_verify_request_sign()
        return self

    def set_private_key(self, private_key):

        self.botMonitor.set_environment_info(private_key, 0)
        return self

    def add_launch_handler(self, func):
        """
        添加对LaunchRequest的处理函数
        :param func:    回调方法
        :return:
        """

        return self.__add_handler('LaunchRequest', func)

    def add_session_ended_handler(self, func):
        """
        添加对SessionEndedRequest的处理函数
        :param func:    回调方法
        :return:
        """

        return self.__add_handler('SessionEndedRequest', func)

    def add_intent_handler(self, intent_name, func):
        """
        添加对特定意图的处理函数
        :param intent_name:  意图英文标识名
        :param func:    回调方法
        :return:
        """

        return self.__add_handler('#' + intent_name, func)

    def __add_handler(self, mix, func):
        """
        私有方法
        添加Handler，条件处理顺序相关，优先匹配先添加的条件
            1、如果满足，则执行，有返回值则停止
            2、满足条件，执行返回null,继续寻找下一个满足的条件
        :param mix:     条件，比如意图以'#'开头的'#intentName'或者'LaunchRequest'、'SessionEndedRequest'
        :param func:    处理函数，满足mix条件后执行该函数
        :return:
        """

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

    def add_intercept(self, intercept):
        """
        添加拦截器
        :param intercept:
        :return:
        """

        if isinstance(intercept, Intercept):
            self.intercept.append(intercept)

    def add_event_listener(self, event, func):
        """
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
        """

        if event and func:
            self.event[event] = func

    def add_default_event_listener(self, func):
        """
        默认兜底事件的处理函数
        :param event:
        :param func:
        :return:
        """
        if hasattr(func, '__call__'):
            self.event['__default__'] = func

    def get_intent_name(self):
        """
        获取第一个Intent的名字
        :return:
        """

        return self.nlu.get_intent_name() if self.nlu else ''

    def get_session_attribute(self, field, default):
        """
        获取session某个字段值
        :param field:
        :param default:
        :return:
        """

        return self.session.get_data(field, default)

    def set_session_attribute(self, field, value, default):
        """
        设置session某个字段值
        :param field:
        :param value:
        :param default:
        :return:
        """
        self.session.set_data(field, value, default)

    def clear_session_attribute(self):
        """
        清空session
        :return:
        """

        self.session.clear()

    def get_slots(self, field, index=0):
        """
        获取槽位值
        :param field:
        :param index:
        :return:
        """

        if self.nlu and field is not None:
            return self.nlu.get_slot(field, index)

    def set_slots(self, field, value, index=0):
        """
        设置槽位值
        :param field:
        :param value:
        :param index:
        :return:
        """

        if self.nlu and field is not None:
            self.nlu.set_slot(field, value, index)

    def wait_answer(self):
        """
        告诉DuerOS, 在多轮对话中，等待用户回答
        :return:
        """

        if self.response:
            self.response.set_should_end_session(False)

    def end_dialog(self):
        """
        告诉DuerOS 需要结束对话
        :return:
        """

        if self.response:
            self.response.set_should_end_session(True)

    def end_session(self):
        """
        告诉DuerOS 需要结束对话
        :return:
        """
        self.end_dialog()

    def run(self, build=True):
        """
        事件路由添加后，需要执行此函数，对添加的条件、事件进行判断
        将第一个return 非null的结果作为此次的response
        :param build: False:不进行response封装，直接返回handler的result
        :return:
        """

        if self.certificate and not self.certificate.verify_request():
            return self.response.illegal_request()

        event_handler = self.__get_register_event_handler()

        if self.request.get_type() == 'IntentRequest' and not self.nlu and not event_handler:
            return self.response.default_result()

        ret = {}
        for intercept in self.intercept:
            self.botMonitor.set_pre_event_start()
            ret = intercept.preprocess(self)
            self.botMonitor.set_pre_event_end()
            if ret:
                return

        if not ret:
            if event_handler:
                self.botMonitor.set_device_event_start()
                event = self.request.get_event_data()
                ret = self.__call_func(event_handler, event)
                self.botMonitor.set_device_event_end()
            else:
                self.botMonitor.set_event_start()
                ret = self.__dispatch()
                self.botMonitor.set_event_end()

        for intercept in self.intercept:
            self.botMonitor.set_post_event_start()
            ret = intercept.postprocess(self, ret)
            self.botMonitor.set_post_event_end()

        res = self.response.build(ret)
        self.botMonitor.set_response_data(res)
        self.botMonitor.update_data()

        if self.callback_data:
            return json.dumps(ret)

        if not build:
            return json.dumps(ret)
        else:
            return json.dumps(res)

    def __dispatch(self):
        """
        分发请求并调用回调方法
        :return:
        """
        if not self.handler:
            return

        # 循环遍历handler 通过正则判断调用哪个handler
        for item in self.handler:
            if item:
                # 获取rule(其实是自己的技能意图的英文标识)
                rule = item['rule']
                # 校验handler
                if self.__check_handler(rule):
                    # 匹配到handler获取对应的回调方法并立即执行
                    func = item['func']
                    ret = self.__call_func(func, None)
                    if ret:
                        return ret
        # 调用回调
        self.un_match_handler(self.callback_data)

    def __get_register_event_handler(self):

        event_data = self.request.get_event_data()
        if event_data and event_data['type']:
            key = event_data['type']
            if key is not None and Utils.checkKeysInDict(self.event, key):
                return self.event[key]
            elif self.event['__default__']:
                return self.event['__default__']

    def __call_func(self, func, arg):
        """
        自定义方法调用
        :param func:    可以为方法、字符串，如果是字符串默认调用Bot的方法
        :param arg:     参数
        :return:
        """

        ret = ''
        if hasattr(func, '__call__'):
            if arg is None:
                ret = func()
            else:
                ret = func(arg)
        elif isinstance(func, str):
            directive_func = getattr(self, func, None)
            if directive_func:
                ret = directive_func(arg)
        return ret

    def get_token(self, rule):
        """

        :param rule:
        :return:
        """
        token = {}
        return self.get_slots(token, rule)
        pass

    def __get_token(self, token, rule):
        """

        :param token:
        :param rule:
        :return:
        """

        if rule == '' or not rule:
            return token
        pass

    def __check_handler(self, handler):
        """
        根据意图标识英文名 和 请求类型判断是否是此handler
        :param handler:
        :return:
        """

        rg = {
            'intent': r'#([\w\.\d_]+)',
            'requestType': r'^(LaunchRequest|SessionEndedRequest)$'
        }

        if re.match(rg['requestType'], handler):
            if self.request.get_type() == handler:
                self.callback_data = None
                return True
            else:
                self.un_match_handler({'type': 'requestType', 'message': u'未匹配到:' + self.request.get_type()})

        if re.match(rg['intent'], handler):
            if ('#' + self.get_intent_name()) == handler:
                self.callback_data = None
                return True
            else:
                self.callback_data = {'type': 'intent', 'message': u'handler未匹配到:' + self.get_intent_name()}

        if handler == 'true' or handler is True:
            return True

        return False

    def set_callback(self, func):
        """
        设置回调方法
        :param func:
        :return:
        """
        if hasattr(func, '__call__'):
            self.callback_func = func

    def un_match_handler(self, data):
        """
        未匹配到Handler回调
        :param data:
        :return:
        """
        if self.callback_func and data:
            self.callback_func(data)

    # TODO
    def token_value(self, str):
        '''

        :param str:
        :return:
        '''
        pass

    def declare_effect(self):
        self.response.set_need_determine()

    def effect_confirmed(self):
        self.request.is_determined()

    def set_expect_speech(self, expect_speech):
        """
        通过控制expectSpeech来控制麦克风开
        :param expect_speech:
        :return:
        """

        self.response.set_expect_speech(expect_speech)

    def set_fallback(self):
        """
        标识本次返回的结果是兜底结果
        :return:
        """

        self.response.set_fallback()

    def ask(self, slot):
        if self.nlu:
            self.nlu.ask(slot)

    def is_support_display(self):
        """
        判断设备是否支持Display
        :return:
        """
        return self.__is_support_interface('Display')

    def is_support_audio_player(self):
        """
        检测AudioPlayer对象是否存在
        :return:
        """
        return self.__is_support_interface('AudioPlayer')

    def is_support_video_player(self):
        """
        检测VideoPlayer对象是否存在
        :return:
        """
        return self.__is_support_interface('VideoPlayer')

    def __is_support_interface(self, support_func):
        """
        校验是否支持
        :param support_func:
        :return:
        """
        supported_interfaces = self.request.get_supported_interfaces()
        if supported_interfaces and isinstance(supported_interfaces, dict):
            return Utils.checkKeyInDict(supported_interfaces, support_func)
        else:
            return False


if __name__ == '__main__':
    pass
