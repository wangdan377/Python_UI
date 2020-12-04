from appium  import webdriver
import time,os
import unittest
from TestCase02 import test_beautify
from TestCase02.test_beautify import Beautify_Fair



class universally(object):
    """通用"""
    def __init__(self):
        # self.pic = Beautify_Fair()
        # self.pic.devices()
        # self.pic.connecting01()
        self.pics = Beautify_Fair()
        self.driver = self.pics.devices()
        self.pics.connecting01()
    def camera_pan01(self):
        driver = self.driver
        driver.find_element_by_id("com.zhiyun.cama:id/iv_setting").click()  # 右上角设置的三个点
        driver.find_element_by_id("com.zhiyun.cama:id/rb_general").click()   #通用
        return '通用按钮'
    def camera_pan02(self):
        driver = self.driver
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]").click()		#设备管理
        return '设备管理按钮'
    def camera_pan03(self):
        driver = self.driver
        driver.find_element_by_id("com.zhiyun.cama:id/iv_scan").click()		#刷新
        return '刷新'
    def camera_pan04(self):
        driver = self.driver
        driver.find_element_by_id("com.zhiyun.cama:id/bt_connect").click()		#连接
        return '未连接，点击连接，连接成功'
    def camera_pan05(self):
        driver = self.driver
        driver.find_element_by_id("com.zhiyun.cama:id/tv_cancel").click()  # 取消
        return '点击对勾，然后弹出弹框，点击取消--未连接。点击确定--断开'

    def camera_pan06(self):
        driver = self.driver
        driver.find_element_by_id("com.zhiyun.cama:id/tv_confirm").click()		#断开
        return '点击对勾，然后弹出弹框，点击取消--未连接。点击确定--断开'
    def camera_pan07(self):
        driver = self.driver
        driver.find_element_by_id("com.zhiyun.cama:id/iv_close").click()		#左上角关闭按钮
        return '左上角关闭'

if __name__ == '__main__':
    univ = universally()
    print(univ.camera_pan01())
    print(univ.camera_pan02())
    print(univ.camera_pan03())
    print(univ.camera_pan04())
    print(univ.camera_pan05())
    print(univ.camera_pan06())
    print(univ.camera_pan07())


