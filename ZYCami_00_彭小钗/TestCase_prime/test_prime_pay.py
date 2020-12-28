#!/usr/bin/python
# -*- coding: utf-8 -*-
from ddt import ddt,data,unpack
from Public.Function import *
from Public import Caplictily
from Public.Logins import LogIn
from PO.Login_Element import Login_Page
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
        self.fun = BaseFun(self.driver)
        self.logins = LogIn(self.driver)
        self.prime_pays = Prime_Pay(self.driver)
        self.wx = Wx_Page(self.driver)
        self.wx_pays = Wx_Config(self.driver)   #微信支付密码
        self.prime_buy_equipment = Prime_Buy_Equipment(self.driver)   #购买设备
        self.members = Prime_Members(self.driver)

    # 关闭驱动
    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    # @data(*get_log_data())      #装饰测试方法，拿到几个数据就可以执行用例
    # @unpack                     #根据拿到的数据以都好及逆行拆分
    # @pytest.mark.flaky(rerus=3)
    def test_prime_pay01(self):
        """
        是否会员，如果是会员则续费 ，否则选择套餐进行购买，购买套餐3
        :return:
        """

        """try:
            self.login.click_File_me()  # 登录状态下，点击【我的】页面
            if self.prime.click_File_prime01() == None:  # 如果找到(我的页面里prime)该元素，就继续下面的操作。否则就执行else
                self.fun.saveScreenshot('is login')  # 截图
                # log.logger.error('已登录')

        except:
            self.logins.login_01()
            time.sleep(2)
            self.fun.saveScreenshot('not login')  # 截图
            # log.logger.error('未登录')

        try:
            time.sleep(2)
            # self.prime.click_File_prime01()  # 点击prime
            self.prime.click_File_meal_03()
            if self.prime.click_File_open01() == None:

                # self.fun.saveScreenshot('not prime')  # 截图
                # log.logger.error('继续开通')
                self.wx.click_File_wx_closed()  # 微信支付方式关闭
                self.prime_pays.primes_13()  # 素材与协议
                # self.fun.saveScreenshot('material')  # 截图
                # log.logger.error('开通页素材')
                self.prime_pays.primes_18()  # 素材-有效期
                # self.fun.saveScreenshot('material')  # 截图
                # log.logger.error('续费页素材')

        except:
            self.prime_pays.primes_16()  # 续费开通
            # self.fun.saveScreenshot('is prime')  # 截图
            # log.logger.error('续费开通')
            self.wx.click_File_wx_closed()  # 微信支付方式关闭
            self.prime_pays.primes_13()  # 开通页面素材与协议
            # self.fun.saveScreenshot('material')  # 截图
            # log.logger.error('开通页面素材与协议')
            self.prime_pays.primes_18()  # 开通返回-素材-有效期
            # self.fun.saveScreenshot('material')  # 截图
            # log.logger.error('续费页素材')"""
        """try:
            self.login.click_File_me()
            self.prime.click_File_prime01()
            time.sleep(2)
            # self.fun.saveScreenshot('is login')  # 截图
            # self.driver.save_screenshot('../screen/' + sys._getframe().f_code.co_name + '.png')
        except:
            self.logins.login_01()
            time.sleep(2)
            self.prime.click_File_prime01()
            # self.fun.saveScreenshot('is not login')  # 截图
        finally:
            self.members.prime_user()"""
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


    def test_prime_pay02(self):
        '''
        是否会员，如果是会员则续费 ，否则选择套餐进行购买，购买套餐2
        :return:
        '''
        eles = self.driver.find_elements_by_xpath("//*[@text='立即续费']")  # 可用
        if len(eles) == 1:
            self.prime.click_File_opens02()  #续费
            self.members.prime_user02() #选择套餐2 进行开通

        else:
            self.members.prime_user02() #选择套餐2 进行开通
    def test_prime_pay03(self):
        '''
        是否会员，如果是会员则续费 ，否则选择套餐进行购买，购买套餐1
        :return:
        '''
        eles = self.driver.find_elements_by_xpath("//*[@text='立即续费']")  # 可用
        if len(eles) == 1:
            self.prime.click_File_opens01()  #续费
            self.members.prime_user03() #选择套餐3 进行开通

        else:
            self.members.prime_user03() #选择套餐3 进行开通


# 构建测试套件
"""def Suit():
    suite = unittest.TestSuite()
    # AddTest是要测试的类名，test_01是要执行的测试方法
    suite.addTest(Test_Prime_pay("test_prime_pay01"))
    suite.addTest(Test_Prime_pay("test_prime_pay02"))
    suite.addTest(Test_Prime_pay("test_prime_pay03"))
    return suite"""
if __name__ == '__main__':
    unittest.main()
    """suite = unittest.TestSuite()
    suite.addTest(Test_Prime_pay("test_prime_pay01"))
    soundbox_device = 'XYBK01011204300001'
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    ##将当前时间加入到报告文件名称中，定义测试报告存放路径
    filename = '../report/' + now + 'result.html'  # 第一种方法,相对路径下
    fp = open(filename, 'wb')
    runner = HTMLTestRunnerCN3_pie_chart_screen.HTMLTestRunner(stream=fp, title='测试报告', tester='王丹',
                                                               device=(soundbox_device),
                                                               description='用例执行情况:')
    runner.run(suite)
    # runner.run(Suit())
    fp.close()"""


# if __name__=="__main__":
#     pytest.main(['-s','-q','--alluredir','report/result','test_prime_pay.py'])

# if __name__=="__main__":
#     pytest.main(['-s','-q','--alluredir','report/result','test_abc.py'])
