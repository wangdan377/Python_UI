#!/usr/bin/python
# -*- coding: utf-8 -*-


from Public.Base_Function import *
from Public.Desired_Capabilities import *
import unittest
import HtmlTestRunner
import os
from Page.Home_Page import *
from Page.Login_Page import *
from Page.My_Page import *
from Page.Setting_Page import *
from ddt import ddt, data, unpack, file_data
from Public import Read_Excel

excel_path = "E:\\AppiumTest\\Data\\Automation.xlsx"
sheet_name = "Sheet1"
test_data = Read_Excel.Excel_Data(excel_path, sheet_name).dict_data()
print(test_data)


@ddt
class HomePage_test(unittest.TestCase):
    @data(*test_data)
    @unpack
    #1.点击“我”->登录按钮
    def test_me_loginbtn(self, username, password):
    # def test_me_loginbtn(self):
        time.sleep(2)
        self.function.click(my_icon)
        time.sleep(2)
        self.function.click(login_btn)
        time.sleep(2)
        self.assertTrue(self.function.elementIsExist(register_btn))
        time.sleep(2)
        self.function.click(email_login)
        time.sleep(2)
        # self.function.send_keys(email_text, "fredpeng1@163.com")
        # self.function.send_keys(password_text, "123456zhi")
        self.function.send_keys(email_text, username)
        time.sleep(2)
        self.function.send_keys(password_text, password)
        time.sleep(2)
        # self.function.set_vale(email_text, username)
        # self.function.set_vale(password_text, password)
        self.function.click(login_btn)
        time.sleep(2)
        self.assertTrue(self.function.elementIsExist(zhiyun_prime_banner))
        time.sleep(2)
        self.function.click(my_icon)
        time.sleep(2)
        self.function.click(setting_btn)
        self.function.click(logout_btn)
        self.function.click(confirm_btn)
        # self.function.click(back_btn)


    # # 1.点击“我”->登录按钮
    # def test_me(self):
    #     self.function.click(my_icon)
    #     time.sleep(1)

    #1.初始化，使用装饰器，在用例执行前只初始化一次
    @classmethod
    def setUpClass(cls):
        cls.driver = desired_cap()
        time.sleep(10)
        #实例化类
        cls.function = Base_Function(cls.driver)


    #2.关闭驱动
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    # unittest.main()
    # 定义报告存放的位置
    report_path = "E:\\AppiumTest\\Report"
    # 获取系统时间，生成唯一报告
    # sys_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # 实例化测试用例，执行所有的测试用例
    # suit = all_case()
    suit = unittest.TestSuite()
    suit.addTest(HomePage_test("test_me_loginbtn"))

    # 定义输出报告
    runner = HtmlTestRunner.HTMLTestRunner(output=report_path, report_title="自动化测试报告", descriptions="测试用例执行情况",
                                           report_name='report', combine_reports=True)
    # 执行用例
    runner.run(suit)
