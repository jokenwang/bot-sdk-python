#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/30

"""
    desc:pass
"""
from dueros.directive.BaseDirective import BaseDirective


class RecordSpeech(BaseDirective):
    """
    录音指令
    """

    def __init__(self):
        BaseDirective.__init__(self, 'Record.RecordSpeech')
        self.data['token'] = self.gen_token()

    def set_token(self, token):
        if token and isinstance(token, str):
            self.data['token'] = token


if __name__ == '__main__':
    pass