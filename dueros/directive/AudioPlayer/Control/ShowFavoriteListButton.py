#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/28

from dueros.directive.AudioPlayer.Control.Button import Button


class ShowFavoriteListButton(Button):

    def __init__(self):
        super(ShowFavoriteListButton, self).__init__('SHOW_FAVORITE_LIST')
