#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/1/16

"""
    desc:pass
"""

import requests

import base64

class test_server:
    pass


if __name__ == '__main__':
    # headers = {
    #     'HOST':'',
    #     'Content-Type': 'application/x-www-form-urlencoded',
    #     'Content-Length': '',
    #     'SIGNATURE': ''
    # }
    # response = requests.post("http://127.0.0.1:8000",data='adfasdfadfasdfasdfasdfadf', headers=headers)
    # print(response.content)

    decode = '''
    eyJzZXJ2aWNlRGF0YSI6IHsic2RrVHlwZSI6ICJweXRob24iLCAic2RrVmVyc2lvbiI6ICIxLjAuMCIsICJyZXF1ZXN0SWQiOiAiY2Y5ZTQ1NThjYjY2NGVkMDk5M2E0ZjNmNTY2MmVmYjdfMSIsICJxdWVyeSI6ICJcdTY3ZTVcdTRlMmFcdTdhMGUiLCAicmVhc29uIjogIlVTRVJfSU5JVElBVEVEIiwgImRldmljZUlkIjogImRldmljZUlkcmVhbCIsICJyZXF1ZXN0VHlwZSI6ICJJbnRlbnRSZXF1ZXN0IiwgInVzZXJJZCI6ICI1NTE4ODEzNyIsICJpbnRlbnROYW1lIjogImlucXVpcnkiLCAic2Vzc2lvbklkIjogInNlc3Npb25JZCIsICJsb2NhdGlvbiI6IHsiYmQwOWxsIjogeyJsb25naXR1ZGUiOiAxMTYuNDE2NTA1ODU3NjUsICJsYXRpdHVkZSI6IDM5LjkyMjU4OTgyMzI2NX0sICJ3Z3M4NCI6IHsibG9uZ2l0dWRlIjogMTE2LjQwMzg3Mzk3LCAibGF0aXR1ZGUiOiAzOS45MTQ4ODkwOH0sICJiZDA5bWMiOiB7ImxvbmdpdHVkZSI6IDEyOTU5NTY3LjQwMzAzNCwgImxhdGl0dWRlIjogNDgyNzAyMS44MjM1MDc1fX0sICJzbG90VG9FbGljaXQiOiAibW9udGhseXNhbGFyeSIsICJzaG91bGRFbmRTZXNzaW9uIjogZmFsc2UsICJvdXRwdXRTcGVlY2giOiB7InR5cGUiOiAiU1NNTCIsICJ0ZXh0IjogIiIsICJzc21sIjogImphdmEtc2RrXHU2MGE4XHU3Njg0XHU3YTBlXHU1MjRkXHU1ZGU1XHU4ZDQ0XHU2NjJmXHU1OTFhXHU1YzExXHU1NDYyPyJ9LCAicmVwcm9tcHQiOiB7InR5cGUiOiAiU1NNTCIsICJ0ZXh0IjogIiIsICJzc21sIjogImphdmEtc2RrXHU2MGE4XHU3Njg0XHU3YTBlXHU1MjRkXHU1ZGU1XHU4ZDQ0XHU2NjJmXHU1OTFhXHU1YzExXHU1NDYyPyJ9LCAiYXVkaW9VcmwiOiAiYmFpZHUiLCAiYXBwSW5mbyI6IHsiYXBwTmFtZSI6ICJiYWlkdSIsICJwYWNrYWdlTmFtZSI6IG51bGwsICJkZWVwTGluayI6ICJiYWlkdSJ9LCAicmVxdWVzdFN0YXJ0VGltZSI6IDE1MTYxMDc0NzEsICJyZXF1ZXN0RW5kVGltZSI6IDE1MTYxMDc0NzEsICJ0aW1lc3RhbXAiOiAxNTE2MTA3NDcxLCAic3lzRXZlbnQiOiB7InByZUV2ZW50TGlzdCI6IHt9LCAicG9zdEV2ZW50TGlzdCI6IHt9LCAiZXZlbnRDb3N0VGltZSI6IDAsICJkZXZpY2VFdmVudENvc3RUaW1lIjogMH0sICJ1c2VyRXZlbnQiOiB7ImFhMSI6IDAsICJhYTIiOiAwLCAiYWEzIjogMH19fQ=='''
    print(str(base64.b64decode(decode)))
    pass