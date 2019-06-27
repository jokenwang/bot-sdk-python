#!/usr/bin/env python3
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
    name='dueros-bot',
    version='3.2.0',
    author='jack',
    author_email='mupdf@sina.com',
    description='Third party DuerOS Bot Python SDK',
    keywords='DuerOS Bot',
    url='https://github.com/jokenwang/bot-sdk-python',
    packages=[
        'dueros',
        'dueros.card',
        'dueros.directive',
        'dueros.directive.Base',
        'dueros.directive.AppLauncher',
        'dueros.directive.AudioPlayer',
        'dueros.directive.AudioPlayer.Control',
        'dueros.directive.Display',
        'dueros.directive.Display.media',
        'dueros.directive.Display.tag',
        'dueros.directive.Display.template',
        'dueros.directive.DPL',
        'dueros.directive.DPL.Commands',
        'dueros.directive.Pay',
        'dueros.directive.Permission',
        'dueros.directive.Record',
        'dueros.directive.VideoPlayer',
        'dueros.directive.WebBrowser',
        'dueros.monitor',
        'dueros.monitor.model',
        'dueros.plugins',
    ],
    platforms='py3',
    install_requires=[
        'pycryptodome >= 3.6.6',
        'requests',
	    'pyOpenSSL'
    ]
)
