#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from Public.Function import BaseFun


#--------------------发布-----------------
class Publish_Page(BaseFun):

# ------------------------------------------------------------发布---------------------------------------------------------------

    # 发布按钮
    # File_publish_btn = (By.XPATH, '//*[@resource-id="com.zhiyun.cama:id/tv_publish"]')
    File_publish_btn = (By.XPATH, '//*[@resource-id="com.zhiyun.cama:id/fl_publish"]')

    #添加描述文本框
    File_introduction = (By.XPATH, '//*[@resource-id="com.zhiyun.cama:id/et_introduction"]')

    # 添加标签文本
    File_add_tag = (By.XPATH, '//*[@text="#添加标签"]')

    # 添加标签文本框
    File_add_tag_edit_text = (By.XPATH, '//*[@resource-id="com.zhiyun.cama:id/et_content"]')

    #添加按钮
    File_add_btn = (By.XPATH, '//*[@resource-id="com.zhiyun.cama:id/tv_add"]')

    #生成视频成功信息
    File_generated_video_msg = (By.XPATH, '//*[@text="视频已保存到相册"]')

    #发布页面-输入作品描述信息
    def input_File_introduction(self, value):
        self.send_keys(self.File_introduction, value)

    #发布页面-点击添加标签文本
    def click_File_add_tag(self):
        self.tap_element(self.File_add_tag)

    #发布页面-输入作品标签信息
    def input_File_add_tag_edit_text(self, value):
        self.send_keys(self.File_add_tag_edit_text, value)

    # 发布页面-点击添加按钮
    def click_File_add_btn(self):
        self.tap_element(self.File_add_btn)

    #点击发布按钮
    def click_File_publish_btn(self):
        self.tap_element(self.File_publish_btn)















