#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# description:
# author:jack
# create_time: 2017/12/30

"""
卡片基类
"""

import json

class BaseCard(object):

	data = {}

	def __init__(self, field):
		print('field %s' % field)
		self.supportSetField = field

	def addCueWords(self, arr):
		'''
		为卡片添加cue words 提示用户输入
		:param arr:
		:return:
		'''
		pass

	def setAnchor(self, url, anchorText):
		if(url):
			self.data['url'] = url
			if(anchorText):
				self.data['anchorText'] = anchorText
		return self

	def getData(self, key):
		if(key):
			return self.data[key]
		else:
			return self.data

	def getContentData(self):

		return self.data['content']
