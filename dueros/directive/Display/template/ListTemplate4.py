#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/17

from dueros.directive.Display.template.ListTemplate import ListTemplate


class ListTemplate4(ListTemplate):
    """
        纵向列表模板基类
    """

    def __init__(self):
        super(ListTemplate4, self).__init__('ListTemplate4')
