#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/1/6

"""
    desc:pass
"""

from setuptools import setup
from setuptools import find_packages

setup(
    name='dueros-bot-python2',
    version='1.2.6',
    author='jack',
    author_email='mupdf@sina.com',
    description='Third party DuerOS Bot Python SDK ',
    keywords='DuerOS Bot',
    url='https://github.com/jokenwang/bot-sdk-python',
    packages=find_packages(),
    install_requires=[
        'pycrypto>=2.6.1',
        'requests',
	    'pyOpenSSL'
    ]
)
