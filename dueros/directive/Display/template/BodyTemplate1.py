#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/26

"""
    desc:pass
"""

from dueros.directive.Display.template.BaseTemplate import BaseTemplate

class BodyTemplate1(BaseTemplate):

    def __init__(self):
        super(BodyTemplate1, self).__init__(['token','title','type'])
        self.setType('BodyTemplate1')
        pass

    def setPlainTextContent(self, text, position = ''):
        textStructure = self.createTextStructure(text, position)
        if textStructure:
            if not 'textContent' in self.data.keys():
                self.data['textContent'] = {}
            self.data['textContent']['text'] = textStructure.getData()
            return self

if __name__ == '__main__':
    bodytemplate = BodyTemplate1()
    bodytemplate.setTitle('呵呵')
    bodytemplate.setToken("tttt")
    bodytemplate.setBackGroundImage('htt[://///')
    bodytemplate.setPlainTextContent('bodyTemplate')
    print(bodytemplate.getData())
    pass