__author__ = 'dingxinhui'
# -*-coding:utf-8-*-
import os, time
# 截图函数
def insert_img(driver,file_name):
    # 获得当前时间的列表  年月日
    now = time.strftime('%Y-%m-%d')
    # 定义截图路径，根据自己的环境配置， windows系统目录分隔符为'\\'，Mac为'/'
    # path = r'D:\study\appium\appium_case\web_laobai\picture\photo'
    '''
    跑一条用例时路径配置，如case_01，当前路径为*/web_laobai_new/test_case/test_case_1/*
    '''
    # path = os.path.abspath('../../picture/photo')

    '''
    跑多条用例时路径配置，如all_run,当前路径为*/web_laobai_new/*
    '''
    path = os.path.abspath('./picture/photo')
    print(path)
    setpath = path+'\\'+now
    print(setpath)
    try:
        if(os.path.exists(setpath)):
            print(u"文件已存在")
        else:
            os.mkdir(path+'\\'+now)
            # os.chdir(path+'\\'+now)
    except Exception as e:
        print(e)

    now2 = time.strftime('%Y-%m-%d_%H_%M_%S_')
    file_path = setpath + '\\' + 'picture_' + now2 + file_name
    driver.get_screenshot_as_file(file_path)
