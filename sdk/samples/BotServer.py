#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/1/3

"""
    desc:pass
"""
from cgi import parse_qs, escape
import json
from sdk.samples.Bot import Bot

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except(ValueError):
        request_body_size = 0

    request_body = environ['wsgi.input'].read(request_body_size)
    print(type(request_body))
    bot = Bot(request_body)
    #验证签名enableVerifyRequestSign  disableVerifyRequestSign 关闭验证签名
    bot.initCertificate(environ).enableVerifyRequestSign()
    body_str = bot.run()

    body = body_str.encode('utf-8')
    return [body]

def askContol():
        response = '''
        {
        "session": {
            "attributes": {}
        },
        "version": "2.0",
        "response": {
            "resource": null,
            "outputSpeech": {
                "text": "请告诉您的指令，比如调小空调风速、设置温度为30度",
                "type": "PlainText"
            },
            "directives": [
                {
                "updatedIntent": {
                    "slots": {
                        "deviceName": {
                            "name": "deviceName",
                            "value": "kongtiao"
                        },
                        "city": {
                            "score": 0,
                            "name": "city",
                            "value": "beijing",
                            "confirmationStatus": "NONE"
                        }
                    },
                    "name": "dueros.device_interface.smart_device.control"
                },
                "type": "Dialog.ElicitSlot",
                "slotToElicit": "deviceName"
                }
            ],
            "reprompt": null,
            "shouldEndSession": false,
            "card": {
                "content": "请告诉您的指令，比如调小空调风速、设置温度为30度",
                "type": "txt"
            }
        },
        "context": {
            "intent": {
                "slots": {
                    "deviceName": {
                        "name": "deviceName",
                        "value": "kongtiao"
                    },
                    "city": {
                        "score": 0,
                        "name": "city",
                        "value": "beijing",
                        "confirmationStatus": "NONE"
                    }
                },
                "score": 100,
                "name": "dueros.device_interface.smart_device.control",
                "confirmationStatus": "NONE"
            }
        }
    }'''
        return response

