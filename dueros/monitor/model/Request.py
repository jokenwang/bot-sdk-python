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
        self.requestType = data['request']['type']

    def getData(self):
        '''
        返回request请求头
        :return:
        '''
        return self.data

    def getDeviceData(self):
        '''

        :return:
        '''
        return self.deviceData

    def getDeviceId(self):

        return Utils.getDictDataByKeys(self.data,['context','System','device','deviceId'])

    def getAudioPlayerContext(self):
        '''
        获取设备音频播放的状态
        :return:
        '''
        return Utils.getDictDataByKeys(self.data,['context','AudioPlayer'])

    def getAppLauncherContext(self):
        '''
        获取设备app安装列表
        :return:
        '''
        return Utils.getDictDataByKeys(self.data,['context','AppLauncher'])

    def getEventData(self):
        '''
        获取event请求
        :return:
        '''
        if self.requestType == 'IntentRequest' or self.isLaunchRequest():
            return None
        else:
            return self.data['request']

    def getUserInfo(self):
        '''

        :return:
        '''
        if Utils.checkKeysInDict(self.data, ['user_info']):
            return self.data['user_info']
        return None

    def getType(self):
        '''
        获取request类型
        :return:
        '''
        return self.requestType

    def getUserId(self):

        return Utils.getDictDataByKeys(self.data,['context', 'System', 'user', 'userId'])

    def getCuid(self):

        return self.data['cuid']

    def getQuery(self):
        '''
        获取query
        :return:
        '''
        if self.requestType == 'IntentRequest':
            return self.data['request']['query']['original']
        return None

    def getLocation(self):
        return Utils.getDictDataByKeys(self.data,['context','System','user', 'userInfo','location','geo'])

    def getTimestamp(self):

        return Utils.getDictDataByKeys(self.data,['request','timestamp'])

    def getLogId(self):

        return self.data['log_id']

    def getBotId(self):
        return Utils.getDictDataByKeys(self.data,['context','System','application','applicationId'])

    def getRequestId(self):

        return Utils.getDictDataByKeys(self.data,['request','requestId'])

    def getReson(self):

        return Utils.getDictDataByKeys(self.data,['request','reason'])

    def getIntentName(self):

        if self.data['request'] and 'intents' in self.data['request'] and self.data['request']['intents'] and self.data['request']['intents'][0]:
            return self.data['request']['intents'][0]['name']

        return None


    def getSessionId(self):

        return Utils.getDictDataByKeys(self.data,['session', 'sessionId'])

    def isDialogStateCompleted(self):
        if Utils.checkKeysInDict(self.data, ['request', 'dialogState']):
            return self.data['request']['dialogState'] == 'COMPLETED'
        return False

if __name__ == '__main__':
    pass
