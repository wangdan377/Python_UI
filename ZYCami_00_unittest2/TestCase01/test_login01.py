
#!/usr/bin/python
# -*- coding: utf-8 -*-
from ddt import ddt,data,unpack
from Public.Function import *
from Public import Caplictily
from PO.login import *
from PO.login_Element import Login_Page
from Data.data import *
from common.loged import *
import unittest,pytest
import time,os,sys
import warnings
import HTMLTestRunnerCN3_pie_chart_screen


#最开始的方法，可以出报告，可以用
class Test_Login_01(unittest.TestCase):

    #初始化，使用装饰器，这样在用例执行前只初始化一次
    @classmethod
    def setUpClass(cls):
        warnings.simplefilter("ignore", ResourceWarning)
        # cls.driver = appium_desired()     #之前的方法
        # cls.driver.start_activity(appPackage,appActivity)     #另外一种启动方式
        #实例化类
        # self.fun = BaseFun(self.driver)
        driver = Caplictily.Driver_Config()
        cls.driver = driver.get_driver()
        cls.fun = BaseFun(cls.driver)
        # cls.login = Login_Page(cls.driver)
        # driver = Caplictily.Driver_Config()
        # self.driver = driver.get_driver()
        # self.login = Login_page(self.driver)
        # self.fun = BaseFun(self.driver)
        # 关闭驱动
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_01(self):        #封裝*的問題
        """self.login.click_File_me()
        self.login.click_File_tv_login()
        time.sleep(2)
        self.fun.send_keys(File_et_name,username)
        time.sleep(2)
        # self.driver.find_element_by_id("com.zhiyun.cama:id/et_name").send_keys("17195453626")
        self.fun.send_keys(File_et_pass,password)
        time.sleep(2)
        # self.driver.find_element_by_id("com.zhiyun.cama:id/et_pass").send_keys("00000000")
        self.login.click_File_tv_commit()
        time.sleep(2)"""


        #之前的老办法
        time.sleep(2)
        self.fun.click(File_me)
        time.sleep(2)
        self.fun.click(File_tv_login)
        time.sleep(2)
        self.fun.send_keys(File_et_name, username)
        time.sleep(2)
        self.fun.send_keys(File_et_pass, password)
        time.sleep(2)
if __name__ == '__main__':
    unittest.main()

    suite = unittest.TestSuite()
    suite.addTest(Test_Login_01("test_login_01"))
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

