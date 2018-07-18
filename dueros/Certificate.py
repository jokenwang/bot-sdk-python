#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/1/3

"""
    desc:pass
"""
import os
import fcntl
import hashlib
# import OpenSSL
import urllib2
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA
from base64 import b64encode, b64decode
from dueros.Base import Base


class Certificate(Base):

    def __init__(self, environ, request_body, privatekey_content=""):
        '''
        私钥内容,使用统计功能必须要提供
        :param environ: 环境上下文
        :param request_body:
        :param privatekey_content:
        '''

        super(Certificate, self).__init__()

        self.environ = environ
        self.data = request_body
        self.privatekey = privatekey_content
        self.verify_request_sign = False

    def enable_verify_request_sign(self):
        self.verify_request_sign = True

    def disable_verify_request_sign(self):
        self.verify_request_sign = False

    def get_request_publickey(self):

        filename = self.environ['HTTP_SIGNATURECERTURL']
        if not filename:
            return
        md5 = hashlib.md5()
        md5.update(filename.encode('utf-8'))
        cache = os.getcwd() + os.path.sep + md5.hexdigest()
        content = ''
        if not os.path.exists(cache):
            content = urllib2.urlopen(filename).read()
            if not content:
                return
            with open(cache, 'w') as f:
                fcntl.flock(f, fcntl.LOCK_EX)
                f.write(content)
                fcntl.flock(f, fcntl.LOCK_UN)
        content = self.getFileContentSafety(cache)
        return self.getPublicKeyFromX509(content)

    def verify_request(self):
        '''
        数据验证
        :return:
        '''
        if not self.verify_request_sign:
            return True

        publickey = self.get_request_publickey()

        if not publickey or not self.data:
            return False

        key = RSA.importKey(publickey)
        if key:
            digest = SHA.new()
            digest.update(self.data)
            verifier = PKCS1_v1_5.new(key)
            if verifier.verify(digest, b64decode(self.get_request_sign())):
                return True
            return False
        return False

    def get_sign(self, content):
        '''
        生成签名
        :param content: 待签名内容
        :return:
        '''
        if not self.privatekey or not content:
            return False

        rsakey = RSA.importKey(self.privatekey)
        if rsakey:
            digest = SHA.new()
            digest.update(content)
            signer = PKCS1_v1_5.new(rsakey)
            signature = signer.sign(digest)
            return b64encode(signature)
        else:
            return False

    def get_request_sign(self):
        return self.environ['HTTP_SIGNATURE']
    
    def get_publickey_fromX509(self, content):
        '''
        获取publicKey
        :param X509 content
        :return publicKey
        '''
        x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, content)
        pk = x509.get_pubkey()
        publickey = OpenSSL.crypto.dump_publickey(OpenSSL.crypto.FILETYPE_PEM, pk)
        return publickey

    def get_file_content_safety(self, filename):
        '''
        获取文件内容
        :param filename
        :return content
        '''
        with open(filename, 'r') as f:
            fcntl.flock(f,fcntl.LOCK_SH)
            content = f.read()
            return content
            fcntl.flock(f,fcntl.LOCK_UN)

if __name__ == '__main__':

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
    pubKey = '''-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDKoeRzRVf8WoRSDYYqUzThpYCr
90jfdFwTSXHJ526K8C6TEwdTUA+CFPQPRUg9jrYgFcown+J2myzO8BRLynD+XHb9
ilLb49Mqk2CvDt/yK32lgHv3QVx14Dpb6h8isjncSF965fxBxlHGbvPwnHkJ9etR
IYdYV3QpYohFszH3wQIDAQAB
-----END PUBLIC KEY-----'''

    data = 'partner="2088701924089318"&seller="774653@qq.com"&out_trade_no="123000"&subject="123456"&body="2010新款NIKE 耐克902第三代板鞋 耐克男女鞋 386201 白红"&total_fee="0.01"¬ify_url="http://notify.java.jpxx.org/index.jsp'
    def sign(data):
        key = RSA.importKey(priKey)
        digest = SHA.new()
        digest.update(data)
        signer = PKCS1_v1_5.new(key)
        signature = signer.sign(digest)
        return b64encode(signature)


    def verify(data, signature):
        key = RSA.importKey(pubKey)
        digest = SHA.new()
        digest.update(data)
        verifier = PKCS1_v1_5.new(key)
        if verifier.verify(digest, b64decode(signature)):
            return True
        return False

    signData = sign(data)
    print(sign(data))
    print(verify(data, signData))
    pass
