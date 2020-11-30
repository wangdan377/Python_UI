# -*- coding: UTF-8 -*-
# Administrator
# 2020/4/20 18:53

from Common.basepage import BasePage
from PageLocators.uploadPage_locator import UploadPageLoctor as UP

import time

class UploadPage(BasePage):
    '''上传合同页面'''
    def isExist_upload_ele(self):
        try:
            self.wait_ele_exists(UP.addContract_loc,"上传合同页面_上传合同元素")
            return True
        except:
            return False

    def uploadFile(self,filepath):

        # 屏幕切到元素底部对齐
        self.scroll_into_bottom(UP.nextStep_loc, "添加签署人页面_切换到窗口点击下一步元素的底部对齐")
        time.sleep(3)
        #添加合同
        self.input_text(UP.addContract_loc,filepath,"上传合同页面_上传合同文件")
        # time.sleep(3)
        #添加附件
        self.input_text(UP.uploadFile_loc,filepath,"上传合同页面_上传附件")
        time.sleep(1)
        #下一步
        self.click_element(UP.nextStep_loc,"上传合同页面_点击下一步")

    def uploadFile2(self,filepath):
        # 屏幕切到元素底部对齐
        self.scroll_into_bottom(UP.nextStep_loc, "添加签署人页面_切换到窗口点击下一步元素的底部对齐")
        time.sleep(3)
        # 添加合同
        self.input_text(UP.addContract_loc, filepath, "上传合同页面_上传合同文件")
        time.sleep(1)
        # 下一步
        self.click_element(UP.nextStep_loc, "上传合同页面_点击下一步")


    def get_error(self):
        #不添加合同点击下一步
        self.click_element(UP.nextStep_loc,"不上传合同_点击下一步")
        time.sleep(1)
        return self.get_text(UP.error_loc,"上传合同页面_不上传合同错误提示")

