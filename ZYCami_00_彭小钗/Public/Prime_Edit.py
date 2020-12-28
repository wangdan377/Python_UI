#!/usr/bin/python
# -*- coding: utf-8 -*-

from PO.Edit_Element import Edit_Page
from PO.Login_Element import Login_Page
from PO.Prime_Element import Prime_Page
from Public.Prime_Pay import Prime_Pay
from Public.Logins import LogIn
from Public.Function import BaseFun
# 已登录-未开通-编辑-云剪辑-立即开通-微信支付
# 未登录-未开通-编辑-云剪辑-登录-云剪辑-立即开通-微信支付
# 已登录-已开通-编辑-云编辑-制作
# 未登录-已开通-编辑-云编辑-制作

class Prime_Edits():
    def __init__(self,driver):
        self.driver = driver
        self.edit = Edit_Page(self.driver)
        self.login = Login_Page(self.driver)
        self.prime = Prime_Page(self.driver)
        self.prime_pay = Prime_Pay(self.driver)
        self.logins = LogIn(self.driver)
        self.fun = BaseFun(self.driver)
    def edit_01(self):
        '''
        未登录状态下，home-未开通-云剪辑-登录-云剪辑-选择套餐-立即开通-微信支付
        :return:
        '''
        self.login.File_Editor() #点击编辑home键
        self.edit.File_cloud_engine()   #点击云编辑
        self.logins.login_01()#登录
        self.edit.File_cloud_engine()  # 点击云编辑
        self.prime.click_File_meal_03() #选择套餐
        self.prime.click_File_open01()  #立即开通

    def edit_02(self):
        '''
        未登录状态下，home-已开通-云剪辑-登录-云剪辑-制作-开始使用-选择视频
        :return:
        '''
        self.login.File_Editor() #点击编辑home键
        self.edit.File_cloud_engine()   #点击云编辑
        self.logins.login_01()  # 登录
        self.edit.File_cloud_engine()  # 点击云编辑
        self.fun.swip_yun_Make()  # 制作
        self.edit.click_File_start_user()  # 开始使用
    def edit_03(self):
        '''
        已登录-未开通-编辑-云编辑-选择套餐-立即开通
        :return:
        '''
        self.login.File_Editor() #点击编辑home键
        self.edit.File_cloud_engine()   #点击云编辑
        self.prime.click_File_meal_03()  # 选择套餐
        self.prime.click_File_open01()  # 立即开通

    def edit_04(self):
        '''
        已登录-已开通-编辑-云编辑-制作-开始使用-选择视频
        :return:
        '''
        self.login.File_Editor() #点击编辑home键
        self.edit.File_cloud_engine()   #点击云编辑
        self.logins.login_01()#登录
        self.edit.File_cloud_engine()  # 点击云编辑
        self.fun.swip_yun_Make()    #制作
        self.edit.click_File_start_user()  #开始使用
        self.edit.click_File_id_back()      #选择视频后返回按钮
    def edit_05(self):
        '''
        home-云编辑
        :return:
        '''
        self.login.click_File_Editor() #点击编辑home键
        self.edit.click_File_cloud_engine()   #点击云编辑
