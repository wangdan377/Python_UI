#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from Public.Function import BaseFun


#--------------------上传作品-----------------
class Upload_Work_Page(BaseFun):

# ------------------------------------------------------------我---------------------------------------------------------------

    #上传作品页面中的作品列表
    File_works = (By.XPATH, '//*[@resource-id="com.zhiyun.cama:id/image"]')

    #确定按钮
    File_confirm = (By.XPATH, '//*[@text="确定"]')

    # 点击确定按钮
    def click_File_confirm(self):
        self.tap_element(self.File_confirm)