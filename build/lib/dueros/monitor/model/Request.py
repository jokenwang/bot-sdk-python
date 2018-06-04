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

        if Utils.checkKeysInDict(self.data,['context','System','device','deviceId']):
            return self.data['context']['System']['device']['deviceId']
        return None

    def getAudioPlayerContext(self):
        '''
        获取设备音频播放的状态
        :return:
        '''
        if Utils.checkKeysInDict(self.data,['context','AudioPlayer']):
            return self.data['context']['AudioPlayer']
        return None

    def getAppLauncherContext(self):
        '''
        获取设备app安装列表
        :return:
        '''
        if Utils.checkKeysInDict(self.data,['context','AppLauncher']):
            return self.data['context']['AppLauncher']
        return None

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

        if Utils.checkKeysInDict(self.data, ['context', 'System', 'user', 'userId']):
            return self.data['context']['System']['user']['userId']
        return None

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
        if Utils.checkKeysInDict(self.data, ['context','System','user', 'userInfo','location','geo']):
            return self.data['context']['System']['user']['userInfo']['location']['geo']
        return None

    def getTimestamp(self):

        if Utils.checkKeysInDict(self.data, ['request','timestamp']):
            return self.data['request']['timestamp']
        return None

    def getLogId(self):

        return self.data['log_id']

    def getBotId(self):
        if Utils.checkKeysInDict(self.data,['context','System','application','applicationId']):
            return self.data['context']['System']['application']['applicationId']
        return None

    def getRequestId(self):

        if Utils.checkKeysInDict(self.data,['request','requestId']):
            return self.data['request']['requestId']

        return None

    def getReson(self):

        if Utils.checkKeysInDict(self.data, ['request','reason']):
            return self.data['request']['reason']
        return None

    def getIntentName(self):

        if self.data['request'] and 'intents' in self.data['request'] and self.data['request']['intents'] and self.data['request']['intents'][0]:
            return self.data['request']['intents'][0]['name']

        return None


    def getSessionId(self):

        if Utils.checkKeysInDict(self.data,['session', 'sessionId']):
            return self.data['session']['sessionId']
        return None

    def isDialogStateCompleted(self):
        if Utils.checkKeysInDict(self.data, ['request', 'dialogState']):
            return self.data['request']['dialogState'] == 'COMPLETED'
        return False

if __name__ == '__main__':
    pass
