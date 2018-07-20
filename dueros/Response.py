#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# description:
# author:jack
# create_time: 2017/12/30
"""
处理完后构建返回数据
详见：https://dueros.baidu.com/didp/doc/dueros-bot-platform/dbp-custom/response_markdown#response
"""
import re
from dueros.card.TextCard import TextCard
from dueros.directive.BaseDirective import BaseDirective
from dueros.Base import Base


class Response(Base):

    def __init__(self, request, session, nlu):
        """
        :param request:
        :param session:
        :param nlu:
        """
        super(Response, self).__init__()
        self.request = request
        self.session = session
        self.nlu = nlu
        self.source_type = self.request.get_bot_id()
        self.should_end_session = True
        self.need_determine = None
        self.expect_speech = None
        self.fallback = None

    def set_should_end_session(self, val):
        """
        设置对话结束
        :param val:
        :return:
        """
        if val:
            self.should_end_session = True
        else:
            self.should_end_session = False

    def default_result(self):

        return {
            'status': 0,
            'msg': ''
        }

    def __pre_build(self, data):

        if self.nlu and self.nlu.has_asked():
            self.should_end_session = False

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
        """
        构造response 返回结果
        :param data:
        data = {
            'card': card,
            'directives': directives,
            'outputSpeech': string,
            'reprompt': string
        }
        :return:
        """

        if data is None:
            data = {}

        self.__pre_build(data)

        if 'directives' in data:
            directives = data.get('directives')
        else:
            directives = []

        if len(directives) > 0:
            directives = list(map(lambda value: value.get_data(), list(filter(lambda value: isinstance(value, BaseDirective), directives))))

        if self.nlu:
            arr = self.nlu.to_directive()
            if arr:
                directives.append(arr)

        if not data['outputSpeech'] and data['card'] and isinstance(data['card'], TextCard):
            data['outputSpeech'] = data['card'].get_data()['content']

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
                "shouldEndSession": self.should_end_session,
                "card": data['card'].get_data() if data['card'] else None,
                "resource": data['resource'],
                "outputSpeech": self.format_speech(data['outputSpeech']),
                "reprompt": {"outputSpeech": self.format_speech(data['reprompt'])}
            }
        }

        if isinstance(self.need_determine, bool):
            ret['response']['needDetermine'] = self.need_determine

        if isinstance(self.expect_speech, bool):
            ret['response']['expectSpeech'] = self.expect_speech

        if isinstance(self.fallback, bool):
            ret['response']['fallBack'] = self.fallback
        return ret

    def format_speech(self, mix):
        """
        通过正则 判断是纯文本还是ssml
        :param mix:
        :return:
        """
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


    def illegal_request(self):

        return {
            'status': 1,
            'msg': '非法请求'
        }

    def set_need_determine(self):

        self.need_determine = True

    def set_expect_speech(self, expect_speech=False):
        """
        通过控制expect_speech来控制麦克风开关
        :param expect_speech:
        :return:
        """
        if isinstance(expect_speech, bool):
            self.expect_speech = expect_speech

    def set_fallback(self):
        """
        表示本次返回的结果为兜底结果
        :return:
        """

        self.fallback = True


if __name__ == '__main__':

    pass
