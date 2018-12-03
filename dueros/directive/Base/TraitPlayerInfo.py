#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/19

"""
    desc:pass
"""
from dueros.directive.AudioPlayer.Control.BaseButton import BaseButton
from dueros.directive.Base.BasePlayerInfoContent import BasePlayerInfoContent


class TraitPlayerInfo:

    def __init__(self):
        self.data = {}
        self.controls = []
        self.content = None

    def set_controls(self, controls):
        self.controls = []
        if isinstance(controls, BaseButton):
            self.controls.append(controls)
        if isinstance(controls, list):
            temp = list(filter(lambda value: isinstance(value, BaseButton), controls))
            self.controls = self.controls + temp

    def add_control(self, control):
        if isinstance(control, BaseButton):
            self.controls.append(control)

    def set_content(self, content):

        if isinstance(content, BasePlayerInfoContent):
            self.content = content

    def get_data(self):

        if not self.data:
            self.data = []

        if self.content:
            self.data['content'] = self.content.get_data()

        if self.controls:
            controls_data = list(map(lambda value: value.get_data(), self.controls))
            self.data['controls'] = controls_data
        return self.data
    pass


if __name__ == '__main__':
    pass