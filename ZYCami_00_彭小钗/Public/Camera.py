#!/usr/bin/python
# -*- coding: utf-8 -*-
from PO.Camera_Element import Camera_Page
from Public.Function import BaseFun
import time


#发布的公共方法
class Camera():
    def __init__(self,driver):
        self.driver = driver
        self.camera = Camera_Page(self.driver) #发布视频页面元素
        self.fun = BaseFun(self.driver)


    def auto_generate_videos(self):
        '''
        自动生成视频，一个视频10s，一个视频20s
        '''
        #点击相机按钮
        self.camera.click_File_iv_camera()
        #点击帮助按钮
        self.camera.click_File_ib_help()
        #点击直接进入
        self.camera.click_File_enter()
        time.sleep(3)
        #点击samrt图标
        self.camera.click_File_script_smart()
        time.sleep(1)
        #点击拍照按钮
        self.camera.click_File_photo_text()
        time.sleep(5)
        #点击录像文本
        self.camera.click_File_recoding()
        time.sleep(1)
        #生成第1个20s的视频
        # 点击录像按钮
        self.camera.click_File_action()
        time.sleep(20)
        #点击录像按钮
        self.camera.click_File_action()
        # 生成第2个10s的视频
        # 点击录像按钮
        self.camera.click_File_action()
        time.sleep(10)
        #点击录像按钮
        self.camera.click_File_action()
        #点击返回主页按钮
        self.camera.click_File_iv_home()

    def input_introduction(self):
        '''
        输入描述信息
        '''
        #用“你好”与当前系统时间组合
        msg = "你好！"+self.fun.get_system_time()
        #输入描述信息
        self.publish.input_File_introduction(msg)

    def add_tag(self):
        '''
        添加标签
        '''
        #获取时间戳作为唯一标签
        msg = self.fun.get_timestamp()
        #点击添加标签文本
        self.publish.click_File_add_tag()
        #输入标签信息
        self.publish.input_File_add_tag_edit_text(msg)
        #点击添加按钮
        self.publish.click_File_add_btn()

    def vefify_generated_video_msg(self):
        '''
        验证生成视频成功信息是否出现
        '''
        # 定义变量flag，初始值为False
        flag = False
        # 获取生成视频开始时间
        star_time = self.fun.get_sys_time()
        # print("star_time", star_time)
        print("生成视频开始时间：", star_time)
        # 间隔时间检查生成视频成功信息是否出现
        for i in range(20):
            if self.fun.is_element_exist(self.publish.File_generated_video_msg):
                flag = True
                # print("Generated video flag:", flag)
                print("生成视频是否成功标志:", flag)
                break
        # 获取生成视频结束时间
        end_time = self.fun.get_sys_time()
        # 生成视频所用时间
        generated_video_time = (end_time-star_time).seconds
        # print("end_time", end_time)
        print("生成视频结束时间:", end_time)
        # print("Generated video time:", generated_video_time)
        print("生成视频所用时间：%d秒." % generated_video_time)
        return flag













