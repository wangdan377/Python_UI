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
from Public.Logins import LogIn
from PO.Login_Element import Login_Page
# from Public.loged import Logger
# log = Logger('D:\ZYCami_00\logs\\error.log', level='debug')
from selenium.webdriver.common.by import By
class Prime_Members():
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
        self.logins = LogIn(self.driver)
    def prime_user01(self):
        '''
        已登录且会员
        :return:
        '''

        """try:
            self.driver.find_element_by_android_uiautomator('new UiSelector().text("立即续费")').click()
            self.fun.swip_meal03()        # 第3个套餐
            self.driver.find_element_by_android_uiautomator('new UiSelector().text("立即开通")').click()
            self.wx.click_File_wx_closed()  # 微信支付方式关闭
            self.prime_pays.primes_18()  # 开通页面与续费页面的素材与协议


        except:
            time.sleep(2)
            self.fun.swip_meal03()          # 第3个套餐
            time.sleep(2)
            self.driver.find_element_by_android_uiautomator('new UiSelector().text("立即开通")').click()
            self.wx.click_File_wx_closed()  # 微信支付方式关闭
            self.prime_pays.primes_13()  # 开通页面的素材与协议"""
        self.login.click_File_me()
        self.prime.click_File_prime01()

        self.driver.find_element_by_android_uiautomator('new UiSelector().text("立即续费")').click()
        self.fun.swip_meal03()  # 第3个套餐
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("立即开通")').click()
        self.wx.click_File_wx_closed()  # 微信支付方式关闭
        self.prime_pays.primes_18()  # 开通页面与续费页面的素材与协议

    def prime_user02(self):
        '''
        已登录且非会员
        :return:
        '''
        self.login.click_File_me()
        self.prime.click_File_prime01()

        self.fun.swip_meal03()  # 第3个套餐
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("立即开通")').click()
        self.wx.click_File_wx_closed()  # 微信支付方式关闭
        self.prime_pays.primes_13()  # 开通页面的素材与协议


    def prime_user03(self):
        '''
        未登录且非会员
        :return:
        '''
        self.login.click_File_me()
        self.logins.login_01()

        self.prime.click_File_prime01()
        self.fun.swip_meal03()  # 第3个套餐
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("立即开通")').click()
        self.wx.click_File_wx_closed()  # 微信支付方式关闭
        self.prime_pays.primes_13()  # 开通页面的素材与协议

    def prime_user04(self):
        '''
        未登录且会员
        :return:
        '''
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("立即续费")').click()
        self.fun.swip_meal03()  # 第3个套餐
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("立即开通")').click()
        self.wx.click_File_wx_closed()  # 微信支付方式关闭
        self.prime_pays.primes_18()  # 开通页面与续费页面的素材与协议



if __name__ == '__main__':
    members = Prime_Members()
    print(members.prime_user())

