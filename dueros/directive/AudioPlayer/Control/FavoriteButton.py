#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/28

"""
    desc:pass
"""

from dueros.directive.AudioPlayer.Control.Button import Button


class FavoriteButton(Button):

    def __init__(self):
        Button.__init__(self, 'FAVORITE')

    pass


if __name__ == '__main__':
    pass