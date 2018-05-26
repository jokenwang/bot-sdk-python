#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/26

"""
    desc:pass
"""

from dueros.card.BaseCard import BaseCard
from dueros.Utils import Utils
from dueros.card.template.TextStructure import TextStructure
from dueros.card.template.ImageStructure import ImageStructure

class BodyTemplate(BaseCard):

    def __init__(self):
        super(BodyTemplate, self).__init__()
        self.data['type'] = 'Display.RenderTemplate'
        self.data['template'] = {}
        self.textContent = TextStructure()
        self.backgroundImage = ImageStructure()

    def setToken(self, token):
        '''

        :param token:
        :return:
        '''
        if token:
            self.data['template']['token'] = token

    def setType(self, type):
        '''

        :param type:
        :return:
        '''
        if type:
            self.data['template']['type'] = type


    def setBackgroundImage(self, url):

        if url:
            self.backgroundImage.setUrl(url)
            self.data['template']['backgroundImage'] = self.backgroundImage.getData()
        pass

    def setBackgroundImage(self, image):
        '''

        :param image:
        :return:
        '''
        if isinstance(image, ImageStructure):
            self.backgroundImage = image
            self.data['template']['backgroundImage'] = image.getData()

    def setTitle(self, title):
        '''

        :param title:
        :return:
        '''
        if type:
            self.data['template']['title'] = title
        pass


if __name__ == '__main__':

    bodytemplate = BodyTemplate()
    bodytemplate.setTitle('呵呵')
    bodytemplate.setToken("tttt")
    bodytemplate.setBackgroundImage('background')
    # bodytemplate.setPlainTextContent('bodyTemplate')
    # bodytemplate.setPosition('LEFT')
    print(bodytemplate.getData())
    pass