#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/1/3 下午1:12

"""
    desc:pass
"""

from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from base64 import b64encode, b64decode

class Certificate(object):

    def __init__(self, privateKeyContent = ""):
        '''
        私钥内容,使用统计功能必须要提供
        :param privateKeyContent:
        '''
        self.privateKey = privateKeyContent

    def getSig(self, content):
        '''
        生成签名
        :param content: 待签名内容
        :return:
        '''
        if(not self.privateKey or not content):
            return False

        rsakey = RSA.importKey(self.privateKey)
        if(rsakey):
            signer = PKCS1_v1_5.new(rsakey)
            digest = SHA256.new()
            # It's being assumed the data is base64 encoded, so it's decoded before updating the digest
            digest.update(b64decode(content))
            sign = signer.sign(digest)
            return b64encode(sign)
        else:
            return False

    def verifyRequest(self):
        return True
    pass


if __name__ == '__main__':

    c = Certificate('http://www.baidu.com')
    r = c.getSig('asdfasdfasd')
    print(r)
    pass