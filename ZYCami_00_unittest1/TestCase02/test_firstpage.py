#coding=utf-8
import os,time
from appium import webdriver
from time import sleep

class FirstPage(object):
    '''编辑'''
    def setup(self):
        desire_capa = {
            'platformName': 'Android',
            'deviceName': '7HX0219918017044',
            'platformVersion': '10',
            'appPackage': 'com.zhiyun.cama',
            'appActivity': '.splash.SplashActivity',
            "noReset": 'true'  # 不做清空操作
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_capa)
        sleep(5)

    def teardown(self):
        self.driver.quit()  # 资源回收

    def test_edit(self):
        pass
        '''打开app
        在首页，点击【+】按钮，切换到编辑页面
        点击【X】,返回
        点击创作，进入选择照片页面，（点击添加音乐、添加字幕、贴纸、比例、滤镜、切割、变速、音量、旋转、画面、排序、删除、撤销、切换横竖屏、多个视频进行切换、播放按钮、编辑使用说明、发布按钮、返回按钮）
        选择照片，
        点击（√）按钮。跳转至发布页面，进行编辑
        # 点击【X】,返回.返回到编辑页面
        点击【发布】按钮
        在合成发布页面，点击获取位置按钮
        在合成发布页面，点击【发布】按钮
        未发布，点击【返回】按钮
        是否保存的弹框，点击【退出】按钮，点击【保存并退出】按钮，返回到编辑页面'''

        self.driver.find_element_by_id("com.zhiyun.cama:id/icon").click()
        self.driver.find_element_by_id("com.zhiyun.cama:id/back").click()
        self.driver.find_element_by_id("com.zhiyun.cama:id/create").click()
        self.driver.find_element_by_id("com.zhiyun.cama:id/iv_thumbnail").click()
        self.driver.find_element_by_id("com.zhiyun.cama:id/fl_go_editor").click()
        # self.driver.find_element_by_id("com.zhiyun.cama:id/iv_title_left").click()    #返回
        self.driver.find_element_by_id("com.zhiyun.cama:id/btn_title_right").click()   #发布
        self.driver.find_element_by_id("com.zhiyun.cama:id/cb_location").click()      #获取位置按钮
        self.driver.find_element_by_id("com.zhiyun.cama:id/pb_compose").click()      #合成发布
        self.driver.find_element_by_accessibility_id()

