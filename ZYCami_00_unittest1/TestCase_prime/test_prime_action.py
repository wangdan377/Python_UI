#!/usr/bin/python
# -*- coding: utf-8 -*-
from ddt import ddt,data,unpack
from Public.Function import *
from Public import Caplictily
from Public.Logins import LogIn
from Public.Prime_Action import Prime_Action
from PO.login_Element import Login_Page
from PO.Prime_Element import Prime_Page
from PO.Edit_Element import Edit_Page
from Public.Prime_Edit_Member import Prime_Edit_Members
from PO.Wx_Element import Wx_Page
from Public.Prime_Pay import Prime_Pay
from Public.Wx_Pay import Wx_Config
from Public.Prime_Equipment import Prime_Buy_Equipment
from Public.Prime_Backstage import Prime_Bcak
from Public.Prime_Receive_Member import prime_receive_user
from Data.data import *
from common.loged import *
import unittest,pytest
import time,os,sys
import warnings
from appium.webdriver import Remote
import HTMLTestRunnerCN3_pie_chart_screen

# @ddt  #装饰器类
class Test_Prime_01(unittest.TestCase):
    '''已登录、未登录状态下，激活设备'''
    #初始化，使用装饰器，这样在用例执行前只初始化一次
    @classmethod
    def setUpClass(self):
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
        self.prime_back = Prime_Bcak(self.driver)
        self.receive_member = prime_receive_user(self.driver)
        self.edit = Edit_Page(self.driver)
        self.edit_member = Prime_Edit_Members(self.driver)
        self.actions = Prime_Action()
    # @data(*get_log_data())      #装饰测试方法，拿到几个数据就可以执行用例
    # @unpack                     #根据拿到的数据以都好及逆行拆分
    # @pytest.mark.flaky(rerus=3)
    def test_prime_receive_01(self):
        """
        相机-连接-地理位置-下一步
        1.激活-完成-个人主页-首页-弹框领取
        登录-账号-密码-激活-完成
        2.更换-登录-账号-密码-激活-完成
        :param username: 账号
        :param password: 密码
        :return:
        """
        try:    #已登录连接相机激活
            self.actions.test_prime_03_11()
        except:  #未登录 去登录
            self.actions.test_prime_03_14()
        
        finally:    #首页领取prime
            self.actions.test_prime_03_16()
    def test_prime_receive_02(self):
        """
        app启动 - 领取—查看权益 - 立即续费
        app启动 - 关闭—确定关闭 - 个人 / edit
        个人 - prime - 待领取 - 领取 - 查看权益 - 立即续费
        个人 - prime - 待领取 - 领取 - 关闭 - 立即续费
        home - 云编辑 - 领取 - 查看权益 - 立即续费
        home - 云编辑 - 领取 - 关闭 - 立即续费
        :param username: 账号
        :param password: 密码
        :return:
        """
        try:  # app启动-首页领取
            self.receive_member.prime_user_01()
            # self.prime.click_File_interests()
            # time.sleep(3)
            # self.prime.click_File_interests()
            # time.sleep(3)
            # self.prime.click_File_Renew()
        except:  # 如果找不到-则去个人主页领取（第一次领取，有待领取）
            self.receive_member.prime_user_02()
            # self.login.click_File_me()
            # self.prime.click_File_prime01()
            # self.prime.click_File_receive_interests()  # 待领取
            # self.prime.click_File_me_receive()
            # self.fun.swip_prime_closed()
            time.sleep(3)
        finally:  # 第二次直接领取
            self.receive_member.prime_user_03()
            # self.receive_member.prime_user()   #待领取
            # time.sleep(5)
    def test_prime_receive_03(self):
        """
        app启动 - 领取—查看权益 - 立即续费
        app启动 - 关闭—确定关闭 - 个人 / edit
        个人 - prime - 待领取 - 领取 - 查看权益 - 立即续费
        个人 - prime - 待领取 - 领取 - 关闭 - 立即续费
        home - 云编辑 - 领取 - 查看权益 - 立即续费
        home - 云编辑 - 领取 - 关闭 - 立即续费
        :param username: 账号
        :param password: 密码
        :return:
        """
        try:  # app启动-首页领取
            self.receive_member.prime_user_01()
            # self.prime.click_File_interests()
            # time.sleep(3)
            # self.prime.click_File_interests()
            # time.sleep(3)
            # self.prime.click_File_Renew()
        except:  # 如果找不到-则去edit领取
            self.receive_member.prime_user_04()
    # 关闭驱动
    @classmethod
    def tearDownClass(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()
