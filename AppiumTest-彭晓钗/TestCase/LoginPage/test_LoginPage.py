#coding:utf-8

# from selenium.webdriver.support.wait import WebDriverWait
# import appium
from Public.Base_Function import *
from Public.Desired_Capabilities import *
import unittest
import HtmlTestRunner
from Page.Login_Page import *
from Page.My_Page import *
from Page.Setting_Page import *
from Page.Home_Page import *
from Public import Read_Excel
import sys
from Public.Common_Function import *



#获取excel表格中的测试用例数据
excel_path = "../Data/Automation.xlsx"
sheet_name = "Sheet1"
test_data = Read_Excel.Excel_Data(excel_path, sheet_name).dict_data()
# 定义一个字典存放数据
data = dict()
driver = desired_cap()


class LoginPage_test(unittest.TestCase):
    #邮件登录
    def email_login(self, username, password):
        #点击我图标
        self.function.click(my_icon)
        #点击登录按钮
        self.function.click(login_btn)
        #判断是否在登录页面
        self.assertTrue(self.function.elementIsExist(register_btn))
        #点击邮箱登录链接
        self.function.click(email_login)
        #输入用户名
        self.function.send_keys(email_text, username)
        #输入密码
        self.function.send_keys(password_text, password)
        #点击登录按钮
        self.function.click(login_btn)

    # @getImage
    #1.正常登录，正确用户名，密码
    def test_01_login_correct_usr_psd(self):
        #获取当前测试用例名称
        case_name = sys._getframe().f_code.co_name
        #获取当前测试用例的数据
        data = self.function.get_expected_data(test_data, "TestCaseName", case_name)
        #使用邮件账号登录
        self.email_login(data["username"], data["password"])
        #判断是否登录成功，是否有ZHIYUN Prime标志
        self.assertTrue(self.function.elementIsExist(zhiyun_prime_banner))
        #点击设置按钮并退出登录
        self.function.click(setting_btn)
        self.function.click(logout_btn)
        self.function.click(confirm_btn)
        try:
            self.function.click(back_btn)
        except:
            pass

    # @getImage
    # 2.登录失败，正确用户名，错误密码
    def test_02_login_correct_usr_incorrect_psd(self):

        # 获取当前测试用例名称
        case_name = sys._getframe().f_code.co_name
        # 获取当前测试用例的数据
        data = self.function.get_expected_data(test_data, "TestCaseName", case_name)
        #使用邮件账号登录
        self.email_login(data["username"], data["password"])
        #验证是否有账号或者密码错误信息弹出
        # self.assertTrue(self.function.elementIsExist(user_psw_incorect_tex))
        try:
            self.assertFalse(self.function.elementIsExist(user_psw_incorect_tex), msg="账号或者密码错误信息框弹出")
            # self.assertTrue(self.function.elementIsExist(user_psw_incorect_tex), msg="账号或者密码错误信息框弹出")
        except Exception as msg:
            self.function.get_screenshot(case_name, msg)





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
    report_path = "../Report"
    # 获取系统时间，生成唯一报告
    # sys_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # 实例化测试用例，执行所有的测试用例
    # suit = all_case()
    suit = unittest.TestSuite()
    suit.addTest(LoginPage_test("test_me_loginbtn"))

    # 定义输出报告
    runner = HtmlTestRunner.HTMLTestRunner(output=report_path, report_title="自动化测试报告", descriptions="测试用例执行情况",
                                           report_name='report', combine_reports=True)
    # 执行用例
    runner.run(suit)

