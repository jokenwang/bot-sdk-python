#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/1/16

"""
    desc:pass
"""

from dueros.monitor.model.Response import Response
import os
import json

class test_response:
    pass


if __name__ == '__main__':

    def responseData():
        with open("../data/test_response_tax.json", 'r', encoding='utf-8') as load_f:
            return load_f.read()
    responseData = responseData()
    # print(responseData)

    response = Response(json.loads(responseData))

    print(response.getSlotName())
    print(response.getShouldEndSession())
    print(response.getOutputSpeech())
    print(response.getReprompt())

    pass
