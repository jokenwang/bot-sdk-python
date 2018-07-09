#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# description:
# author:jack
# create_time: 2017/12/30

import json
from dueros.Nlu import Nlu
from dueros.Session import Session
from dueros.Base import Base
from dueros.Utils import Utils

class Request(Base):
    '''
        DuerOS对Bot的请求封装
    '''

    def __init__(self, data):
        '''

        :param data:  请求数据
        '''
        super(Request, self).__init__()
        if isinstance(data, dict):
            self.data = data
        elif isinstance(data, str):
            self.data = json.loads(data)

        self.requestType = self.data['request']['type']
        self.session = Session(self.data['session'])
        self.nlu = None
        if self.requestType == 'IntentRequest':
            self.nlu = Nlu(self.data['request']['intents'])
        self.deviceData = None
        self.arrUserProfile = None


    def getData(self):
        '''
        返回request 请求体
        :return:
        '''
        return self.data

    def getSession(self):
        '''
        返回Session实例
        :return:
        '''
        return self.session

    def getNlu(self):
        '''
        获取nlu实例
        :return:
        '''
        return self.nlu

    def getDeviceData(self):
        '''
        返回设备信息
        :return:
        '''
        return self.deviceData

    def getDeviceId(self):
        '''
        获取设备Id
        :return:
        '''
        return Utils.getDictDataByKeys(self.data, ['context', 'System', 'device', 'deviceId'])

    def getOriginalDeviceId(self):
        '''
        获取来自端上报的原始设备Id
        :return:
        '''
        return Utils.getDictDataByKeys(self.data, ['context', 'System', 'device', 'originalDeviceId' ])

    def getAudioPlayerContext(self):
        '''
        获取设备音频播放状态
        :return:
        '''
        return Utils.getDictDataByKeys(self.data, ['context', 'AudioPlayer'])

    def getVideoPlayerContext(self):

        return Utils.getDictDataByKeys(self.data, ['context', 'VideoPlayer'])

    def getScreenContext(self):
        return Utils.getDictDataByKeys(self.data, ['context', 'Screen'])

    def getScreenTokenFromContext(self):
        return Utils.getDictDataByKeys(self.data, ['context', 'Screen', 'token'])

    def getScreenTokenFromContext(self):
        return Utils.getDictDataByKeys(self.data, ['context', 'Screen', 'token'])

    def getScreenCardFromContext(self):
        return Utils.getDictDataByKeys(self.data, ['context', 'Screen', 'card'])


    def getAppLauncherContext(self):
        '''
        获取设备app安装列表
        :return:
        '''

        return Utils.getDictDataByKeys(self.data, ['context', 'AppLauncher'])

    def getEventData(self):
        '''
        获取event请求
        :return:
        '''

        if self.requestType == 'IntentRequest' or self.isSessionEndedRequest() or self.isLaunchRequest():
            return
        else:
            return self.data['request']

    def getUserInfo(self):
        '''
        获取用户信息
        :return:
        '''

        return Utils.getDictDataByKeys(self.data, ['context', 'System', 'user', 'userInfo'])

    def getBaiduUid(self):
        '''
        获取百度Id
        :return:
        '''

        return Utils.getDictDataByKeys(self.data,
                                       ['context', 'System', 'user', 'userInfo', 'account', 'baidu', 'baiduUid'])

    def getType(self):
        '''
        获取Request类型
        :return:
        '''
        return self.requestType

    def getUserId(self):
        '''
        获取用户ID
        :return:
        '''
        return Utils.getDictDataByKeys(self.data, ['context', 'System', 'user', 'userId'])

    def getAccessToken(self):

        '''
        获取accessToken
        :return:
        '''
        return self.__getSystemUser()['accessToken']

    def __getSystemUser(self):

        return Utils.getDictDataByKeys(self.data, ['context', 'System', 'user'])

    def getExternalAccessTokens(self):
        '''
        获取
        :return:
        '''

        return self.__getSystemUser()['externalAccessTokens']

    def getCuid(self):
        return self.data['cuid']

    def getQuery(self):
        '''
        获取请求的Query
        :return:
        '''

        if self.requestType == 'IntentRequest' and self.data['request']['query']['original']:
            return Utils.getDictDataByKeys(self.data, ['request', 'query', 'original'])
        else:
            return ''

    def getLocation(self):
        '''
        获取设备位置信息
        :return:
        '''
        if self.__getSystemUser()['userInfo']['location']:
            return self.__getSystemUser()['userInfo']['location']

    def isDetermined(self):

        if self.requestType == 'IntentRequest' and Utils.getDictDataByKeys(self.data, ['request', 'determined']):
            return Utils.getDictDataByKeys(self.data, ['request', 'determined'])
        else:
            return False

    def isLaunchRequest(self):
        '''
        是否为调起bot请求
        :return:
        '''
        return self.data['request']['type'] == 'LaunchRequest'

    def isSessionEndRequest(self):
        '''
        是否关闭bot请求
        :return:
        '''
        return self.data['request']['type'] == 'SessionEndedRequest'

    def isSessionEndedRequest(self):
        return self.isSessionEndRequest()

    def getTimestamp(self):

        return Utils.getDictDataByKeys(self.data, ['request', 'timestamp'])

    def getLogId(self):

        return Utils.getDictDataByKeys(self.data, ['request', 'requestId'])

    def getBotId(self):

        return Utils.getDictDataByKeys(self.data, ['context', 'System', 'application', 'applicationId'])

    def isDialogStateCompleted(self):
        '''
        槽位是否填完

        :return:
        '''
        return self.data['request']['dialogState'] == 'COMPLETED'



if __name__ == '__main__':
    pass
