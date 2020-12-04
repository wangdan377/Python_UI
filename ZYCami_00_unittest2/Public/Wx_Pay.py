#!/usr/bin/python
# -*- coding: utf-8 -*-
from common.loged import *
import os,time
from PO.Wx_Element import Wx_Page
# 公共方法：微信支付


class Wx_Config():
    def __init__(self,driver):
        self.driver = driver
        self.wx_pages = Wx_Page(self.driver)
    def wx_pay01(self):
        '''
        微信支付，输入支付密码进行支付
        :return:    支付成功
        '''
        # log = Logger('D:\ZYCami_00\logs\\error.log', level='debug')
        try:
            # self.wx_pages.click_File_wx()     #选择微信支付
            self.driver.tap([(955, 1325)])  #微信支付
            time.sleep(2)
            self.driver.find_element_by_accessibility_id("立即支付").click()        #微信支付
            time.sleep(2)
            self.driver.tap([(188, 1804)])  #1
            time.sleep(1)
            self.driver.tap([(582, 1801)])  #2
            time.sleep(1)
            self.driver.tap([(972, 1799)])  #3
            time.sleep(1)
            self.driver.tap([(190, 1960)])  #4
            time.sleep(1)
            self.driver.tap([(570, 1965)])  #5
            time.sleep(1)
            self.driver.tap([(969, 1967)])  #6
            self.driver.click_File_return_app() #支付成功返回app
            time.sleep(5)
        except Exception as e:
            # log.logger.error('输入错误')
            print(e)

    def wx_pay02(self):
        '''
        微信支付，关闭支付-放弃
        :return:    支付成功
        '''
        # log = Logger('D:\ZYCami_00\logs\\error.log', level='debug')
        try:
            # self.wx_pages.click_File_wx()  # 选择微信支付
            self.driver.tap([(955, 1325)])  # 微信支付
            time.sleep(2)
            self.wx_pages.click_File_pay_x()  #左上角x 取消支付
            time.sleep(2)
            self.wx_pages.click_File_give_up_pay()#放弃支付
            time.sleep(2)
            self.driver.tap([(188, 1804)])  # 1
            time.sleep(1)
            self.driver.tap([(582, 1801)])  # 2
            time.sleep(1)
            self.driver.tap([(972, 1799)])  # 3
            time.sleep(1)
            self.driver.tap([(190, 1960)])  # 4
            time.sleep(1)
            self.driver.tap([(570, 1965)])  # 5
            time.sleep(1)
            self.driver.tap([(969, 1967)])  # 6
            time.sleep(1)
            self.driver.tap([(190, 2131)])  #7
            time.sleep(1)
            self.driver.tap([(584, 2136)])  #8
            time.sleep(5)
            self.wx_pages.click_File_return_app()  # 返回商家
        except Exception as e:
            # log.logger.error('输入错误')
            print(e)

    def wx_pay03(self):
        '''
        微信支付，关闭-继续支付-立即支付（输入支付密码）-关闭-关闭-放弃
        :return:    支付成功
        '''
        # log = Logger('D:\ZYCami_00\logs\\error.log', level='debug')
        try:
            # self.wx_pages.click_File_wx()     #选择微信支付
            self.driver.tap([(955, 1325)])  # 微信支付
            time.sleep(2)
            self.wx_pages.click_File_pay_x()      #左上角x 取消支付
            time.sleep(2)
            self.wx_pages.click_File_connectinue_pay()    #继续支付
            time.sleep(2)
            self.driver.find_element_by_accessibility_id("立即支付").click()  # 微信支付
            time.sleep(2)
            self.wx_pages.click_File_closed_password()    #支付密码弹框关闭
            time.sleep(2)
            self.wx_pages.click_File_pay_x()  # 取消支付  x
            time.sleep(2)
            self.wx_pages.click_File_give_up_pay()  # 放弃支付
            time.sleep(2)
            self.driver.tap([(188, 1804)])  # 1
            time.sleep(1)
            self.driver.tap([(582, 1801)])  # 2
            time.sleep(1)
            self.driver.tap([(972, 1799)])  # 3
            time.sleep(1)
            self.driver.tap([(190, 1960)])  # 4
            time.sleep(1)
            self.driver.tap([(570, 1965)])  # 5
            time.sleep(1)
            self.driver.tap([(969, 1967)])  # 6
            time.sleep(5)
            self.wx_pages.click_File_return_app()       #返回商家
        except Exception as e:
            # log.logger.error('输入错误')
            print(e)