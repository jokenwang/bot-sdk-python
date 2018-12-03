#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/17

"""
    纵向列表模板基类
"""
from dueros.directive.Display.template.ListTemplate import ListTemplate


class ListTemplate4(ListTemplate):

    def __init__(self):
        ListTemplate.__init__(self, 'ListTemplate4')


if __name__ == '__main__':
    pass