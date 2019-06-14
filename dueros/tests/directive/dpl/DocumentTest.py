#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2019-06-13

"""
    desc:pass
"""
import unittest
import json

from dueros.directive.DPL.Document import Document

class DocumentTest(unittest.TestCase):

    def setUp(self):
        self.document = Document()

    def test_get_document_path(self):

        self.document.get_document_from_path('./doc.json')

        print(self.document.get_data())

    def test_init_document(self):
        with open('./doc.json', encoding='utf-8') as f:
            content = f.read()
            self.document.init_data(json.loads(content, encoding='utf-8'))
            print(self.document.get_data())

if __name__ == '__main__':
    pass