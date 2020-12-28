#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from Public import Caplictily
from PO.Prime_Element import Prime_Page
from Public.Function import BaseFun
from Public.Wx_Pay import Wx_Config
from PO.Edit_Element import Edit_Page
from PO.Login_Element import Login_Page
from Public.Prime_Me_Member import Prime_Members

# from Public.loged import Logger
# log = Logger('D:\ZYCami_00\logs\\error.log', level='debug')
class Prime_Edit_Members():
    '''是否 是会员'''
    def __init__(self,driver):
        self.driver = driver
        # driver = Caplictily.Driver_Config()
        # self.driver = driver.get_driver()
        self.login = Login_Page(self.driver)  # 登录
        self.prime = Prime_Page(self.driver)  # prime
        self.fun = BaseFun(self.driver)
        self.login = Login_Page(self.driver)
        self.wx_pays = Wx_Config(self.driver)
        self.edit = Edit_Page(self.driver)
        self.members = Prime_Members(self.driver)
    def prime_edit_user(self):
        '''
        是会员，则续费-选择套餐-开通
        :return:
        '''
        # self.login.click_File_Editor()  # 编辑
        # self.edit.click_File_cloud_engine()  # 云编辑
        time.sleep(2)
        self.fun.swip_yun_Make()   #制作
        self.edit.click_File_start_user()   #开始使用


    """def prime_edit_user01(self):
        '''
        登录非会员
        :return:
        '''

        self.login.click_File_Editor()  # 编辑
        self.edit.click_File_cloud_engine()  # 云编辑
        time.sleep(2)
        self.fun.swip_meal03()  # 第3个套餐
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("立即开通")').click()

        # self.fun.swip_yun_Make()  # 立即制作
        # time.sleep(2)
        # self.edit.click_File_start_user()  # 开始使用


    def prime_edit_user02(self):
        '''
        是登录会员-直接制作
        :return:
        '''
        self.login.click_File_Editor()  # 编辑
        self.edit.click_File_cloud_engine()  # 云编辑
        self.fun.swip_yun_Make()  # 立即制作
        time.sleep(2)
        self.edit.click_File_start_user()  # 开始使用"""


if __name__ == '__main__':
    edits = Prime_Edit_Members()
    print(edits.prime_edit_user())
