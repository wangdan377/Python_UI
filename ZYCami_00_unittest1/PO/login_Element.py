#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from appium.webdriver.common import mobileby
from PO.Base_page import Base_Page

import os,time
class Login_Page(Base_Page):
    by = mobileby.MobileBy()
    # 首页
    File_Home = (By.XPATH, '//android.widget.FrameLayout[@content-desc=\"Home\"]/android.widget.ImageView')
    # home
    File_Editor = (By.XPATH, '//android.widget.FrameLayout[@content-desc=\"Editor\"]/android.widget.ImageView')
    #我的按钮
    File_me= (By.XPATH,'//android.widget.FrameLayout[@content-desc=\"Me\"]/android.widget.ImageView')
    #点击登录按钮
    File_tv_login = (By.ID,'tv_login')
    # 输入用户名
    user = (By.ID,'et_name')
    # 输入密码
    password = (By.ID,'et_pass')
    # 点击登录提交按钮
    File_tv_commit = (By.ID,'tv_commit')
    #点击我的按钮
    def click_File_me(self):
        self.find_element(self.File_me).click()
    #单击登录
    def click_File_tv_login(self):
        self.find_element(self.File_tv_login).click()
    # 输入手机号码
    def input_user(self, username):
        self.send_keys(username, self.user)

    # 输入密码
    def input_password(self, pwd):
        self.send_keys(pwd, self.password)

    # 点击登录按钮
    def click_File_tv_commit(self):
        self.find_element(self.File_tv_commit).click()

    # 首页
    def click_File_Home(self):
        self.find_element(self.File_Home).click()

    # home
    def click_File_Editor(self):
        self.find_element(self.File_Editor).click()

    # # 点击注册按钮
    # def click_register_button(self):
    #     self.find_element(*self.register_button).click()


