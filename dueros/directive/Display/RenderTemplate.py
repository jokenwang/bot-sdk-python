#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/27

"""
    desc:pass
"""

from dueros.directive.BaseDirective import BaseDirective
from dueros.directive.Display.template.BaseTemplate import BaseTemplate

class RenderTemplate(BaseDirective):

    def __init__(self, baseTemplate):

        super(RenderTemplate, self).__init__('Display.RenderTemplate')
        self.set_template(baseTemplate)

    def set_template(self, template):
        '''
        设置模板
        :param template:
        :return:
        '''
        if isinstance(template, BaseTemplate):
            self.data['template'] = template.get_data()

if __name__ == '__main__':
    pass