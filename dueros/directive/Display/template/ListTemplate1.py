#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/26

"""
    desc:pass
"""


from dueros.directive.Display.template.ListTemplate import ListTemplate
from dueros.directive.Display.template.ListTemplateItem import ListTemplateItem
class ListTemplate1(ListTemplate):

    def __init__(self):
        super(ListTemplate1, self).__init__('ListTemplate1')

if __name__ == '__main__':
    listTemplate = ListTemplate1()
    listTemplate.setToken('4234234')
    listTemplate.setBackGroundImage('https://skillstore.cdn.bcebos.com/icon/100/c709eed1-c07a-be4a-b242-0b0d8b777041.jpg')
    listTemplate.setTitle('托尔斯泰')

    item = ListTemplateItem()
    item.setToken('1')
    item.setPlainPrimaryText('p')
    item.setPlainSecondaryText('s')
    item.setImage('asfasdf')
    listTemplate.addItem(item)
    print(listTemplate.getData())
    pass