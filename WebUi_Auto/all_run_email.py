__author__ = 'dingxinhui'
# !/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from HTMLTestRunner import HTMLTestRunner
import time
# 处理文件和目录
import os
# 发送邮件
import smtplib
# 导入MIMEText类,实现支持HTML格式的邮件，支持所有HTML格式的元素，包括表格，图片，动画，css样式，表单等
from email.mime.text import MIMEText
# 导入MIMEMultipart,生成包括多个部分的邮件体
from email.mime.multipart import MIMEMultipart
# 导入邮件头
from email.header import Header

# 2.定义：取最新测试报告
def new_file(test_dir):
    # 列举test_dir目录下的所有文件，结果以列表形式返回。
    lists = os.listdir(test_dir)
    # s ort按key的关键字进行排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间
    # 最后对lists元素，按文件修改时间大小从小到大排序。windows系统目录分隔符为'\\'，Mac为'/'
    lists.sort(key=lambda fn: os.path.getmtime(test_dir+'/'+fn))
    # 获取最新文件的绝对路径
    file_path = os.path.join(test_dir, lists[-1])
    print('文件的绝对路径：', file_path)
    return file_path


# 3.定义：发送邮件，发送最新测试报告html
def send_email(newfile):
    # 打开文件
    f = open(newfile, 'rb')
    # 读取文件内容
    mail_body = f.read()
    # 调试使用
    # print u'打印'
    # print mail_body
    # 关闭文件
    f.close()

    # 发送邮箱服务器
    smtpserver = 'smtp.qq.com'
    # 发送邮箱用户名/密码
    user = '发件人邮箱'
    password = '发件人邮箱密码（服务密码）'
    # 发送邮箱
    sender = '发件人邮箱'
    # 多个接收邮箱，单个收件人的话，直接是receiver='XXX@126.com'
    receiver = ['收件人邮箱']
    # 发送邮件主题
    subject = 'web_TestReport'

    # 编写 HTML类型的邮件正文
    # MIMEText这个效果和下方用MIMEMultipart效果是一致的，已通过。
    # msg = MIMEText(mail_body,'html','utf-8')

    msg = MIMEMultipart('mixed')

    # 注意：由于msg_html在msg_plain后面，所以msg_html以附件的形式出现
    # text = "Dear all!\nThe attachment is new testreport.\nPlease check it."
    # 中文测试ok
    # text = "Dear all!\n附件是最新的测试报告。\n麻烦下载下来看，用火狐浏览器打开查看。\n请知悉，谢谢。"
    # msg_plain = MIMEText(text,'plain', 'utf-8')
    # msg.attach(msg_plain)

    msg_html1 = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(msg_html1)

    msg_html = MIMEText(mail_body, 'html', 'utf-8')
    msg_html["Content-Disposition"] = 'attachment; filename="TestReport.html"'
    msg.attach(msg_html)

    # 要加上msg['From']这句话，否则会报554的错误。
    # 要在163有限设置授权码（即客户端的密码）
    msg['From'] = '发件人邮箱'
    #  msg['To'] = 'XXX@doov.com.cn'
    # 多个收件人
    msg['To'] = ";".join(receiver)
    msg['Subject'] = Header(subject, 'utf-8')

    # 连接发送邮件,QQ邮箱需要使用smtplib.SMTP_SSL方法
    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    # smtp.connect(smtpserver, 465)
    smtp.login(user, password)
    # smtp.set_debuglevel(1)
    # smtp.starttls()
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

if __name__=='__main__':
    print('=====AutoTest Start======')
    # 1.执行测试用例，生成最新的测试用例
    # 指定测试用例为当前文件夹下的test_case目录
    # 如果用/可以不用r
    # 获得当前时间的列表
    now1 = time.strftime('%Y-%m-%d')
    now = time.strftime('%Y-%m-%d_%H_%M_%S_')
    test_case_dir = './test_case/test_case_1'
    discover = unittest.defaultTestLoader.discover(test_case_dir, pattern='start_*.py')
    # windows系统目录分隔符为'\\'，Mac为'/'
    test_report_dir = './report'
    report_dir = test_report_dir + '/' + now1
    print("测试报告的路径，带年月日：" + report_dir)
    try:
        if (os.path.exists(report_dir)) :
            print(u"文件已存在")
        else:
            os.mkdir(report_dir)
            # os.chdir(report_dir)
    except Exception as e:
        print(e)

	# windows系统目录分隔符为'\\'，Mac为'/'
    filename = report_dir + '/' + 'web_report_' + now + '.html'
    print(u'测试报告名称：' + filename)
    # 需屏蔽fp中的中文文字说明。
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title=u'LaobaiWeb_TestReport', description=u'Case Results：', verbosity=2, retry=1, save_last_try=False)
    runner.run(discover)
    print(discover)
    # 注意：调用函数一定要加括号
    fp.close()

    # 取最新测试报告
    new_report = new_file(report_dir)
    # 调试用的
    print('最新测试报告名称', new_report)

    # 发送邮件，发送最新测试报告html
    send_email(new_report)
    print("发送邮件~~~~~~~~：", new_report)
    print('=====AutoTest Over======')
