#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2019-06-13

"""
    desc:pass
"""

from dueros.directive.BaseDirective import BaseDirective
from dueros.directive.DPL.Document import Document


class RenderDocument(BaseDirective):

    def __init__(self):
        super(RenderDocument, self).__init__('DPL.RenderDocument')

    def set_document(self, document):
        if isinstance(document, Document):
            self.data['document'] = document.get_data()

    def set_data_source(self, data_source):
        if data_source:
            self.data['dataSources'] = data_source



if __name__ == '__main__':
    pass