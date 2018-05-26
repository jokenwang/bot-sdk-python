#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/26

"""
    desc:pass
"""


from dueros.card.template.BodyTemplate import BodyTemplate
from dueros.card.template.TextStructure import TextStructure
from dueros.card.template.ImageStructure import ImageStructure
from dueros.card.template.ListTemplateItem import ListTemplateItem

class ListTemplate(BodyTemplate):

    def __init__(self):
        super(ListTemplate, self).__init__()
        self.data['listItems'] = []

    def addItem(self, item):
        if isinstance(item, ListTemplateItem):
            self.data['listItems'].append(item.getData())

    pass


if __name__ == '__main__':

    listTemplate = ListTemplate()
    listTemplate.setToken('4234234')
    listTemplate.setBackgroundImage('https://skillstore.cdn.bcebos.com/icon/100/c709eed1-c07a-be4a-b242-0b0d8b777041.jpg')
    listTemplate.setTitle('托尔斯泰')

    item = ListTemplateItem()
    item.setToken('1')
    item.setPlainPrimaryText('p')
    item.setPlainSecondaryText('s')
    item.setImage('asfasdf')
    listTemplate.addItem(item)
    print(listTemplate.getData())
    pass