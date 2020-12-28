#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from Public import Caplictily
from PO.Prime_Element import Prime_Page
from Public.Function import BaseFun
from Public.Wx_Pay import Wx_Config
from Public.Prime_Equipment import Prime_Buy_Equipment
from PO.Login_Element import Login_Page
from Public.Prime_Pay import Prime_Pay
from PO.Wx_Element import Wx_Page

# from Public.loged import Logger
# log = Logger('D:\ZYCami_00\logs\\error.log', level='debug')
class Prime_Equit_Members():
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
        self.prime_buy_equipment = Prime_Buy_Equipment(self.driver)  # 购买设备
    def prime_equit_user(self):
        '''
        是会员，则续费-选择套餐-开通
        :return:
        '''
        """try:
            self.prime.click_File_opens02()  # 立即续费
            self.prime.click_File_meal03()  # 第3个套餐
            self.prime_buy_equipment.Prime_buy_Equipment_04()  # 购买多台设备
        except:
            time.sleep(2)
            self.prime.click_File_meal03()  # 第3个套餐
            time.sleep(2)
            self.prime_buy_equipment.Prime_buy_Equipment_04()  # 购买多台设备
"""
        # self.login.click_File_me()  # 个人主页
        # self.prime.click_File_prime01()  # 点击prime
        # self.prime.click_File_opens02()  # 立即续费
        self.prime_buy_equipment.Prime_buy_Equipment_04()
        """self.prime.click_File_equip_buy()  # 购买设备1
        time.sleep(2)
        self.fun.swip_return()  # 万能返回
        time.sleep(2)
        self.fun.swip_prime_left01()  # 向左滑动
        time.sleep(2)
        self.prime.click_File_equip_buy()  # 购买设备
        time.sleep(2)
        self.fun.swip_return()  # 万能返回
        time.sleep(2)
        self.fun.swip_prime_right01()  # 向右滑动
        time.sleep(2)
        self.prime.click_File_equip_buy()  # 购买设备2
        time.sleep(2)
        self.fun.swip_return()  # 万能返回
        time.sleep(2)"""

if __name__ == '__main__':
      equips= Prime_Equit_Members()
      print(equips.prime_equit_user())