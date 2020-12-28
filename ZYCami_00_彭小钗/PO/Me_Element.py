#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from Public.Function import BaseFun


#--------------------我-----------------
class Me_Page(BaseFun):

# ------------------------------------------------------------我---------------------------------------------------------------
    #我-上传作品成功和分享信息
    File_publish_success_msg = (By.XPATH, '//*[@text="上传成功！你可以分享到："]')


    # #发布页面-输入作品描述信息
    # def input_File_introduction(self, value):
    #     self.send_keys(self.File_introduction, value)















