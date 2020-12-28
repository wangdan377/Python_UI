#!/usr/bin/python
# -*- coding: utf-8 -*-
from PO.Login_Element import Login_Page
from PO.Create_Element import Create_Page
from PO.Edit_Element import Edit_Page
from PO.Publish_Element import Publish_Page
from PO.Me_Element import Me_Page
from Public.Function import BaseFun


#我的公共方法
class Me():
    def __init__(self,driver):
        self.driver = driver
        self.login = Login_Page(self.driver)  # 登录页面元素
        self.create = Create_Page(self.driver)  # 创作页面元素
        self.edit = Edit_Page(self.driver)  #编辑器页面元素
        self.publish = Publish_Page(self.driver) #发布视频页面元素
        self.me = Me_Page(self.driver) #我页面元素
        self.fun = BaseFun(self.driver)

    def vefify_publish_success_msg(self):
        '''
        验证发布视频成功信息是否出现
        '''
        #定义变量flag，初始值为False
        flag = False
        #获取发布视频开始时间
        star_time = self.fun.get_sys_time()
        # print("star_time", star_time)
        print("发布视频开始时间：", star_time)
        #间隔时间检查发布视频成功信息是否出现
        for i in range(20):
            if self.fun.is_element_exist(self.me.File_publish_success_msg):
                flag = True
                # print("Publish video success flag:", flag)
                print("发布视频是否成功标志:", flag)
                break
        # 获取发布视频结束时间
        end_time = self.fun.get_sys_time()
        # 发布视频所用时间
        publish_success_time = (end_time - star_time).seconds
        # print("end_time", end_time)
        print("发布视频结束时间：", end_time)
        # print("Generated video time:", publish_success_time)
        print("发布视频所用时间：%s秒." % publish_success_time)
        return flag













