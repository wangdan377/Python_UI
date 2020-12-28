#!/usr/bin/python
# -*- coding: utf-8 -*-
from ddt import ddt,data,unpack
from Public.Function import *
from Public import Caplictily
from PO.login_element import Login_Page
from PO.Prime_Element import Prime_Page
from PO.Edit_Element import Edit_Page
from PO.Activation_page import Activation_Page
from Data.data import *
from Public.loged import *
import unittest,pytest

import time,os,sys
import warnings
from appium.webdriver import Remote
import HTMLTestRunnerCN3_pie_chart_screen
log = Logger('D:\ZYCami_00\logs\\error.log', level='debug')

@ddt  #装饰器类
class Test_Prime_03(unittest.TestCase):
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
    #初始化，使用装饰器，这样在用例执行前只初始化一次
    @classmethod
    def setUpClass(self):
        warnings.simplefilter("ignore", ResourceWarning)
        # cls.driver = appium_desired()     #之前的方法
        # cls.driver.start_activity(appPackage,appActivity)     #另外一种启动方式
        #实例化类
        # self.fun = BaseFun(self.driver)
        driver = Caplictily.Driver_Config()
        self.driver = driver.get_driver()
        self.login = Login_Page(self.driver)    #登录
        self.prime = Prime_Page(self.driver)     #prime
        self.action = Activation_Page(self.driver)      #激活设备
        self.fun = BaseFun(self.driver)
    @data(*get_log_data())      #装饰测试方法，拿到几个数据就可以执行用例
    @unpack                     #根据拿到的数据以都好及逆行拆分
    @pytest.mark.flaky(rerus=3)
    def test_prime_03_01(self,username,password):
        '''
        已登录状态下成功激活设备。相机-连接-地理位置-下一步-激活-完成-弹框领取-关闭-确定-非prime用户
        :param username: 账号
        :param password: 密码
        :return:
        '''
        '''try:
            self.fun.click(File_name)
        except AttributeError:
            log.logger.error('访问不到该对象属性')
            self.fun.saveScreenshot('camera01')
        except NoSuchElementException as a:  # 元素不存在，则调用捕获异常处理
            log.logger.error('元素不存在')
            self.fun.saveScreenshot('camera02')
        except NoAlertPresentException as b:  # 捕获意外的异常
            log.logger.warning('警告')
            self.fun.saveScreenshot('camera03')
        except Exception as result:
            log.logger.critical('严重')
            self.fun.saveScreenshot('camera04')
        else:
            pass  # 没有错的情况下执行
        finally:
            pass  # 有没有错，都会执行'''
        self.action.click_File_iv_camera01()    #相机
        time.sleep(5)
        self.action.click_File_bt_connect()     #连接
        time.sleep(5)
        self.action.click_File_authorize_switch()     #地理位置信息
        self.action.click_File_prepare_next()         #下一步
        self.action.click_File_prepare_next()  # 激活
        self.action.click_File_action_complete()  # 完成
        # self.action.click_File_tv_get()       #领取/查看权益
        self.driver.tap([(969, 539)])       #关闭按钮
        time.sleep(5)
        self.action.File_positive()     #关闭后的确定按钮

        # self.action.click_File_cancel()       #弹框取消
        # self.action.click_File_confirm()      #登录
        # self.login.click_File_tv_login()
        # self.login.input_user(username)
        # self.login.input_password(password)
        # self.login.click_File_tv_commit()
        # self.action.File_login_back()   #更换手机号,然后进行登录


        # self.login.click_File_me()            #我的页面
        # self.prime.click_File_prime01()         #点击【prime】
        # self.prime.click_File_year()        #年
        # time.sleep(5)
        # self.prime.click_File_open01()      #立即开通
        # time.sleep(5)
        # self.prime.click_File_Service_Agreement()     #服务协议
        # self.prime.click_File_Service_Back()        #服务协议返回按钮
        # self.prime.click_File_Privacy_Policy()      #隐私政策
        # self.prime.click_File_Service_Back()        #隐私政策返回按钮
        # time.sleep(2)
        # self.fun.swip_left02()                        #向左滑动
        # time.sleep(5)
        # self.prime.click_File_buy_equipment02()       #购买二设备
        # time.sleep(5)
        # self.driver.keyevent(4)                     #返回按钮
        # time.sleep(2)
        # self.fun.swip_up()
        # time.sleep(5)



        """# self.driver.get_screenshot_as_file('../screen/test_camera.png')   #直接存入报告
        self.fun.saveScreenshot('camera')
        self.fun.saveScreenshot('help')

        self.fun.click(File_enter)"""

    def test_prime_03_02(self, username, password):
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
        # self.action.click_File_cancel()       #弹框取消
        # self.action.click_File_confirm()      #登录
        # self.login.click_File_tv_login()
        # self.login.input_user(username)
        # self.login.input_password(password)
        # self.login.click_File_tv_commit()

        # self.action.File_login_back()   #更换手机号,然后进行登录
        # self.action.click_File_confirm()      #登录
        # self.login.click_File_tv_login()
        # self.login.input_user(username)
        # self.login.input_password(password)
        # self.login.click_File_tv_commit()
        self.action.click_File_prepare_next()  # 激活
        time.sleep(3)
        self.action.click_File_action_complete()  # 完成
        time.sleep(10)
        self.action.click_File_tv_get()     #领取
        self.action.click_File_tv_get()     #查看权益
        self.action.click_File_open_at_back()  #返回按钮


        # self.login.click_File_me()            #我的页面
        # self.prime.click_File_prime01()         #点击【prime】
        # self.prime.click_File_year()        #年
        # time.sleep(5)
        # self.prime.click_File_open01()      #立即开通
        # time.sleep(5)
        # self.prime.click_File_Service_Agreement()     #服务协议
        # self.prime.click_File_Service_Back()        #服务协议返回按钮
        # self.prime.click_File_Privacy_Policy()      #隐私政策
        # self.prime.click_File_Service_Back()        #隐私政策返回按钮
        # time.sleep(2)
        # self.fun.swip_left02()                        #向左滑动
        # time.sleep(5)
        # self.prime.click_File_buy_equipment02()       #购买二设备
        # time.sleep(5)
        # self.driver.keyevent(4)                     #返回按钮
        # time.sleep(2)
        # self.fun.swip_up()
        # time.sleep(5)
    def test_prime_03_03(self, username, password):
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
            self.action.File_login_back()   #更换手机号,然后进行登录
            self.action.click_File_confirm()      #登录
            self.login.click_File_tv_login()
            self.login.input_user(username)
            self.login.input_password(password)
            self.login.click_File_tv_commit()
            self.action.click_File_prepare_next()  # 激活
            time.sleep(3)
            self.action.click_File_action_complete()  # 完成
            time.sleep(10)
            self.action.click_File_tv_get()  # 领取
            self.action.click_File_tv_get()  # 查看权益
            self.action.click_File_open_at_back()  # 返回按钮
    def test_prime_03_04(self, username, password):
        '''
        已登录状态下成功激活设备。相机-连接-地理位置-下一步-激活-完成-关闭-确定-我的页面-体验卡领取-领取成功-关闭弹框-立即续费-立即开通-微信支付
        :param username: 账号
        :param password: 密码
        :return:
        '''
        '''try:
            self.fun.click(File_name)
        except AttributeError:
            log.logger.error('访问不到该对象属性')
            self.fun.saveScreenshot('camera01')
        except NoSuchElementException as a:  # 元素不存在，则调用捕获异常处理
            log.logger.error('元素不存在')
            self.fun.saveScreenshot('camera02')
        except NoAlertPresentException as b:  # 捕获意外的异常
            log.logger.warning('警告')
            self.fun.saveScreenshot('camera03')
        except Exception as result:
            log.logger.critical('严重')
            self.fun.saveScreenshot('camera04')
        else:
            pass  # 没有错的情况下执行
        finally:
            pass  # 有没有错，都会执行'''
        self.action.click_File_iv_camera01()  # 相机
        time.sleep(5)
        self.action.click_File_bt_connect()  # 连接
        time.sleep(5)
        self.action.click_File_authorize_switch()  # 地理位置信息
        self.action.click_File_prepare_next()  # 下一步
        self.action.click_File_prepare_next()  # 激活
        self.action.click_File_action_complete()  # 完成
        self.driver.tap([(969, 539)])       #关闭
        self.action.click_File_positive()       #确定按钮
        self.login.click_File_me()      # 我的页面
        self.prime.click_File_prime01()  # 点击【prime】
        self.action.click_File_new_card()      #新的权益卡待领取
        self.action.click_File_receive()        #立即领取
        self.driver.tap([(969, 539)])           # 关闭按钮
        self.action.click_File_Renew_now()  # 立即续费
        self.prime.click_File_open01()  # 立即开通
        self.action.click_File_pay_closed()  # 支付方式关闭
        # self.action.click_File_wx()             #选择微信支付
    def test_prime_03_05(self, username, password):
        '''
        已登录状态下成功激活设备。相机-连接-地理位置-下一步-激活-完成-关闭-确定-我的页面-体验卡领取-领取成功-查看权益-立即续费-立即开通-微信支付
        :param username: 账号
        :param password: 密码
        :return:
        '''
        '''try:
            self.fun.click(File_name)
        except AttributeError:
            log.logger.error('访问不到该对象属性')
            self.fun.saveScreenshot('camera01')
        except NoSuchElementException as a:  # 元素不存在，则调用捕获异常处理
            log.logger.error('元素不存在')
            self.fun.saveScreenshot('camera02')
        except NoAlertPresentException as b:  # 捕获意外的异常
            log.logger.warning('警告')
            self.fun.saveScreenshot('camera03')
        except Exception as result:
            log.logger.critical('严重')
            self.fun.saveScreenshot('camera04')
        else:
            pass  # 没有错的情况下执行
        finally:
            pass  # 有没有错，都会执行'''
        self.action.click_File_iv_camera01()  # 相机
        time.sleep(5)
        self.action.click_File_bt_connect()  # 连接
        time.sleep(5)
        self.action.click_File_authorize_switch()  # 地理位置信息
        self.action.click_File_prepare_next()  # 下一步
        self.action.click_File_prepare_next()  # 激活
        self.action.click_File_action_complete()  # 完成
        self.driver.tap([(969, 539)])       # 关闭
        self.action.click_File_positive()  # 确定按钮
        self.login.click_File_me()          # 我的页面
        self.prime.click_File_prime01()     # 点击【prime】
        self.action.click_File_new_card()   # 新的权益卡待领取
        self.action.click_File_receive()    # 立即领取
        self.action.click_File_tv_get()     #查看权益
        self.action.click_File_Renew_now()      #立即续费
        self.prime.click_File_open01()          #立即开通
        self.action.click_File_pay_closed()     #支付方式关闭
        # self.action.click_File_wx()             #选择微信支付
        # self.action.click_File_tv_get()     #领取
        # self.action.click_File_tv_get()    #查看权益
        # time.sleep(5)
        # self.action.File_positive()  # 关闭后的确定按钮
        # self.action.click_File_cancel()       #弹框取消
        # self.action.click_File_confirm()      #登录
        # self.login.click_File_tv_login()
        # self.login.input_user(username)
        # self.login.input_password(password)
        # self.login.click_File_tv_commit()
        # self.action.File_login_back()   #更换手机号,然后进行登录
        # self.login.click_File_me()            #我的页面
        # self.prime.click_File_prime01()         #点击【prime】
        # self.prime.click_File_year()        #年
        # time.sleep(5)
        # self.prime.click_File_open01()      #立即开通
        # time.sleep(5)
        # self.prime.click_File_Service_Agreement()     #服务协议
        # self.prime.click_File_Service_Back()        #服务协议返回按钮
        # self.prime.click_File_Privacy_Policy()      #隐私政策
        # self.prime.click_File_Service_Back()        #隐私政策返回按钮
        # time.sleep(2)
        # self.fun.swip_left02()                        #向左滑动
        # time.sleep(5)
        # self.prime.click_File_buy_equipment02()       #购买二设备
        # time.sleep(5)
        # self.driver.keyevent(4)                     #返回按钮
        # time.sleep(2)
        # self.fun.swip_up()
        # time.sleep(5)

        """# self.driver.get_screenshot_as_file('../screen/test_camera.png')   #直接存入报告
        self.fun.saveScreenshot('camera')
        self.fun.saveScreenshot('help')

        self.fun.click(File_enter)"""

    def test_prime_03_06(self, username, password):
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
        self.action.click_File_confirm()      #登录
        self.login.click_File_tv_login()
        self.login.input_user(username)
        self.login.input_password(password)
        self.login.click_File_tv_commit()
        self.action.click_File_prepare_next()  # 激活
        self.action.click_File_action_complete()  # 完成
        # self.action.click_File_tv_get()       #领取/查看权益
        self.driver.tap([(969, 539)])  # 关闭按钮
        time.sleep(5)
        self.action.File_positive()  # 关闭后的确定按钮

    def test_prime_03_07(self, username, password):
            '''
            未登录状态下，相机-连接-地理位置-下一步-登录-账号-密码-激活-完成-弹框领取-查看权益-prime用户-返回
            :param username: 账号
            :param password: 密码
            :return:
            '''
            '''try:
                self.fun.click(File_name)
            except AttributeError:
                log.logger.error('访问不到该对象属性')
                self.fun.saveScreenshot('camera01')
            except NoSuchElementException as a:  # 元素不存在，则调用捕获异常处理
                log.logger.error('元素不存在')
                self.fun.saveScreenshot('camera02')
            except NoAlertPresentException as b:  # 捕获意外的异常
                log.logger.warning('警告')
                self.fun.saveScreenshot('camera03')
            except Exception as result:
                log.logger.critical('严重')
                self.fun.saveScreenshot('camera04')
            else:
                pass  # 没有错的情况下执行
            finally:
                pass  # 有没有错，都会执行'''
            self.action.click_File_iv_camera01()  # 相机
            time.sleep(5)
            self.action.click_File_bt_connect()  # 连接
            time.sleep(5)
            self.action.click_File_authorize_switch()  # 地理位置信息
            self.action.click_File_prepare_next()  # 下一步
            self.action.click_File_confirm()  # 登录
            self.login.click_File_tv_login()
            self.login.input_user(username)
            self.login.input_password(password)
            self.login.click_File_tv_commit()
            self.action.click_File_prepare_next()  # 激活
            self.action.click_File_action_complete()  # 完成
            self.action.click_File_tv_get()       #领取/查看权益
            self.action.click_File_tv_get()  # 领取/查看权益
            self.action.click_File_open_at_back()  # 返回按钮
    def test_prime_03_08(self, username, password):
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
            self.action.click_File_confirm()      #登录
            self.login.click_File_tv_login()
            self.login.input_user(username)
            self.login.input_password(password)
            self.login.click_File_tv_commit()
            self.action.File_login_back()  # 更换手机号,然后进行登录
            self.action.click_File_confirm()  # 登录
            self.login.click_File_tv_login()
            self.login.input_user(username)
            self.login.input_password(password)
            self.login.click_File_tv_commit()
            self.action.click_File_prepare_next()  # 激活
            time.sleep(3)
            self.action.click_File_action_complete()  # 完成
            time.sleep(10)
            self.action.click_File_tv_get()  # 领取
            self.action.click_File_tv_get()  # 查看权益
            self.action.click_File_open_at_back()  # 返回按钮

    def test_prime_03_09(self, username, password):
        '''
        未登录状态下，相机-连接-地理位置-下一步-登录-账号-密码-激活-完成-关闭激活弹框-确定-我的页面-体验卡领取-领取-领取成功-关闭弹框-立即续费-立即开通-微信支付
        :param username: 账号
        :param password: 密码
        :return:
        '''
        '''try:
            self.fun.click(File_name)
        except AttributeError:
            log.logger.error('访问不到该对象属性')
            self.fun.saveScreenshot('camera01')
        except NoSuchElementException as a:  # 元素不存在，则调用捕获异常处理
            log.logger.error('元素不存在')
            self.fun.saveScreenshot('camera02')
        except NoAlertPresentException as b:  # 捕获意外的异常
            log.logger.warning('警告')
            self.fun.saveScreenshot('camera03')
        except Exception as result:
            log.logger.critical('严重')
            self.fun.saveScreenshot('camera04')
        else:
            pass  # 没有错的情况下执行
        finally:
            pass  # 有没有错，都会执行'''
        self.action.click_File_iv_camera01()  # 相机
        time.sleep(5)
        self.action.click_File_bt_connect()  # 连接
        time.sleep(5)
        self.action.click_File_authorize_switch()  # 地理位置信息
        self.action.click_File_prepare_next()  # 下一步
        self.action.click_File_confirm()  # 登录
        self.login.click_File_tv_login()
        self.login.input_user(username)
        self.login.input_password(password)
        self.login.click_File_tv_commit()
        self.action.click_File_prepare_next()  # 激活
        self.action.click_File_action_complete()  # 完成
        self.driver.tap([(969, 539)])  # 关闭
        self.action.click_File_positive()  # 确定按钮
        self.login.click_File_me()  # 我的页面
        self.prime.click_File_prime01()  # 点击【prime】
        self.action.click_File_new_card()  # 新的权益卡待领取
        self.action.click_File_receive()  # 立即领取
        self.driver.tap([(969, 539)])  # 关闭按钮
        self.action.click_File_Renew_now()  # 立即续费
        self.prime.click_File_open01()  # 立即开通
        self.action.click_File_pay_closed()  # 支付方式关闭
        # self.action.click_File_wx()             #选择微信支付

    def test_prime_03_10(self, username, password):
        '''
        未登录状态下，相机-连接-地理位置-下一步-登录-账号-密码-激活-完成-关闭激活弹框-确定-我的页面-体验卡领取-领取-领取成功-查看权益-立即续费-立即开通-微信支付
        :param username: 账号
        :param password: 密码
        :return:
        '''
        '''try:
            self.fun.click(File_name)
        except AttributeError:
            log.logger.error('访问不到该对象属性')
            self.fun.saveScreenshot('camera01')
        except NoSuchElementException as a:  # 元素不存在，则调用捕获异常处理
            log.logger.error('元素不存在')
            self.fun.saveScreenshot('camera02')
        except NoAlertPresentException as b:  # 捕获意外的异常
            log.logger.warning('警告')
            self.fun.saveScreenshot('camera03')
        except Exception as result:
            log.logger.critical('严重')
            self.fun.saveScreenshot('camera04')
        else:
            pass  # 没有错的情况下执行
        finally:
            pass  # 有没有错，都会执行'''
        self.action.click_File_iv_camera01()  # 相机
        time.sleep(5)
        self.action.click_File_bt_connect()  # 连接
        time.sleep(5)
        self.action.click_File_authorize_switch()  # 地理位置信息
        self.action.click_File_prepare_next()  # 下一步
        self.action.click_File_confirm()  # 登录
        self.login.click_File_tv_login()
        self.login.input_user(username)
        self.login.input_password(password)
        self.login.click_File_tv_commit()
        self.action.click_File_prepare_next()  # 激活
        self.action.click_File_action_complete()  # 完成
        self.driver.tap([(969, 539)])  # 关闭
        self.action.click_File_positive()  # 确定按钮
        self.login.click_File_me()  # 我的页面
        self.prime.click_File_prime01()  # 点击【prime】
        self.action.click_File_new_card()  # 新的权益卡待领取
        self.action.click_File_receive()  # 立即领取
        self.action.click_File_tv_get()  # 查看权益
        self.action.click_File_Renew_now()  # 立即续费
        self.prime.click_File_open01()  # 立即开通
        self.action.click_File_pay_closed()  # 支付方式关闭
        # self.action.click_File_wx()             #选择微信支付


    # 关闭驱动
    @classmethod
    def tearDownClass(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main
    """suite = unittest.TestSuite()
    suite.addTest(Camera_test("test_camera"))
    soundbox_device = 'XYBK01011204300001'
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    ##将当前时间加入到报告文件名称中，定义测试报告存放路径
    filename = '../report/' + now + 'result.html'  # 第一种方法,相对路径下
    '''# filename = '../report/report' + now + 'result.html'  # 第二种方法,相对路径下+report报告名字
    # filename = '../report'+ os.sep+ 'report' + now + 'result.html'    #第二种方法,相对路径下,上级目录../report文件夹下,分隔符下文件名  os.sep+ 'report'
    # filename = os.getcwd() + os.sep+ 'report' + now + 'result.html'   #相对路径下,该路径下的,所以就到test_case下面了
    # filename = os.path.dirname(os.path.dirname(__file__))+ os.sep + 'report' + now + 'result.html'  #相对路径下,该路径下的,所以就到test_case下面了
    # filename = 'D:\py\ZY_Cami\\report\\report' + now + 'result.html'   #绝对路径下
    # filename = '../' + now + 'result.html'   #../是上级目录,还是在上级目录下
    # filename = '../' + os.sep + 'report' + now + 'result.html'   #还是在上级目录下
    # filename = '../report' + now + 'result.html'  #还是在上级目录下'''
    fp = open(filename, 'wb')
    runner = HTMLTestRunnerCN3_pie_chart_screen.HTMLTestRunner(stream=fp, title='测试报告', tester='王丹',
                                                               device=(soundbox_device),
                                                               description='用例执行情况:')
    runner.run(suite)
    # runner.run(Suit())
    fp.close()"""
