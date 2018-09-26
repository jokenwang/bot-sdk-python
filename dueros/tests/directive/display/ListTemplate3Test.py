#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/19

"""
    desc:pass
"""
import unittest

from dueros.directive.Display.RenderAudioPlayerInfo import RenderAudioPlayerInfo
from dueros.directive.AudioPlayer.AudioPlayerInfoContent import AudioPlayerInfoContent
from dueros.directive.AudioPlayer.Control.PlayPauseButton import PlayPauseButton
from dueros.directive.AudioPlayer.Control.RepeatButton import RepeatButton
from dueros.directive.Display.template.ListTemplate3 import ListTemplate3
from dueros.directive.Display.template.ListTemplateItem import ListTemplateItem
from dueros.directive.Display.tag.FreeTag import FreeTag
from dueros.directive.Display.tag.CustomTag import CustomTag
from dueros.directive.Display.tag.PayTag import PayTag

import json

class ListTemplate3Test(unittest.TestCase):

    def testGetData(self):
        listTemplate = ListTemplate3()
        with open("../../json/list_template3.json", encoding='utf-8') as f:
            fileContent = f.read()
        self.data = json.loads(fileContent)
        listTemplate = ListTemplate3();
        listTemplate.set_token('test_token')
        listTemplate.set_background_image('www. backgroundImage.com')
        listTemplate.set_title('title')
        freeTag = FreeTag()
        payTag = PayTag()
        tags = [freeTag, payTag]
        listTemplateItem = ListTemplateItem()
        listTemplateItem.set_token('token1')
        listTemplateItem.set_image('www.image1.com', 200, 200)
        listTemplateItem.set_image_tags(tags)

        listTemplateItem.set_content('text1')
        listTemplate.add_item(listTemplateItem)
        customTag = CustomTag('自定义')
        customTag.set_color('#000000')
        customTag.set_background_color('#FFFFFF')

        tags = [customTag]

        listTemplateItem = ListTemplateItem()
        listTemplateItem.set_token('token2')
        listTemplateItem.set_image('www.image2.com', 200, 200)
        listTemplateItem.set_image_tags(tags)

        listTemplateItem.set_content('text2')
        listTemplate.add_item(listTemplateItem)


        self.assertEqual(listTemplate.get_data(), self.data)

if __name__ == '__main__':
    pass