#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/28

"""
    desc:pass
"""
PLAIN_TEXT = 'PlainText'
RICH_TEXT = 'RichText'


def in_enum(text_type):
    return text_type == PLAIN_TEXT or text_type == RICH_TEXT


if __name__ == '__main__':
    # position = TextContentPosition()
    print(PLAIN_TEXT)
    pass
