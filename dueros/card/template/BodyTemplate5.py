#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/26

"""
    desc:pass
"""

from dueros.card.template.BodyTemplate2 import BodyTemplate2
from dueros.card.template.TextStructure import TextStructure
from dueros.card.template.ImageStructure import ImageStructure
from dueros.card.template.ImageStructure import ImageStructure

class BodyTemplate5(BodyTemplate2):

    def __init__(self):
        super(BodyTemplate5, self).__init__()
        self.setType('BodyTemplate5')
        self.data['images'] = []

    def addImages(self, imageStructure):

        if isinstance(imageStructure,ImageStructure):
            self.data['images'].append(imageStructure.getData())
        return self
    pass


if __name__ == '__main__':
    pass