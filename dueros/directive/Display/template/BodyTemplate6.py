#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/17

"""
    上图下文模版类
"""

from dueros.directive.Display.template.TextImageTemplate import TextImageTemplate


class BodyTemplate6(TextImageTemplate):
    """
     bodyTemplate = new BodyTemplate6()
     bodyTemplate.set_token('token')
     bodyTemplate.set_image('https://skillstore.cdn.bcebos.com/icon/100/c709eed1-c07a-be4a-b242-0b0d8b777041.jpg')
     bodyTemplate.set_background_image('https://skillstore.cdn.bcebos.com/icon/100/c709eed1-c07a-be4a-b242-0b0d8b777041.jpg')
     bodyTemplate.set_title('托尔斯泰的格言')
     bodyTemplate.set_plain_content('拖尔斯泰-理想的书籍是智慧的钥匙')
    """
    def __init__(self):
        super(BodyTemplate6, self).__init__('BodyTemplate6')



if __name__ == '__main__':
    pass