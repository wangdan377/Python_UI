#!/usr/bin/python
# -*- coding: utf-8 -*-
from ddt import ddt,data,unpack
from Public.Function import *
from Public import Caplictily
from PO.login_element import Login_Page
from Data.data import *
# from common import loged
import unittest,pytest
import time,os,sys
import warnings
import HTMLTestRunnerCN3_pie_chart_screen

"""@ddt  #装饰器类         # ddt与classmethod不能连用
class Test_Login(unittest.TestCase):

    #初始化，使用装饰器，这样在用例执行前只初始化一次
    @classmethod
    def setUpClass(self):
        warnings.simplefilter("ignore", ResourceWarning)
        # cls.driver = appium_desired()     #之前的方法
        # cls.driver.start_activity(appPackage,appActivity)     #另外一种启动方式
        #实例化类
        # self.fun = BaseFun(self.driver)
        driver = Caplictily.Driver_Config()
        self.driver = driver.get_driver()
        self.login = Login_Page(self.driver)
        self.fun = BaseFun(self.driver)

    # 关闭驱动
    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    @data(*get_log_data())      #装饰测试方法，拿到几个数据就可以执行用例
    @unpack                     #根据拿到的数据以都好及逆行拆分
    @pytest.mark.flaky(rerus=2)
    def test_login(self,username,password):
      

        self.login.click_File_me()
        self.login.click_File_tv_login()
        self.login.input_user(username)
        self.login.input_password(password)
        self.login.click_File_tv_commit()"""

#出不来测试报告
@ddt  # 装饰器类
class Test_Login(unittest.TestCase):

    # 初始化，使用装饰器，这样在用例执行前只初始化一次
    @classmethod
    def setUpClass(self):
        warnings.simplefilter("ignore", ResourceWarning)
        # cls.driver = appium_desired()     #之前的方法
        # cls.driver.start_activity(appPackage,appActivity)     #另外一种启动方式
        # 实例化类
        # self.fun = BaseFun(self.driver)
        driver = Caplictily.Driver_Config()
        self.driver = driver.get_driver()
        self.login = Login_Page(self.driver)
        self.fun = BaseFun(self.driver)



    @data(*get_log_data())  # 装饰测试方法，拿到几个数据就可以执行用例
    @unpack  # 根据拿到的数据以都好及逆行拆分
    @pytest.mark.flaky(rerus=1)
    def test_login(self, username, password):
        self.login.click_File_me()
        self.login.click_File_tv_login()
        self.login.input_user(username)
        self.login.input_password(password)
        time.sleep(2)
        self.login.click_File_tv_commit()

    # 关闭驱动
    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(Test_Login("test_login"))
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
    fp.close()