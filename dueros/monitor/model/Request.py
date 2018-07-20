#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/1/3

"""
    desc:pass
"""

from dueros.monitor.Utils import Utils


class Request:

    def __init__(self, data):
        self.data = data
        self.request_type = data['request']['type']

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
        return self.device_data

    def get_device_id(self):

        return Utils.get_dict_data_by_keys(self.data, ['context', 'System', 'device', 'deviceId'])

    def get_audio_player_context(self):
        '''
        获取设备音频播放的状态
        :return:
        '''
        return Utils.get_dict_data_by_keys(self.data, ['context', 'AudioPlayer'])

    def get_app_launcher_context(self):
        '''
        获取设备app安装列表
        :return:
        '''
        return Utils.get_dict_data_by_keys(self.data, ['context', 'AppLauncher'])

    def get_event_data(self):
        '''
        获取event请求
        :return:
        '''
        if self.requestType == 'IntentRequest' or self.is_launch_request():
            return None
        else:
            return self.data['request']

    def get_user_info(self):
        '''

        :return:
        '''
        return Utils.get_dict_data_by_keys(self.data, ['user_info'])

    def get_type(self):
        '''
        获取request类型
        :return:
        '''
        return self.request_type

    def get_user_id(self):

        return Utils.get_dict_data_by_keys(self.data, ['context', 'System', 'user', 'userId'])

    def get_cuid(self):

        return self.data['cuid']

    def get_query(self):
        '''
        获取query
        :return:
        '''
        if self.request_type == 'IntentRequest':
            return self.data['request']['query']['original']
        return None

    def get_location(self):
        return Utils.get_dict_data_by_keys(self.data, ['context', 'System', 'user', 'userInfo', 'location', 'geo'])

    def get_timestamp(self):

        return Utils.get_dict_data_by_keys(self.data, ['request', 'timestamp'])

    def get_log_id(self):

        return self.data['log_id']

    def get_bot_id(self):
        return Utils.get_dict_data_by_keys(self.data, ['context', 'System', 'application', 'applicationId'])

    def get_request_id(self):

        return Utils.get_dict_data_by_keys(self.data, ['request', 'requestId'])

    def get_reson(self):

        return Utils.get_dict_data_by_keys(self.data, ['request', 'reason'])

    def get_intent_name(self):

        if self.data['request'] and 'intents' in self.data['request'] and self.data['request']['intents'] and self.data['request']['intents'][0]:
            return self.data['request']['intents'][0]['name']

        return None

    def get_session_id(self):

        return Utils.get_dict_data_by_keys(self.data, ['session', 'sessionId'])

    def is_dialog_state_completed(self):

        if Utils.checkKeysInDict(self.data, ['request', 'dialogState']):
            return self.data['request']['dialogState'] == 'COMPLETED'
        return False

if __name__ == '__main__':
    pass
