#!/usr/bin/python
# -*- coding: utf-8 -*-
from PO.Login_Element import Login_Page
from PO.Create_Element import Create_Page
from PO.Edit_Element import Edit_Page
from Public.Function import BaseFun
import time


#创作的公共方法
class Create():
    def __init__(self, driver):
        self.driver = driver
        self.login = Login_Page(self.driver)  # 登录页面元素
        self.create = Create_Page(self.driver)  # 创作页面元素
        self.edit = Edit_Page(self.driver)  #编辑器页面元素
        self.fun = BaseFun(self.driver)

    def to_create_page(self):
        '''
        导航到创作页面
        '''
        #点击编辑器
        self.login.click_File_Editor()
        #点击创作按钮
        self.edit.click_File_create()
        time.sleep(1)

    def select_first_video(self):
        '''
        在创作页面-选择第一个视频
        '''
        #选择第一个视频
        self.create.click_File_first_video()
        #点击打钩按钮
        self.create.click_File_go_editor()
        time.sleep(1)

    def select_ten_videos(self):
        '''
        在创作页面-选择10个视频
        '''
        self.fun.tap_elements(self.create.File_create_videos, 10)

    def add_music(self):
        '''
        创作页面-添加音乐
        '''
        #点击添加音乐按钮
        self.create.click_File_add_music()
        #点击音乐图标
        self.create.click_File_tv_music()
        #点击专辑-欢快logo
        self.create.click_File_lively()
        #将所有音乐播放按钮点击一次
        self.create.click_File_iv_music_play_btns()
        #若下载按钮存在，则先下载音乐
        if self.fun.is_element_exist(self.create.File_download):
            #点击下载按钮
            self.create.click_File_download()
            time.sleep(6)
        #随机选择使用音乐
        self.create.select_randomly_music()

    def add_text(self):
        '''
        创作页面-添加文本
        '''
        # 点击添加字幕按钮
        self.create.click_File_add_text()
        # 点击添加字幕-编辑框
        self.create.input_File_edit_text("Hello!"+self.fun.get_system_time())
        # 点击添加字幕-确定按钮
        self.create.click_File_edit_ok()
        #依次点击添加字幕的字体（前面2个）
        self.create.click_File_texts()
        #若存在下载按钮，点击下载按钮
        if self.fun.is_element_exist(self.create.File_text_download_btn):
            self.create.click_File_text_download_btn()
        #随机选择字体（前面2个）
        self.fun.select_randomly_element(self.create.File_texts, nums=1)
        # 点击添加字幕-样式tab
        self.create.click_File_style_tab()
        # 点击添加字幕-第二个样式，第一个为取消样式
        # self.create.click_File_second_style()
        #依次点击添加字幕的样式（前面5个）
        self.create.click_File_styles()
        #若存在下载按钮，点击下载按钮
        if self.fun.is_element_exist(self.create.File_style_download_btn):
            self.create.click_File_style_download_btn()
        #随机选择样式（前面5个）
        self.fun.select_randomly_element(self.create.File_styles, nums=4)
        # 点击添加字幕-颜色tab
        self.create.click_File_color_tab()
        #点击不同的颜色
        self.create.click_File_colors()
        # 点击添加字幕-红色按钮
        self.create.click_File_red_color()
        #移动控制条，从头到尾
        self.create.move_File_opacity_seek_bar()
        # 点击不透明度控制条
        self.create.click_File_opacity_seek_bar()
        # 点击确认按钮
        self.create.click_File_iv_confirm()

    def add_tags(self):
        '''
        创作页面-添加贴纸
        '''
        # 点击添加贴纸按钮
        self.create.click_File_tags_tab()
        # # 点击添加贴纸-第一个贴纸
        # self.create.click_File_first_tag()
        #依次点击贴纸，前面6个
        self.create.click_File_tags()
        #若存在下载按钮，点击下载按钮
        if self.fun.is_element_exist(self.create.File_tag_download_btn):
            self.create.click_File_tag_download_btn()
        #随机选择贴纸
        self.fun.select_randomly_element(self.create.File_tags, nums=5)
        # 点击确认按钮
        self.create.click_File_iv_confirm()

    def add_video(self):
        '''
        创作页面-添加视频
        '''
        # 点击添加视频按钮
        self.create.click_File_add_video()
        # # 点击添加视频-第三个视频
        # self.create.click_File_third_video()
        # 点击添加视频-第二个视频
        self.create.click_File_second_video()
        # 点击添加视频-打钩按钮
        self.create.click_File_tick()

    def select_ratio(self):
        '''
        创作页面-点击不同的比例-随机选择比例
        '''
        self.create.click_File_ratio()
        # self.create.click_File_nine_to_sixteen()
        #点击不同的比例
        self.create.click_File_ratio_list()
        #随机选择比例
        self.fun.select_randomly_element(self.create.File_ratio_list)
        #点击确认按钮
        self.create.click_File_iv_confirm()

    def select_filter(self):
        '''
        创作页面-选择滤镜-随机选择滤镜
        '''
        #点击滤镜
        self.create.click_File_filter()
        #点击不同的滤镜
        self.create.click_File_filter_name_list()
        #若存在下载按钮，点击下载按钮
        if self.fun.is_element_exist(self.create.File_filter_download_btn):
            self.create.click_File_filter_download_btn()
        #随机选择滤镜
        self.fun.select_randomly_element(self.create.File_filter_name_list, nums=1)
        #移动控制条
        self.fun.move_seek_bar(self.create.File_filter_seek_bar)
        #点击控制条
        self.create.click_File_filter_seek_bar()
        self.create.click_File_iv_confirm()

    def select_shifting(self):
        '''
        创作页面-选择变速-随机选择变速
        '''
        #点击变速
        self.create.click_File_shifting()
        # #选择1/4x
        # self.create.click_File_one_fourth()
        #点击不同的变速按钮
        self.create.click_File_shifting_list()
        #随机选择变速
        self.fun.select_randomly_element(self.create.File_shifting_list)
        self.create.click_File_iv_confirm()

    def select_volume(self):
        '''
        创作页面-选择音量
        '''
        #点击音量
        self.create.click_File_volume()
        #移动控制条
        self.fun.move_seek_bar(self.create.File_volume_seek_bar)
        #点击控制条
        self.create.click_File_volume_seek_bar()
        self.create.click_File_iv_confirm()

    def select_rotation(self):
        '''
        创作页面-选择旋转
        '''
        # 找到旋转
        self.create.find_rotation()
        # 点击旋转
        self.create.click_File_rotation()
        #点击左右旋转
        self.create.click_File_rotation_left_right()
        self.create.click_File_iv_confirm()

    def select_frames(self):
        '''
        创作页面-选择画面
        '''
        #找到画面
        self.create.find_frames()
        #点击画面
        self.create.click_File_frames()
        #选择对比度
        self.create.click_File_contrast()
        # 点击控制条
        self.create.click_File_stretch_seek_bar()
        self.create.click_File_iv_confirm()

    def select_sort(self):
        '''
        创作页面-选择排序
        '''
        #找到排序
        self.create.find_sort()
        #点击排序
        self.create.click_File_sort()
        #交换两个视频顺序
        self.create.swap_two_vedio()
        self.create.click_File_iv_confirm()

    def vefify_more_than_nine_videos_msg(self):
        '''
        验证最多只能选择9段视频信息是否出现
        '''
        # 定义变量flag，初始值为False
        flag = False
        # 间隔时间检查生成视频成功信息是否出现
        for i in range(20):
            if self.fun.is_element_exist(self.create.File_more_than_videos_msg):
                flag = True
                print("最多只能选择9段视频信息是否出现:", flag)
                break
        return flag









