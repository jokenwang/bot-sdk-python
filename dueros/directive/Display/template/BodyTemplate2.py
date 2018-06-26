#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/26

"""
    desc:pass
"""

from dueros.directive.Display.template.TextImageTemplate import TextImageTemplate


class BodyTemplate2(TextImageTemplate):

    def __init__(self):
        super(BodyTemplate2, self).__init__('BodyTemplate2')
        pass

if __name__ == '__main__':
    bodytemplate = BodyTemplate2()
    bodytemplate.setTitle('呵呵')
    bodytemplate.setToken("tttt")
    bodytemplate.setBackGroundImage('http://adfasdf')
    bodytemplate.setPlainContent('bodyTemplate')
    print(bodytemplate.getData())
    pass
