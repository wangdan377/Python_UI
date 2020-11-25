# -*-coding:utf-8-*-
"""
============================
author:chenglei
time:2019/8/9
E-mail:461419962@qq.com
============================
"""
from selenium.webdriver.common.by import By


class LoginPageLocator:
    # 用户名输入框
    user_loc = (By.XPATH, '//input[@icon = "search user_bg"]')
    # 密码输入框
    passwd_loc = (By.XPATH, '//input[@icon = "search psd_bg"]')
    #登录提交按钮
    login_button_loc=(By.XPATH,'//button[contains (@class,"el-button el-button--primary")]')
    # 用户名表单错误提示
    form_error_user_loc = (By.XPATH, '//i[@class = "el-input__icon el-icon-search user_bg"]//parent::*//following-sibling::div')
    #密码表单错误提示
    form_error_pswd_loc = (By.XPATH, '//i[@class = "el-input__icon el-icon-search psd_bg"]//parent::*//following-sibling::div')
    #用户名或密码错误
    form_errr_userPd_loc = (By.XPATH,'//span[@class = "errTip"]')

    # 页面中间错误提示
    # page_center_loc = (By.XPATH, '//div[@class = "layui-layer-content"]')
