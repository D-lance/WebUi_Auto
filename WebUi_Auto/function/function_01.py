__author__ = 'dingxinhui'
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# function/function_01.py
# 业务功能脚本（用例脚本可调用此处的功能脚本）

from encapsulation.encapsulation import UIHandle
from constant.constant_1 import LOGIN_URL
import config.login_config
from config.config_01 import browser_config
from picture.picture1 import *
import time

def login(username,password):

    # 打开浏览器
    driver = browser_config['chrome']
    # print(driver)
    # driver.maximize_window()
    print(driver.get_window_size())
    driver.set_window_size(1200,800)
    print(driver.get_window_size())

    driver.implicitly_wait(30)
    # 脚本运行时，错误的信息将被打印到这个列表中
    driver.verificationErrors = []
    # #是否继续接受下一下警告
    driver.accept_next_alert = True
    # 传入driver对象
    uihandle = UIHandle(driver)
    # 输入url地址
    uihandle.get(LOGIN_URL)
    uihandle.Click("老白首页", "首页登录按钮")
    time.sleep(3)
    uihandle.Clear('老白首页', '用户名')
    uihandle.Input('老白首页', '用户名', username)
    uihandle.Input('老白首页', '密码', password)
    uihandle.Click('老白首页', '登录页面登录按钮')
    time.sleep(3)

    res = driver.page_source
    title = driver.title
    img = get_screenshot(driver)

    a = [res, title, img]

    return a


