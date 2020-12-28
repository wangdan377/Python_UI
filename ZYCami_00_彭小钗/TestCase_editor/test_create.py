#!/usr/bin/python
# -*- coding: utf-8 -*-
from Public.Function import *
from Public import Caplictily
from Public.Logins import LogIn
from PO.Login_Element import Login_Page
from PO.Edit_Element import Edit_Page
from PO.Create_Element import Create_Page
from PO.Publish_Element import Publish_Page
from PO.Me_Element import Me_Page
from PO.Camera_Element import Camera_Page
from Public.Create import Create
from Public.Publish import Publish
from Public.Me import Me
from Public.Camera import Camera
import unittest,pytest
import time,os,sys
import warnings
from common.loged import Logger
import pytest
from common import HTMLTestRunnerCN3_pie_chart_screen


class Test_Create(unittest.TestCase):
    #初始化，使用装饰器，这样在用例执行前只初始化一次
    @classmethod
    def setUpClass(self):
        warnings.simplefilter("ignore", ResourceWarning)
        driver = Caplictily.Driver_Config()
        self.driver = driver.get_driver()
        self.login = Login_Page(self.driver)    #登录
        self.create = Create_Page(self.driver)   #创作
        self.publish = Publish_Page(self.driver) #发布
        self.camera = Camera_Page(self.driver)
        self.me = Me_Page(self.driver)  # 我
        self.me = Camera_Page(self.driver)  # 相机
        self.fun = BaseFun(self.driver)
        self.logins = LogIn(self.driver)
        self.create_fun = Create(self.driver)
        self.publish_fun = Publish(self.driver)
        self.me_fun = Me(self.driver)
        self.camera_fun = Camera(self.driver)
        self.edit = Edit_Page(self.driver)

    # 关闭驱动
    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    #1.测试编辑器中创作功能模块，如添加音乐，添加文本，添加样式，添加视频
    #2.对视频的比例，滤镜，变速，声音，旋转，画面，排序进行操作
    #3.发布视频
    #4.上传视频
    def test_create_001(self):
        # self.camera_fun.auto_generate_videos()
        # time.sleep(5)

        # #点击我的
        # self.login.click_File_me()
        # # time.sleep(15)
        # flag = self.fun.is_element_exist(self.login.File_tv_login)
        # #未登录，则先登录，否则是已登录状态
        # if flag:
        #     self.logins.login_01()

        #导航到创作页面
        self.create_fun.to_create_page()
        #创作页面-选择第一个视频
        self.create_fun.select_first_video()
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

        # 选择滤镜
        # self.create_fun.select_filter()

        # # 选择变速
        # self.create_fun.select_shifting()

        # # 选择音量
        # self.create_fun.select_volume()
        time.sleep(10)
        # # 选择旋转
        # self.create_fun.select_rotation()
        # # 选择画面
        # self.create_fun.select_frames()
        # # 选择排序
        # self.create_fun.select_sort()
        # time.sleep(2)
        # #创作页面-点击发布按钮
        # self.create.click_File_publish()
        # #验证生成视频信息是否出现
        # self.assertTrue(self.publish_fun.vefify_generated_video_msg(), msg="生成视频成功信息没有出现，请检查！")
        # #在发布页面输入视频描述信息
        # self.publish_fun.input_introduction()
        # #添加标签
        # self.publish_fun.add_tag()
        # #在发布页面点击发布按钮
        # self.publish.click_File_publish_btn()
        # #验证发布视频成功信息是否出现
        # self.assertTrue(self.me_fun.vefify_publish_success_msg(), msg="发布视频成功信息没有出现，请检查！")
        # time.sleep(2)


    #验证最多选择9个视频
    def test_create_002(self):
        #点击我的
        self.login.click_File_me()
        time.sleep(1)
        flag = self.fun.is_element_exist(self.login.File_tv_login)
        #未登录，则先登录，否则是已登录状态
        if flag:
            self.logins.login_01()

        #导航到创作页面
        self.create_fun.to_create_page()
        #选择10个视频
        self.create_fun.select_ten_videos()
        #验证最多只能选择9段视频信息是否出现
        self.assertTrue(self.create_fun.vefify_more_than_nine_videos_msg())
        time.sleep(2)


    #选择视频并在发布页面退出
    def test_create_003(self):
        #点击我的
        self.login.click_File_me()
        time.sleep(1)
        flag = self.fun.is_element_exist(self.login.File_tv_login)
        #未登录，则先登录，否则是已登录状态
        if flag:
            self.logins.login_01()

        # 导航到创作页面
        self.create_fun.to_create_page()
        # 创作页面-选择第一个视频
        self.create_fun.select_first_video()
        # 创作页面-点击发布按钮
        self.create.click_File_publish()
        # 验证生成视频信息是否出现
        self.assertTrue(self.publish_fun.vefify_generated_video_msg(), msg="生成视频成功信息没有出现，请检查！")
        # 在发布页面输入视频描述信息
        self.publish_fun.input_introduction()
        # 添加标签
        self.publish_fun.add_tag()
        # 在发布页面点击发布按钮
        self.publish.click_File_publish_btn()
        # 验证发布视频成功信息是否出现
        self.assertTrue(self.me_fun.vefify_publish_success_msg(), msg="发布视频成功信息没有出现，请检查！")
        time.sleep(2)










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



