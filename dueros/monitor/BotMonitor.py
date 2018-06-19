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

    def __init__(self, postData, privateKey = ''):
        if not isinstance(postData, dict):
            postData = json.loads(postData)
        self.data = postData
        self.requestStartTime = self.getMillisecond()
        self.requestEndTime = 0
        self.request = Request(postData)
        self.audioUrl = None
        self.appName = None
        self.packageName = None
        self.deepLink = None
        self.eventStartTime = 0
        self.eventCostTime = 0
        self.deviceEventStartTime = 0
        self.deviceEventCostTime = 0
        self.userEventList = {}
        self.isEventMakePair = {}
        self.config = BotMonitorConfig()
        self.privateKey = privateKey
        self.environment = 0
        self.enabled = True
        self.certificate = None
        self.response = None

    def setEnvironmentInfo(self, privateKey, environment):
        print(privateKey)
        self.privateKey = privateKey
        self.environment = environment
        self.certificate = Certificate(None, self.data, privateKey)

    def setMonitorEnabled(self, enabled):
        '''
        设置是否可用
        :param enabled:
        :return:
        '''
        self.enabled = enabled

    def setResponseData(self, responseData):

        if self.isShouldDisable():
            return
        self.requestEndTime = self.getMillisecond()
        self.response = Response(responseData)

    def setEventStart(self):

        if self.isShouldDisable():
            return
        self.eventStartTime = self.getMillisecond()

    def setEventEnd(self):

        if self.isShouldDisable():
            return
        self.eventCostTime = self.getMillisecond() - self.eventStartTime

    def setDeviceEventStart(self):

        if self.isShouldDisable():
            return
        self.deviceEventStartTime = self.getMillisecond()

    def setDeviceEventEnd(self):

        if self.isShouldDisable():
            return
        self.deviceEventCostTime = self.getMillisecond() - self.deviceEventStartTime

    def setOprationTic(self, taskName):

        if self.isShouldDisable():
            return
        if taskName:
            self.userEventList[taskName] = self.getMillisecond()
            self.isEventMakePair[taskName] = False

    def setOprationToc(self, taskName):

        if self.isShouldDisable():
            return
        if taskName:

            if taskName in self.userEventList:
                oldTime = self.userEventList[taskName]
            else:
                oldTime = None
            costTime = 0

            if oldTime:
                currTime = self.getMillisecond()
                costTime = currTime - oldTime

            self.userEventList[taskName] = costTime
            self.isEventMakePair[taskName] = True

    def setAppName(self, appName):

        if self.isShouldDisable():
            return
        if appName:
            self.appName = appName

    def setPackageName(self, packageName):

        if self.isShouldDisable():
            return
        if packageName:
            self.packageName = packageName

    def setDeepLink(self, deepLink):

        if self.isShouldDisable():
            return
        if deepLink:
            self.deepLink = deepLink

    def setAudioUrl(self, audioUrl):

        if self.isShouldDisable():
            return
        if audioUrl:
            self.audioUrl = audioUrl

    def updateData(self):
        if self.isShouldDisable():
            return
        botId = self.request.getBotId()

        #组装数据 返回元祖(base64后的data, 时间戳)
        tup = self.__buildUploadData()

        base64Data = tup[0]
        timestamp = tup[1]
        pkversion = tup[2]
        signData = "%s%s%s%s" % (base64Data, botId, timestamp, pkversion)
        print('signData = %s' % signData)
        signature = self.certificate.getSign(signData)
        print('signature = %s' % (str(signature, 'utf-8')))

        if not signature or len(pkversion) == 0:
            return

        print('content-length=%s, signature=%s, botId=%s, timestamp=%s' % (str(len(base64Data)),signature,str(botId), str(timestamp)))
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': str(len(base64Data)),
            'SIGNATURE': signature,
            'botId': str(botId),
            'timestamp': str(timestamp),
            'pkversion': str(pkversion)
        }

        thread = threading.Thread(target=self.__uploadData, args=(base64Data, headers))
        thread.start()

    def __uploadData(self, data, headers):
        '''
        发送请求
        :param url:
        :param data:
        :param headers:
        :return:
        '''
        response = requests.post(self.config.getUploadUrl(), data=data, headers=headers)
        print(response.text)

    def __buildUploadData(self):

        sysEvent = {
            'preEventList': {},
            'postEventList': {},
            'eventCostTime': self.eventCostTime,
            'deviceEventCostTime': self.deviceEventCostTime
        }

        timestamp = self.getMillisecond()

        retData = {
            'serviceData': {
                'sdkType': self.config.getSdkType(),
                'sdkVersion': self.config.getSdkVersion(),
                'requestId': self.request.getRequestId(),
                'query': self.request.getQuery(),
                'reason': self.request.getReson(),
                'deviceId': self.request.getDeviceId(),
                'requestType': self.request.getType(),
                'userId': self.request.getUserId(),
                'intentName': self.request.getIntentName(),
                'sessionId': self.request.getSessionId(),
                'location': self.request.getLocation(),
                'slotToElicit': self.response.getSlotName(),
                'shouldEndSession': self.response.getShouldEndSession(),
                'outputSpeech': self.response.getOutputSpeech(),
                'reprompt': self.response.getReprompt(),
                'audioUrl': self.audioUrl,
                'appInfo': {
                    'appName': self.appName,
                    'packageName': self.packageName,
                    'deepLink': self.deepLink
                },
                'requestStartTime': self.requestStartTime,
                'requestEndTime': self.requestEndTime,
                'timestamp': timestamp,
                'sysEvent': sysEvent,
                'userEvent': self.userEventList
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

    def isShouldDisable(self):
        '''
        判断Monitor是否可用
        :return:
        '''

        if not self.privateKey or len(self.privateKey) == 0 or not self.enabled:
            return True
        return False


    def getMillisecond(self):
        '''
        获取当前时间
        :return:
        '''

        return int(time.time())

if __name__ == '__main__':

    pass
