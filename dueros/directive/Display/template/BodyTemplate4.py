#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/26

"""
BodyTemplate4模板
详见文档：https://dueros.baidu.com/didp/doc/dueros-bot-platform/dbp-custom/display-template_markdown#BodyTemplate4
"""

from dueros.directive.Display.template.TextImageTemplate import TextImageTemplate


class BodyTemplate4(TextImageTemplate):

    def __init__(self):
        super(BodyTemplate4, self).__init__('BodyTemplate4')


if __name__ == '__main__':
    pass