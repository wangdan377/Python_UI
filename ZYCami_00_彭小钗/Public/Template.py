#!/usr/bin/python
# -*- coding: utf-8 -*-
from PO.Login_Element import Login_Page
from PO.Edit_Element import Edit_Page
from PO.Template_Element import Template_Page
from Public.Function import BaseFun
import time

#模板的公共方法
class Template():
    def __init__(self,driver):
        self.driver = driver
        self.login = Login_Page(self.driver)  # 登录页面元素
        self.edit = Edit_Page(self.driver)  #编辑器页面元素
        self.template = Template_Page(self.driver) #模板页面元素
        self.fun = BaseFun(self.driver)

    def to_template_page(self):
        '''
        导航到模板页面
        '''
        #点击编辑器
        self.login.click_File_Editor()
        #点击模板按钮
        self.edit.click_File_template()
        time.sleep(1)

    def click_download_completed_btn(self):
        '''
        判断模板是否下载，没有下载则先下载，再点击使用
        '''
        #判断下载按钮是否存在
        if self.fun.is_element_exist(self.template.File_progress_download):
            #点击下载按钮
            self.template.click_File_progress_download()

        #点击使用按钮
        self.template.click_File_tv_download_completed()

    def select_videos(self):
        '''
        选择视频
        '''
        #选择前面两个视频
        self.fun.tap_elements(self.template.File_tv_videos, 2)
        #点击下一步按钮
        self.template.click_File_next_btn()













