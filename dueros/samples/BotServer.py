#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/1/3

"""
    desc:pass
"""
#默认使用个税查询技能， 如果需要切换自己的技能  注意需要要更换成自己的Bot
# from dueros.samples.personal_income_tax.Bot import Bot
from dueros.samples.audio_play.Bot import Bot
def application(environ, start_response):
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except(ValueError):
        request_body_size = 0
    request_body = environ['wsgi.input'].read(request_body_size).decode('utf-8')
    print('request_body = %s\n' % request_body)
    if not request_body:
        return writeResponse(start_response, '未获取到请求数据')

    bot = Bot(request_body)
    #添加错误回调方法
    bot.setCallBack(callback)

    #验证签名enableVerifyRequestSign  disableVerifyRequestSign 关闭验证签名
    # bot.initCertificate(environ).enableVerifyRequestSign()
    # bot.initCertificate(environ).disableVerifyRequestSign()

    body_str = bot.run()

    return writeResponse(start_response, body_str)

def writeResponse(start_response, body_str):

    body = body_str.encode('utf-8')

    response_headers = [('Content-Type', 'application/json'),
                        ('Content-Length', str(len(body)))]
    status = '200 OK'

    start_response(status, response_headers)

    return [body]

def callback(data):
    print(data)
