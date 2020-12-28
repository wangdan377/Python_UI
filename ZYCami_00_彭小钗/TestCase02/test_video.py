from appium  import webdriver
import time,os
import unittest
from TestCase02 import test_beautify
from TestCase02.test_beautify import Beautify_Fair


class Video_Setting(object):
    """视频"""
    def __init__(self):
        self.pics = Beautify_Fair()
        self.driver = self.pics.devices()
        self.pics.connecting01()

    def three_points(self):
        driver = self.driver
        driver.find_element_by_id("com.zhiyun.cama:id/iv_setting").click()   #右上角设置的三个点
        return '相机右上角三点设置'
    """def flash_light01(self):
        driver = self.driver
        driver.find_element_by_id("com.zhiyun.cama:id/cb_video_flash").click()
        return '闪光灯页面下拉'
    def flash_light02(self):
        driver = self.driver
        driver.find_element_by_id("com.zhiyun.cama:id/rb_flash_close").click()
        return '闪光灯关闭'
    def flash_light03(self):
        driver = self.driver
        driver.find_element_by_id("com.zhiyun.cama:id/rb_flash_torch").click()
        return '闪光灯常亮'
    def flash_light04(self):
        driver = self.driver
        driver.find_element_by_id("com.zhiyun.cama:id/cb_video_flash").click()
        return '闪光灯页面回收'
    def net_display01(self):
        driver = self.driver
        driver.find_element_by_id("com.zhiyun.cama:id/cb_video_grid").click()
        return '网络显示下拉'
    def net_display02(self):
        driver = self.driver
        driver.find_element_by_id("com.zhiyun.cama:id/rb_grid_none").click()
        return '网络关闭'
    def net_display03(self):
        driver = self.driver
        driver.find_element_by_id("com.zhiyun.cama:id/rb_grid").click()
        return '网络方格'
    def net_display04(self):
        driver = self.driver
        driver.find_element_by_id("com.zhiyun.cama:id/rb_grid_and_diagonal").click()
        return '网络对角线+方格'
    def net_display05(self):
        driver = self.driver
        driver.find_element_by_id("com.zhiyun.cama:id/cb_video_grid").click()
        return '网络显示回收'"""
    def white_balance01(self):
        driver = self.driver
        driver.find_element_by_id("com.zhiyun.cama:id/tv_white_balance").click()  # 白平衡打开按钮
        return '白平衡下拉框打开'

    def white_balance02(self):
        driver = self.driver
        driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RadioGroup/android.widget.RadioButton[1]").click()
        # driver.find_element_by_id("com.zhiyun.cama:id/iv_back").click()   #返回按钮
        return '白平衡自动'
    def white_balance03(self):
        driver = self.driver
        # self.white_balance01()
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RadioGroup/android.widget.RadioButton[2]").click()
        # driver.find_element_by_id("com.zhiyun.cama:id/iv_back").click()   #返回按钮
        return '白平衡晴天'
    def white_balance04(self):
        driver = self.driver
        # self.white_balance01()
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RadioGroup/android.widget.RadioButton[3]").click()
        # driver.find_element_by_id("com.zhiyun.cama:id/iv_back").click()   #返回按钮
        return '白平衡阴天'
    def white_balance05(self):
        driver = self.driver
        # self.white_balance01()
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RadioGroup/android.widget.RadioButton[4]").click()
        # driver.find_element_by_id("com.zhiyun.cama:id/iv_back").click()   #返回按钮
        return '白平衡白炽灯'
    def white_balance06(self):
        driver = self.driver
        # self.white_balance01()
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RadioGroup/android.widget.RadioButton[5]").click()  #荧光灯
        time.sleep(3)
        driver.find_element_by_id("com.zhiyun.cama:id/iv_back").click()   #返回按钮
        return '白平衡荧光灯'

    def gesture_control01(self):
        driver = self.driver
        # self.slides01()
        """x = driver.get_window_size()["width"]
        y = driver.get_window_size()["height"]
        driver.swipe(x * 0.15, y * 0.8, x * 0.15, y * 0.3, 200)  # 向下滑动  x不变  y由大变小  美颜向上滑动"""
        driver.find_element_by_id("com.zhiyun.cama:id/tv_gesture").click()
        return '手势控制下拉框'

    def gesture_control02(self):
        driver = self.driver
        driver.find_element_by_id("com.zhiyun.cama:id/fl_follow_take").click()  #跟随+拍摄
        # driver.find_element_by_id("com.zhiyun.cama:id/iv_back").click()   #返回按钮   #返回按钮
        return '跟随+拍摄'
    def gesture_control03(self):
        driver = self.driver
        # self.gesture_control02()
        driver.find_element_by_id("com.zhiyun.cama:id/fl_only_take").click()   #仅拍摄
        driver.find_element_by_id("com.zhiyun.cama:id/iv_back").click()  # 返回按钮
        return '仅拍摄'
    def watermark(self):
        driver = self.driver
        driver.find_element_by_id("com.zhiyun.cama:id/cb_watermark").click()   #水印开关
        driver.find_element_by_id("com.zhiyun.cama:id/cb_watermark").click()
        return '水印'

if __name__ == '__main__':
    vide = Video_Setting()
    print(vide.three_points())
    # print(vide.flash_light01())
    # print(vide.flash_light02())
    # print(vide.flash_light03())
    # print(vide.flash_light04())
    # print(vide.net_display01())
    # print(vide.net_display02())
    # print(vide.net_display03())
    # print(vide.net_display04())
    # print(vide.net_display05())
    print(vide.white_balance01())
    print(vide.white_balance02())
    print(vide.white_balance03())
    print(vide.white_balance04())
    print(vide.white_balance05())
    print(vide.white_balance06())
    print(vide.gesture_control01())
    print(vide.gesture_control02())
    print(vide.gesture_control03())
    print(vide.watermark())
