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

        
    }
}
