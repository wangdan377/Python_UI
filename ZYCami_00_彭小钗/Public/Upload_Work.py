#!/usr/bin/python
# -*- coding: utf-8 -*-
from PO.Login_Element import Login_Page
from PO.Edit_Element import Edit_Page
from PO.Upload_Work_Element import Upload_Work_Page
from Public.Function import BaseFun
import time

#上传作品的公共方法
class Upload_Work():
    def __init__(self,driver):
        self.driver = driver
        self.login = Login_Page(self.driver)  # 登录页面元素
        self.edit = Edit_Page(self.driver)  #编辑器页面元素
        self.upload_work = Upload_Work_Page(self.driver) #上传作品页面元素
        self.fun = BaseFun(self.driver)

    def to_upload_work_page(self):
        '''
        导航到上传作品页面
        '''
        #点击编辑器
        self.login.click_File_Editor()
        #点击上传作品按钮
        self.edit.click_File_upload_work()
        time.sleep(1)


    def select_works(self):
        '''
        选择作品
        '''
        #选择第一个视频
        self.fun.tap_elements(self.upload_work.File_works, 1)
        #点击确定按钮
        self.upload_work.click_File_confirm()













