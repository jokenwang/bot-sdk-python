#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/26

"""
    desc:pass
"""

from dueros.card.BaseCard import BaseCard
from dueros.card.template.TextStructure import TextStructure
from dueros.card.template.ImageStructure import ImageStructure
class ListTemplateItem(BaseCard):

    def __init__(self):
        super(ListTemplateItem, self).__init__()
        self.data['textContent'] = {}

    def setPlainPrimaryText(self, primaryText):
        if primaryText:
            primaryTextStructure = TextStructure()
            primaryTextStructure.setType('PlainText')
            primaryTextStructure.setText(primaryText)
            self.data['textContent']['primaryText'] = primaryTextStructure.getData()
        pass

    def setPlainSecondaryText(self,secondaryText):
        if secondaryText:
            secondaryTextStructure = TextStructure()
            secondaryTextStructure.setType('PlainText')
            secondaryTextStructure.setText(secondaryText)
            self.data['textContent']['secondaryText'] = secondaryTextStructure.getData()
        pass

    def setTertiaryText(self,tertiaryText):
        if tertiaryText:
            tertiaryTextStructure = TextStructure()
            tertiaryTextStructure.setType('PlainText')
            tertiaryTextStructure.setText(tertiaryText)
            self.data['textContent']['tertiaryText'] = tertiaryTextStructure.getData()
        pass

    def setImage(self, url):
        if url:
            image = ImageStructure()
            image.setUrl(url)
            self.data['image'] = image.getData()
    pass


if __name__ == '__main__':
    pass