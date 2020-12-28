#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from Public.Function import BaseFun


#--------------------模板-----------------
class Template_Page(BaseFun):

# ------------------------------------------------------------模板---------------------------------------------------------------

    #模板页面-下载按钮
    File_progress_download = (By.XPATH, '//*[@resource-id="com.zhiyun.cama:id/progress_download"]')

    #使用按钮
    File_tv_download_completed = (By.XPATH, '//*[@text="使用"]')

    #添加视频-视频列表（多个视频）
    File_tv_videos = (By.XPATH, '//*[@resource-id="com.zhiyun.cama:id/iv_thumbnail"]')

    #下一步按钮
    File_next_btn = (By.XPATH, '//*[@text="下一步"]')


    # 发布按钮
    File_publish_btn = (By.XPATH, '//*[@text="发布"]')

    # 点击下载按钮
    def click_File_progress_download(self):
        self.tap_element(self.File_progress_download)

    # 点击使用按钮
    def click_File_tv_download_completed(self):
        self.tap_element(self.File_tv_download_completed)

    # 点击下一步按钮
    def click_File_next_btn(self):
        self.tap_element(self.File_next_btn)

    # 点击发布按钮
    def click_File_publish_btn(self):
        self.tap_element(self.File_publish_btn)
