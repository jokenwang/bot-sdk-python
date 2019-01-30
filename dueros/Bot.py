#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# description:
# author:jack
# create_time: 2017/12/30
"""
Bot入口, 实现自己的技能需要继承此类。并在构造方法内添加意图的处理方法
"""

import json
import re
import logging
import urllib3
from dueros.monitor.BotMonitor import BotMonitor
from dueros.Certificate import Certificate
from dueros.Intercept import Intercept
from dueros.Request import Request
from dueros.Response import Response
from dueros.Base import Base
from dueros.Utils import Utils
from dueros.Constants import constants


class Bot(Base):

    def __init__(self, request_data, private_key=''):
        """
        构造方法
        :param request_data:
        :param private_key  私钥 此私钥和在技能 服务配置 中配置的公钥 为一对秘钥
        """

        Base.__init__(self)
        self.request_data = request_data
        logging.info('技能收到的请求数据:%s' % request_data)
        self._request = Request(request_data)
        self._session = self._request.get_session()
        self._nlu = self._request.get_nlu()
        self._response = Response(self._request, self._session, self._nlu)
        self._handler = []
        self._botMonitor = BotMonitor(request_data, private_key)
        self._intercept = []
        self._certificate = None
        self._callback_func = None
        self._callback_data = None
        self._event = {}

    def init_certificate(self, environ, private_key=''):
        """
        创建Certificate
        :param environ:
        :param private_key
        :return:
        """

        self._certificate = Certificate(environ, self.request_data, private_key)
        return self

    def enable_verify_request_sign(self):
        """
        开启签名验证
        :return:
        """

        if self._certificate:
            self._certificate.enable_verify_request_sign()
        return self

    def disable_verify_request_sign(self):
        """
        关闭签名验证
        :return:
        """
        if self._certificate:
            self._certificate.disable_verify_request_sign()
        return self

    def set_monitor_enabled(self, enable=False):
        """
        设置是否开启Monitor 默认开启
        :param enable:
        :return:
        """
        if isinstance(enable, bool):
            self._botMonitor.set_monitor_enabled(enable)
        return self

    def set_monitor_url(self, url):
        """
        设置数据统计url，不依赖百度的数据统计，自己可以实现数据统计。否则使用百度的数据统计
        :param url:
        :return:
        """
        if self._botMonitor:
            self._botMonitor.set_monitor_url(url)

    def set_private_key(self, private_key):
        """
        Deprecated
        :param private_key:
        :return:
        """
        self._botMonitor.set_environment_info(private_key, 0)
        return self

    def set_environment_info(self, private_key, environment=0):
        """
        设置私钥和环境模式 默认debug
        :param private_key: 私钥
        :param environment: 0代表你的Bot在DBP平台debug环境，1或者其他整数代表online环境
        :return:
        """
        self._botMonitor.set_environment_info(private_key, environment)
        return self

    def set_delegate(self):
        """
        设置delegate 某个槽位或确认意图
        :return:
        """
        if self._nlu:
            self._nlu.set_delegate()

    def set_confirm_slot(self, field):
        """
        设置对一个槽位的确认
        :param field:
        :return:
        """
        if self._nlu:
            self._nlu.set_confirm_slot(field)

    def set_confirm_intent(self):
        """
        设置confirm 意图。询问用户是否对意图确认，设置后需要自行返回outputSpeech
        :return:
        """
        if self._nlu:
            self._nlu.set_confirm_intent()

    def add_launch_handler(self, func):
        """
        添加对LaunchRequest的处理函数
        :param func:    回调方法
        :return:
        """
        if hasattr(func, '__call__'):
            def innerfunc():
                self.set_session_attribute(constants.SESSION_KEY_API_ACCESS_TOKEN, self.get_api_access_token(), '')
                return func()
            self._add_handler('LaunchRequest', innerfunc)

    def add_session_ended_handler(self, func):
        """
        添加对SessionEndedRequest的处理函数, 如果想要获取结束原因
        func方法需要接收event  方法应定义为 func(event), 否则不会传递event到func
        :param func:    回调方法
        :return:
        """
        if hasattr(func, '__call__'):
            argcount = func.__code__.co_argcount
            if argcount == 1:
                def innerfunc(event):
                    return func()
                return self.add_session_ended_event_listener(innerfunc)
            elif argcount == 2:
                return self.add_session_ended_event_listener(func)

    def add_session_ended_event_listener(self, func):
        """
        添加对SessionEndedRequest的处理函数,可以获取到终止原因, function(event), event为事件数据
        :param func:
        :return:
        """
        self.add_event_listener('SessionEndedRequest', func)

    def add_intent_handler(self, intent_name, func):
        """
        添加对特定意图的处理函数
        :param intent_name:  意图英文标识名
        :param func:    回调方法
        :return:
        """

        return self._add_handler('#' + intent_name, func)

    def _add_handler(self, mix, func):
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

            self._handler.append({
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
            self._intercept.append(intercept)

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

        if isinstance(event, str) and hasattr(func, '__call__'):
            self._event[event] = func

    def add_default_event_listener(self, func):
        """
        默认兜底事件的处理函数
        :param event:
        :param func:
        :return:
        """
        if hasattr(func, '__call__'):
            self._event['__default__'] = func

    def get_intent_name(self):
        """
        获取第一个Intent的名字
        :return:
        """

        return self._nlu.get_intent_name() if self._nlu else ''

    def get_session_attribute(self, field, default=''):
        """
        获取session某个字段值
        :param field:   属性名
        :param default: 未获取 返回默认值
        :return:
        """
        if field is not None and isinstance(field, str):
            return self._session.get_data(field, default)
        else:
            return default

    def set_session_attribute(self, field, value, default):
        """
        设置session某个字段值
        :param field:       属性名
        :param value:       属性值
        :param default:     默认值
        :return:
        """
        if field is not None and isinstance(field, str):
            self._session.set_data(field, value)
        else:
            self._session.set_data(field, default)

    def clear_session_attribute(self):
        """
        清空session字段所有值
        :return:
        """

        self._session.clear()

    def get_slots(self, field, index=0):
        """
        获取槽位值
        :param field:   槽位名
        :param index:   槽位 位置 默认值为0
        :return:
        """

        if self._nlu and field and isinstance(field, str):
            return self._nlu.get_slot(field, index)

    def set_slots(self, field, value, index=0):
        """
        设置槽位值
        :param field:   槽位名称(创建技能时的槽位名)
        :param value:   槽位填充的值(通过Dueros处理后放置进来的,为定义的词典值)
        :param index:
        :return:
        """

        if self._nlu and field and isinstance(field, str):
            self._nlu.set_slot(field, value, index)

    def wait_answer(self):
        """
        告诉DuerOS, 在多轮对话中，等待用户回答。用来设置session是否为新的会话
        :return:
        """

        if self._response:
            self._response.set_should_end_session(False)

    def _end_dialog(self):
        """
        告诉DuerOS 需要结束对话
        :return:
        """

        if self._response:
            self._response.set_should_end_session(True)

    def end_session(self):
        """
        告诉DuerOS 需要结束对话, 当技能需要关闭的时候在对应的意图中调用此方法
        :return:
        """
        self._end_dialog()

    def run(self, build=True):
        """
        Bot SDK 主要逻辑在这里
        1、判断是否校验请求数据的合法性
        2、获取事件的处理器Handler(通过addEventListener添加事件处理器)
        3、判断事件处理器是否存在是否能处理

        事件路由添加后，需要执行此函数，对添加的条件、事件进行判断
        将第一个return 非null的结果作为此次的response
        :param build: False:不进行response封装，直接返回handler的result
        :return:
        """

        if self._certificate and not self._certificate.verify_request():
            return self._response.illegal_request()

        event_handler = self._get_register_event_handler()

        if self._request.get_type() == 'IntentRequest' and not self._nlu and not event_handler:
            return self._response.default_result()

        ret = {}
        for intercept in self._intercept:
            self._botMonitor.set_pre_event_start()
            ret = intercept.preprocess(self)
            self._botMonitor.set_pre_event_end()
            if ret:
                return

        if not ret:
            if event_handler:
                self._botMonitor.set_device_event_start()
                event = self._request.get_event_data()
                ret = self._call_func(event_handler, event)
                self._botMonitor.set_device_event_end()
            else:
                self._botMonitor.set_event_start()
                ret = self._dispatch()
                self._botMonitor.set_event_end()

        for intercept in self._intercept:
            self._botMonitor.set_post_event_etart()
            ret = intercept.postprocess(self, ret)
            self._botMonitor.setPost_event_end()
        res = self._response.build(ret)
        logging.info('技能返回数据: %s' % json.dumps(res, ensure_ascii=False))
        self._botMonitor.set_response_data(res)
        self._botMonitor.update_data()

        if self._callback_data:
            return json.dumps(self._callback_data, ensure_ascii=False)

        if not build:
            return json.dumps(ret, ensure_ascii=False)
        else:
            return json.dumps(res, ensure_ascii=False)
    
    def _dispatch(self):
        """
        分发请求并调用回调方法
        1、判断handler是否
        :return:
        """

        if not self._handler:
            return

        #循环遍历handler 通过正则判断调用哪个handler
        for item in self._handler:
            if item:
                #获取rule(其实是自己的技能意图的英文标识)
                rule = item['rule']
                #校验handler
                if self._check_handler(rule):
                    #匹配到handler获取对应的回调方法并立即执行
                    func = item['func']
                    ret = self._call_func(func, None)
                    if ret:
                        return ret
        #调用回调
        self.un_match_handler(self._callback_data)

    def _get_register_event_handler(self):
        """
        根据Dueros传递来的事件，在本地查找是否注册过本事件，如果找到则返回对应的handler方法，否则返回默认的handler
        :see addEventListener
        :return:
        """

        event_data = self._request.get_event_data()
        if event_data and event_data['type']:
            key = event_data['type']
            if key is not None and Utils.checkKeyInDict(self._event, key):
                return self._event[key]
            elif Utils.checkKeyInDict(self._event, '__default__'):
                return self._event['__default__']
            else:
                logging.info('request type = %s 未匹配到任何处理事件' % key)
                return None

    def _call_func(self, func, arg):
        """
        自定义方法调用
        :param func:    可以为方法、字符串，如果是字符串默认调用Bot的方法
        :param arg:     参数
        :return:
        """

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

    def get_token(self, rule):
        """
        :param rule:
        :return:
        """

        token = {}
        return self.get_slots(token, rule)
        pass

    def _check_handler(self, handler):
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
            if self._request.get_type() == handler:
                self._callback_data = None
                return True
            else:
                self.un_match_handler({'type': 'requestType', 'message': u'未匹配到:' + self._request.get_type()})

        if re.match(rg['intent'], handler):
            if ('#' + self.get_intent_name()) == handler:
                self._callback_data = None
                return True
            else:
                self._callback_data = {'type': 'intent', 'message': u'handler未匹配到:' + self.get_intent_name()}

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
            self._callback_func = func

    def un_match_handler(self, data):
        """
        未匹配到Handler回调
        :param func:
        :return:
        """

        if self._callback_func and data:
            self._callback_func(data)

    def declare_effect(self):

        self._response.set_need_determine()

    def effect_confirmed(self):

        self._request.is_determined()

    def set_expect_speech(self, expect_speech=False):
        """
        通过控制expectSpeech来控制麦克风开
        详见文档：
        https://dueros.baidu.com/didp/doc/dueros-bot-platform/dbp-custom/response_markdown#response%E5%8F%82%E6%95%B0%E8%AF%B4%E6%98%8E
        中的expectSpeech字段描述
        :param expect_speech:
        :return:
        """

        self._response.set_expect_speech(expect_speech)

    def set_fallback(self):
        """
        标识本次返回的结果是兜底结果
        :return:
        """

        self._response.set_fallback()

    def ask(self, slot):
        """
        询问槽位信息
        :param slot:
        :return:
        """

        if self._nlu and slot:
            self._nlu.ask(slot)

    def is_support_display(self):
        """
        判断设备是否支持Display
        :return:
        """
        return self._is_support_interface('Display')

    def is_support_audio_player(self):
        """
        检测AudioPlayer对象是否存在
        :return:
        """
        return self._is_support_interface('AudioPlayer')

    def is_support_video_player(self):
        """
        检测VideoPlayer对象是否存在
        :return:
        """
        return self._is_support_interface('VideoPlayer')

    def _is_support_interface(self, support_func):
        """
        校验是否支持
        :param support_func:
        :return:
        """
        supported_interfaces = self._request.get_supported_interfaces()
        if supported_interfaces and isinstance(supported_interfaces, dict):
            return Utils.checkKeyInDict(supported_interfaces, support_func)
        else:
            return False

    def get_api_access_token(self):
        """
        获取LaunchRequest 中的apiAccessToken
        :return:
        """
        return self._request.get_api_access_token()

    def get_api_endpoint(self):
        """
        获取ApiEndPoint
        :return:
        """
        return self._request.get_api_endpoint()

    def get_device_id(self):
        """
        获取设备ID
        :return:
        """
        return self._request.get_device_id()

    def default_event(self):
        """
        默认事件处理"""
        self.wait_answer()
        self.set_expect_speech(False)

    def add_expect_text_response(self, text):
        """
        技能所期待的用户回复，技能将该信息反馈给DuerOS，有助于DuerOS在语音识别以及识别纠错时向该信息提权。
        :param text:
        :return:
        """
        self._response.add_expect_text_response(text)

    def add_expect_slot_response(self, slot):
        """
        技能所期待的用户回复，技能将该信息反馈给DuerOS，有助于DuerOS在语音识别以及识别纠错时向该信息提权。
        :param slot:
        :return:
        """
        self._response.add_expect_slot_response(slot)

    def get_user_id(self):
        """
        获取用户ID
        :return:
        """
        return self._request.get_user_id()

    def get_bot_id(self):
        """
        获取技能ID
        :return:
        """
        return self._request.get_bot_id()

    def get_query(self):
        """
        获取请求的Query
        :return:
        """
        return self._request.get_query()

    """==================================Dueros通用意图=================================="""

    def add_common_default_intent_handler(self, func):
        """
        在无法识别用户需求的场景下，则直接将用户请求发给技能
        :param func:
        :return:
        """
        self.add_intent_handler('ai.dueros.common.default_intent', func)

    def add_common_stop_intent_handler(self, func):
        """
        停止的意图用于用户表达停止内容资源(音乐、视频、有声)等场景。
        已经为你富集好了用户表达确认的多样化表达，可直接引用停止的意图。
        :param func:
        :return:
        """
        self.add_intent_handler('ai.dueros.common.stop_intent', func)

    def add_common_next_intent_handler(self, func):
        """
        下一个的意图用于用户表达下一个内容资源(音乐、视频、有声)等场景。
        已经为你富集好了用户表达确认的多样化表达，可直接引用下一个的意图。
        :param func:
        :return:
        """
        self.add_intent_handler('ai.dueros.common.next_intent', func)

    def add_common_cancel_intent_handler(self, func):
        """
        取消的意图用于用户中断对话任务的场景。已经为你富集好了用户表达确认的多样化表达，可直接引用取消的意图
        :param func:
        :return:
        """
        self.add_intent_handler('ai.dueros.common.cancel_intent', func)

    def add_common_confirm_intent_handler(self, func):
        """
        确认的意图用于用户确认对话任务的场景。已经为你 富集好了用户表达确认的多样化表达，可直接引用确认的意图。
        :param func:
        :return:
        """
        self.add_intent_handler('ai.dueros.common.confirm_intent', func)

    def add_common_pause_intent_handler(self, func):
        """
        暂停的意图用于用户表达暂停内容资源(音乐、视频、有声)等场景。
        已经为你富集好了用户表达确认的多样化表达，可直接引用暂停的意图。
        :param func:
        :return:
        """
        self.add_intent_handler('ai.dueros.common.pause_intent', func)

    def add_common_continue_intent_handler(self, func):
        """
        继续的意图用于用户表达继续内容资源(音乐、视频、有声)等场景。
        已经为你富集好了用户表达确认的多样化表达，可直接引用暂停的意图。
        :param func:
        :return:
        """
        self.add_intent_handler('ai.dueros.common.continue_intent', func)

    def add_common_previous_intent_handler(self, func):
        """
        上一个的意图用于用户表达上一个内容资源(音乐、视频、有声)等场景。
        已经为你富集好了用户表达确认的多样化表达，可直接引用上一个的意图。
        :param func:
        :return:
        """
        self.add_intent_handler('ai.dueros.common.previous_intent', func)

    """==================================Dueros授权事件=================================="""

    def add_permission_granted_event(self, func=None):
        """
        授权成功事件,如果func存在则回调给用户自己处理，否则内部处理授权返回授权信息，回调permission_granted
        :param func:
        :return:
        """
        if hasattr(func, '__call__'):
            self.add_event_listener('Permission.Granted', func)
        else:
            self.add_event_listener('Permission.Granted', self._permission_granted_event)

    def _permission_granted_event(self, event):
        return self.get_user_profile()

    def permission_granted(self, user_info):
        """
        授权成功 返回用户信息
        :param user_info:
        :return:
        """
        raise NotImplementedError('需要自己实现')

    def add_permission_rejected_event(self, func):
        """
        表示用户拒绝授权
        :param func:
        :return:
        """
        if hasattr(func, '__call__'):
            self.add_event_listener('Permission.Rejected', func)

    def add_permission_grant_failed_event(self, func):
        """
        表示用户同意授权，但是由于其他原因导致授权失败
        :param func:
        :return:
        """
        if hasattr(func, '__call__'):
            self.add_event_listener('Permission.GrantFailed', func)

    """==================================Dueros事件=================================="""

    def add_display_element_selected(self, func):
        """
        选择事件回调,示例:
        'request': {
            'type': 'Display.ElementSelected',
            'requestId': '{{STRING}}',
            'timestamp': '{{STRING}}',
            'token': '{{STRING}}'
        }
        通过token去完成自己后续的业务逻辑
        :param func:
        :return:
        """

        self.add_event_listener('Display.ElementSelected', func)

    def add_form_button_clicked(self, func):
        """
        屏幕点击事件回调, 根据event['name'] 控件名称判断
        'request': {
            'type': 'Form.ButtonClicked',
            'name": "{{控件名称}}',
            'requestId': '{{STRING}}',
            'timestamp': '{{STRING}},
            'token': '{{STRING}}
        }
        控件名称详见https://dueros.baidu.com/didp/doc/dueros-bot-platform/dbp-custom/form_markdown
        :param func:
        :return:
        """
        self.add_event_listener('Form.ButtonClicked', func)

    def add_form_radio_button_clicked(self, func):
        """
        屏幕RadioButton点击事件回调
        {
           'type': 'RADIO_BUTTON',
            'name': '{{STRING}}',
            'selectedValue': '{{STRING}}'
        }
        :param func:
        :return:
        """
        self.add_event_listener('Form.RadioButtonClicked', func)

    def get_user_profile(self):
        """
        获取用户百度账号信息
        :return:
        """

        opts = {
            'path': '/saiya/v1/user/profile'
        }
        return self._http_request(opts)

    def get_record_speech(self, audio_token):
        """
        获取用户录音数据
        :return:
        """

        opts = {
            'path': '/saiya/v1/user/record/speech',
            'data': {
                'audioToken': audio_token
            }
        }
        return self._http_request(opts)

    def get_device_location(self):
        """
        获取地理位置
        :return:
        """

        opts = {
            'path': '/saiya/v1/devices/location'
        }
        return self._http_request(opts)

    def call_smarthome_printer(self, data):
        """
        智能家居打印服务
        :param data:
        :return:
        """
        data['path'] = '/saiya/v1/smarthome/printer'
        opts = self._build_request_post(data)
        return self._http_request(opts)

    def send_mateapp_notification(self, data):
        """

        :param data:
        :return:
        """
        data['path'] = '/saiya/v1/mateapp/notification'
        opts = self._build_request_post(data)
        return self._http_request(opts)

    def _build_request_post(self, data):
        api_access_token = self.get_api_access_token()
        headers = {
            'Authorization': 'bearer %s' % api_access_token,
            'Content-Type': 'application/json'
        }
        opts = {
            'path': data['path'],
            'method': 'POST',
            'data': data,
            'headers': headers
        }
        return opts

    def _http_request(self, opts):

        api_access_token = self.get_api_access_token()
        api_endpoint = self.get_api_endpoint()
        header = {
            'Authorization': 'bearer %s' % api_access_token
        }
        default_opts = {
            'url': '',
            'method': 'GET',
            'timeout': 1,
            'uri': api_endpoint,
            'path': '',
            'data': {},
            'headers': header
        }
        if isinstance(opts, dict):
            opts = {**default_opts, **opts}
        else:
            opts = default_opts

        http = urllib3.PoolManager()
        url = opts['uri'] + opts['path'] if not opts['url'] else ''
        method = opts['method']
        logging.info('请求地址:%s , Method:%s' % (url, method))
        if method == 'GET' or method == 'POST':
            try:
                r = http.request(method, url, fields=opts['data'], headers=opts['headers'],
                             timeout=opts['timeout'])
                result = str(r.data, 'utf-8')
                return json.loads(result)
            except Exception as e:
                logging.error('请求失败:%s' % e)
                return None
        else:
            logging.error('暂不支持其他类型的请求:', method)
            pass


if __name__ == '__main__':
    pass
