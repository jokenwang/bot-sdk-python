#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/1

"""
    desc:pass
"""
import unittest
from dueros.directive.Display.RenderVideoList import RenderVideoList
from dueros.directive.Display.media.VideoItem import VideoItem


class RenderVideoListTest(unittest.TestCase):

    def setUp(self):
        self.videoList = RenderVideoList('video_list_title')

    def testGetData(self):
        
        data = {
            'type': 'Display.RenderVideoList',
            'token' : 'video_list_token',
            'title' : 'video_list_title',
            'behavior' : 'REPLACE',
            'size' : 1,
            'videoItems' : [
                {
                    'title' : 'video_item_title',
                    'titleSubtext1' : 'titleSubtext1',
                    'titleSubtext2' : 'titleSubtext2',
                    'isFavorited' : True,
                    'mediaLengthInMilliseconds' : 10000,
                    'image' : {
                        'src' : 'image.png'
                    },
                    'token' : 'token'
                }
            ]
        }

        self.videoList.set_token('video_list_token')
        videoItem = VideoItem('video_item_title', 'titleSubtext1')
        videoItem.set_media_length_in_milliseconds(10000)
        videoItem.set_favorited(True)
        videoItem.set_image('image.png')
        videoItem.set_token('token');
        videoItem.set_title_subtext2('titleSubtext2')
        self.videoList.add_video_item(videoItem)

        self.assertEqual(self.videoList.get_data(), data)
    pass


if __name__ == '__main__':
    pass