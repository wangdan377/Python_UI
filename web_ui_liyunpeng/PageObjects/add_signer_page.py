# -*- coding: UTF-8 -*-
# Administrator
# 2020/4/21 17:45

from Common.basepage import BasePage
from PageLocators.addSinger_locator import AddSignerLocator as AS
import time

class AddSingerPage(BasePage):
    '''添加签署人页面'''
    def isExist_addSigner_ele(self):
        #是否成功进入当前页面
        try:
            self.wait_ele_exists(AS.sign_object_loc,"添加签署人页面_添加签署人元素")
            return True
        except:
            return False


    def click_signer_next(self):
        # 进入签署人页面不修改信息直接点击下一步
        time.sleep(5)
        self.click_element(AS.nextStep_loc,"添加签署人页面_下一步按钮")

    def add_signer(self,mobile):
        #添加签署人，指定用户付

        #点击添加签署人
        self.click_element(AS.addSigner_loc,"添加签署人页面_点击添加签署人")
        #输入添加签署人手机号或邮箱
        self.input_text(AS.account_input_loc,mobile,"添加签署人页面_输入签署人")
        #点击空白或者无连接处带出签署人信息
        self.click_element(AS.sign_object_loc,"添加签署人页面_点击空白或者无连接处")
        #点击指定付按钮
        self.click_element(AS.Specify_button_loc,"添加签署人页面_点击指定付按钮")
        time.sleep(3)
        # 屏幕切到元素底部对齐
        self.scroll_into_bottom(AS.nextStep_loc, "添加签署人页面_切换到窗口点击下一步元素的底部对齐")
        time.sleep(3)
        #点击请选择
        self.click_element(AS.choose_users_loc,"添加签署人页面_点击请选择用户")
        time.sleep(3)
        #选择指定付用户
        self.click_element(AS.Specify_users_loc,"添加签署人页面_选择指定付用户")
        #点击下一步
        self.click_element(AS.nextStep_loc,"添加签署人页面_点击下一步")