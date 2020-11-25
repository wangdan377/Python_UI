# -*- coding: UTF-8 -*-
# Administrator
# 2020/4/27 16:27

from Common.basepage import BasePage
from PageLocators.signaturePage_locator import SingaturePageLoctor as SP
import time

class SignaturePage(BasePage):
    """文件签署页面"""
    def isExists_signature(self):
        #本页面元素是否存在
        try:
            self.wait_ele_exists(SP.signer_text_loc,"合同签署页面_定位给待签署人标记签署的位置文本是否存在")
            return True
        except:
            return False

    def sign_success(self):
        # time.sleep(3)
        #鼠标按住签章拖动到目标位置盖章
        self.mouse_drag_and_drop(SP.Cloud_signature_loc,"800","100","文件签署页面_鼠标按住签章拖动到目标位置盖章")
        time.sleep(3)
        #点击完成签署
        self.click_element(SP.sign_complete_loc,"文件签署页面_点击完成签署")
        # time.sleep(3)
        #点击密码验证
        self.click_element(SP.password_ver_loc,"文件签署页面_点击密码验证")
        # time.sleep(3)
        #输入密码
        self.input_text(SP.password_input_loc,"123456","文件签署页面_输入密码")
        # time.sleep(3)
        #点击确定
        self.click_element(SP.confirm_button_loc,"文件签署页面_点击确认签署按钮")
