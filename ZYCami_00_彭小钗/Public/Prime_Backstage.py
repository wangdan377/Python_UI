#!/usr/bin/python
# -*- coding: utf-8 -*-
from PO.Prime_Element import Prime_Page
from PO.Login_Element import Login_Page
from Public.Function import BaseFun
from Public.Wx_Pay import Wx_Config
import time
class Prime_Bcak():
    '''到个人页面 在个人页面领取、未领取
    在首页领取，如未领取，则去首页领取'''
    def __init__(self,driver):
        self.driver =  driver
        self.prime = Prime_Page(self.driver)
        self.wx = Wx_Config(self.driver)
        self.fun = BaseFun(self.driver)
        self.login = Login_Page(self.driver)


    def primes_back_01(self):
        '''
        #启动app-领取-查看权益-立即续费
        :return:
        '''
        self.prime.click_File_interests()  #领取
        self.prime.click_File_interests()  # 查看权益
        self.prime.click_File_Renew()  # 立即续费


    def primes_back_02(self):
        '''
        启动app-关闭弹框-确定按钮-个人主页-prime-新权益卡领取-领取-立即续费
        :return:
        '''

        self.fun.swip_prime_closed()  # 关闭弹框
        self.prime.click_File_positive()        #prime弹框关掉后，有个确定按钮
        self.login.click_File_me()
        self.prime.click_File_prime01()  # 点击prime
        self.prime.click_File_receive_interests()  # 新的权益卡待领取
        self.prime.click_File_me_receive()  # 立即领取
        self.prime.click_File_interests()  # 查看权益
        self.prime.click_File_Renew()  # 立即续费


    def primes_back_03(self):
        '''
        个人主页-prime-新权益卡领取-领取-查看权益-立即续费
        :return:
        '''
        try:
            self.login.click_File_me()      #个人页面
            self.prime.click_File_prime01()  # 点击prime
            self.prime.click_File_receive_interests()  # 新的权益卡待领取
            self.prime.click_File_me_receive()  # 立即领取
            self.prime.click_File_interests()  # 查看权益
            self.prime.click_File_Renew()  # 立即续费
        except:  #直接领取
            self.prime.click_File_me_receive()
            self.prime.click_File_interests()
            self.prime.click_File_Renew()

    def primes_back_04(self):
        '''
        个人主页-prime-新权益卡领取-领取成功-关闭弹框-立即续费
        :return:
        '''
        self.login.click_File_me()      #个人页面
        self.prime.click_File_prime01()  # 点击prime
        # self.prime.click_File_receive_interests()  # 新的权益卡待领取
        self.prime.click_File_me_receive()  # 立即领取
        self.prime.click_File_me_receive()  # 立即领取.
        time.sleep()
        # self.prime.click_File_me_receive()  # 查看权益
        self.fun.swip_prime_closed()  # 关闭弹框
        self.prime.click_File_Renew()  # 立即续费

    def primes_back_05(self):
        '''
        无prime	待领取页面	素材向左	素材向右	服务协议	返回	隐私协议	万能返回到个人主页
        :return:
        '''
        self.login.click_File_me()      #个人页面
        self.prime.click_File_prime01()  # 点击prime
        self.fun.swip_material_left02()  # 向左
        self.fun.swip_material_right02()  # 向右
        self.fun.swip_prime_closed()  # 服务协议
        self.prime.click_File_Renew()  # 立即续费
        self.prime.click_File_Service_Agreement()  # 隐私协议
        self.prime.click_File_Service_Back()  # 返回
        self.prime.click_File_Privacy_Policy()  # 服务协议
        self.prime.click_File_Service_Back()  # 返回
        self.fun.swip_return()      #万能返回



