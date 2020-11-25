#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from PO.Base_page import Base_Page
import os,time



#--------------------编辑-----------------
class Edit_Page(Base_Page):
    # 个人主页按钮
    File_me = (By.XPATH,'//android.widget.FrameLayout[@content-desc=\"Me\"]/android.widget.ImageView')
    #返回键按钮公用页面-home页面、模板、上传作品
    File_back = (By.ID,'com.zhiyun.cama:id/back')
    #云剪辑
    File_cloud_engine = (By.ID,'com.zhiyun.cama:id/cloud_engine')
    #开通prime的返回按钮
    File_open_back = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[1]/android.view.View')

    #创作
    File_create = (By.ID,'com.zhiyun.cama:id/create')
    #创作关闭按钮
    File_title_left = (By.ID,'com.zhiyun.cama:id/iv_title_left')
    #模板
    File_template = (By.ID,'com.zhiyun.cama:id/template')
    #上传作品
    File_upload_work = (By.ID,'com.zhiyun.cama:id/upload_work')

    # 开始使用
    File_start_user = (By.ID, 'com.zhiyun.cama:id/start')

    # 选择视频后返回
    File_id_back = (By.ID, 'com.zhiyun.cama:id/back')

    # 第一个套餐
    File_Edit_meal_01 = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View/android.widget.ListView/android.view.View[1]')

    # 第二个套餐
    File_Edit_meal_02 = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View/android.view.View[2]')

    # 第三个套餐
    File_Edit_meal_03 = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View/android.view.View')
    # 开通
    File_Edit_open01 = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.widget.Button')

    # 购买第一个设备
    File_Edit_buy_equipment01 = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[6]/android.view.View[1]/android.view.View[1]/android.view.View/android.view.View[2]/android.widget.Button')

    # 购买第二个设备
    File_Edit_buy_equipment02 = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[6]/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View[2]/android.widget.Button')

    # 兑换码
    File_exchange = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[1]/android.view.View[2]')

    # 领取
    File_edit_receive = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[6]/android.widget.Button')
    # 查看权益
    File_interests = (By.ID, 'com.zhiyun.cama:id/tv_get')




    # 个人主页按钮
    def click_File_me(self):
        self.find_element(self.File_me).click()
    # 返回键按钮公用页面-home页面、模板、上传作品
    def File_back(self):
        self.find_element(self.File_back).click()
    # 云剪辑
    def click_File_cloud_engine(self):
        self.find_element(self.File_cloud_engine).click()
    # 开通prime的返回按钮
    def click_File_open_back(self):
        self.find_element(self.File_open_back).click()
    # 创作
    def click_File_create(self):
        self.find_element(self.File_create).click()
    # 创作关闭按钮
    def click_File_title_left(self):
        self.find_element(self.File_title_left).click()
    # 模板
    def click_File_template(self):
        self.find_element(self.File_template).click()
    # 上传作品
    def click_File_upload_work(self):
        self.find_element(self.File_upload_work).click()

    # 开始使用
    def click_File_start_user(self):
        self.find_element(self.File_start_user).click()

    # 选择视频后返回
    def click_File_id_back(self):
        self.find_element(self.File_id_back).click()

    # 第一个套餐
    def click_File_Edit_meal_01(self):
        self.find_element(self.File_Edit_meal_01).click()

    # 第二个套餐
    def click_File_Edit_meal_02(self):
        self.find_element(self.File_Edit_meal_02).click()

    # 第三个套餐
    def click_File_Edit_meal_03(self):
        self.find_element(self.File_Edit_meal_03).click()

    # 开通
    def click_File_Edit_open01(self):
        self.find_element(self.File_Edit_open01).click()

    # 购买第一个设备
    def click_File_Edit_buy_equipment01(self):
        self.find_element(self.File_Edit_buy_equipment01).click()

    # 购买第二个设备
    def click_File_Edit_buy_equipment02(self):
        self.find_element(self.File_Edit_buy_equipment02).click()

    # 兑换码
    def click_File_exchange(self):
        self.find_element(self.File_exchange).click()

    # 领取
    def click_File_edit_receive(self):
        self.find_element(self.File_edit_receive).click()

    # 查看权益
    def click_File_interests(self):
        self.find_element(self.File_interests).click()