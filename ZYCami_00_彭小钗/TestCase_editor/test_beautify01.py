#!/usr/bin/python
# -*- coding: utf-8 -*-

from Public import Caplictily
import unittest
import time
import warnings
from Public.Camera_beauti import Beautify_beau

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
        self.beaut = Beautify_beau()

    # 关闭驱动
    @classmethod
    def tearDownClass(self):
        self.driver.quit()


    def test_beau01(self):
        """
        是否会员，如果是会员则续费 ，否则选择套餐进行购买，购买套餐3
        :return:
        """
        time.sleep(5)
        self.beaut.beautify_01()
        time.sleep(5)

if __name__ == '__main__':
    unittest.main()