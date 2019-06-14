#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2019-06-14

"""
    desc:pass
"""
import unittest
from dueros.directive.DPL.RenderDocument import RenderDocument
from dueros.directive.DPL.Document import Document


class RenderDocumentTest(unittest.TestCase):

    def testGetData(self):
        doc = Document()
        doc.init_data(doc_data)
        renderDocument = RenderDocument()
        renderDocument.set_token('test_token')
        renderDocument.set_document(doc)
        renderDocument.set_data_source({
            'data': {
                'content': 'test content'
            }
        })
        print(renderDocument.get_data())
        self.assertEqual(renderDocument.get_data(), data)


doc_data = {
    'type': 'DPL',
    'version': '1.0',
    'dataSource': {
        'pageData': [
            {
                'text1': 'the first item text1',
                'src1': 'https://dbp-dict.bj.bcebos.com/homecard1024-520.jpg'
            },
            {
                'text2': 'this second item text2',
                'src2': 'https://dbp-dict.bj.bcebos.com/%E5%9C%A8%E5%AE%B6%E8%B4%B4.png'
            }
        ],
        'data': {
            'a': 10,
            'b': 20,
            'src': 'https://duerstatic.bj.bcebos.com/swan/dbp/compare/compare_vs.png',
            'text': '一段较大的字体的文本!',
            'text1': '一段较大的字体的文本1!',
            'text2': '一段较大的字体的文本2!',
            'text3': '一段较大的字体的文本3!',
            'content': 'This is custom content',
            'content1': 'This is mylayout text',
            'layout3': 'layout3 in data',
            'layout4': 'layout4 in data'
        },
        'listData': [
            {
                'text': 'text1',
                'src': 'http://src1'
            },
            {
                'text': 'text2',
                'src': 'http://src2'
            }
        ],
        'content': 'This is custom content'
    },
    'mainTemplate': {
        'parameters': [
                'payload'
        ],
        'items': [
            {
                'type': 'Header',
                'headerTitle': 'Pager-页面'
            },
            {
                'type': 'Pager',
                'initialPage': 1,
                'componentId': 'test_page_pageId1',
                'data': '${payload.pageData}',
                'firstItem': [
                    {
                        'type': 'Text',
                        'text': 'This is page firstItem text'
                    }
                ],
                'items': [
                    {
                        'type': 'Text',
                        'lineHeight': 10,
                        'textAlign': 'left',
                        'text': '${data.text1}'
                    },
                    {
                        'type': 'Image',
                        'src': '${data.src3}'
                    }
                ]
            }
        ]
    }
}


data = {
    'type': 'DPL.RenderDocument',
    'token': 'test_token',
    'document': {
        'type': 'DPL',
        'version': '1.0',
        'dataSource': {
            'pageData': [
                {
                    'text1': 'the first item text1',
                    'src1': 'https://dbp-dict.bj.bcebos.com/homecard1024-520.jpg'
                },
                {
                    'text2': 'this second item text2',
                    'src2': 'https://dbp-dict.bj.bcebos.com/%E5%9C%A8%E5%AE%B6%E8%B4%B4.png'
                }
            ],
            'data': {
                'a': 10,
                'b': 20,
                'src': 'https://duerstatic.bj.bcebos.com/swan/dbp/compare/compare_vs.png',
                'text': '一段较大的字体的文本!',
                'text1': '一段较大的字体的文本1!',
                'text2': '一段较大的字体的文本2!',
                'text3': '一段较大的字体的文本3!',
                'content': 'This is custom content',
                'content1': 'This is mylayout text',
                'layout3': 'layout3 in data',
                'layout4': 'layout4 in data'
            },
            'listData': [
                {
                    'text': 'text1',
                    'src': 'http://src1'
                },
                {
                    'text': 'text2',
                    'src': 'http://src2'
                }
            ],
            'content': 'This is custom content'
        },
        'mainTemplate': {
            'parameters': [
                        'payload'
            ],
            'items': [
                {
                    'type': 'Header',
                    'headerTitle': 'Pager-页面'
                },
                {
                    'type': 'Pager',
                    'initialPage': 1,
                    'componentId': 'test_page_pageId1',
                    'data': '${payload.pageData}',
                    'firstItem': [
                        {
                            'type': 'Text',
                            'text': 'This is page firstItem text'
                        }
                    ],
                    'items': [
                        {
                            'type': 'Text',
                            'lineHeight': 10,
                            'textAlign': 'left',
                            'text': '${data.text1}'
                        },
                        {
                            'type': 'Image',
                            'src': '${data.src3}'
                        }
                    ]
                }
            ]
        }
    },
    'dataSources': {
        'data': {
            'content': 'test content'
        }
    }
}

if __name__ == '__main__':
    pass