#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/1/3

"""
    desc:pass
"""
import json
from dueros.monitor.Utils import Utils


class Request:

    def __init__(self, data):
        if not isinstance(data, dict):
            data = json.loads(data)
        self.data = data
        self.requestType = data['request']['type']

    def get_data(self):
        '''
        返回request请求头
        :return:
        '''
        return self.data

    def get_device_data(self):
        '''

        :return:
        '''
        return self.deviceData

    def get_device_id(self):

        if Utils.checkKeysInDict(self.data,['context','System','device','deviceId']):
            return self.data['context']['System']['device']['deviceId']
        return None

    def get_audio_player_context(self):
        '''
        获取设备音频播放的状态
        :return:
        '''
        if Utils.checkKeysInDict(self.data,['context','AudioPlayer']):
            return self.data['context']['AudioPlayer']
        return None

    def get_app_launcher_context(self):
        '''
        获取设备app安装列表
        :return:
        '''
        if Utils.checkKeysInDict(self.data,['context','AppLauncher']):
            return self.data['context']['AppLauncher']
        return None

    def get_event_data(self):
        '''
        获取event请求
        :return:
        '''
        if self.requestType == 'IntentRequest' or self.isLaunchRequest():
            return None
        else:
            return self.data['request']

    def get_user_info(self):
        '''

        :return:
        '''
        if Utils.checkKeysInDict(self.data, ['user_info']):
            return self.data['user_info']
        return None

    def get_type(self):
        '''
        获取request类型
        :return:
        '''
        return self.requestType

    def get_user_id(self):

        if Utils.checkKeysInDict(self.data, ['context', 'System', 'user', 'userId']):
            return self.data['context']['System']['user']['userId']
        return None

    def get_cuid(self):

        return self.data['cuid']

    def get_query(self):
        '''
        获取query
        :return:
        '''
        if self.requestType == 'IntentRequest':
            return self.data['request']['query']['original']
        return None

    def get_location(self):
        if Utils.checkKeysInDict(self.data, ['context','System','user', 'userInfo','location','geo']):
            return self.data['context']['System']['user']['userInfo']['location']['geo']
        return None

    def get_timestamp(self):

        if Utils.checkKeysInDict(self.data, ['request','timestamp']):
            return self.data['request']['timestamp']
        return None

    def get_log_id(self):

        return self.data['log_id']

    def get_botid(self):
        if Utils.checkKeysInDict(self.data,['context','System','application','applicationId']):
            return self.data['context']['System']['application']['applicationId']
        return None

    def get_request_id(self):

        if Utils.checkKeysInDict(self.data,['request','requestId']):
            return self.data['request']['requestId']

        return None

    def get_reson(self):

        if Utils.checkKeysInDict(self.data, ['request','reason']):
            return self.data['request']['reason']
        return None

    def get_intent_name(self):

        if self.data['request'] and 'intents' in self.data['request'] and self.data['request']['intents'] and self.data['request']['intents'][0]:
            return self.data['request']['intents'][0]['name']

        return None


    def get_session_id(self):

        if Utils.checkKeysInDict(self.data,['session', 'sessionId']):
            return self.data['session']['sessionId']
        return None

    def is_dialog_state_completed(self):
        if Utils.checkKeysInDict(self.data, ['request', 'dialogState']):
            return self.data['request']['dialogState'] == 'COMPLETED'
        return False

if __name__ == '__main__':
    pass
