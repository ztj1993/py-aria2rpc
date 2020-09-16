# -*- coding: utf-8 -*-
# Intro: Aria2 RPC 调用模块
# Author: Ztj
# Email: ztj1993@gmail.com

import unittest
import warnings

from ZtjAria2Rpc import Aria2Rpc

uri = 'http://127.0.0.1:6800/rpc'


class TestAria2Rpc(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)

    def test_version(self):
        """测试初始化"""
        rpc = Aria2Rpc(uri)
        self.assertTrue('version' in rpc.get_version())


if __name__ == '__main__':
    unittest.main()
