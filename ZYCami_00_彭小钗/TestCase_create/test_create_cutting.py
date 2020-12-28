#!/usr/bin/python
# -*- coding: utf-8 -*-
from ddt import ddt,data,unpack
from Public.Function import *
from Public import Caplictily
from Public.Logins import LogIn
from PO.Login_Element import Login_Page
from PO.Edit_Element import Edit_Page
from PO.Create_Element import Create_Page
from PO.Publish_Element import Publish_Page
from PO.Prime_Element import Prime_Page
from Public.Prime_Pay import Prime_Pay
from Public.Prime_Equipment import Prime_Buy_Equipment
from Public.Prime_Me_Member import Prime_Members
from Public.Create import Create
from Public.Publish import Publish
from Public import Function
import unittest,pytest
import time,os,sys
import warnings
from common.loged import Logger
import pytest
from common import HTMLTestRunnerCN3_pie_chart_screen


class Test_Create_cutting(unittest.TestCase):
    #初始化，使用装饰器，这样在用例执行前只初始化一次
    @classmethod
    def setUpClass(self):
        warnings.simplefilter("ignore", ResourceWarning)
        driver = Caplictily.Driver_Config()
        self.driver = driver.get_driver()
        self.login = Login_Page(self.driver)    #登录
        self.create = Create_Page(self.driver)   #创作
        self.publish = Publish_Page(self.driver) #发布
        self.fun = BaseFun(self.driver)
        self.logins = LogIn(self.driver)
        self.create_fun = Create(self.driver)
        self.publish_fun = Publish(self.driver)
        self.prime_buy_equipment = Prime_Buy_Equipment(self.driver)   #购买设备
        self.members = Prime_Members(self.driver)
        self.edit = Edit_Page(self.driver)

    # 关闭驱动
    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_create_cutting01(self):
        #点击我的
        self.login.click_File_me()
        time.sleep(1)
        flag = self.fun.is_element_exist(self.login.File_tv_login)
        #未登录，则先登录，否则是已登录状态
        if flag:
            self.logins.login_01()

        #导航到创作页面
        self.create_fun.to_create_page()
        time.sleep(1)
        #创作页面-选择第一个视频
        self.create_fun.select_first_video()
        time.sleep(1)
        # #添加音乐
        # self.create_fun.add_music()
        # #添加文本
        # self.create_fun.add_text()
        # #添加贴纸
        # self.create_fun.add_tags()
        # #添加视频
        # self.create_fun.add_video()
        # #选择比例
        # self.create_fun.select_ratio()
        # # 选择滤镜
        # self.create_fun.select_filter()
        # # 选择变速
        # self.create_fun.select_shifting()
        # # 选择音量
        # self.create_fun.select_volume()
        # # 选择旋转
        # self.create_fun.select_rotation()
        # # 选择画面
        # self.create_fun.select_frames()
        # # 选择排序
        # self.create_fun.select_sort()
        #点击发布按钮
        self.create.click_File_publish()
        time.sleep(15)
        self.publish_fun.input_introduction()
        self.publish_fun.add_tag()
        self.publish.click_File_publish_btn()
        time.sleep(15)


        # self.assertTrue(flag, msg='登录按钮不存在')
        # eles = self.driver.find_elements_by_xpath("//*[@text='登录']")  # 登录
        # time.sleep(2)
        # if len(eles) == 1:
        #     self.logins.login_01()
        #     self.prime.click_File_prime01()
        #     eles = self.driver.find_elements_by_xpath("//*[@text='立即续费']")  # 可用
        #
        #     if len(eles) == 1:
        #         self.prime_pays.primes_20()  # 续费页面 有效期/素材
        #         self.prime.click_File_opens02()  # 续费
        #         self.members.prime_user01()  # 选择套餐3 进行开通
        #         self.prime_pays.primes_19()  # 开通页面素材
        #     else:
        #         self.members.prime_user01()  # 选择套餐3 进行开通
        #         self.prime_pays.primes_19()  # 开通页面素材
        # else:
        #     self.prime.click_File_prime01()
        #     eles = self.driver.find_elements_by_xpath("//*[@text='立即续费']")  # 可用
        #
        #     if len(eles) == 1:
        #         self.prime_pays.primes_20()  # 续费页面 有效期/素材
        #         self.prime.click_File_opens02()  # 续费
        #         self.members.prime_user01()  # 选择套餐1 进行开通
        #         self.prime_pays.primes_19()  # 开通页面素材
        #     else:
        #         self.members.prime_user01()  # 选择套餐1 进行开通
        #         self.prime_pays.primes_19()  # 开通页面素材


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



