from appium  import webdriver
import time,os
import unittest
from TestCase02.test_beautify import Beautify_Fair
from TestCase02.test_video import Video_Setting

class Camera_Pan(object):
    """云台"""
    def __init__(self):
        # self.pics = Beautify_Fair
        # self.driver = self.pics.devices()
        # self.pics.connecting01()

        self.pics = Beautify_Fair()  # 是实例化
        # self.vides = Video_Setting()
        self.driver = self.pics.devices()
        self.pics.connecting01()

    def camera_pan01(self):
        driver = self.driver
        # self.vides.three_points()
        driver.find_element_by_id("com.zhiyun.cama:id/iv_setting").click()  # 右上角设置的三个点
        driver.find_element_by_id("com.zhiyun.cama:id/rb_stabilizer").click()  # 云台
        return '云台按钮'

    """def scene_mode01(self):
        driver = self.driver
        driver.find_element_by_id("com.zhiyun.cama:id/rb_walk").click()		#行走
        return '情景模式，行走'
    def scene_mode02(self):
        driver = self.driver
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/com.zhiyun.cama.camera.widget.CheckedGroup/android.widget.RadioButton[2]").click()		#运动
        return '情景模式，运动'
    def follow_mode01(self):
        driver = self.driver
        driver.find_element_by_id("com.zhiyun.cama:id/tv_ptz_follow").click()	#进入跟随模式
        return '进入跟随模式'
    def follow_mode02(self):
        driver = self.driver
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/com.zhiyun.cama.camera.widget.CheckedGroup/android.widget.RadioButton[1]").click()		#左右跟随
        return '跟随模式，左右跟随'
    def follow_mode03(self):
        driver = self.driver
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/com.zhiyun.cama.camera.widget.CheckedGroup/android.widget.RadioButton[2]").click()		#全锁定
        return '跟随模式，全锁定'
    def follow_mode04(self):
        driver = self.driver
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/com.zhiyun.cama.camera.widget.CheckedGroup/android.widget.RadioButton[3]").click()		#横滚航向跟随
        return '跟随模式，横航向跟随'
    def follow_mode05(self):
        driver = self.driver
        driver.find_element_by_id("com.zhiyun.cama:id/iv_back").click()	#返回按钮
        return '跟随模式，返回按钮'
    def rocking_bar01(self):
        driver = self.driver
        driver.find_element_by_id("com.zhiyun.cama:id/iv_back").click()	#返回按钮
        return '摇杆速度，快'
    def rocking_bar02(self):
        driver = self.driver
        driver.find_element_by_id("com.zhiyun.cama:id/iv_back").click()	#返回按钮
        return '摇杆速度，中'
    def rocking_bar03(self):
        driver = self.driver
        driver.find_element_by_id("com.zhiyun.cama:id/iv_back").click()	#返回按钮
        return '摇杆速度，慢'

    def focus(self):
        driver = self.driver
        driver.find_element_by_id("com.zhiyun.cama:id/sb_zoom_speed").click()  # 变焦速度
        time.sleep(2)
        driver.tap([(500, 700)])  # 变焦进度条
        return '变焦速度，慢'

    def slides01(self):  # 向上滑动
        driver = self.driver
        x = driver.get_window_size()["width"]
        y = driver.get_window_size()["height"]
        driver.swipe(x * 0.15, y * 0.8, x * 0.15, y * 0.3, 200)  # 向上滑动
        time.sleep(2)
        return '向上滑动'
    def horizontal(self):
        driver = self.driver
        driver.find_element_by_id("com.zhiyun.cama:id/ctv_yaw_reverse").click()		#水平开关
        return '水平反向开'
    def perpendicular(self):
        driver = self.driver
        driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView").click()  # 垂直反向
        driver.find_element_by_id("com.zhiyun.cama:id/ctv_roll_reverse").click()  # 垂直开关
        return '垂直反向开'

    def click01(self):
        driver = self.driver
        driver.find_element_by_id("com.zhiyun.cama:id/cb_video_click_m").click()  	#点击单击M键按钮
        #这里需要再加一步向上滑动
        return '单击M键按钮'
    def click02(self):
        driver = self.driver
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/com.zhiyun.cama.camera.widget.CheckedGroup/android.widget.RadioButton[1]").click()		#默认
        return '单击M键默认'
    def click03(self):
        driver = self.driver
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/com.zhiyun.cama.camera.widget.CheckedGroup/android.widget.RadioButton[2]").click()		#切换拍照/录像
        return '切换拍照/录像'
    def click04(self):
        driver = self.driver
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/com.zhiyun.cama.camera.widget.CheckedGroup/android.widget.RadioButton[3]").click()		#快捷键菜单
        #再加一步关闭M键
        return '快捷键菜单'
    def automatic_calibration(self):
        driver = self.driver
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.TextView[2]").click()		#按钮
        driver.find_element_by_id("com.zhiyun.cama:id/positive").click()  # 开始
        time.sleeep(2)
        return '水平反向开'"""

if __name__ == '__main__':
    came = Camera_Pan()
    print(came.camera_pan01())
    """print(came.scene_mode01())
    print(came.scene_mode02())
    print(came.scene_mode03())
    print(came.scene_mode04())
    print(came.scene_mode05())
    print(came.focus())
    print(came.slides01())
    print(came.rocking_bar03())
    print(came.horizontal())
    print(came.perpendicular())
    print(came.click01())
    print(came.click02())
    print(came.click03())
    print(came.click04())
    print(came.automatic_calibration())"""
