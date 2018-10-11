__author__ = 'dingxinhui'
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# config/config_01.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import selenium.webdriver.remote.webdriver
from selenium.webdriver.common.action_chains import *
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver



# config配置部分

# 浏览器种类维护在此处
# 此配置为远程chrome，需启动java -jar selenium-server-standalone-3.13.0.jar
# browser_config = {
#     'chrome': webdriver.Remote(command_executor='http://10.10.20.179:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
# }
# 此配置项为本机chrome
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--display-gpu")
# chrome_options.add_argument("--no-sandbox")

# config配置部分

# 浏览器种类维护在此处
# 此配置为远程chrome，需启动java -jar selenium-server-standalone-3.13.0.jar
browser_config = {
    'chrome': webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
}
# 此配置项为本机chrome
# browser_config = {
#     'chrome': webdriver.Chrome
# }

#定位信息维护在此处，维护结构由外到内为：页面名称--页面下元素名称--元素的定位方式+参数
locat_config = {
    '老白首页': {
        '个人信息': ['link', '技术部测试账号，打扰请见谅'],
        '注销': ['link', '注销'],
        '全部商品分类': ['xpath', '//a[contains(text(),"全部商品分类")]'],
        '首页': ['link', '首页'],
        '医药馆': ['xpath', '//a[contains(text(),"医药馆")]'],
        '保健品': ['xpath', '(//a[contains(text(),"保健品")])[2]'],
        '医疗器械': ['xpath', '//a[contains(@href, "/module?type=ylqx")]'],
        '隐形眼镜': ['xpath', '(//a[contains(text(),"隐形眼镜")])[2]'],
        '计生用品': ['xpath', '//a[contains(@href, "/module?type=jsyp")]'],
        '登录': ['xpath', '//div[4]/button'],
        '搜索输入框': ['css', 'input[type=\"text\"]'],
        '搜索按钮': ['css', 'a[class="searchCli"]'],

        '个人中心': ['css', 'a>p'],
        '家庭医生': ['css', 'li.indexTwo>a>i'],
        '老白快报': ['css', 'li.indexFive>a>i'],
        '常用药': ['css', 'li.indexFour>a>i'],
        '极速达': ['css', 'li.indexThree>a>i'],
        '隐形眼镜1': ['css', 'li.indexSix>a>i'],
        '关闭家庭医生': ['css', 'div.close'],
        '用户中心': ['css', 'a[title="用户中心"]'],
        '我的购物车': ['css', 'a[title="我的购物车"]'],
        '在线客服': ['css', 'a[title="在线客服"]'],
        '输入字符': ['css', 'textarea'],
        '发送字符': ['css', 'div.chat-view-submit'],
        '关闭在线客服': ['xpath', '//*[@class="ntalk-button-close"]'],


        # 购物流程
        '第一个商品': ['css', 'div.text'],
        '加入购物车': ['css', 'div.orange.btn'],
        '去结算': ['css', 'a.deleteCancel'],
        '提交订单': ['xpath', '//*[@class="submitOrderBtn"]'],
        # 我的订单
        '我的订单': ['css', 'a.jump'],
        '待付款': ['xpath', '(//a[contains(@href,"/order?type=1&page=1")])[2]'],
        '待发货': ['xpath', '(//a[contains(@href,"/order?type=2&page=1")])[2]'],
        '待收货': ['xpath', '(//a[contains(@href,"/order?type=3&page=1")])[2]'],
        '待评价': ['xpath', '(//a[contains(@href,"/order?type=4&page=1")])[2]'],
        # 订单管理
        '信息概要': ['xpath', '//a[@id="section1"]/span'],
        '我的评价': ['xpath', '//a[@id="section3"]/span'],
        # 应用管理
        '我的优惠券': ['xpath', '//a[@id="section4"]/span'],
        '健康豆兑换优惠券': ['xpath', '//a[@id="section5"]/span'],
        '免费领取优惠券': ['xpath', '(//a[@id="section5"]/span)[2]'],
        '我的健康豆': ['xpath', '//a[@id="section7"]/span'],
        '我的余额': ['xpath', '//a[@id="A1"]/span'],
        # 账户信息
        '我的资料': ['xpath', '//a[@id="section8"]/span'],
        '修改密码': ['xpath', '//a[@id="section10"]/span'],
        '收货地址管理': ['xpath', '//a[@id="section11"]/span'],
        '系统消息': ['xpath', '//a[@id="section12"]/span'],
        '我的收藏夹': ['xpath', '//a[@id="section13"]/span'],
        # 我的老白
        '我的老白': ['xpath', '(//a[contains(@href,"/user/")])[2]'],
        # 签到
        '签到': ['css', 'a.bth'],
        '确定': ['css', 'div.deleteConfirm'],




        '截图': ['', 'file_name']

    }
}