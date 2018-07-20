#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/1/3
"""
    desc:pass
"""
from dueros.monitor.model.Request import Request
from dueros.monitor.model.Response import Response
from dueros.monitor.BotMonitorConfig import BotMonitorConfig
from dueros.Certificate import Certificate
import json
import base64
import time
import requests
import threading


class BotMonitor:

    def __init__(self, post_data, private_key=''):
        if not isinstance(post_data, dict):
            post_data = json.loads(post_data)
        self.data = post_data
        self.request_start_time = self.get_millisecond()
        self.request_end_time = 0
        self.request = Request(post_data)
        self.audio_url = None
        self.app_name = None
        self.package_name = None
        self.deep_link = None
        self.event_start_time = 0
        self.event_cost_time = 0
        self.device_event_start_time = 0
        self.device_event_cost_time = 0
        self.user_event_list = {}
        self.is_event_make_pair = {}
        self.config = BotMonitorConfig()
        self.private_key = private_key
        self.environment = 0
        self.enabled = True
        self.certificate = None
        self.response = None

    def set_environment_info(self, private_key, environment):
        print(private_key)
        self.private_key = private_key
        self.environment = environment
        self.certificate = Certificate(None, self.data, private_key)

    def set_monitor_enabled(self, enabled):
        '''
        设置是否可用
        :param enabled:
        :return:
        '''
        self.enabled = enabled

    def set_response_data(self, response_data):

        if self.is_should_disable():
            return
        self.request_end_time = self.get_millisecond()
        self.response = Response(response_data)

    def set_event_start(self):

        if self.is_should_disable():
            return
        self.event_start_time = self.get_millisecond()

    def set_event_end(self):

        if self.is_should_disable():
            return
        self.event_cost_time = self.get_millisecond() - self.event_start_time

    def set_device_event_start(self):

        if self.is_should_disable():
            return
        self.device_event_start_time = self.get_millisecond()

    def set_device_event_end(self):

        if self.is_should_disable():
            return
        self.device_event_cost_time = self.get_millisecond() - self.device_event_start_time

    def set_opration_tic(self, task_name):

        if self.is_should_disable():
            return
        if task_name:
            self.user_event_list[task_name] = self.get_millisecond()
            self.is_event_make_pair[task_name] = False

    def set_opration_toc(self, task_name):

        if self.is_should_disable():
            return
        if task_name:

            if task_name in self.user_event_list:
                old_time = self.user_event_list[task_name]
            else:
                old_time = None
            cost_time = 0

            if old_time:
                curr_time = self.get_millisecond()
                cost_time = curr_time - old_time

            self.user_event_list[task_name] = cost_time
            self.is_event_make_pair[task_name] = True

    def set_app_name(self, app_nme):

        if self.is_should_disable():
            return
        if app_nme:
            self.app_nme = app_nme

    def set_package_name(self, package_name):

        if self.is_should_disable():
            return
        if package_name:
            self.package_name = package_name

    def set_deep_link(self, deep_link):

        if self.is_should_disable():
            return
        if deep_link:
            self.deep_link = deep_link

    def set_audio_url(self, audio_url):

        if self.is_should_disable():
            return
        if audio_url:
            self.audio_url = audio_url

    def update_data(self):
        if self.is_should_disable():
            return
        bot_id = self.request.get_bot_id()

        #组装数据 返回元祖(base64后的data, 时间戳)
        tup = self.__build_upload_data()

        base64Data = tup[0]
        timestamp = tup[1]
        pkversion = tup[2]
        signData = "%s%s%s%s" % (base64Data, bot_id, timestamp, pkversion)
        signature = self.certificate.get_sign(signData)
        if not signature or len(pkversion) == 0:
            return

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': str(len(base64Data)),
            'SIGNATURE': signature,
            'botId': str(bot_id),
            'timestamp': str(timestamp),
            'pkversion': str(pkversion)
        }

        thread = threading.Thread(target=self.__upload_data, args=(base64Data, headers))
        thread.start()

    def __upload_data(self, data, headers):
        '''
        发送请求
        :param url:
        :param data:
        :param headers:
        :return:
        '''
        response = requests.post(self.config.get_upload_url(), data=data, headers=headers)
        print('回调结果:%s' % response.text)

    def __build_upload_data(self):

        sysEvent = {
            'preEventList': {},
            'postEventList': {},
            'eventCostTime': self.event_cost_time,
            'deviceEventCostTime': self.device_event_cost_time
        }

        timestamp = self.get_millisecond()

        retData = {
            'serviceData': {
                'sdkType': self.config.get_sdk_type(),
                'sdkVersion': self.config.get_sdk_version(),
                'requestId': self.request.get_request_id(),
                'query': self.request.get_query(),
                'reason': self.request.get_reson(),
                'deviceId': self.request.get_device_id(),
                'requestType': self.request.get_type(),
                'userId': self.request.get_user_id(),
                'intentName': self.request.get_intent_name(),
                'sessionId': self.request.get_session_id(),
                'location': self.request.get_location(),
                'slotToElicit': self.response.get_slot_name(),
                'shouldEndSession': self.response.get_should_end_session(),
                'outputSpeech': self.response.get_output_speech(),
                'reprompt': self.response.get_reprompt(),
                'audioUrl': self.audio_url,
                'appInfo': {
                    'appName': self.app_name,
                    'packageName': self.package_name,
                    'deepLink': self.deep_link
                },
                'requestStartTime': self.request_start_time,
                'requestEndTime': self.request_end_time,
                'timestamp': timestamp,
                'sysEvent': sysEvent,
                'userEvent': self.user_event_list
            }
        }

        orginData = json.dumps(retData)
        print('orginData = %s' % orginData)

        base64Data = str(base64.b64encode(orginData.encode('utf-8')), 'utf-8')
        print(base64Data)
        if self.environment == 0:
            pkversion = 'debug'
        else:
            pkversion = 'online'

        return (base64Data, timestamp, pkversion)

    def is_should_disable(self):
        '''
        判断Monitor是否可用
        :return:
        '''

        if not self.private_key or len(self.private_key) == 0 or not self.enabled:
            return True
        return False


    def get_millisecond(self):
        '''
        获取当前时间
        :return:
        '''

        return int(time.time())

if __name__ == '__main__':

    pass
