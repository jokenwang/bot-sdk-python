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

class ListTemplate2(ListTemplate):

    def __init__(self):
        super(ListTemplate2, self).__init__('ListTemplate2')

if __name__ == '__main__':

    listTemplate = ListTemplate2()
    listTemplate.setToken('toke')
    listTemplate.setBackGroundImage('http://www.baidu.com')
    listTemplate.setTitle('title')

    listTemplateItem = ListTemplateItem()
    listTemplateItem.setToken('aaa')
    listTemplateItem.setImage('http://wwww.www')
    listTemplateItem.setPlainPrimaryText('一级')
    listTemplateItem.setPlainSecondaryText('二级')
    listTemplateItem.setTertiaryText('三级')
    listTemplate.addItem(listTemplateItem)
    print(listTemplate.getData())
    pass