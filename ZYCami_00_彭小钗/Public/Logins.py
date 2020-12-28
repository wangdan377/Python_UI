#!/usr/bin/python
# -*- coding: utf-8 -*-
from PO.Login_Element import Login_Page
from PO.Prime_Element import Prime_Page
import time
from common.loged import Logger

#登录的公共方法(点击登录按钮-用户名-密码-提交)
class LogIn():
    def __init__(self,driver):
        self.driver =  driver
        self.login = Login_Page(self.driver)  # 登录页面元素
        self.prime = Prime_Page(self.driver)  #prime
    def login_01(self):
        '''
        未登录-去登录
        :return:已登录
        '''
        # self.login.click_File_me()
        self.login.click_File_tv_login()
        self.login.input_user(17195453626)
        self.login.input_password('00000000')
        self.login.click_File_tv_commit()

        # self.login.click_File_tv_login()
        # self.login.input_user(17195453626)
        # self.login.input_password('00000000')
        # self.login.click_File_tv_commit()
        # log.logger.error('登录报错')
    def login_02(self):
        '''
        已登录-prime
        :return:已登录
        '''
        self.login.click_File_me()
        self.prime.click_File_prime01() #点击prime
        # log.logger.error('登录报错')
    def login_03(self):
        '''
        未登录-点击登录按钮
        :return:已登录
        '''
        self.login.click_File_me()
        self.login.click_File_tv_login()    #点击登录按钮
        # log.logger.error('登录报错')