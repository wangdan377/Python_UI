#!/usr/bin/python
# -*- coding: utf-8 -*-
from ddt import ddt,data,unpack
from Public.Function import *
from Public import Caplictily
from Public.Logins import LogIn
from PO.login_Element import Login_Page
from PO.Prime_Element import Prime_Page
from PO.Wx_Element import Wx_Page
from Public.Prime_Pay import Prime_Pay
from Public.Wx_Pay import Wx_Config
from Public.Prime_Equipment import Prime_Buy_Equipment
from Public.Prime_Me_Member import Prime_Members
import unittest,pytest
import time,os,sys
import warnings
import HTMLTestRunnerCN3_pie_chart_screen
from common.loged import Logger
import pytest
# @ddt  #装饰器类
class Test_Prime_pay(unittest.TestCase):
    '''已登录状态下，是否会员，去购买套餐，协议/素材'''

    def setUp_class(self):
        warnings.simplefilter("ignore", ResourceWarning)
        driver = Caplictily.Driver_Config()
        self.driver = driver.get_driver()
        self.login = Login_Page(self.driver)    #登录
        self.prime = Prime_Page(self.driver)     #prime
        self.fun = BaseFun(self.driver)
        self.logins = LogIn(self.driver)
        self.prime_pays = Prime_Pay(self.driver)
        self.wx = Wx_Page(self.driver)
        self.wx_pays = Wx_Config(self.driver)   #微信支付密码
        self.prime_buy_equipment = Prime_Buy_Equipment(self.driver)   #购买设备
        self.members = Prime_Members(self.driver)
    def tearDown_class(self):
        self.driver.quit()
    def test_prime_pay01(self):
        """
        是否会员，如果是会员则续费 ，否则选择套餐进行购买，购买套餐3
        :return:
        """

        self.login.click_File_me()
        eles = self.driver.find_elements_by_xpath("//*[@text='登录']")  # 登录
        time.sleep(2)
        if len(eles) == 1:
            self.logins.login_01()
            self.prime.click_File_prime01()
            eles = self.driver.find_elements_by_xpath("//*[@text='立即续费']")  # 可用

            if len(eles) == 1:
                self.prime_pays.primes_20()  # 续费页面 有效期/素材
                self.prime.click_File_opens02()  # 续费
                self.members.prime_user01()  # 选择套餐3 进行开通
                self.prime_pays.primes_19()  # 开通页面素材
            else:
                self.members.prime_user01()  # 选择套餐3 进行开通
                self.prime_pays.primes_19()  # 开通页面素材
        else:
            self.prime.click_File_prime01()
            eles = self.driver.find_elements_by_xpath("//*[@text='立即续费']")  # 可用

            if len(eles) == 1:
                self.prime_pays.primes_20()  # 续费页面 有效期/素材
                self.prime.click_File_opens02()  # 续费
                self.members.prime_user01()  # 选择套餐1 进行开通
                self.prime_pays.primes_19()  # 开通页面素材
            else:
                self.members.prime_user01()  # 选择套餐1 进行开通
                self.prime_pays.primes_19()  # 开通页面素材


    # def test_prime_pay02(self):
    #     '''
    #     是否会员，如果是会员则续费 ，否则选择套餐进行购买，购买套餐2
    #     :return:
    #     '''
    #     eles = self.driver.find_elements_by_xpath("//*[@text='立即续费']")  # 可用
    #     if len(eles) == 1:
    #         self.prime.click_File_opens02()  #续费
    #         self.members.prime_user02() #选择套餐2 进行开通
    #
    #     else:
    #         self.members.prime_user02() #选择套餐2 进行开通
    # def test_prime_pay03(self):
    #     '''
    #     是否会员，如果是会员则续费 ，否则选择套餐进行购买，购买套餐1
    #     :return:
    #     '''
    #     eles = self.driver.find_elements_by_xpath("//*[@text='立即续费']")  # 可用
    #     if len(eles) == 1:
    #         self.prime.click_File_opens01()  #续费
    #         self.members.prime_user03() #选择套餐3 进行开通
    #
    #     else:
    #         self.members.prime_user03() #选择套餐3 进行开通




# if __name__ == '__main__':
#     unittest.main()

if __name__=="__main__":
    pytest.main(['-s','test_prime_pay00.py'])
    # pytest.main(['-s','test_prime_pay00.py'])
# if __name__=="__main__":
#     pytest.main(['-s','-q','--alluredir','report/result','test_prime_pay00.py'])


