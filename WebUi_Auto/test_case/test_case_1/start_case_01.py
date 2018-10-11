__author__ = 'dingxinhui'
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# test_case/test_case_1/start_case_01.py

import unittest
from function.function_01 import *
from config.config_01 import browser_config
from picture.picture import *
from selenium import webdriver
import time,os
from config.config_01 import *
from picture.picture1 import *
# 用例
class Case_01(unittest.TestCase):

    '''
    登录
    '''
    def setUp(self):
        # self.driver = browser_config['chrome']
        # driver = self.driver1
        self.imgs = []
        # return driver


    def test_login(self):
        # self.driver = self.driver1
        # driver = self.driver
        # print(driver)


        # page = login("tpacs001","2wsx1qaZ","123456")
        b = login("15814417206", "123456")
        #
        # print("这是res" + b[0] + "这是结尾啊啊啊")
        # print("这是title" + b[1] + "这是结尾啊啊啊")
        self.imgs.append(b[2])

        assert "注销" in b[0]
        # self.assertEqual(u"注销",  b[0])
        # return driver

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()