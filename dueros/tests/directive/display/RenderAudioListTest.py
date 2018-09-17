#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/1

"""
    desc:pass
"""
import unittest
from dueros.directive.Display.RenderAudioList import RenderAudioList
from dueros.directive.Display.media.AudioItem import AudioItem


class RenderAudioListTest(unittest.TestCase):

    def setUp(self):
        self.audiolist = RenderAudioList('audio_list_title')

    def testGetData(self):
        data = {
            'type': 'Display.RenderAudioList',
            'token':'audio_list_token',
            'title': 'audio_list_title',
            'behavior': 'REPLACE',
            'size': 1,
            'audioItems': [
                {
                    'title': 'audio_item_title',
                    'titleSubtext1': 'titleSubtext1',
                    'titleSubtext2': 'titleSubtext2',
                    'isFavorited': True,
                    'isMusicVideo': True,
                    'image':{
                        'src': 'image.png'
                    },
                'token':'token'
                }
            ]
        }
        self.audiolist.set_token('audio_list_token');
        audio_item = AudioItem('audio_item_title', 'titleSubtext1')
        audio_item.set_music_video_tag(True)
        audio_item.set_favorited(True)
        audio_item.set_image('image.png')
        audio_item.set_token('token');
        audio_item.set_title_subtext2('titleSubtext2')
        self.audiolist.add_audio_item(audio_item)
        self.assertEqual(self.audiolist.get_data(), data)
    pass


if __name__ == '__main__':
    pass