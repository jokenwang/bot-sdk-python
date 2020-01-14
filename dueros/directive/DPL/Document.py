#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2019-06-13

import json
import logging
from dueros.Utils import Utils


class Document(object):

    def __init__(self, doc=None):
        self.data = dict()
        if isinstance(doc, dict):
            self.data = doc

    def init_data(self, doc):
        """
        初始化文档对象数据
        :param doc:
        :return:
        """

        if isinstance(doc, dict):
            self.data = doc

    def set_document_duration(self, duration):
        """
        设置页面停留时间
        :param duration:
        :return:
        """

        if Utils.is_numeric(duration):
            self.data['duration'] = duration

    def get_data(self):
        return self.data

    @staticmethod
    def get_document_from_path(path):
        """
        从指定路径(绝对路径)加载数据
        :param path:
        :return:
        """

        if path and isinstance(path, str):
            try:
                with open(path, encoding='utf-8') as f:
                    content = f.read()
                    data = json.loads(content, encoding='utf-8')
                    return data
            except FileNotFoundError as fileError:
                logging.error(fileError)
        else:
            logging.error('path:%s is error' % path)
