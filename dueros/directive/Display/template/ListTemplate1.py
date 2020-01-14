#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/26

from dueros.directive.Display.template.ListTemplate import ListTemplate
from dueros.directive.Display.template.ListTemplateItem import ListTemplateItem


class ListTemplate1(ListTemplate):
    """
    ListTemplate1模板
    详见文档：https://dueros.baidu.com/didp/doc/dueros-bot-platform/dbp-custom/display-template_markdown#ListTemplate1
    """

    def __init__(self):
        super(ListTemplate1, self).__init__('ListTemplate1')
