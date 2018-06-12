#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/28

"""
    desc:pass
"""
from dueros.directive.AudioPlayer.Control.Button import Button


class PlayPauseButton(Button):

    def __init__(self):
        super(PlayPauseButton, self).__init__('PLAY_PAUSE')


if __name__ == '__main__':
    pass