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

class ListTemplate1(BodyTemplate):
    def __init__(self):
        super(ListTemplate1, self).__init__()
        self.setType('ListTemplate1')

    pass


if __name__ == '__main__':
    pass