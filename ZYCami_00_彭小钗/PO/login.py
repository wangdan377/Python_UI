#!/usr/bin/python
# -*- coding: utf-8 -*-
from appium.webdriver.common import mobileby
from PO.Base_page import Base_Page
from selenium.webdriver.common.by import By
import os,time

#原有的第一种方法
username = '17195453626'
password = '00000000'
#我的按钮
File_me= (By.XPATH,'//android.widget.FrameLayout[@content-desc=\"Me\"]/android.widget.ImageView')
# my_icon = (By.XPATH, '//*[@resource-id="com.zhiyun.cama:id/main_bottom_me"]')
#点击登录按钮
File_tv_login = (By.ID,'com.zhiyun.cama:id/tv_login')
# 输入用户名
File_et_name = (By.ID,'com.zhiyun.cama:id/et_name')
# 输入密码
File_et_pass = (By.ID,'com.zhiyun.cama:id/et_pass')
# 点击登录提交按钮
File_tv_commit = (By.ID,'tv_commit')



#点击我的按钮
"""def click_File_me(self):
    self.find_element(*self.File_me).click()
def click_File_tv_login(self):
    self.find_element(*self.File_tv_login).click()
# 输入手机号码
def input_user(self, username):
    self.send_keys(username, *self.user)

# 输入密码
def input_password(self, pwd):
    self.send_keys(pwd, *self.password)

# 点击登录按钮
def click_File_tv_commit(self):
    self.find_element(*self.File_tv_commit).click()"""
