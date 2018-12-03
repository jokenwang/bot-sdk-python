#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/19

"""
    desc:pass
"""
from dueros.directive.AudioPlayer.PlayerInfo import PlayerInfo


class AudioPlayerInfo(PlayerInfo):

    def __init__(self, content, controls=[]):
        PlayerInfo.__init__(self, content, controls)


if __name__ == '__main__':
    pass