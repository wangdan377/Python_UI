#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from Public import Caplictily
from PO.Prime_Element import Prime_Page
from Public.Function import BaseFun
from Public.Wx_Pay import Wx_Config
from PO.Login_Element import Login_Page
from Public.Prime_Pay import Prime_Pay
from PO.Wx_Element import Wx_Page
from PO.Edit_Element import Edit_Page
# from Public.loged import Logger
# log = Logger('D:\ZYCami_00\logs\\error.log', level='debug')
class prime_receive_user():
    '''是否 是会员'''
    def __init__(self,driver):
        self.driver = driver

        # driver = Caplictily.Driver_Config()
        # self.driver = driver.get_driver()
        self.login = Login_Page(self.driver)  # 登录
        self.prime = Prime_Page(self.driver)  # prime
        self.fun = BaseFun(self.driver)
        self.login = Login_Page(self.driver)
        self.wx_pays = Wx_Config(self.driver)
        self.prime_pays = Prime_Pay(self.driver)
        self.wx = Wx_Page(self.driver)
        self.edit=Edit_Page(self.driver)
    def prime_user_01(self):
        '''
        体验卡待领取-领取-查看权益-立即续费
        体验卡待领取-领取-关闭-立即续费
        app启动-领取—查看权益-立即续费
        app启动-关闭—确定关闭-个人/edit
        个人-prime-待领取-领取-查看权益-立即续费
        个人-prime-待领取-领取-关闭-立即续费
        home-云编辑-领取-查看权益-立即续费
        home-云编辑-领取-关闭-立即续费

        :return:
        '''
        # app启动-首页领取
        self.prime.click_File_interests()
        time.sleep(3)
        self.prime.click_File_interests()
        time.sleep(3)
        self.prime.click_File_Renew()
    def prime_user_02(self):
        '''
        体验卡待领取-领取-查看权益-立即续费
        体验卡待领取-领取-关闭-立即续费
        app启动-领取—查看权益-立即续费
        app启动-关闭—确定关闭-个人/edit
        个人-prime-待领取-领取-查看权益-立即续费
        个人-prime-待领取-领取-关闭-立即续费
        home-云编辑-领取-查看权益-立即续费
        home-云编辑-领取-关闭-立即续费

        :return:
        '''
        # 如果找不到-则去个人主页领取（第一次领取，有待领取）
        self.login.click_File_me()
        self.prime.click_File_prime01()
        self.prime.click_File_receive_interests()  # 待领取
        self.prime.click_File_me_receive()
        # self.fun.swip_prime_closed()
        time.sleep(3)
    def prime_user_03(self):
        '''
        体验卡待领取-领取-查看权益-立即续费
        体验卡待领取-领取-关闭-立即续费
        app启动-领取—查看权益-立即续费
        app启动-关闭—确定关闭-个人/edit
        个人-prime-待领取-领取-查看权益-立即续费
        个人-prime-待领取-领取-关闭-立即续费
        home-云编辑-领取-查看权益-立即续费
        home-云编辑-领取-关闭-立即续费

        :return:
        '''
        #第二次（直接领取）
        self.prime.click_File_me_receive()
        self.prime.click_File_interests()
        self.prime.click_File_Renew()

    def prime_user_04(self):
        '''
        体验卡待领取-领取-查看权益-立即续费
        体验卡待领取-领取-关闭-立即续费
        app启动-领取—查看权益-立即续费
        app启动-关闭—确定关闭-个人/edit
        个人-prime-待领取-领取-查看权益-立即续费
        个人-prime-待领取-领取-关闭-立即续费
        home-云编辑-领取-查看权益-立即续费
        home-云编辑-领取-关闭-立即续费

        :return:
        '''
        # 如果找不到-则去edit领取
        self.login.click_File_Home()
        self.edit.click_File_cloud_engine()
        self.edit.click_File_edit_receive()
        self.edit.click_File_interests()
        self.prime.click_File_Renew()




