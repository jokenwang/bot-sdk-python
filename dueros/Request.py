#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# description:
# author:jack
# create_time: 2017/12/30
"""
DuerOS对Bot的请求封装
"""
import json
from dueros.Nlu import Nlu
from dueros.Session import Session
from dueros.Base import Base
from dueros.Utils import Utils


class Request(Base):

    def __init__(self, request_data):
        """
        :param data:  请求数据
        """
        super(Request, self).__init__()
        if isinstance(request_data, str):
            request_data = json.loads(request_data)

        self.data = request_data

        self.request_type = self.data['request']['type']
        self.session = Session(self.data['session'])
        self.nlu = None
        if self.request_type == 'IntentRequest':
            self.nlu = Nlu(self.data['request']['intents'])
        self.device_data = None
        self.arr_user_profile = None

    def get_data(self):
        """
        返回request 请求体
        :return:
        """
        return self.data

    def get_session(self):
        """
        返回Session实例
        :return:
        """
        return self.session

    def get_nlu(self):
        """
        获取nlu实例
        :return:
        """
        return self.nlu

    def get_device_data(self):
        """
        返回设备信息
        :return:
        """
        return self.device_data

    def get_device_id(self):
        """
        获取设备Id
        :return:
        """
        return Utils.get_dict_data_by_keys(self.data, ['context', 'System', 'device', 'deviceId'])

    def get_original_device_id(self):
        """
        获取来自端上报的原始设备Id
        :return:
        """
        return Utils.get_dict_data_by_keys(self.data, ['context', 'System', 'device', 'originalDeviceId' ])

    def get_audio_player_context(self):
        """
        获取设备音频播放状态
        :return:
        """
        return Utils.get_dict_data_by_keys(self.data, ['context', 'AudioPlayer'])

    def get_video_player_context(self):

        return Utils.get_dict_data_by_keys(self.data, ['context', 'VideoPlayer'])

    def get_screen_context(self):

        return Utils.get_dict_data_by_keys(self.data, ['context', 'Screen'])

    def get_screen_token_from_context(self):

        return Utils.get_dict_data_by_keys(self.data, ['context', 'Screen', 'token'])

    def get_screen_token_from_context(self):

        return Utils.get_dict_data_by_keys(self.data, ['context', 'Screen', 'token'])

    def get_screen_card_from_context(self):

        return Utils.get_dict_data_by_keys(self.data, ['context', 'Screen', 'card'])


    def get_app_launcher_context(self):
        """
        获取设备app安装列表
        :return:
        """

        return Utils.get_dict_data_by_keys(self.data, ['context', 'AppLauncher'])

    def get_event_data(self):
        """
        获取event请求
        :return:
        """

        if self.request_type == 'IntentRequest' or self.is_session_ended_request() or self.is_launch_request():
            return
        else:
            return self.data['request']

    def get_user_info(self):
        """
        获取用户信息
        :return:
        """

        return Utils.get_dict_data_by_keys(self.data, ['context', 'System', 'user', 'userInfo'])

    def get_baidu_uid(self):
        """
        获取百度Id
        :return:
        """

        return Utils.get_dict_data_by_keys(self.data,
                                       ['context', 'System', 'user', 'userInfo', 'account', 'baidu', 'baiduUid'])

    def get_type(self):
        """
        获取Request类型
        :return:
        """
        return self.request_type

    def get_user_id(self):
        """
        获取用户ID
        :return:
        """
        return Utils.get_dict_data_by_keys(self.data, ['context', 'System', 'user', 'userId'])

    def get_access_token(self):
        """
        获取accessToken
        :return:
        """
        return self.__get_system_user()['accessToken']

    def __get_system_user(self):

        return Utils.get_dict_data_by_keys(self.data, ['context', 'System', 'user'])

    def get_external_access_tokens(self):
        """
        获取
        :return:
        """

        return self.__get_system_user()['externalAccessTokens']

    def get_cuid(self):

        return self.data['cuid']

    def get_query(self):
        """
        获取请求的Query
        :return:
        """

        if self.request_type == 'IntentRequest' and self.data['request']['query']['original']:
            return Utils.get_dict_data_by_keys(self.data, ['request', 'query', 'original'])
        else:
            return ''

    def get_location(self):
        """
        获取设备位置信息
        :return:
        """
        if self.__get_system_user()['userInfo']['location']:
            return self.__get_system_user()['userInfo']['location']

    def is_determined(self):

        if self.request_type == 'IntentRequest' and Utils.get_dict_data_by_keys(self.data, ['request', 'determined']):
            return Utils.get_dict_data_by_keys(self.data, ['request', 'determined'])
        else:
            return False

    def is_launch_request(self):
        """
        是否为调起bot请求
        :return:
        """
        return self.data['request']['type'] == 'LaunchRequest'

    def is_session_end_request(self):
        """
        是否关闭bot请求
        :return:
        """
        return self.data['request']['type'] == 'SessionEndedRequest'

    def is_session_ended_request(self):
        return self.is_session_end_request()

    def get_timestamp(self):

        return Utils.get_dict_data_by_keys(self.data, ['request', 'timestamp'])

    def get_log_id(self):

        return Utils.get_dict_data_by_keys(self.data, ['request', 'requestId'])

    def get_bot_id(self):

        return Utils.get_dict_data_by_keys(self.data, ['context', 'System', 'application', 'applicationId'])

    def is_dialog_state_completed(self):
        """
        槽位是否填完

        :return:
        """
        return self.data['request']['dialogState'] == 'COMPLETED'

    def get_supported_interfaces(self):

        return Utils.get_dict_data_by_keys(self.data, ['context', 'System', 'device', 'supportedInterfaces'])


if __name__ == '__main__':
    pass
