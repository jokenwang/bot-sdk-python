#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/17

"""
    横向列表模板
"""
from dueros.directive.Display.template.ListTemplate import ListTemplate


class ListTemplate3(ListTemplate):

    def __init__(self):
        ListTemplate.__init__(self, 'ListTemplate3')


if __name__ == '__main__':
    pass