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

class ListTemplate2(BodyTemplate):
    def __init__(self):
        super(ListTemplate2, self).__init__()
        self.setType('ListTemplate2')

    pass


if __name__ == '__main__':
    pass