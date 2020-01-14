#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/17

from dueros.directive.Display.template.ListTemplate import ListTemplate


class ListTemplate3(ListTemplate):
    """
        横向列表模板
    """

    def __init__(self):
        super(ListTemplate3, self).__init__('ListTemplate3')