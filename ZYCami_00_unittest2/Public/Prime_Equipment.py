#!/usr/bin/python
# -*- coding: utf-8 -*-
from PO.Prime_Element import Prime_Page
from PO.login_Element import Login_Page
from Public.Function import BaseFun
import time
class Prime_Buy_Equipment():
    def __init__(self,driver):
        self.driver = driver
        self.prime = Prime_Page(self.driver)
        self.login = Login_Page(self.driver)
        self.fun = BaseFun(self.driver)
    def Prime_buy_Equipment_01(self):
        '''
        已是prime  个人主页-prime-立即续费-购买第一台-返回-向左滑动-购买第二台-返回
        :return:
        '''
        self.login.click_File_me() #个人主页
        self.prime.click_File_prime01()  # 点击prime
        self.prime.click_File_opens01()  # 立即续费
        time.sleep(2)
        self.prime.click_File_equip_buy()  # 购买设备
        time.sleep(2)
        self.fun.swip_return()  #万能返回
        self.fun.swip_prime_left01()  # 向左滑动
        self.prime.click_File_equip_buy()  # 购买设备
        time.sleep(2)
        self.fun.swip_return()  # 万能返回
    def Prime_buy_Equipment_02(self):
        '''
        已是prime 个人主页-prime-立即续费-向左滑动-购买第二台-返回-向右滑动-购买第一台-返回
        :return:
        '''
        self.login.click_File_me()  # 个人主页
        self.prime.click_File_prime01()  # 点击prime
        self.prime.click_File_opens01()  # 立即续费
        self.fun.swip_prime_left01()  #向左滑动
        time.sleep(2)
        self.prime.click_File_equip_buy()  # 购买设备
        time.sleep(2)
        self.fun.swip_return()  # 万能返回
        time.sleep(2)

    def Prime_buy_Equipment_3(self):
        '''
        无prime 个人主页-prime-向左滑动-购买第二台-返回-向右滑动-购买第一台-返回
        :return:
        '''
        self.login.click_File_me()  # 个人主页
        self.prime.click_File_prime01()  # 点击prime
        self.fun.swip_prime_left01()  # 向左滑动
        time.sleep(2)
        self.prime.click_File_equip_buy()  # 购买设备
        time.sleep(2)
        self.fun.swip_return()  # 万能返回
        time.sleep(2)

    def Prime_buy_Equipment_04(self):
        '''
        个人主页-prime-购买第一台-返回-左滑动-购买第二台-返回-向右滑动-购买第一台
        :return:
        '''
        # self.login.click_File_me()  # 个人主页
        # self.prime.click_File_prime01()  # 点击prime
        # self.prime.click_File_opens02()  # 立即续费
        # self.prime.click_File_buy_equipment01()  # 第1台
        # self.driver.find_element_by_android_uiautomator('new UiSelector().text("购买")').click()
        # self.prime.click_File_equip_buy()
        self.prime.click_File_equip_buy()  # 购买设备
        time.sleep(2)
        self.fun.swip_return()  # 万能返回
        time.sleep(2)
        self.fun.swip_prime_left01()  #向左滑动
        time.sleep(2)
        self.prime.click_File_equip_buy()  # 购买设备

        time.sleep(2)
        self.fun.swip_return()  # 万能返回
        time.sleep(2)
        self.fun.swip_prime_right01() # 向右滑动
        time.sleep(2)
        self.prime.click_File_equip_buy()  # 购买设备
        time.sleep(2)
        self.fun.swip_return()  # 万能返回
        time.sleep(2)


