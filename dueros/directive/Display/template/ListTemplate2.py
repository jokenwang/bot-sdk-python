#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/26

"""
ListTemplate2模板
详见文档：https://dueros.baidu.com/didp/doc/dueros-bot-platform/dbp-custom/display-template_markdown#ListTemplate2
"""

from dueros.directive.Display.template.ListTemplate import ListTemplate
from dueros.directive.Display.template.ListTemplateItem import ListTemplateItem


class ListTemplate2(ListTemplate):

    def __init__(self):
        super(ListTemplate2, self).__init__('ListTemplate2')

if __name__ == '__main__':

    listTemplate = ListTemplate2()
    listTemplate.set_token('toke')
    listTemplate.set_background_image('http://www.baidu.com')
    listTemplate.set_title('title')

    listTemplateItem = ListTemplateItem()
    listTemplateItem.set_token('aaa')
    listTemplateItem.set_image('http://wwww.www')
    listTemplateItem.set_plain_primary_text('一级')
    listTemplateItem.set_plain_secondary_text('二级')
    listTemplateItem.set_tertiary_text('三级')
    listTemplate.add_item(listTemplateItem)
    print(listTemplate.get_data())
    pass