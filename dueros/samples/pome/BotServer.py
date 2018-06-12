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
from dueros.samples.Bot import Bot

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

def application(environ, start_response):
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except(ValueError):
        request_body_size = 0
    request_body = environ['wsgi.input'].read(request_body_size).decode('utf-8')
    if not request_body:
        return writeResponse('暂未获取到请求数据', start_response)

    bot = Bot(request_body)
    #添加错误回调方法
    #bot.setCallBack(callback)

    #确保在技能配置的公钥和这里配置的私钥是一对
    #验证签名enableVerifyRequestSign  disableVerifyRequestSign 关闭验证签名
    bot.initCertificate(environ, priKey).enableVerifyRequestSign()
    #设置统计用的私钥
    bot.setPrivateKey(priKey)
    body_str = bot.run()
    return writeResponse(body_str, start_response)

def writeResponse(response, start_response):

    body = response.encode('utf-8')
    response_headers = [('Content-Type', 'application/json'),
                        ('Content-Length', str(len(body)))]
    status = '200 OK'
    start_response(status, response_headers)
    return [body]

def callback(data):
    print(data)

