#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/1/3 下午1:12

"""
    desc:pass
"""
from monitor.botmonitor.model.Request import Request
from monitor.botmonitor.model.Response import Response
from monitor.botmonitor.Certificate import Certificate
from monitor.botmonitor.BotMonitorConfig import BotMonitorConfig

class BotMonitor:

    def __init__(self, postData):
        self.appInfo = {}

        self.requestStartTime = self.getMillisecond()
        self.eventCostTIme = 0.0
        self.deviceEveCostTime = 0.0
        self.preEventList = {}
        self.postEventList = {}
        self.userEventList = {}
        self.appInfo['appName'] = ''
        self.appInfo['packageName'] = ''
        self.appInfo['deepLink'] = ''
        self.__initConfig()
        self.request = Request(postData)

    def __initConfig(self):
        config = BotMonitorConfig.getConfig()
        self.uploadUrl = config['uploadUrl']
        self.sdkType = config['sdkType']
        self.sdkVersion = config['sdkVersion']
        self.enabled = True

    def setEnvironmentInfo(self, privateKey, environment):
        self.environment = environment
        self.privateKey = privateKey
        self.certificate = Certificate(privateKey)

    def setMonitorEnabled(self, enabled):
        pass

    def setResponseData(self, responseData):
        print('botMobitor setResponseData', responseData)
        if(isinstance(responseData, str)):

            self.response = Response(responseData)
        else:
            self.response = Response(responseData)

    def setPreEventStart(self):
        print('botMobitor setPreEventStart')
        if(self.isShouldDisable()):
            return
        keyStr = 'preEvent' + str(len(self.preEventList))
        self.preEventList[keyStr] = self.getMillisecond()

    def setPreEventEnd(self):
        print('botMobitor setPreEventEnd')

        pass

    def setPostEventStart(self):
        print('botMonitor setPostEventStart')
        pass

    def setPostEventEnd(self):
        print('botMonitor setPostEventEnd')

        pass

    def setEventStart(self):
        print('botMonitor setEventStart')

        pass

    def setEventEnd(self):
        print('botMonitor setEventEnd')

        pass

    def setDeviceEventStart(self):
        print('botMonitor setDeviceEventStart')
        pass

    def setDeviceEventEnd(self):
        print('botMonitor setDeviceEventEnd')

        pass

    def setOprationTic(self):
        pass

    def setOprationToc(self):
        pass

    def setAppName(self, appName):
        pass

    def setPackageName(self, packageName):
        pass

    def setDeepLink(self, deepLink):
        pass

    def setAudioUrl(self,audioUrl):
        pass

    def getMillisecond(self):
        pass

    def collectData(self):
        pass

    def updateData(self):
        print('botMobitor updateData')

        pass

    def postWithoutWait(self, request):
        pass

    def isShouldDisable(self):
        pass


if __name__ == '__main__':
    pass