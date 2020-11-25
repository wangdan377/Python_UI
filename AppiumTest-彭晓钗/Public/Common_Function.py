#coding:utf-8
'''
操作元素以外的一些方法，如发送邮件
'''

import smtplib
import os
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from functools import wraps

#发送自动化测试报告邮件
#file_new：最新的测试报告
def send_email(file_new):
    #邮件服务器
    smtp_server = 'smtp.163.com'
    #发件箱用户名
    sender = 'fredpeng1@163.com'
    #发件箱密码
    pwd = 'WNQKVXAUWOLSDFLT'
    #邮件主题
    mail_title = "自动化测试报告"
    #收件人
    msg_to = ["352898598@qq.com", "fredpeng1@163.com", "fredpeng1@sina.com"]

    #读取文件
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    #邮件正文
    body = MIMEText(mail_body, 'html', 'utf-8')
    msg = MIMEMultipart()

    #邮件主题
    msg['subject'] = Header(mail_title, 'utf-8').encode()
    msg['from'] = sender
    msg['to'] = ','.join(msg_to)
    msg.attach(body)

    #附件
    att = MIMEText(mail_body, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="test_report.html"'
    msg.attach(att)

    #发送邮件
    try:
        #创建连接
        s = smtplib.SMTP()
        #连接服务器
        s.connect(smtp_server)
        #登录服务器
        s.login(sender, pwd)
        #填入邮件相关信息并发送
        s.sendmail(sender, msg['To'].split(","), msg.as_string())
        print('邮件发送成功！')
    except:
        print('邮件发送失败，请检查！！！')

#获取最新的自动化测试报告
def get_newest_report(test_report):
    #列出目录下的所有文件和文件夹保存到lists
    lists = os.listdir(test_report)
    #按时间排序
    lists.sort(key=lambda fn: os.path.getmtime(test_report+"\\"+fn))
    #将最新的文件保存到file_new
    file_new = os.path.join(test_report, lists[-1])
    print(file_new)
    return file_new



# #装饰器，用例失败后截图
# def getImage(function):
#     @wraps(function)
#     def get_ErrImage(self, *args, **kwargs):
#         try:
#             result = function(self, *args, **kwargs)
#         except:
#             timestr = time.strftime("%Y-%m-%d_%H_%M_%S")
#             self.driver.get_screenshot_as_file("./ScreenShot"+"screenshot"+timestr+".png")
#         return result
#     return get_ErrImage



if __name__ == '__main__':
    test_path = "E:\\AppiumTest\\Report"
    file_view = new_rep.new_report(test_path)
    test = send_mail(file_view)
