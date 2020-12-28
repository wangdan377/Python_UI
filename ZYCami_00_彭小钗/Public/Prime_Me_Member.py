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
from PO.Base_page import Base_Page
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
        self.basepage = Base_Page(self.driver)
    def prime_user03(self):
        '''
        选择套餐3-开通
        :return:
        '''
        """try:
            time.sleep(3)
            self.login.click_File_me()
            self.prime.click_File_prime01()
            self.prime.click_File_Renew()  # 立即续费
            self.prime.click_File_meal_03()  # 第3个套餐
            self.prime.click_File_open01()  # 立即开通，然后走支付
            self.wx.click_File_wx_closed()  # 微信支付方式关闭
            self.prime_pays.primes_18()  # 开通页面的素材与协议
        except:
            time.sleep(2)
            self.prime.click_File_meal_03()     #套餐
            time.sleep(2)
            self.prime.click_File_open01()      #开通
            self.wx.click_File_wx_closed()  # 微信支付方式关闭
            self.prime_pays.primes_13()  # 开通页面的素材与协议"""
        #可用,但是有问题，逻辑不通
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
            self.prime_pays.primes_13()  # 开通页面的素材与协议
"""
        """self.login.click_File_me()
        self.prime.click_File_prime01()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("立即续费")').click()
        self.fun.swip_meal03()  # 第3个套餐
        # self.driver.find_element_by_android_uiautomator('new UiSelector().text("立即续费")').click()
        # self.driver.find_elements_by_link_text('立即续费')
        self.driver.find_element_by_xpath("//*[@text='立即续费']")    #可用
        time.sleep(3)
        self.prime.click_File_opens01()  # 立即开通"""

        self.prime.click_File_meal03()
        self.prime.click_File_opens01()
        time.sleep(2)
        self.fun.swip_wx_closed()

        return ''
        # eles = self.prime.click_File_opens02()
        # eles = self.basepage.find_element(File_opens01)
        # eles = self.basepage.find_elements(By.XPATH,"//*[@text='立即续费']")
        # eles = self.find_elements(self.driver.find_elements_by_xpath("//*[@text='立即续费']") ).click()
        """eles = self.driver.find_elements_by_xpath("//*[@text='立即续费']")      #可用
        # eles = self.driver.find_elements(by='xpath', value='//*[@text="立即续费"]') #可用

           # 续费
        if len(eles) == 1:
            self.prime.click_File_opens02()
            self.prime.click_File_meal03()
            self.prime.click_File_opens01()
        else:
            self.prime.click_File_meal03()
            self.prime.click_File_opens01()"""

    def prime_user02(self):
        self.prime.click_File_meal02()
        self.prime.click_File_opens01()
        time.sleep(2)
        self.fun.swip_wx_closed()

        return ''
    def prime_user01(self):
        self.prime.click_File_meal01()
        self.prime.click_File_opens01()
        time.sleep(2)
        self.fun.swip_wx_closed()

        return ''

if __name__ == '__main__':
    members = Prime_Members()
    print(members.prime_user03())
    print(members.prime_user02())
    print(members.prime_user01())
