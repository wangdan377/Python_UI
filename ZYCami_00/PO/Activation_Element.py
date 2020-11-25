#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from PO.Base_page import Base_Page
class Activation_Page(Base_Page):
    #点击相机按钮
    File_iv_camera1 = (By.ID,'com.zhiyun.cama:id/iv_camera')
    #连接设备
    File_bt_connect = (By.ID, 'com.zhiyun.cama:id/bt_connect')
    # 获取设备和地理位置信息
    File_authorize_switch = (By.ID,'com.zhiyun.cama:id/authorize_switch')
    #下一步
    File_prepare_next = (By.ID,'com.zhiyun.cama:id/tv_prepare_next')
    #激活成功
    File_action_complete = (By.ID,'com.zhiyun.cama:id/tv_complete')
    # 未连接状态下，点击下一步  激活设备是否需要登录（弹框） 有取消and登录 进行登录
    #取消
    File_cancel = (By.ID,'com.zhiyun.cama:id/tv_cancel')

    #登录
    File_confirm = (By.ID,'com.zhiyun.cama:id/tv_confirm')

    # 登录成功后可更换手机号，更换按钮    再次进行登录
    File_charge_phone = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[4]')    # 更换手机进行激活

    # 登录页面返回按钮，未更换
    File_login_back = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView[1]')

    # 查看权益和弹框领取
    File_tv_get = (By.ID, 'com.zhiyun.cama:id/tv_get')

    # 开通和立即续费返回按钮
    File_open_at_back = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[1]/android.view.View')
    #弹框关闭后，确定按钮
    File_positive = (By.ID, 'com.zhiyun.cama:id/positive')

    #---------我的页面----------
    # 新的权益卡待领取
    File_new_card = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.widget.Button')
    # 立即领取
    File_receive = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[6]/android.widget.Button')
    # 立即续费
    File_Renew_now = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[3]')

    # 支付方式关闭按钮
    File_pay_closed = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout')
    # 微信
    File_wx = (By.ID, 'com.zhiyun.cama:id/btn_wx')
    # 点击相机按钮
    def click_File_iv_camera01(self):
        self.find_element(*self.File_iv_camera1).click()

    # 连接设备
    def click_File_bt_connect(self):
        self.find_element(*self.File_bt_connect).click()

    # 获取设备和地理位置信息
    def click_File_authorize_switch(self):
        self.find_element(*self.File_authorize_switch).click()

    # 下一步
    def click_File_prepare_next(self):
        self.find_element(*self.File_prepare_next).click()

    # 激活成功
    def click_File_action_complete(self):
        self.find_element(*self.File_action_complete).click()

    # 未连接状态下，点击下一步  激活设备是否需要登录（弹框） 有取消and登录 进行登录
    # 取消
    def click_File_cancel(self):
        self.find_element(*self.File_cancel).click()

    # 登录
    def click_File_confirm(self):
        self.find_element(*self.File_confirm).click()

    # 登录成功后可更换手机号，更换按钮    再次进行登录
    def click_File_charge_phone(self):
        self.find_element(*self.File_charge_phone).click()

    # 登录页面返回按钮，未更换
    def click_File_login_back(self):
        self.find_element(*self.File_login_back).click()

    # 查看权益和弹框领取
    def click_File_tv_get(self):
        self.find_element(*self.File_tv_get).click()

    # 弹框关闭后，确定按钮
    def click_File_positive(self):
        self.find_element(*self.File_positive).click()

    # 开通和立即续费返回按钮
    def click_File_open_at_back(self):
        self.find_element(*self.File_open_at_back).click()

    # 新的权益卡待领取
    def click_File_new_card(self):
        self.find_element(*self.File_new_card).click()

    # 立即领取
    def click_File_receive(self):
        self.find_element(*self.File_receive).click()
    # 立即续费
    def click_File_Renew_now(self):
        self.find_element(*self.File_Renew_now).click()

    # 支付方式关闭按钮
    def click_File_pay_closed(self):
        self.find_element(*self.File_pay_closed).click()

    # 微信
    def click_File_wx(self):
        self.find_element(*self.File_wx).click()






