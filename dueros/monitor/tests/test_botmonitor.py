#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/1/16

"""
    desc:pass
"""

from dueros.monitor.model.Response import Response
from dueros.monitor.model.Request import Request
from dueros.monitor.BotMonitor import BotMonitor
from dueros.Certificate import Certificate
import json
import os
import hashlib
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA
from base64 import b64encode, b64decode
class test_botmonitor:
    pass


if __name__ == '__main__':

    privatePemContent = '''-----BEGIN RSA PRIVATE KEY-----
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

    def requestData():
        with open("../data/intent_request_tax.json", 'r', encoding='utf-8') as load_f:
            return load_f.read()

    def responseData():
        with open("../data/test_response_tax.json", 'r', encoding='utf-8') as load_f:
            return load_f.read()

    requestData = requestData()

    responseData = responseData()

    botmonitor = BotMonitor(json.loads(requestData))

    botmonitor.set_environment_info(privatePemContent, 0)

    botmonitor.set_opration_tic('aa1')
    botmonitor.set_opration_toc('aa1')
    botmonitor.set_opration_toc('aa2')
    botmonitor.set_opration_toc('aa2')
    botmonitor.set_opration_toc('aa3')
    botmonitor.set_event_start()
    botmonitor.set_event_end()
    botmonitor.set_device_event_start()
    botmonitor.set_device_event_end()
    botmonitor.set_app_name('baidu')
    botmonitor.set_audio_url('baidu')
    botmonitor.set_deep_link('baidu')
    botmonitor.set_deep_link('baidu')
    botmonitor.set_response_data(responseData)
    botmonitor.update_data()




    def verify(data, signature):
        key = RSA.importKey(pubKey)
        digest = SHA.new()
        digest.update(data.encode('utf-8'))
        verifier = PKCS1_v1_5.new(key)
        if verifier.verify(digest, b64decode(signature)):
            return True
        return False
    orginData = '''eyJzZXJ2aWNlRGF0YSI6IHsic2RrVHlwZSI6ICJweXRob24iLCAic2RrVmVyc2lvbiI6ICIxLjAuMCIsICJyZXF1ZXN0SWQiOiAiY2Y5ZTQ1NThjYjY2NGVkMDk5M2E0ZjNmNTY2MmVmYjdfMSIsICJxdWVyeSI6ICJcdTY3ZTVcdTRlMmFcdTdhMGUiLCAicmVhc29uIjogIlVTRVJfSU5JVElBVEVEIiwgImRldmljZUlkIjogImRldmljZUlkcmVhbCIsICJyZXF1ZXN0VHlwZSI6ICJJbnRlbnRSZXF1ZXN0IiwgInVzZXJJZCI6ICI1NTE4ODEzNyIsICJpbnRlbnROYW1lIjogImlucXVpcnkiLCAic2Vzc2lvbklkIjogInNlc3Npb25JZCIsICJsb2NhdGlvbiI6IHsiYmQwOWxsIjogeyJsb25naXR1ZGUiOiAxMTYuNDE2NTA1ODU3NjUsICJsYXRpdHVkZSI6IDM5LjkyMjU4OTgyMzI2NX0sICJ3Z3M4NCI6IHsibG9uZ2l0dWRlIjogMTE2LjQwMzg3Mzk3LCAibGF0aXR1ZGUiOiAzOS45MTQ4ODkwOH0sICJiZDA5bWMiOiB7ImxvbmdpdHVkZSI6IDEyOTU5NTY3LjQwMzAzNCwgImxhdGl0dWRlIjogNDgyNzAyMS44MjM1MDc1fX0sICJzbG90VG9FbGljaXQiOiAibW9udGhseXNhbGFyeSIsICJzaG91bGRFbmRTZXNzaW9uIjogZmFsc2UsICJvdXRwdXRTcGVlY2giOiB7InR5cGUiOiAiU1NNTCIsICJ0ZXh0IjogIiIsICJzc21sIjogImphdmEtc2RrXHU2MGE4XHU3Njg0XHU3YTBlXHU1MjRkXHU1ZGU1XHU4ZDQ0XHU2NjJmXHU1OTFhXHU1YzExXHU1NDYyPyJ9LCAicmVwcm9tcHQiOiB7InR5cGUiOiAiU1NNTCIsICJ0ZXh0IjogIiIsICJzc21sIjogImphdmEtc2RrXHU2MGE4XHU3Njg0XHU3YTBlXHU1MjRkXHU1ZGU1XHU4ZDQ0XHU2NjJmXHU1OTFhXHU1YzExXHU1NDYyPyJ9LCAiYXVkaW9VcmwiOiAiYmFpZHUiLCAiYXBwSW5mbyI6IHsiYXBwTmFtZSI6ICJiYWlkdSIsICJwYWNrYWdlTmFtZSI6IG51bGwsICJkZWVwTGluayI6ICJiYWlkdSJ9LCAicmVxdWVzdFN0YXJ0VGltZSI6IDE1MTYxMDk4NDQsICJyZXF1ZXN0RW5kVGltZSI6IDE1MTYxMDk4NDQsICJ0aW1lc3RhbXAiOiAxNTE2MTA5ODQ0LCAic3lzRXZlbnQiOiB7InByZUV2ZW50TGlzdCI6IHt9LCAicG9zdEV2ZW50TGlzdCI6IHt9LCAiZXZlbnRDb3N0VGltZSI6IDAsICJkZXZpY2VFdmVudENvc3RUaW1lIjogMH0sICJ1c2VyRXZlbnQiOiB7ImFhMSI6IDAsICJhYTIiOiAwLCAiYWEzIjogMH19fQ==97d6bf29-4482-934e-c44c-626b151b46ba1516109844debug'''
    signData = '''VNt+71reYkBFvPlqMwpRmUQFXDlBSeLEyOiEu9+Sd1azfvyms/lHu9TFFHmVf6NFJA1e3f1fNhJq0XhFGvoc/gina7HTdHh1gGZrQcO/UZgQp80j6kaJAZXenQiwCz10rI/cooHQXMsh7vyVdmS14jUt+9I/Cwn6BHfxSwhFlYY='''
    print(verify(orginData,signData))
    pass
