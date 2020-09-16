# -*- coding: utf-8 -*-
# Intro: Aria2 RPC 调用模块安装文件
# Author: Ztj
# Email: ztj1993@gmail.com

import os.path
import re

from setuptools import setup

f = open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf8')
readme = f.read()
f.close()

f = open(os.path.join(os.path.dirname(__file__), 'ZtjAria2Rpc.py'), encoding='utf8')
version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)
f.close()

setup(
    name='py-ztj-aria2rpc',
    version=version,
    description='python aria2rpc package',
    long_description=readme,
    long_description_content_type='text/markdown',
    py_modules=['ZtjAria2Rpc'],
    url='https://github.com/ztj1993/py-aria2rpc',
    author='ZhangTianJie',
    author_email='ztj1993@gmail.com',
    keywords='aria2 rpc client',
    license='MIT License',
)
