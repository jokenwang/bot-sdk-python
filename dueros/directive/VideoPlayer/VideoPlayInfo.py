#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/19

"""
    desc:pass
"""
from dueros.directive.Base.TraitPlayerInfo import TraitPlayerInfo


class VideoPlayInfo(TraitPlayerInfo):

    def __init__(self, content, controls=[]):
        super(VideoPlayInfo, self).__init__()
        self.set_content(content)
        self.set_controls(controls)

    pass


if __name__ == '__main__':
    pass