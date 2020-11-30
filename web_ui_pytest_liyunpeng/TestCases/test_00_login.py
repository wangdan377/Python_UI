# -*-coding:utf-8-*-
"""
============================
author:chenglei
time:2019/8/8
E-mail:461419962@qq.com
============================
"""
import pytest
from selenium import  webdriver

from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from TestDatas import common_datas as cd
from TestDatas import login_datas as ld
import time
import logging

#测试用例 = 测试对象的功能+测试数据
@pytest.mark.login
@pytest.mark.usefixtures("init_driver")
class TestLogin:
    """登录"""
    @pytest.mark.slow
    @pytest.mark.parametrize("success_datas",ld.success_datas)
    def test_login_success(self,success_datas,init_driver): # fixture的函数名称，作为参数传给测试用例。函数名称=fixture执行后返回值。
        #登录成功
        print("-----------------------------------{}----------------------------------------------".format(success_datas))
        LoginPage(init_driver).login(success_datas["username"], success_datas["passwd"])  # 测试对象+测试数据
        # 断言 - 页面是否存在   我的帐户   元素   元素定位+元素操作
        assert IndexPage(init_driver).check_userName_exists()  # 测试对象+测试数据
        # url跳转
        # assert init_driver.current_url == ld.success["check"]  # 测试对象+测试数据 # # 正常用例 - 登陆+首页


    # @ddt.data(*ld.invalid_datas)
    @pytest.mark.parametrize("user_datas",ld.user_datas)
    def test_login_noUser(self,user_datas,init_driver):
        #用户名错误
        print("-----------------------------------{}----------------------------------------------".format(user_datas))
        lp = LoginPage(init_driver)
        lp.login_noUsername(user_datas["user"])
        time.sleep(2)
        assert lp.get_form_user_error_info() == user_datas["check"]

    @pytest.mark.parametrize("passwd_datas",ld.passwd_datas)
    def test_login_noPasswd(self,passwd_datas,init_driver):
        #密码错误
        print("-----------------------------------{}----------------------------------------------".format(passwd_datas))
        lp = LoginPage(init_driver)
        lp.login(passwd_datas["user"],passwd_datas["password"])
        time.sleep(2)
        assert lp.get_form_passwd_error_info() ==  passwd_datas["check"]


    @pytest.mark.parametrize("userPd_datas",ld.userPd_datas)
    def test_login_userPd(self,userPd_datas,init_driver):
        #用户名或密码错误
        print("-----------------------------------{}----------------------------------------------".format(userPd_datas))
        lp = LoginPage(init_driver)
        lp.login(userPd_datas["user"],userPd_datas["password"])
        time.sleep(3)
        assert lp.get_form_userPd_error_info() == userPd_datas['check']



    # def test_login_noMobile(self,init_driver):
    #     #步骤
    #     lp = LoginPage(init_driver
    #     lp.login("13213123111","python")
    #     assert "此账号没有经过授权，请联系管理员!" == lp.get_page_center_error_info()
    #
    #


if __name__ == '__main__':
    pytest.main()