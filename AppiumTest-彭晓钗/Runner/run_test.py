#coding:utf-8

import unittest
import os
import HtmlTestRunner
from TestCase.LoginPage.test_LoginPage import LoginPage_test
from Public import Common_Function



def all_case():
    #指定测试用例的路径
    case_path = "../TestCase"
    #创建测试套件
    suit = unittest.TestSuite()
    '''用discover方法查找出目录下要执行的测试用例脚本
    discover方法有3个参数
    case_dir:测试用例所在目录
    pattern:匹配脚本名称，如：test*.py,匹配所有以test开头的脚本
    top_level_dir:顶级目录的名称，一般默认为None    
    '''
    discover = unittest.defaultTestLoader.discover(case_path, pattern='test*.py', top_level_dir=None)
    #用discover筛选出来的用例循环添加到测试套件中
    for casef_file in discover:
        for case in casef_file:
            suit.addTest(case)
    #返回所有的测试用例
    return suit

if __name__ == '__main__':
    # for i in range(3):
    #定义报告存放的位置
    report_path = "E:\\AppiumTest\\Report"
    #获取系统时间，生成唯一报告
    # sys_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #实例化测试用例，执行所有的测试用例
    # suit = all_case()
    suit = unittest.TestSuite()
    # suit.addTest(LoginPage_test("test_01_login_correct_usr_psd"))
    suit.addTest(LoginPage_test("test_02_login_correct_usr_incorrect_psd"))

    #定义输出报告
    runner = HtmlTestRunner.HTMLTestRunner(output=report_path, report_title="自动化测试报告", descriptions="测试用例执行情况", report_name='report', combine_reports=True)
    #执行用例
    runner.run(suit)

    # #获取最新文件
    # file_new = Common_Function.get_newest_report(report_path)
    # #发送邮件
    # Common_Function.send_email(file_new)
    # print(os.getcwd())
    # print(os.path.dirname(os.getcwd())+"\ScreenShot")