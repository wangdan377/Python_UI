#!/usr/bin/python
# -*- coding: utf-8 -*-
from Public.Function import *
from Public import Caplictily
from Public.Logins import LogIn
from PO.Login_Element import Login_Page
from PO.Publish_Element import Publish_Page
from PO.Me_Element import Me_Page
from PO.Upload_Work_Element import Upload_Work_Page
from Public.Publish import Publish
from Public.Me import Me
from Public.Upload_Work import Upload_Work
import unittest,pytest
import time,os,sys
import warnings
from common.loged import Logger
import pytest
from common import HTMLTestRunnerCN3_pie_chart_screen


class Test_Upload_Work(unittest.TestCase):
    #初始化，使用装饰器，这样在用例执行前只初始化一次
    @classmethod
    def setUpClass(self):
        warnings.simplefilter("ignore", ResourceWarning)
        driver = Caplictily.Driver_Config()
        self.driver = driver.get_driver()
        self.login = Login_Page(self.driver)    #登录
        self.publish = Publish_Page(self.driver) #发布
        self.me = Me_Page(self.driver)  # 我
        self.upload_work = Upload_Work_Page(self.driver) #上传作品
        self.fun = BaseFun(self.driver)
        self.logins = LogIn(self.driver)
        self.publish_fun = Publish(self.driver)
        self.me_fun = Me(self.driver)
        self.upload_work_fun = Upload_Work(self.driver)

    # 关闭驱动
    @classmethod
    def tearDownClass(self):
        self.driver.quit()


    #测试编辑器中上传作品的功能
    def test_upload_work_001(self):
        #点击我的
        self.login.click_File_me()
        time.sleep(1)
        flag = self.fun.is_element_exist(self.login.File_tv_login)
        #未登录，则先登录，否则是已登录状态
        if flag:
            self.logins.login_01()

        #导航到上传作品页面
        self.upload_work_fun.to_upload_work_page()
        #上传作品页面-选择第一个视频
        self.upload_work_fun.select_works()
        # 在发布页面输入视频描述信息
        self.publish_fun.input_introduction()
        # 添加标签
        self.publish_fun.add_tag()
        # 在发布页面点击发布按钮
        self.publish.click_File_publish_btn()
        # 验证发布视频成功信息是否出现
        self.assertTrue(self.me_fun.vefify_publish_success_msg(), msg="发布视频成功信息没有出现，请检查！")
        time.sleep(20)

# 构建测试套件
"""def Suit():
    suite = unittest.TestSuite()
    # AddTest是要测试的类名，test_01是要执行的测试方法
    suite.addTest(Test_Prime_pay("test_prime_pay01"))
    suite.addTest(Test_Prime_pay("test_prime_pay02"))
    suite.addTest(Test_Prime_pay("test_prime_pay03"))
    return suite"""
if __name__ == '__main__':
    unittest.main()
    """suite = unittest.TestSuite()
    suite.addTest(Test_Prime_pay("test_prime_pay01"))
    soundbox_device = 'XYBK01011204300001'
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    ##将当前时间加入到报告文件名称中，定义测试报告存放路径
    filename = '../report/' + now + 'result.html'  # 第一种方法,相对路径下
    fp = open(filename, 'wb')
    runner = HTMLTestRunnerCN3_pie_chart_screen.HTMLTestRunner(stream=fp, title='测试报告', tester='王丹',
                                                               device=(soundbox_device),
                                                               description='用例执行情况:')
    runner.run(suite)
    # runner.run(Suit())
    fp.close()"""



