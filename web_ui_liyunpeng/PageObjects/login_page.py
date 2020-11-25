# -*-coding:utf-8-*-
"""
============================
author:chenglei
time:2019/8/8
E-mail:461419962@qq.com
============================
"""

from Common.basepage import BasePage
from PageLocators.loginPage_locator import LoginPageLocator as loc
import time

class LoginPage(BasePage):
    """登录页面"""
    # phone = '13760495929'
    # code = '123456'
    def login(self,username,passwd):
        self.input_text(loc.user_loc,username,"登录页面_输入账户")
        # time.sleep(2)
        self.input_text(loc.passwd_loc,passwd,"登录页面_输入密码")
        # time.sleep(2)
        self.click_element(loc.login_button_loc,"登录页面_点击登录按钮")
        # time.sleep(5)

    #输入账户错误
    def login_noUsername(self, username):
        self.input_text(loc.user_loc, username, "登录页面_输入账号")
        self.click_element(loc.login_button_loc, "登录页面_点击登录")

    #获取账户错误提示信息
    def get_form_user_error_info(self):
        return self.get_text(loc.form_error_user_loc,"登录页面_获取登录表单账户错误提示信息")

    #获取密码错误提示信息
    def get_form_passwd_error_info(self):
        return self.get_text(loc.form_error_pswd_loc, "登录页面_获取登录表单密码错误提示信息")

    #获取账户或密码错误信息
    def get_form_userPd_error_info(self):
        return self.get_text(loc.form_errr_userPd_loc,"登录页面_后去账户或密码错误提示信息")

    # #获取元素中间弹框报错信息
    # def get_page_center_error_info(self):
    #     return self.get_text(loc.page_center_loc,"登录页面_获取页面中间的错误提示信息")
    #
    #
    #
    #




if __name__ == '__main__':
    LoginPage().get_form_user_error_info()


















