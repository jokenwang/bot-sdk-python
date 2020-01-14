#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/1/3

import os
import fcntl
import hashlib
import OpenSSL
import urllib.request
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA
from base64 import b64encode, b64decode
from dueros.Base import Base
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


class Certificate(object):

    def __init__(self, environ, request_body, private_key_content=''):
        """
        私钥内容,使用统计功能必须要提供
        :param environ: 环境上下文
        :param request_body: 请求数据
        :param private_key_content:
        """

        super(Certificate, self).__init__()

        self.environ = environ
        self.data = request_body
        self.private_key = private_key_content
        self.verify_request_sign = False

    def enable_verify_request_sign(self):
        """
        校验请求合法性
        :return:
        """
        self.verify_request_sign = True

    def disable_verify_request_sign(self):
        """
        不校验请求合法性
        :return:
        """
        self.verify_request_sign = False

    def get_request_public_key(self):
        """
        获取Dueros发送过来的公钥(此公钥信息是在技能参数配置中设置的)
        :return:
        """
        filename = self.environ['HTTP_SIGNATURECERTURL']
        if not filename:
            return
        md5 = hashlib.md5()
        md5.update(filename.encode('utf-8'))
        cache = os.getcwd() + os.path.sep + md5.hexdigest()
        if not os.path.exists(cache):
            content = urllib.request.urlopen(filename).read()
            if not content:
                return
            with open(cache, 'w') as f:
                fcntl.flock(f, fcntl.LOCK_EX)
                f.write(content.decode('utf-8'))
                fcntl.flock(f, fcntl.LOCK_UN)
        content = get_file_content_safety(cache)
        return get_public_key_fromX509(content)

    def verify_request(self):
        """
        数据验证
        :return:
        """
        if not self.verify_request_sign:
            return True

        public_key = self.get_request_public_key()

        if not public_key or not self.data:
            return False

        key = RSA.importKey(public_key)
        if key:
            digest = SHA.new()
            digest.update(self.data.encode('utf-8'))
            verifier = PKCS1_v1_5.new(key)
            if verifier.verify(digest, b64decode(self.get_request_sign())):
                return True
            return False
        return False

    def get_sign(self, content):
        """
        生成签名
        :param content: 待签名内容
        :return:
        """
        if not self.private_key or not content:
            return False

        rsakey = RSA.importKey(self.private_key)
        if rsakey:
            digest = SHA.new()
            digest.update(content.encode('utf8'))
            signer = PKCS1_v1_5.new(rsakey)
            signature = signer.sign(digest)
            return b64encode(signature)
        else:
            return False

    def get_request_sign(self):
        return self.environ['HTTP_SIGNATURE']


def get_public_key_fromX509(content):
    """
    获取publicKey
    :param  content
    :return publicKey
    """
    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, content)
    pk = x509.get_pubkey()
    public_key = OpenSSL.crypto.dump_publickey(OpenSSL.crypto.FILETYPE_PEM, pk)
    return public_key


def get_file_content_safety(filename):
    """
    获取文件内容
    :param filename
    :return content
    """
    with open(filename, 'r') as f:
        fcntl.flock(f, fcntl.LOCK_SH)
        content = f.read()
        fcntl.flock(f, fcntl.LOCK_UN)
        return content
