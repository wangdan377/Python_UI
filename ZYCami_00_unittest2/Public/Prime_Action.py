#!/usr/bin/python
# -*- coding: utf-8 -*-
import time,os
from PO.Activation_Element import Activation_Page
from Public.Function import BaseFun
from Public.Logins import LogIn
from PO.login_Element import Login_Page
from Public.Prime_Backstage import Prime_Bcak
from Public.Prime_Receive_Member import prime_receive_user
class Prime_Action():
    '''
        已登录状态下成功激活设备。相机-连接-地理位置-下一步-激活-完成-弹框领取-关闭-确定-非prime用户
        已登录状态下成功激活设备。相机-连接-地理位置-下一步-激活-完成-弹框领取-查看权益-prime用户-返回
        已登录状态下，相机-连接-地理位置-下一步-更换-登录-账号-密码-激活-完成-弹框领取-查看权益-prime用户-返回
        已登录状态下成功激活设备。相机-连接-地理位置-下一步-激活-完成-关闭-确定-我的页面-体验卡领取-领取成功-关闭弹框-立即续费-立即开通-微信支付
        已登录状态下成功激活设备。相机-连接-地理位置-下一步-激活-完成-关闭-确定-我的页面-体验卡领取-领取成功-查看权益-立即续费-立即开通-微信支付
        未登录状态下，相机-连接-地理位置-下一步-登录-账号-密码-激活-完成-弹框领取-关闭-确定-非prime用户
        未登录状态下，相机-连接-地理位置-下一步-登录-账号-密码-激活-完成-弹框领取-查看权益-prime用户-返回
        未登录状态下，相机-连接-地理位置-下一步-登录-账号-密码-更换-登录-账号-密码-激活-完成-弹框领取-查看权益-prime用户-返回
        未登录状态下，相机-连接-地理位置-下一步-登录-账号-密码-激活-完成-关闭激活弹框-确定-我的页面-体验卡领取-领取-领取成功-关闭弹框-立即续费-立即开通-微信支付
        未登录状态下，相机-连接-地理位置-下一步-登录-账号-密码-激活-完成-关闭激活弹框-确定-我的页面-体验卡领取-领取-领取成功-查看权益-立即续费-立即开通-微信支付

        '''
    def __init__(self,driver):
        self.driver = driver
        self.action = Activation_Page(self.driver)
        self.fun = BaseFun(self.driver)
        self.logins = LogIn(self.driver)
        self.login = Login_Page(self.driver)
        self.prime_back = Prime_Bcak(self.driver)
        self.receive_member = prime_receive_user(self.driver)


    def test_prime_03_01(self):
        '''
        已登录状态下成功激活设备。相机-连接-地理位置-下一步-激活-完成-弹框领取-关闭-确定-非prime用户
        :param username: 账号
        :param password: 密码
        :return:
        '''
        self.action.click_File_iv_camera01()  # 相机
        time.sleep(5)
        self.action.click_File_bt_connect()  # 连接
        time.sleep(5)
        self.action.click_File_authorize_switch()  # 地理位置信息
        self.action.click_File_prepare_next()  # 下一步
        self.action.click_File_prepare_next()  # 激活
        self.action.click_File_action_complete()  # 完成
        self.fun.swip_prime_closed()  # 弹框关闭按钮
        time.sleep(2)
        self.action.File_positive()  # 关闭后的确定按钮

    def test_prime_03_02(self):
        '''
        已登录状态下成功激活设备。相机-连接-地理位置-下一步-激活-完成-弹框领取-查看权益-prime用户-返回
        :param username:账号
        :param password:密码
        :return:
        '''
        self.action.click_File_iv_camera01()  # 相机
        time.sleep(10)
        self.action.click_File_bt_connect()  # 连接
        time.sleep(15)
        self.action.click_File_authorize_switch()  # 地理位置信息
        self.action.click_File_prepare_next()  # 下一步
        self.action.click_File_prepare_next()  # 激活
        time.sleep(3)
        self.action.click_File_action_complete()  # 完成
        time.sleep(10)
        self.action.click_File_tv_get()  # 领取
        self.action.click_File_tv_get()  # 查看权益
        self.action.click_File_open_at_back()  # 返回按钮

    def test_prime_03_03(self):
        '''
        已登录状态下，相机-连接-地理位置-下一步-更换-登录-账号-密码-激活-完成-弹框领取-查看权益-prime用户-返回
        :param username:账号
        :param password:密码
        :return:
        '''
        self.action.click_File_iv_camera01()  # 相机
        time.sleep(10)
        self.action.click_File_bt_connect()  # 连接
        time.sleep(15)
        self.action.click_File_authorize_switch()  # 地理位置信息
        self.action.click_File_prepare_next()  # 下一步
        self.action.File_login_back()  # 更换手机号,然后进行登录
        self.action.click_File_confirm()  # 点击登录(更换手机后有个弹框，取消和登录)
        self.logins.login_01()
        self.action.click_File_prepare_next()  # 激活
        time.sleep(3)
        self.action.click_File_action_complete()  # 完成
        time.sleep(10)
        self.action.click_File_tv_get()  # 领取
        self.action.click_File_tv_get()  # 查看权益
        self.action.click_File_open_at_back()  # 返回按钮

    def test_prime_03_04(self):
        '''
        已登录状态下成功激活设备。激活后不领取，去个人主页领取
        相机-连接-地理位置-下一步-激活-完成-关闭-确定-我的页面-prime-体验卡领取-领取-关闭弹框-立即续费
        :param username: 账号
        :param password: 密码
        :return:
        '''
        self.action.click_File_iv_camera01()  # 相机
        time.sleep(15)
        self.action.click_File_bt_connect()  # 连接
        time.sleep(15)
        self.action.click_File_authorize_switch()  # 地理位置信息
        self.action.click_File_prepare_next()  # 下一步
        self.action.click_File_prepare_next()  # 激活
        self.action.click_File_action_complete()  # 完成
        self.fun.swip_prime_closed()  # 弹框关闭按钮
        self.action.click_File_positive()  # 弹框确定按钮
        self.prime_back.primes_back_04()   #领取prime-关闭

    def test_prime_03_05(self):
        '''
        已登录状态下成功激活设备。相机-连接-地理位置-下一步-激活-完成-关闭-确定-我的页面-体验卡领取-领取成功-查看权益-立即续费-立即开通-微信支付
        :param username: 账号
        :param password: 密码
        :return:
        '''
        self.action.click_File_iv_camera01()  # 相机
        time.sleep(5)
        self.action.click_File_bt_connect()  # 连接
        time.sleep(5)
        self.action.click_File_authorize_switch()  # 地理位置信息
        self.action.click_File_prepare_next()  # 下一步
        self.action.click_File_prepare_next()  # 激活
        self.action.click_File_action_complete()  # 完成
        self.fun.swip_prime_closed() # 弹框关闭
        self.action.click_File_positive()  # 确定按钮
        self.prime_back.primes_back_03()   #领取prime-查看权益

    def test_prime_03_06(self):
        '''
        未登录状态下，相机-连接-地理位置-下一步-登录-账号-密码-激活-完成-弹框领取-关闭-确定-非prime用户
        :param username: 账号
        :param password: 密码
        :return:
        '''

        self.action.click_File_iv_camera01()  # 相机
        time.sleep(5)
        self.action.click_File_bt_connect()  # 连接
        time.sleep(5)
        self.action.click_File_authorize_switch()  # 地理位置信息
        self.action.click_File_prepare_next()  # 下一步
        self.action.click_File_confirm()  # 登录
        self.logins.login_01()
        self.action.click_File_prepare_next()  # 激活
        self.action.click_File_action_complete()  # 完成
        self.fun.swip_prime_closed()  # 弹框关闭按钮
        time.sleep(5)
        self.action.File_positive()  # 关闭后的确定按钮

    def test_prime_03_07(self):
        '''
        未登录状态下，相机-连接-地理位置-下一步-登录-账号-密码-激活-完成-弹框领取-查看权益-prime用户-返回
        :param username: 账号
        :param password: 密码
        :return:
        '''

        self.action.click_File_iv_camera01()  # 相机
        time.sleep(5)
        self.action.click_File_bt_connect()  # 连接
        time.sleep(5)
        self.action.click_File_authorize_switch()  # 地理位置信息
        self.action.click_File_prepare_next()  # 下一步
        self.action.click_File_confirm()  # 登录
        self.logins.login_01() #去登录
        self.action.click_File_prepare_next()  # 激活
        self.action.click_File_action_complete()  # 完成
        self.action.click_File_tv_get()  # 领取/查看权益
        self.action.click_File_tv_get()  # 领取/查看权益
        self.action.click_File_open_at_back()  # 返回按钮

    def test_prime_03_08(self):
        '''
        未登录状态下，相机-连接-地理位置-下一步-登录-账号-密码-更换-登录-账号-密码-激活-完成-弹框领取-查看权益-prime用户-返回
        :param username:账号
        :param password:密码
        :return:
        '''
        self.action.click_File_iv_camera01()  # 相机
        time.sleep(10)
        self.action.click_File_bt_connect()  # 连接
        time.sleep(15)
        self.action.click_File_authorize_switch()  # 地理位置信息
        self.action.click_File_prepare_next()  # 下一步
        self.action.click_File_confirm()  # 登录
        self.logins.login_01() #去登录
        self.action.File_login_back()  # 更换手机号,然后进行登录
        self.action.click_File_confirm()  # 登录
        self.logins.login_01() #去登录
        self.action.click_File_prepare_next()  # 激活
        time.sleep(3)
        self.action.click_File_action_complete()  # 完成
        time.sleep(10)
        self.action.click_File_tv_get()  # 领取
        self.action.click_File_tv_get()  # 查看权益
        self.action.click_File_open_at_back()  # 返回按钮

    def test_prime_03_09(self):
        '''
        未登录状态下，相机-连接-地理位置-下一步-登录-账号-密码-激活-完成-关闭激活弹框-确定-我的页面-体验卡领取-领取-领取成功-关闭弹框-立即续费-立即开通-微信支付
        :param username: 账号
        :param password: 密码
        :return:
        '''
        self.action.click_File_iv_camera01()  # 相机
        time.sleep(5)
        self.action.click_File_bt_connect()  # 连接
        time.sleep(5)
        self.action.click_File_authorize_switch()  # 地理位置信息
        self.action.click_File_prepare_next()  # 下一步
        self.action.click_File_confirm()  # 登录
        self.logins.login_01()  #登录
        self.action.click_File_prepare_next()  # 激活
        self.action.click_File_action_complete()  # 完成
        self.fun.swip_prime_closed()  # 弹框关闭
        self.action.click_File_positive()  # 确定按钮
        self.prime_back.primes_back_04()   #领取prime-关闭

    def test_prime_03_10(self):
        '''
        未登录状态下，相机-连接-地理位置-下一步-登录-账号-密码-激活-完成-关闭激活弹框-确定-我的页面-体验卡领取-领取-领取成功-查看权益-立即续费-立即开通-微信支付
        :param username: 账号
        :param password: 密码
        :return:
        '''
        self.action.click_File_iv_camera01()  # 相机
        time.sleep(5)
        self.action.click_File_bt_connect()  # 连接
        time.sleep(5)
        self.action.click_File_authorize_switch()  # 地理位置信息
        self.action.click_File_prepare_next()  # 下一步
        self.action.click_File_confirm()  # 登录
        self.logins.login_01()  #登录
        self.action.click_File_prepare_next()  # 激活
        self.action.click_File_action_complete()  # 完成
        self.fun.swip_prime_closed()  # 弹框关闭按钮
        self.action.click_File_positive()  # 确定按钮
        self.prime_back.primes_back_03()   #领取prime-关闭
    def test_prime_03_11(self):
        '''
        未登录状态下，相机-连接-地理位置-下一步-登录-账号-密码-激活-完成-关闭激活弹框-确定-我的页面-体验卡领取-领取-领取成功-查看权益-立即续费-立即开通-微信支付
        :param username: 账号
        :param password: 密码
        :return:
        '''
        self.action.click_File_iv_camera01()  # 相机
        time.sleep(5)
        self.action.click_File_bt_connect()  # 连接
        time.sleep(5)
        self.action.click_File_authorize_switch()  # 地理位置信息
        self.action.click_File_prepare_next()  # 下一步
        self.action.click_File_prepare_next()  # 激活
        time.sleep(3)
        self.action.click_File_action_complete()  # 完成
        time.sleep(2)

    def test_prime_03_12(self):
        self.action.click_File_prepare_next()  # 激活
        time.sleep(3)
        self.action.click_File_action_complete()  # 完成

        time.sleep(2)

    def test_prime_03_13(self):
        '''
        激活-完成-我的页面-体验卡领取-领取-领取成功-查看权益-立即续费-立即开通-微信支付
        :param username: 账号
        :param password: 密码
        :return:
        '''
        self.prime_back.primes_back_03()   #领取prime-关闭

    def test_prime_03_14(self):
        '''
        未登录状态下-登录-账号-密码-激活-完成
        :param username: 账号
        :param password: 密码
        :return:
        '''

        self.action.click_File_confirm()  # 登录
        self.logins.login_01()  #登录
        self.action.click_File_prepare_next()  # 激活
        self.action.click_File_action_complete()  # 完成

    def test_prime_03_15(self):
        '''
        更换-登录-账号-密码-激活-完成
        :param username:账号
        :param password:密码
        :return:
        '''

        self.action.click_File_charge_phone()   #更换
        self.action.click_File_confirm()  # 点击登录
        self.logins.login_01() #去登录
        self.action.click_File_prepare_next()  # 激活
        time.sleep(3)
        self.action.click_File_action_complete()  # 完成
        time.sleep(2)
    def test_prime_03_16(self):
        '''
        个人中心-首页-领取
        :return:
        '''
        self.login.click_File_me()
        self.login.click_File_Home()
        self.receive_member.prime_user_01()     #首页领取
