#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest
from tools.times import sleep
from page_object.loginpage import LoginPage
import allure, os
from page import Caplictily


# @allure.feature("测试登录页")
# class TestLogin:
#     """测试登录"""
#
#     def setup_class(self):
#         '''启动，并进入相机页面'''
#         driver = Caplictily.Driver_Config()
#         self.driver = driver.get_driver()
#         self.login = LoginPage(self.driver)
#
#
#     @pytest.mark.parametrize("name,pwd", [('16714056631', '00000000')])
#     @allure.story("登录成功")
#     @allure.title("登录成功")
#     def test_login_success(self, name, pwd):
#
#         self.login.me()
#         print("tset")
#         self.login.logins()
#         self.login.username(name)
#         self.login.password(pwd)
#         self.login.submit()
#
#     sleep(3)
#     def tearDownClass(self):
#         self.driver.quit()


@allure.feature("测试登录页")
class TestLogin:
    """测试登录"""



    @pytest.mark.skip(reason="跳过执行这条case")
    @allure.story("进入登录页")
    @allure.title("进入登录页")
    def test_login_success_01(self, get_driver):
        login_page = LoginPage(get_driver)
        login_page.click_me()

    @pytest.mark.skip(reason="跳过执行这条case")
    @pytest.mark.parametrize("username,password", [('167', '0000'), ('167', '00100'), ('16714056631', '00000000')])
    @allure.story("登录成功")
    @allure.title("登录成功")
    def test_login_success_02(self, get_driver, username, password):
        login_page = LoginPage(get_driver)
        if username == '16714056631':
            assert login_page.login_test_lists(username, password, '登录成功') == '登录成功'
        else:
            assert login_page.login_test_lists(username, password, '账号或密码错误') == '账号或密码错误'

if __name__ == '__main__':
    pytest.main(["-s", "test_02_test_login.py"])
    # # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
    # pytest.main(['--alluredir', '../report/result',r'test_02_test_login.py'])
    # # # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    # os.system('allure generate ../report/result -o ../report/html --clean')
    # # pytest.main(['--clean-alluredir', '--alluredir', './report/result'])
    # # os.system('allure generate ./report/result -o ./report/html --clean')
