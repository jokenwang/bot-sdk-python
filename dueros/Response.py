#!/usr/bin/env python2
# -*- encoding: UTF-8 -*-

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
        self.sourceType = self.request.get_botid()
        self.shouldEndSession = True
        self.needDetermine = None
        self.expectSpeech = None
        self.fallBack = None

    def set_should_end_session(self, val):
        '''
        设置对话结束
        :param val:
        :return:
        '''
        if val:
            self.shouldEndSession = True
        else:
            self.shouldEndSession = False

    def default_result(self):

        return {
            'status': 0,
            'msg': ''
        }

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

        if self.nlu and self.nlu.has_asked():
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

        if 'directives' in data:
            directives = data.get('directives')
        else:
            directives = []

        if len(directives) > 0:
            directives = list(map(lambda value: value.getData(), list(filter(lambda value: isinstance(value, BaseDirective), directives))))

        if self.nlu:
            arr = self.nlu.to_directive()
            if(arr):
                directives.append(arr)

        if not data['outputSpeech'] and data['card'] and isinstance(data['card'], TextCard):
            data['outputSpeech'] = data['card'].getData()['content']

        if self.nlu:
            if self.nlu.to_update_intent():
                context = self.nlu.to_update_intent()
            else:
                context = {}
        else:
            context = {}

        ret = {
            "version": "2.0",
            "context": context,
            "session": self.session.to_response(),
            "response": {
                "directives":  directives,
                "shouldEndSession": self.shouldEndSession,
                "card": data['card'].getData() if data['card'] else None,
                "resource": data['resource'],
                "outputSpeech": self.format_speech(data['outputSpeech']),
                "reprompt": {
			        "outputSpeech": self.format_speech(data['reprompt']),
		        }
            }
        }

        if isinstance(self.needDetermine, bool):
            ret['response']['needDetermine'] = self.needDetermine

        if isinstance(self.expectSpeech, bool):
            ret['response']['expectSpeech'] = self.expectSpeech

        if isinstance(self.fallBack, bool):
            ret['response']['fallBack'] = self.fallBack
        return ret

    def format_speech(self, mix):
        '''
        通过正则 判断是纯文本还是ssml
        :param mix:
        :return:
        '''
        if not mix or mix == 'null' or mix == '':
            return None

        result = {}
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


    def illegal_request(self):

        return {
            'status': 1,
            'msg': '非法请求'
        }

    def set_need_determine(self):

        self.needDetermine = True

    def set_expect_speech(self, expectSpeech):
        '''
        通过控制expectSpeech来控制麦克风开关
        :param expectSpeech:
        :return:
        '''
        if isinstance(expectSpeech, bool):
            self.expectSpeech = expectSpeech

    def set_fallback(self):
        '''
        表示本次返回的结果为兜底结果
        :return:
        '''

        self.fallBack = True

if __name__ == '__main__':
    pass
