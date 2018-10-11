__author__ = 'dingxinhui'
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# encapsulation/encapsulation.py

# 封装部分维护在此
import os, time
import yaml
from config.config_01 import locat_config
from log.log import Logger
from selenium.webdriver.support.wait import WebDriverWait
from picture.picture import insert_img
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image, ImageDraw

'''
绝对路径
'''
# f = open(r"D:\study\selenium\web_laobai_new\config\element_data.yml", encoding='utf-8')
'''
跑一条用例时路径配置，如case_01，当前路径为*/web_laobai_new/test_case/test_case_1/*
'''
# f = open(os.path.abspath('../../config/element_data.yml'), encoding='utf-8')
'''
跑多条用例时路径配置，如all_run,当前路径为*/web_laobai_new/*
'''
f = open(os.path.abspath('./config/element_data.yml'), encoding='utf-8')

element_data = yaml.load(f)
# print(element_data)

class UIHandle():
    logger = Logger()

    # 构造方法，用来接收selenium的driver对象
    @classmethod
    def __init__(cls, driver):
        cls.driver = driver

    # 输入地址
    @classmethod
    def get(cls, url):
        cls.logger.loginfo(url)
        cls.driver.get(url)

    # 关闭浏览器驱动
    @classmethod
    def quit(cls):
        cls.driver.quit()

    # element对象（还可加入try，截图等。。。）
    @classmethod
    def element(cls, page, element):
        # 加入日志
        cls.logger.loginfo(page)
        # 加入隐性等待
        # 此处便可以传入config_o1中的dict定位参数

        try:

            # 此配置为读取Py文件
            # el = WebDriverWait(cls.driver, 30).until(EC.presence_of_element_located(locat_config[page][element]))

            # 此配置为读取yaml文件
            el = WebDriverWait(cls.driver, 30).until(EC.presence_of_element_located(element_data[page][element]))
            #  加入日志
            cls.logger.loginfo(page + "-" + element+'  is OK')
            print("页面‘" + page + "’和元素‘" + element + "’ was found")
            return el
        except:
            print("元素没有找到")
            return insert_img(cls.driver, '找不到元素.png')
            # 加入日志
            cls.logger.logdebug("element 没找到")
            # cls.CatchLogger.logError("element 没找到")


    def elements(cls, page, element):
        # 加入日志
        cls.logger.loginfo(page)
        # 加入隐性等待
        WebDriverWait(cls.driver, 10)
        els = cls.driver.find_elements(*element_data[page][element])
        # 注意返回的是list
        return els

    # send_keys方法
    @classmethod
    def Input(cls, page, element, msg):
        el = cls.element(page, element)
        locations = el.location
        sizes = el.size
        rangle = (int(locations['x']), int(locations['y']), int(locations['x'] + sizes['width']),
                  int(locations['y'] + sizes['height']))

        now = time.strftime('%Y-%m-%d')
        path = os.path.abspath('./picture/photo')
        # windows系统目录分隔符为'\\'，Mac为'/'
        setpath = path + '/' + now
        try:
            if (os.path.exists(setpath)):
                print(u"文件已存在")
            else:
                # windows系统目录分隔符为'\\'，Mac为'/'
                os.mkdir(path + '/' + now)
        except Exception as e:
            print(e)

        now1 = time.strftime('%Y-%m-%d_%H_%M_%S_')
        # windows系统目录分隔符为'\\'，Mac为'/'
        file_path = setpath + '/' + 'picture_' + now1

        a = setpath + ".png"
        a1 = file_path + element + ".png"
        cls.driver.save_screenshot(a)
        img01 = Image.open(a)
        b = ImageDraw.Draw(img01)
        b.arc(rangle, 0, 360, fill=(255, 0, 0))
        # b.ellipse(rangle, fill=(0, 0, 255))
        img01.save(a1)
        time.sleep(2)

        el.send_keys(msg)

    # click方法
    @classmethod
    def Click(cls, page, element):
        el = cls.element(page, element)
        locations = el.location
        sizes = el.size
        rangle = (int(locations['x']), int(locations['y']), int(locations['x'] + sizes['width']),
                  int(locations['y'] + sizes['height']))

        now = time.strftime('%Y-%m-%d')
        path = os.path.abspath('./picture/photo')
        # windows系统目录分隔符为'\\'，Mac为'/'
        setpath = path + '/' + now
        try:
            if (os.path.exists(setpath)):
                print(u"文件已存在")
            else:
                # windows系统目录分隔符为'\\'，Mac为'/'
                os.mkdir(path + '/' + now)
        except Exception as e:
            print(e)

        now1 = time.strftime('%Y-%m-%d_%H_%M_%S_')
        # windows系统目录分隔符为'\\'，Mac为'/'
        file_path = setpath + '/' + 'picture_' + now1

        a = setpath + ".png"
        a1 = file_path + element + ".png"
        cls.driver.save_screenshot(a)
        img01 = Image.open(a)
        b = ImageDraw.Draw(img01)
        b.arc(rangle, 0, 360, fill=(255, 0, 0))
        # b.ellipse(rangle, fill=(0, 0, 255))
        img01.save(a1)
        time.sleep(2)

        el.click()

    # clear方法
    @classmethod
    def Clear(cls, page, element):
        el = cls.element(page, element)
        el.clear()

    @classmethod
    def swipe(self, st, sy, ex, ey):
        """
        滑动
        分别为:起始点x,y。结束点x,y。与滑动速度。滑动默认800
        """
        return self.driver.swipe(st, sy, ex, ey, duration=1000)

    @classmethod
    def get_window_size(self):
        """
        获取屏幕分辨率
        {u'width': 1080, u'height': 1920}
        :return: 1080,1920
        """

        screen_size = self.driver.get_window_size()
        width = screen_size['width']
        height = screen_size['height']
        return width, height

    @classmethod
    def switch_to_window(self, window_num):
        """
        切换页签
        """
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[window_num])

    # @classmethod
    # def screen_shot(self, window_num):
    #     """
    #     切换页签
    #     """
    #     screenshot = self.save_screenshot()


    @classmethod
    def setUp(self):
       self.imgs = []
       self.addCleanup(self.cleanup)
