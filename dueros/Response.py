#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# description:
# author:jack
# create_time: 2017/12/30

import re
from dueros.card.TextCard import TextCard
from dueros.directive.BaseDirective import BaseDirective
from dueros.Base import Base

class Response(Base):
    """
    处理完后构建返回数据
    """

    def __init__(self, request, session, nlu):
        '''

        :param request:
        :param session:
        :param nlu:
        '''
        super(Response, self).__init__()
        self.request = request
        self.session = session
        self.nlu = nlu
        self.sourceType = self.request.getBotId()
        self.shouldEndSession = True
        self.needDetermine = False
        self.expectSpeech = False
        self.fallBack = False

    def setShouldEndSession(self, val):
        '''
        设置对话结束
        :param val:
        :return:
        '''
        if val:
            self.shouldEndSession = True
        else:
            self.shouldEndSession = False

    def defaultResult(self):

        return {
            'status': 0,
            'msg': ''
        }

    def __preBuild(self, data):

        if self.nlu and self.nlu.hasAsked():
            self.shouldEndSession = False

        if 'directives' in data:
            data['directives'] = data.get('directives')
        else:
            data['directives'] = []

        if 'card' in data:
            data['card'] = data.get('card')
        else:
            data['card'] = None

        if 'outputSpeech' in data:
            data['outputSpeech'] = data.get('outputSpeech')
        else:
            data['outputSpeech'] = None

        if 'resource' in data:
            data['resource'] = data.get('resource')
        else:
            data['resource'] = None

        if 'reprompt' in data:
            data['reprompt'] = data.get('reprompt')
        else:
            data['reprompt'] = None

    def build(self, data):
        '''
        构造response 返回结果
        :param data:
        data = {
            'card': card,
            'directives': directives,
            'outputSpeech': string,
            'reprompt': string
        }
        :return:
        '''

        self.__preBuild(data)

        if 'directives' in data:
            directives = data.get('directives')
        else:
            directives = []

        if len(directives) > 0:
            directives = list(map(lambda value: value.getData(), list(filter(lambda value: isinstance(value, BaseDirective), directives))))

        if self.nlu:
            arr = self.nlu.toDirective()
            if arr:
                directives.append(arr)

        if not data['outputSpeech'] and data['card'] and isinstance(data['card'], TextCard):
            data['outputSpeech'] = data['card'].getData()['content']

        if self.nlu:
            if self.nlu.toUpdateIntent():
                context = self.nlu.toUpdateIntent()
            else:
                context = {}
        else:
            context = {}

        ret = {
            "version": "2.0",
            "context": context,
            "session": self.session.toResponse(),
            "response": {
                "directives":  directives,
                "shouldEndSession": self.shouldEndSession,
                "card": data['card'].getData() if data['card'] else None,
                "resource": data['resource'],
                "outputSpeech": self.formatSpeech(data['outputSpeech']),
                "reprompt": {
			        "outputSpeech": self.formatSpeech(data['reprompt'])
		        }
            }
        }

        if self.needDetermine:
            ret['response']['needDetermine'] = self.needDetermine

        if self.expectSpeech:
            ret['response']['expectSpeech'] = self.expectSpeech

        if self.fallBack:
            ret['response']['fallBack'] = self.fallBack
        return ret

    def formatSpeech(self, mix):
        '''
        通过正则 判断是纯文本还是ssml
        :param mix:
        :return:
        '''
        if not mix or mix == 'null' or mix == '':
            return None

        if re.search(r'<speak>', mix):
            result = {
                "type": "SSML",
                "ssml": mix
            }
        else:
            result = {
                "type": "PlainText",
                "text": mix
            }
        return result


    def illegalRequest(self):

        return {
            'status': 1,
            'msg': '非法请求'
        }

    def setNeedDetermine(self):

        self.needDetermine = True

    def setExpectSpeech(self, expectSpeech=False):
        '''
        通过控制expectSpeech来控制麦克风开关
        :param expectSpeech:
        :return:
        '''
        if expectSpeech and isinstance(expectSpeech, bool):
            self.expectSpeech = expectSpeech

    def setFallBack(self):
        '''
        表示本次返回的结果为兜底结果
        :return:
        '''

        self.fallBack = True

if __name__ == '__main__':
    pass
