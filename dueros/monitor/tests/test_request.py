#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/1/16

"""
    desc:pass
"""
from dueros.monitor.model.Request import Request
import os
import json

class test_request:
    pass


if __name__ == '__main__':

    def requestData():
        with open("../data/intent_request_tax.json", 'r', encoding='utf-8') as load_f:
            return load_f.read()
    requestData = requestData()

    request = Request(json.loads(requestData))

    print(request.getType())
    print(request.getUserId())
    print(request.getQuery())
    print(request.getBotId())
    print(request.getRequestId())
    print(request.getReson())
    print(request.getIntentName())
    print(request.getSessionId())
    print(request.getDeviceId())
    print(request.getLocation())
    print(request.isDialogStateCompleted())
    pass
