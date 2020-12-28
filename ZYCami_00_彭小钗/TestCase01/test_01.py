#!/usr/bin/python
# -*- coding: utf-8 -*-
from ddt import ddt,data,unpack
from Public.Function import *
from Public import Caplictily
from Public.Logins import LogIn
from PO.login_element import Login_Page
from PO.Prime_Element import Prime_Page
from Public.Prime_Pay import Prime_Pay
from Public.Wx_Pay import Wx_Config
from Public.Prime_Equipment import Prime_Buy_Equipment
from Data.data import *
from common.loged import *
import unittest,pytest
import time,os,sys
import warnings
from appium.webdriver import Remote
import HTMLTestRunnerCN3_pie_chart_screen
log = Logger('D:\ZYCami_00\logs\\error.log', level='debug')

@ddt  #装饰器类
class Test_Prime_01(unittest.TestCase):
    '''已登录状态下，非prime用户，购买一周/二周-协议-隐私政策-购买设备-向上滑动'''
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
        self.wx_pays = Wx_Config(self.driver)   #微信支付密码
        self.prime_buy_equipment = Prime_Buy_Equipment(self.driver)   #购买设备

    @data(*get_log_data())      #装饰测试方法，拿到几个数据就可以执行用例
    @unpack                     #根据拿到的数据以都好及逆行拆分
    @pytest.mark.flaky(rerus=3)

    def test_prime_01(self,username,password):
        """
        未登录状态下去登录，然后购买prime
        :param username: 账号
        :param password: 密码
        :return:
        """


        # self.login.click_File_me()        #登录
        # self.logins.login_01()
        # time.sleep(5)
        # self.prime_pays.primes_06()       #购买第六个套餐
        # self.wx_pays.wx_pay01()       #微信支付
        # self.prime_buy_equipment.Prime_buy_Equipment_01()      #购买设备
        """try:
            # self.login.click_File_me()
            self.prime.click_File_prime01()
            if self.prime.click_File_prime01():
                self.prime_pays.primes_06()
        except:
            self.login.click_File_me()
            time.sleep(2)
            self.logins.login_01()"""
        # 判断是否登录，如果已登录，则继续执行。如果未登录则进行登录
        try:
            self.login.click_File_me()  # 登录状态下，点击【我的】页面
            if self.prime.click_File_prime01() == None:  # 如果找到(我的页面里prime)该元素，就继续下面的操作。否则就执行else
                time.sleep(5)
                print('登录成功')

        except :
            # log.logger.info('没有登录')
            self.logins.login_01()
            time.sleep(5)
        #素材
        """self.login.click_File_me()  # 个人首页
        self.prime.click_File_prime01()  # 点击prime
        self.prime.click_File_Renew()  # 立即续费
        # self.click_File_buy_equipment01()
        time.sleep(2)
        self.fun.swip_up()
        self.fun.swip_material_left01()        #左
        self.fun.swip_material_right01()       #右
        time.sleep(2)"""
        # 判断是否登录，登录了，如果是会员则立即续费，否则选择套餐进行购买
        # 否则进行登录，如果是会员则立即续费，否则选择套餐进行购买
        """try:
            self.login.click_File_me()  # 点击【我的】页面
            self.prime.click_File_prime01()
            if self.prime.click_File_meal_03()== None:  # 如果找到(我的页面里prime)该元素，就继续下面的操作。否则就执行else
                self.prime.click_File_open01()  # 立即开通

        except Exception:

            self.prime.click_File_Renew()  # 立即续费
            time.sleep(5)
            self.prime.click_File_meal_03()
            time.sleep(5)
            self.prime.click_File_open01()
            time.sleep(5)"""
        try:
            self.login.click_File_me()  # 登录状态下，点击【我的】页面
            if self.prime.click_File_prime01() == None:  # 如果找到(我的页面里prime)该元素，就继续下面的操作。否则就执行else
                self.fun.saveScreenshot('is login')  # 截图
                # log.logger.error('已登录')

        except:
            self.logins.login_01()
            time.sleep(2)
            self.fun.saveScreenshot('not login')  # 截图
            # log.logger.error('未登录')

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
