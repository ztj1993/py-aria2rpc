# -*- coding: utf-8 -*-
# Intro: Aria2 RPC 调用模块安装文件
# Author: Ztj
# Email: ztj1993@gmail.com

import pathlib

from setuptools import setup

here = pathlib.Path(__file__).parent.resolve()
readme = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='py-ztj-aria2rpc',
    version='0.0.4',
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
