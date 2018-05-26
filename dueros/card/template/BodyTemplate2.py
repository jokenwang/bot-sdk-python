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


class BodyTemplate2(BodyTemplate):

    def __init__(self):
        super(BodyTemplate2, self).__init__()
        self.image = ImageStructure()
        self.setType('BodyTemplate2')
        pass

    def setImage(self, url):
        if url:
            self.image.setUrl(url)
            self.data['image'] = self.image.getData()

    def setImage(self, image):

        if isinstance(image, ImageStructure):
            self.image = image
            self.data['image'] = self.image.getData()

    def setPlainTextContent(self, plainTextContent):
        if plainTextContent:
            self.textContent.setText(plainTextContent)
            self.textContent.setType('PlainText')
            self.data['template']['content'] = self.textContent.getData()

    def setTextContent(self, textContent):

        if isinstance(textContent, TextStructure):
            self.textContent = textContent
            self.data['template']['content'] = textContent.getData()


if __name__ == '__main__':
    bodytemplate = BodyTemplate2()
    bodytemplate.setTitle('呵呵')
    bodytemplate.setToken("tttt")
    # bodytemplate.setBackgroundImage('background')
    image = ImageStructure()
    image.setUrl('http://www.baidu.com')
    bodytemplate.setBackgroundImage(image)
    bodytemplate.setPlainTextContent('bodyTemplate')
    print(bodytemplate.getData())
    pass
