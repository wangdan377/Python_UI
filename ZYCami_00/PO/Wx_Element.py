#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from PO.Base_page import Base_Page

class Wx_Page(Base_Page):

    # 微信支付
    File_wx = (By.ID, 'com.zhiyun.cama:id/btn_wx')

    # 微信支付方式的关闭按钮
    File_wx_closed = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout')

    # 立即支付
    File_pay_wx = (By.ID, '立即支付')
    # 选择零钱按钮
    File_Change_button = (By.XPATH,'//android.widget.FrameLayout[@content-desc=\"当前所在页面,支付\"]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[2]/com.tencent.mm.ui.MMImageView')
    # 选择零钱支付
    File_Change_pay = (By.XPATH,'//android.widget.FrameLayout[@content-desc=\"当前所在页面,支付\"]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView')
    # 选择建设银行支付
    File_Construction_pay = (By.XPATH,'//android.widget.FrameLayout[@content-desc=\"当前所在页面,支付\"]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
    # 选择江苏银行支付
    File_jsu_pay = (By.XPATH,'//android.widget.FrameLayout[@content-desc=\"当前所在页面,支付\"]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
    # 请输入支付密码框
    File_pay_password = (By.XPATH,'//android.widget.FrameLayout[@content-desc=\"当前所在页面,支付\"]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.RelativeLayout/android.widget.RelativeLayout')
    # 关闭支付密码页面弹框
    File_closed_password = (By.XPATH,'//android.view.ViewGroup[@content-desc=\"关闭\"]/android.view.ViewGroup/com.tencent.mm.ui.MMImageView')
    # 支付页面左上角的X
    File_pay_x = (By.ID, '返回')
    # 继续支付
    File_connectinue_pay = (By.ID, 'com.tencent.mm:id/dom')
    # 放弃
    File_give_up_pay = (By.ID, 'com.tencent.mm:id/doz')
    #支付成功,返回商家
    File_return_app = (By.ID, '返回商家')
    #密码输入错误，重试
    File_doz = (By.ID, 'com.tencent.mm:id/doz')



    # 支付页面左上角的X
    def click_File_pay_x(self):
        self.find_element(*self.File_pay_x).click()

    # 继续支付
    def click_File_connectinue_pay(self):
        self.find_element(*self.File_connectinue_pay).click()

    # 放弃
    def click_File_give_up_pay(self):
        self.find_element(*self.File_give_up_pay).click()


    # 选择微信支付
    def click_File_wx(self):
        self.find_element(*self.File_wx).click()

    # 微信支付方式的关闭按钮
    def click_File_wx_closed(self):
        self.find_element(*self.File_wx_closed).click()

    # 立即支付
    def click_File_pay_wx(self):
        self.find_element(*self.File_pay_wx).click()

    # 选择零钱按钮
    def click_File_Change_button(self):
        self.find_element(*self.File_Change_button).click()

    # 选择零钱支付
    def click_File_Change_pay(self):
        self.find_element(*self.File_Change_pay).click()

    # 选择建设银行支付
    def click_File_Construction_pay(self):
        self.find_element(*self.File_Construction_pay).click()

    # 选择江苏银行支付
    def click_File_jsu_pay(self):
        self.find_element(*self.File_jsu_pay).click()

    # 请输入支付密码框
    def click_File_pay_password(self):
        self.find_element(*self.File_pay_password).click()

    # 关闭支付密码页面弹框
    def click_File_closed_password(self):
        self.find_element(*self.File_closed_password).click()

    #返回商家
    def click_File_return_app(self):
        self.find_element(*self.File_return_app).click()

    # 密码输入错误，重试
    def click_File_doz(self):
        self.find_element(*self.File_doz).click()





