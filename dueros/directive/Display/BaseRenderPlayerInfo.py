#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/19

"""
    desc:pass
"""
from dueros.directive.BaseDirective import BaseDirective
from dueros.directive.Base.TraitPlayerInfo import TraitPlayerInfo


class BaseRenderPlayerInfo(TraitPlayerInfo, BaseDirective):

    def __init__(self, directive_type, content, controls=[]):
        super(BaseRenderPlayerInfo, self).__init__()
        BaseDirective.__init__(self, directive_type)
        self.data['token'] = self.gen_token()
        self.set_content(content)
        self.set_controls(controls)


if __name__ == '__main__':

    t = BaseRenderPlayerInfo('aaa', None)
    print(t.get_data())
    pass