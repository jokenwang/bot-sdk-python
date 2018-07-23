#!/usr/bin/env python2
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
    bodytemplate.set_title('呵呵')
    bodytemplate.set_token("tttt")
    bodytemplate.set_background_image('http://adfasdf')
    bodytemplate.set_plain_content('bodyTemplate')
    print(bodytemplate.get_data())
    pass
