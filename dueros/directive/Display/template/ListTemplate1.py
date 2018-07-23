#!/usr/bin/env python2
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
    listTemplate.set_token('4234234')
    listTemplate.set_background_image('https://skillstore.cdn.bcebos.com/icon/100/c709eed1-c07a-be4a-b242-0b0d8b777041.jpg')
    listTemplate.set_title('托尔斯泰')

    item = ListTemplateItem()
    item.set_token('1')
    item.set_plain_primary_text('p')
    item.set_plain_secondary_text('s')
    item.set_image('asfasdf')
    listTemplate.add_item(item)
    print(listTemplate.get_data())
    pass