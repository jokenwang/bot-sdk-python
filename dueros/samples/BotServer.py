#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/1/3

"""
    desc:pass
"""
from cgi import parse_qs, escape
import json
from dueros.samples.audio_play.Bot import Bot
import sys #要重新载入sys。因为 Python 初始化后会删除 sys.setdefaultencoding 这个方 法
reload(sys)
sys.setdefaultencoding('utf-8')
def application(environ, start_response):
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except(ValueError):
        request_body_size = 0
    request_body = environ['wsgi.input'].read(request_body_size).decode('utf-8')
    print('request_body = %s\n' % request_body)
    if not request_body:
        return writeResponse(start_response,'未获取到请求数据')

    bot = Bot(request_body)
    #添加错误回调方法
    # bot.setCallBack(callback)

    #验证签名enableVerifyRequestSign  disableVerifyRequestSign 关闭验证签名
    # bot.initCertificate(environ).enableVerifyRequestSign()
    bot.init_certificate(environ).disable_verify_request_sign()
    bot.set_private_key(priKey)

    body_str = bot.run()
    print(body_str)
    return writeResponse(start_response, body_str)

def writeResponse(start_response, body_str):

    body = body_str.encode('utf-8')
    response_headers = [('Content-Type', 'application/json'),
                        ('Content-Length', str(len(body)))]
    status = '200 OK'
    print(body)
    start_response(status, response_headers)
    return [body]


priKey = '''-----BEGIN RSA PRIVATE KEY-----
    MIICXQIBAAKBgQDKoeRzRVf8WoRSDYYqUzThpYCr90jfdFwTSXHJ526K8C6TEwdT
    UA+CFPQPRUg9jrYgFcown+J2myzO8BRLynD+XHb9ilLb49Mqk2CvDt/yK32lgHv3
    QVx14Dpb6h8isjncSF965fxBxlHGbvPwnHkJ9etRIYdYV3QpYohFszH3wQIDAQAB
    AoGAFhKqkw/ztK6biWClw8iKkyX3LURjsMu5F/TBK3BFb2cYe7bv7lhjSBVGPL+c
    TfBU0IvvGXrhLXBb4jLu0w67Xhggwwfc86vlZ8eLcrmYVat7N6amiBmYsw20GViU
    UFmePbo1G2BXqMA43JxqbIQwOLZ03zdw6GHj6EVlx369IAECQQD4K2R3K8ah50Yz
    LhF7zbYPIPGbHw+crP13THiYIYkHKJWsQDr8SXoNQ96TQsInTXUAmF2gzs/AwdQg
    gjIJ/dmBAkEA0QarqdWXZYbse1XIrQgBYTdVH9fNyLs1e1sBmNxlo4QMm/Le5a5L
    XenorEjnpjw5YpEJFDS4ijUI3dSzylC+QQJARqcD6TGbUUioobWB4L9GD7SPVFxZ
    c3+EgcxRoO4bNuCFDA8VO/InP1ONMFuXLt1MbCj0ru1yFCyamc63NEUDAQJBALt7
    PjGgsKCRuj6NnOcGDSbDWIitKZhnwfqYkAApfsiBQkYGO0LLaDIeAWG2KoCB9/6e
    lAQZnYPpOcCubWyDq4ECQQCrRDf0gVjPtipnPPS/sGN8m1Ds4znDDChhRlw74MI5
    FydvHFumChPe1Dj2I/BWeG1gA4ymXV1tE9phskV3XZfq
    -----END RSA PRIVATE KEY-----'''
