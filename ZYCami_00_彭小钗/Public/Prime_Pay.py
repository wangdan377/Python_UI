#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from PO.Prime_Element import Prime_Page
from Public.Function import BaseFun
from Public.Wx_Pay import Wx_Config
from PO.Login_Element import Login_Page
from common.loged import Logger
# log = Logger('D:\ZYCami_00\logs\\error.log', level='debug')
class Prime_Pay():
    '''个人页面进行购买'''
    def __init__(self,driver):
        self.driver =  driver
        self.login = Login_Page(self.driver)  # 登录
        self.prime = Prime_Page(self.driver)  # prime
        self.fun = BaseFun(self.driver)
        self.login = Login_Page(self.driver)
        self.wx_pays = Wx_Config(self.driver)
    def primes_01(self):
        #前提是已登录在个人中心页面
        '''
        未购买的情况下，点击prime-第一个套餐-立即开通
        :return:
        '''
        self.login.click_File_me()      #个人首页
        self.prime.click_File_prime01()     #点击prime
        self.fun.swip_meal01()    #第一个套餐
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("立即开通")').click()
        # self.wx_pays.wx_pay01()  #支付成功的
    def primes_02(self):
        '''
        未购买的情况下，点击prime-第二个套餐-立即开通
        :return:
        '''
        self.login.click_File_me()  # 个人首页
        self.prime.click_File_prime01()  # 点击prime
        self.fun.swip_meal02()  # 第二个套餐
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("立即开通")').click()


    def primes_03(self):
        '''
        未购买的情况下，点击prime-第二个套餐-立即开通
        :return:
        '''
        self.login.click_File_me()  # 个人首页
        self.prime.click_File_prime01()  # 点击prime
        self.fun.swip_meal03()  # 第三个套餐
        time.sleep(3)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("立即开通")').click() # 立即开通，然后走支付
        time.sleep(3)
    def primes_04(self):
        '''
        未购买的情况下，第二个套餐-立即开通
        :return:
        '''
        self.login.click_File_me()  # 个人首页
        self.prime.click_File_prime01()  # 点击prime
        self.fun.swip_meal03()  # 第四个套餐
        time.sleep(3)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("立即开通")').click()
        time.sleep(3)

    def primes_05(self):
        '''
        未购买的情况下，第三个套餐-立即开通
        :return:
        '''
        self.fun.swip_meal03()  # 第三个套餐
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("立即开通")').click()

    def primes_06(self):
        '''
        无prime-个人首页-点击prime-第三个套餐-立即开通-支付成功，返回app-关闭弹框-立即续费-第三个套餐-立即开通
        :return:
        '''
        self.login.click_File_me()  # 个人首页
        self.prime.click_File_prime01()  # 点击prime
        self.fun.swip_meal03()  # 第3个套餐
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("立即开通")').click()
        self.wx_pays.wx_pay01()  #支付成功，返回app
        self.fun.swip_prime_closed()  #关闭弹框
        self.prime.click_File_opens02()  # 续费
        self.fun.swip_meal03()  # 第3个套餐
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("立即开通")').click()


    def primes_07(self):
        '''前提是已经开通
        续费-选择套餐-立即开通
        :return:
        '''
        self.login.click_File_me()  # 个人首页
        self.prime.click_File_prime01()  # 点击prime
        self.prime.click_File_opens02()  #续费
        self.fun.swip_meal03()   # 第3个套餐
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("立即开通")').click()
        time.sleep(2)
        # self.wx_pays.wx_pay01()

    def primes_08(self):
        '''
        prime 个人首页-点击prime-立即续费-第三个套餐-立即开通-微信支付成功-返回商家-查看权益-立即续费-第三个套餐-立即开通
        :return:
        '''
        self.login.click_File_me()  # 个人首页
        self.prime.click_File_prime01()  # 点击prime
        self.prime.click_File_opens02()  #续费
        self.fun.swip_meal03()   # 第3个套餐
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("立即开通")').click()
        self.wx_pays.wx_pay01()  #支付成功，返回app
        self.prime.click_File_interests() #查看权益
        self.prime.click_File_opens02()  #续费
        self.fun.swip_meal03()   # 第3个套餐
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("立即开通")').click()

    def primes_09(self):
        '''
        prime-个人首页-点击prime-立即续费-第三个套餐-立即开通-微信支付成功-返回商家-关闭弹框-到立即开通页面-开通返回按钮-立即续费-第三个套餐-立即开通
        :return:
        '''
        self.login.click_File_me()  # 个人首页
        self.prime.click_File_prime01()  # 点击prime
        self.fun.swip_meal03()   # 第3个套餐
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("立即开通")').click()
        time.sleep(2)
        self.fun.swip_meal03()   # 第3个套餐
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("立即开通")').click()
        time.sleep(2)
        self.wx_pays.wx_pay01()  #支付成功，返回app
        self.fun.swip_prime_closed()  #关闭弹框
        self.fun.swip_return()  #开通页面返回按钮
        self.prime.click_File_opens02()  #续费
        self.fun.swip_meal03()   # 第3个套餐
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("立即开通")').click()
    def primes_10(self):
        '''
        prime-个人首页-点击prime-有效期-有效期返回-立即续费-第三个套餐-立即开通
        :return:
        '''
        self.login.click_File_me()  # 个人首页
        self.prime.click_File_prime01()  # 点击prime
        self.prime.click_File_open_record() #有效期
        self.fun.swip_return()  # 有效期返回
        self.prime.click_File_opens02()  #续费
        self.fun.swip_meal03()   # 第3个套餐
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("立即开通")').click()

    def primes_11(self):
        '''
        prime-个人首页-点击prime-立即续费-第三个套餐-立即开通-微信支付成功-返回商家-查看权益-有效期-有效期返回-立即续费-第三个套餐-立即开通
        :return:
        '''
        self.login.click_File_me()  # 个人首页
        self.prime.click_File_prime01()  # 点击prime
        self.prime.click_File_opens02()  #续费
        self.fun.swip_meal03()   # 第3个套餐
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("立即开通")').click()
        self.wx_pays.wx_pay01()  #支付成功，返回app
        self.fun.swip_return()#返回
        self.prime.click_File_interests()#查看权益
        self.prime.click_File_open_record() #有效期
        self.fun.swip_up()  # 向上滑动
        self.fun.swip_return()  # 有效期返回
        self.prime.click_File_opens02()  #续费
        self.fun.swip_meal03()   # 第3个套餐
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("立即开通")').click()
    def primes_12(self):
        '''
        prime-点击prime-立即续费-服务协议-返回-隐私协议-返回-向上滑动-向下滑动
        :return:
        '''
        self.login.click_File_me()  # 个人首页
        self.prime.click_File_prime01()  # 点击prime
        self.prime.click_File_opens02()  #续费
        self.prime.click_File_Service_Agreement()  # 隐私协议
        self.fun. swip_return() # 返回
        self.prime.click_File_Privacy_Policy()  #服务协议
        self.fun. swip_return() # 返回
        self.fun.swip_up()  #向上滑动
        self.fun.swip_down()  # 向下滑动
    def primes_13(self):
        '''
    开通页面-服务协议-返回-隐私协议-返回-向上滑动-向下滑动	-向上滑动-素材向左滑动-素材向右滑动
        :return:
        '''
        # self.login.click_File_me()  # 个人首页
        # self.prime.click_File_prime01()  # 点击prime
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("隐私协议")').click()
        self.fun. swip_return() # 返回
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("ZHIYUN Prime服务协议")').click()
        self.fun. swip_return() # 返回
        self.fun.swip_up()  #向上滑动
        self.fun.swip_down()  # 向下滑动
        self.fun.swip_up()  # 向上滑动
        self.fun.swip_material_left01() #素材向左
        self.fun.swip_material_right01()    #素材向右

    def primes_14(self):
        '''
        无prime-个人首页-点击prime-素材向左滑动-素材向右滑动
        :return:
        '''
        self.login.click_File_me()  # 个人首页
        self.prime.click_File_prime01()  # 点击prime
        self.fun.swip_material_left01() #向左
        self.fun.swip_material_right01()    #向右
    def primes_15(self):
        '''
        prime-个人首页-点击prime-立即续费-向上滑动-素材向左滑动-素材向右滑动
        :return:
        '''
        self.login.click_File_me()  # 个人首页
        self.prime.click_File_prime01()  # 点击prime
        self.prime.click_File_opens02()  #续费
        self.fun.swip_up()  #向上滑动
        self.fun.swip_material_left01() #向左
        self.fun.swip_material_right01()    #向右

    def primes_16(self):
        '''立即续费'''
        # self.login.click_File_me()  # 个人首页
        # self.prime.click_File_prime01()  # 点击prime
        time.sleep(5)
        self.prime.click_File_opens02()  #续费
        self.fun.swip_meal03()          # 第3个套餐
        self.prime.click_File_opens01()  # 立即开通，然后走支付

        time.sleep(2)
    def primes_17(self):
        '''个人页面-点击prime'''
        self.login.click_File_me()  # 个人首页
        self.prime.click_File_prime01()  # 点击prime
        # time.sleep(5)
        # self.fun.swip_meal03()        # 第3个套餐
    def primes_18(self):
        '''从开通页面协议-素材-返回到续费页面，素材向左-素材向右'''
        self.prime.click_File_Privacy_Policy()  #隐私协议
        self.fun.swip_return()  # 返回
        self.prime.click_File_Service_Agreement()  # ZHIYUN Prime服务协议
        self.fun.swip_return()  # 返回
        time.sleep(2)
        self.fun.swip_up()  # 向上滑动
        self.fun.swip_down()  # 向下滑动
        self.fun.swip_up()  # 向上滑动
        self.fun.swip_material_left01()  # 素材向左
        self.fun.swip_material_right01()  # 素材向右
        self.fun.swip_return() # 开通返回到续费
        self.fun.swip_open_record()  # 有效期
        self.fun.swip_up()  # 向上滑动
        self.fun. swip_return() # 返回
        self.fun.swip_material_left01()  # 素材向左
        self.fun.swip_material_right01()  # 素材向右
        time.sleep(5)
    def primes_19(self):
        '''从开通页面协议-素材向左-素材向右'''
        self.prime.click_File_Privacy_Policy()  # 隐私协议
        self.fun.swip_return()  # 返回
        self.prime.click_File_Service_Agreement()  # ZHIYUN Prime服务协议
        self.fun.swip_return()  # 返回
        time.sleep(2)
        self.fun.swip_up()  # 向上滑动
        self.fun.swip_material_left01()  # 素材向左
        self.fun.swip_material_right01()  # 素材向右
        self.fun.swip_down()  # 向下滑动
        time.sleep(5)

    def primes_20(self):
        '''续费页面，素材向左-素材向右'''
        time.sleep(5)
        self.fun.swip_open_record()  # 有效期
        self.fun.swip_up()  # 向上滑动
        self.fun.swip_down()    # 向下滑动
        self.fun.swip_return()  # 有效期返回
        self.fun.swip_material_left01()  # 向左
        self.fun.swip_material_right01()  # 向右
        time.sleep(5)




