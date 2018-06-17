#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# description:
# author:jack
# create_time: 2017/12/30


class BaseCard(object):
	'''
	卡片基类
	'''

	def __init__(self, field = []):
		self.data = {}
		self.supportSetField = field

	def addCueWords(self, arr):
		'''
		为卡片添加cue words 提示用户输入
		:param arr: 数组
		:return:
		'''
		if arr:
			if isinstance(arr, str):
				arr = [arr]

			if 'cueWords' in self.data:
				self.data['cueWords'] = self.data['cueWords']
			else:
				self.data['cueWords'] = []

			self.data['cueWords'].extend(arr)
		return self

	def setAnchor(self, url, anchorText):
		'''
		设置卡片链接
		:param url:	 比如:http(s)://....
		:param anchorText:	链接显示的文字
		:return:
		'''
		if url:
			self.data['url'] = url
			if anchorText:
				self.data['anchorText'] = anchorText
		return self

	def getData(self):
		return self.data

	def __getattr__(self, item):
		'''
		添加魔术方法
		:param item:
		:return:
		'''
		#获取操作类型 set
		operation = item[0:3]
		#获取被操作的属性
		field = item[3:]
		if(operation == 'set' and field and (field.lower() in self.supportSetField)):
			def function(*args):
				self.data[field.lower()] = args[0]
			return function
		else:
			def function(*args):
				print('不支持', operation, field)
			return function

if __name__ == '__main__':

	pass