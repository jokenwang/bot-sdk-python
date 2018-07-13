#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/7/13

"""
    desc:pass
"""

import unittest
from dueros.directive.VideoPlayer.VideoPlayer import VideoPlayer
from dueros.directive.AudioPlayer.PlayBehaviorEnum import PlayBehaviorEnum

class PlayTest(unittest.TestCase):

    url = 'http://dbp-resource.gz.bcebos.com/zhaojing_demo/%E5%91%A8%E6%9D%B0%E4%BC%A6%20-%20%E5%91%8A%E7%99%BD%E6%B0%94%E7%90%83.mp3?authorization=bce-auth-v1%2Fbc881876e7a94578935a868716b6cf69%2F2018-05-29T08%3A13%3A27Z%2F-1%2Fhost%2Fbff1c88a876764a98d3f3f35bc2a4952835190339b64a39c7020e8a4b190b3b9';

    def setUp(self):
        self.play1 = VideoPlayer(self.url, PlayBehaviorEnum.REPLACE_ENQUEUED)
        self.play1.setOffsetInMilliseconds(121321)
        self.play1.setExpiryTime('123213223')
        self.play1.setExpectedPreviousToken('asdsd-1233-dsew-39FG')
        self.play1.setReportDelayInMs(1234.12212)
        self.play1.setReportIntervalInMs(123)
        self.play1.setToken('AGDG-SAHSHD_ASDS_123')
        self.play1.setUrl('http://set-url.com')

    def testGetToken(self):

        self.assertEqual(self.play1.getToken(), 'AGDG-SAHSHD_ASDS_123')

    def testGetData(self):

        data = self.play1.getData()
        data['videoItem']['videoItemId'] = 'AGDG-SAHSHD_ASDS_123'
        print(data)
        ret = {
            'type': 'VideoPlayer.Play',
            'playBehavior': PlayBehaviorEnum.REPLACE_ENQUEUED.value,
            'videoItem': {
                'videoItemId': 'AGDG-SAHSHD_ASDS_123',
                'stream': {
                    'url': 'http://set-url.com',
                    'offsetInMilliseconds': 121321,
                    'token': 'AGDG-SAHSHD_ASDS_123',
                    'expiryTime': '123213223',
                    'expectedPreviousToken': 'asdsd-1233-dsew-39FG',
                    'progressReport': {
                        'progressReportDelayInMilliseconds': 1234,
                        'progressReportIntervalInMilliseconds': 123
                    }
                }
            }
        }

        self.assertEqual(data, ret)

    pass


if __name__ == '__main__':
    pass