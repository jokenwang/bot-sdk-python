#!/usr/bin/env python3
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

    def __init__(self):
        super(RenderTemplate, self).__init__('Display.RenderTemplate')

    def setTemplate(self, template):
        if isinstance(template, BaseTemplate):
            self.data['template'] = template.getData()


if __name__ == '__main__':
    pass