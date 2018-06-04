#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/26

"""
    desc:pass
"""


from dueros.directive.Display.template.BaseTemplate import BaseTemplate
from dueros.directive.Display.template.ListTemplateItem import ListTemplateItem

class ListTemplate(BaseTemplate):

    def __init__(self, type):
        super(ListTemplate, self).__init__(['token','title','type'])
        self.setType(type)
        self.data['listItems'] = []

    def addItem(self, item):
        if isinstance(item, ListTemplateItem):
            self.data['listItems'].append(item.getData())
        return self


if __name__ == '__main__':

    #
    pass