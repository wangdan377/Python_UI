#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from Public.Function import BaseFun
import time,random
from PO.Edit_Element import Edit_Page

#--------------------创作-----------------
class Create_Page(BaseFun):

    #创作页面-第一个视频
    File_first_video = (By.XPATH, '(//*[@resource-id="com.zhiyun.cama:id/iv_thumbnail"])[1]')
    #视频列表
    File_create_videos = (By.XPATH, '//*[@resource-id="com.zhiyun.cama:id/iv_thumbnail"]')
    #最多只能选择9段视频文本信息
    File_more_than_videos_msg = (By.XPATH, '//*[@text="最多只能选择9段视频"]')
    #打钩按钮
    File_go_editor = (By.XPATH, '//*[@resource-id="com.zhiyun.cama:id/fl_go_editor"]')
# ------------------------------------------------------------发布---------------------------------------------------------------
    # 发布按钮
    File_publish = (By.XPATH, '//*[@text="发布"]')
    #编辑器帮助按钮
    File_help = (By.XPATH, '(//*/android.widget.ImageView)[2]')


    #添加音乐按钮
    File_add_music = (By.XPATH, '//*/android.widget.ImageButton[1]')
    #音乐logo
    File_tv_music = (By.XPATH, '//*/android.widget.ImageView[1]')
    #录音logo
    File_tv_record = (By.XPATH, '//*/android.widget.ImageView[2]')
    #专辑-欢快logo
    File_lively = (By.XPATH, '(//*[@resource-id="com.zhiyun.cama:id/iv_album_thumb"])[1]')
    #下载按钮
    File_download = (By.XPATH, '(//*[@text="下载"])[1]')
    #使用按钮
    File_use = (By.XPATH, '(//*[@text="使用"])[1]')
    #使用按钮列表
    File_use_btns = (By.XPATH, '//*[@text="使用"]')
    #播放按钮列表
    File_iv_music_play_btns = (By.XPATH, '//*[@resource-id="com.zhiyun.cama:id/iv_music_play"]')
    #音乐名称文本列表
    File_tv_music_name_texts = (By.XPATH, '//*[@resource-id="com.zhiyun.cama:id/tv_music_name"]')


    #添加字幕按钮
    File_add_text = (By.XPATH, '//*/android.widget.ImageButton[2]')
    #添加字幕-编辑框
    File_edit_text = (By.XPATH, '//*[@resource-id="com.zhiyun.cama:id/et_text"]')
    #添加字幕-确定按钮
    File_edit_ok = (By.XPATH, '//*[@text="确定"]')
    #添加字幕-第一个字体
    File_first_style = (By.XPATH, '(//*[@resource-id="com.zhiyun.cama:id/iv_font"])[1]')
    #字幕列表
    File_texts = (By.XPATH, '//*[@resource-id="com.zhiyun.cama:id/iv_font"]')
    #字幕下载按钮
    File_text_download_btn = (By.XPATH, '(//*/android.view.ViewGroup/android.view.View[2])[1]')

    #添加样式-样式tab
    File_style_tab = (By.XPATH, '//*/androidx.appcompat.app.ActionBar.Tab[3]')
    #样式列表
    File_styles = (By.XPATH, '//*[@resource-id="com.zhiyun.cama:id/iv_style"]')
    #样式下载按钮
    File_style_download_btn = (By.XPATH, '(//*/android.view.ViewGroup/android.view.View[2])[1]')
    #添加字幕-第二个样式，第一个为取消样式
    # File_second_style = (By.XPATH, '//*/android.view.ViewGroup[2]/android.view.View')
    File_second_style = (By.XPATH, '(//*[@resource-id="com.zhiyun.cama:id/iv_style"])[2]')
    #添加字幕-颜色tab
    File_color_tab = (By.XPATH, '//*/androidx.appcompat.app.ActionBar.Tab[4]')
    #添加字幕-红色按钮
    File_red_color = (By.XPATH, '//*/android.view.ViewGroup[4]/android.view.View')
    #添加字幕-颜色列表
    File_colors = (By.XPATH, '//*/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup')
    #添加字幕-不透明度控制条
    File_opacity_seek_bar = (By.XPATH, '//*[@resource-id="com.zhiyun.cama:id/seek_bar_opacity"]')

    #添加贴纸按钮
    File_tags_tab = (By.XPATH, '//*/android.widget.ImageButton[3]')
    #添加贴纸-第一个贴纸
    File_first_tag = (By.XPATH, '(//*[@resource-id="com.zhiyun.cama:id/iv_sticker_thumbnail"])[1]')
    #贴纸列表
    File_tags = (By.XPATH, '//*[@resource-id="com.zhiyun.cama:id/iv_sticker_thumbnail"]')
    #添加贴纸-下载按钮
    File_tag_download_btn = (By.XPATH, '(//*/android.view.ViewGroup/android.view.View)[2]')

    #添加视频按钮
    File_add_video = (By.XPATH, '//*/android.widget.ImageButton[4]')
    #添加视频-第二个视频
    File_second_video = (By.XPATH, '(//*[@resource-id="com.zhiyun.cama:id/iv_thumbnail"])[2]')
    #添加视频-第三个视频
    File_third_video = (By.XPATH, '(//*[@resource-id="com.zhiyun.cama:id/iv_thumbnail"])[3]')
    #添加视频-打钩按钮
    File_tick = (By.XPATH, '//*[@resource-id="com.zhiyun.cama:id/fl_go_editor"]')

    #取消按钮
    File_iv_cancel = (By.XPATH, '//*[@resource-id="com.zhiyun.cama:id/iv_cancel"]')
    #确认按钮
    File_iv_confirm = (By.XPATH, '//*[@resource-id="com.zhiyun.cama:id/iv_confirm"]')


    #比例按钮
    File_ratio = (By.XPATH, '//*[@text="比例"]')
    #比例--9:16
    File_nine_to_sixteen = (By.XPATH, '//*/android.view.ViewGroup[1]/android.view.View[2]')
    #比例列表
    File_ratio_list = (By.XPATH, '//*/android.view.ViewGroup[1]/android.view.View')

    #滤镜按钮
    File_filter = (By.XPATH, '//*[@text="滤镜"]')
    # File_original_text = (By.XPATH, '//*[@text="原片"]')
    # File_moring_text = (By.XPATH, '//*[@text="清晨"]')
    # File_polaroid_text = (By.XPATH, '//*[@text="宝丽来"]')
    # File_lime_text = (By.XPATH, '//*[@text="青柠"]')

    #滤镜名称列表
    File_filter_name_list = (By.XPATH, '//*[@resource-id="com.zhiyun.cama:id/tv_filter_name"]')

    #滤镜下载按钮
    File_filter_download_btn = (By.XPATH, '(//*/android.view.ViewGroup/android.view.View[2])[1]')

    #滤镜-清晨
    File_morning = (By.XPATH, '//*/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]')
    #滤镜-控制条
    File_filter_seek_bar = (By.XPATH, '//*[@resource-id="com.zhiyun.cama:id/seek_bar_filter_percent"]')

    #变速按钮
    File_shifting = (By.XPATH, '//*[@text="变速"]')
    #变速-1/4变速
    File_one_fourth = (By.XPATH, '//*[@text="1/4x"]')
    #变速列表
    File_shifting_list = (By.XPATH, '//*/android.widget.CheckedTextView')

    #音量按钮
    File_volume = (By.XPATH, '//*[@text="音量"]')
    #音量-音量控制条
    File_volume_seek_bar = (By.XPATH, '//*[@resource-id="com.zhiyun.cama:id/seek_bar_volume"]')

    #旋转按钮
    File_rotation = (By.XPATH, '//*[@text="旋转"]')
    #旋转-左右旋转
    File_rotation_left_right = (By.XPATH, '//*[@resource-id="com.zhiyun.cama:id/iv_contrast"]')

    #画面按钮
    File_frames = (By.XPATH, '//*[@text="画面"]')
    #画面-对比度
    File_contrast = (By.XPATH, '//*[@resource-id="com.zhiyun.cama:id/iv_contrast"]')
    #画面-对比度控制条
    File_stretch_seek_bar = (By.XPATH, '//*[@resource-id="com.zhiyun.cama:id/seek_bar_stretch"]')

    #排序按钮
    File_sort = (By.XPATH, '//*[@text="排序"]')
    #排序-第一个视频
    File_sort_first_video = (By.XPATH, '(//*[@resource-id="com.zhiyun.cama:id/iv_cover"])[1]')
    #排序-第一个视频时间
    File_sort_first_video_time = (By.XPATH, '(//*/android.widget.TextView)[1]')
    #排序-第二个视频
    File_sort_second_video = (By.XPATH, '(//*[@resource-id="com.zhiyun.cama:id/iv_cover"])[2]')
    #排序-第二个视频时间
    File_sort_second_video_time = (By.XPATH, '(//*/android.widget.TextView)[2]')


    #创作页面-选择第一个视频
    def click_File_first_video(self):
        # self.find_element(self.File_first_video).click
        self.tap_element(self.File_first_video)

    #点击打钩按钮
    def click_File_go_editor(self):
        self.tap_element(self.File_go_editor)

    # #点击创作关闭按钮
    # def click_File_title_left(self):
    # File_title_left = (By.ID,'com.zhiyun.cama:id/iv_title_left')

    #点击发布按钮
    def click_File_publish(self):
        self.tap_element(self.File_publish)

    #点击编辑器帮助按钮
    def click_File_help(self):
        self.tap_element(self.File_help)

    #点击添加音乐按钮
    def click_File_add_music(self):
        self.tap_element(self.File_add_music)

    #点击音乐logo
    def click_File_tv_music(self):
        self.tap_element(self.File_tv_music)

    #点击录音logo
    def click_File_tv_record(self):
        self.tap_element(self.File_tv_record)

    #点击专辑-欢快logo
    def click_File_lively(self):
        self.tap_element(self.File_lively)


    #点击下载按钮
    def click_File_download(self):
        self.tap_element(self.File_download)

    #点击使用按钮
    def click_File_use(self):
        self.tap_element(self.File_use)


    #点击添加字幕按钮
    def click_File_add_text(self):
        self.tap_element(self.File_add_text)

    #在添加字幕-编辑框输入文本
    def input_File_edit_text(self, value):
        self.send_keys(self.File_edit_text, value)

    #点击添加字幕-确定按钮
    def click_File_edit_ok(self):
        self.tap_element(self.File_edit_ok)

    #点击添加字幕-第一个字体
    def click_File_first_style(self):
        self.tap_element(self.File_first_style)

    #点击添加字幕-样式tab
    def click_File_style_tab(self):
        self.tap_element(self.File_style_tab)

    #点击添加字幕-第二个样式，第一个为取消样式
    def click_File_second_style(self):
        self.tap_element(self.File_second_style)

    #点击添加字幕-颜色tab
    def click_File_color_tab(self):
        self.tap_element(self.File_color_tab)

    #点击添加字幕-红色按钮
    def click_File_red_color(self):
        self.tap_element(self.File_red_color)

    #点击颜色-不透明度控制条
    def click_File_opacity_seek_bar(self):
        self.swipe_seek_bar(self.File_opacity_seek_bar, 400)

    #移动颜色-不透明度控制条
    def move_File_opacity_seek_bar(self):
        self.move_seek_bar(self.File_opacity_seek_bar)

    #点击添加贴纸按钮
    def click_File_tags_tab(self):
        self.tap_element(self.File_tags_tab)

    #点击添加贴纸-第一个贴纸
    def click_File_first_tag(self):
        self.tap_element(self.File_first_tag)

    #点击添加视频按钮
    def click_File_add_video(self):
        self.tap_element(self.File_add_video)

    #点击添加视频按钮
    def click_File_add_video(self):
        self.tap_element(self.File_add_video)

    #点击添加视频-第三个视频
    def click_File_third_video(self):
        self.tap_element(self.File_third_video)

    #点击添加视频-第二个视频
    def click_File_second_video(self):
        self.tap_element(self.File_second_video)

    #点击添加视频-打钩按钮
    def click_File_tick(self):
        self.tap_element(self.File_tick)

    #点击取消按钮
    def click_File_iv_cancel(self):
        self.tap_element(self.File_iv_cancel)

    #点击确认按钮
    def click_File_iv_confirm(self):
        self.tap_element(self.File_iv_confirm)

    # 点击比例按钮
    def click_File_ratio(self):
        self.tap_element(self.File_ratio)

    # 点击比例--9:16
    def click_File_nine_to_sixteen(self):
        self.tap_element(self.File_nine_to_sixteen)

    # 点击滤镜按钮
    def click_File_filter(self):
        self.tap_element(self.File_filter)

    # 点击滤镜-清晨
    def click_File_morning(self):
        self.tap_element(self.File_morning)

    # 点击滤镜-控制条
    def click_File_filter_seek_bar(self):
        self.swipe_seek_bar(self.File_filter_seek_bar, 300)

    # 点击变速按钮
    def click_File_shifting(self):
        self.tap_element(self.File_shifting)

    # 点击变速-1/4变速
    def click_File_one_fourth(self):
        self.tap_element(self.File_one_fourth)

    # 点击音量按钮
    def click_File_volume(self):
        self.tap_element(self.File_volume)

    # 点击音量-音量控制条
    def click_File_volume_seek_bar(self):
        self.swipe_seek_bar(self.File_volume_seek_bar, 300)

    # 点击旋转按钮
    def click_File_rotation(self):
        self.tap_element(self.File_rotation)

    # 点击旋转-左右旋转
    def click_File_rotation_left_right(self):
        self.tap_element(self.File_rotation_left_right)

    # 点击画面按钮
    def click_File_frames(self):
        self.tap_element(self.File_frames)
    # 点击画面-对比度
    def click_File_contrast(self):
        self.tap_element(self.File_contrast)
    # 点击画面-对比度控制条
    def click_File_stretch_seek_bar(self):
        self.swipe_seek_bar(self.File_stretch_seek_bar, 300)

    # 点击排序按钮
    def click_File_sort(self):
        self.tap_element(self.File_sort)

    #排序-交换两个视频的顺序
    def swap_two_vedio(self):
        #第一个视频元素的坐标
        x1 = self.get_ele_x(self.File_sort_first_video)
        y1 = self.get_ele_y(self.File_sort_first_video)
        #将第二个视频元素的x,y坐标加上20，使其能交换视频顺序成功
        x2 = self.get_ele_x(self.File_sort_second_video)+20
        y2 = self.get_ele_y(self.File_sort_second_video)+20
        #交换视频
        self.move(x1, y1, x2, y2)

    #向左滑动-找到旋转按钮
    def find_rotation(self):
        self.swipe_left_find_ele(self.File_rotation)

    #向左滑动-找到画面按钮
    def find_frames(self):
        self.swipe_left_find_ele(self.File_frames)

    #向左滑动-找到排序按钮
    def find_sort(self):
        self.swipe_left_find_ele(self.File_sort)

    #从上到下点击各个播放音乐按钮
    def click_File_iv_music_play_btns(self):
        #找到多个元素
        eles = self.find_elements(self.File_iv_music_play_btns)
        #获取元素个数
        nums = self.get_elements_num(self.File_iv_music_play_btns)
        for i in range(nums):
            eles[i].click()
            time.sleep(6)
            eles[i].click()

    #随机选取使用音乐，并输出使用的音乐名称
    def select_randomly_music(self):
        #找到多个使用元素
        eles = self.find_elements(self.File_use_btns)
        #找到多个音乐名称元素
        music_name_eles = self.find_elements(self.File_tv_music_name_texts)
        #获取元素个数
        nums = self.get_elements_num(self.File_use_btns) - 1
        #随机选取
        i = random.randint(0, nums)
        print("使用元素的下标为：", i)
        #获取音乐名称
        music_name = music_name_eles[i].text
        print("使用的音乐名称为：", music_name)
        #点击选中的使用按钮
        eles[i].click()

    #点击不同的文本
    def click_File_texts(self):
        self.click_elements(self.File_texts, nums=2)

     #点击文本中的下载按钮
    def click_File_text_download_btn(self):
        self.find_element(self.File_text_download_btn).click()
        time.sleep(2)

    #点击不同的样式
    def click_File_styles(self):
        self.click_elements(self.File_styles, nums=5)

     #点击样式中的下载按钮
    def click_File_style_download_btn(self):
        self.find_element(self.File_style_download_btn).click()
        time.sleep(2)

    #点击不同的颜色
    def click_File_colors(self):
        self.click_elements(self.File_colors)

    #点击不同的贴纸
    def click_File_tags(self):
        self.click_elements(self.File_tags, nums=6)

     #点击贴纸中的下载按钮
    def click_File_tag_download_btn(self):
        self.find_element(self.File_tag_download_btn).click()
        time.sleep(2)


    #点击不同的比例
    def click_File_ratio_list(self):
        self.click_elements(self.File_ratio_list)

    #点击不同的滤镜
    def click_File_filter_name_list(self):
        #定义列表，存放滤镜名称
        filter_name_list = []
        flag = True
        while flag:
            #定位滤镜列表
            eles = self.find_elements(self.File_filter_name_list)
            # 获取滤镜列表元素个数
            nums = self.get_elements_num(self.File_filter_name_list)
            #点击不同的滤镜
            for i in range(nums):
                #若滤镜不为"青橙"，则点击
                if eles[i].text != "青橙":
                    #首次点击所有滤镜元素
                    if eles[i].text not in filter_name_list:
                        eles[i].click()
                        #将已点击的滤镜存放到列表中
                        filter_name_list.append(eles[i].text)
                    #点击到最后一个元素，执行滑动操作
                    if i == nums-1:
                        self.scrool_page_by_eles(eles[i], eles[0])
                #若找到的滤镜为"青橙"，则退出
                else:
                    flag = False
            time.sleep(2)
        print("滤镜名称列表为：", filter_name_list)


     #点击滤镜中的下载按钮
    def click_File_filter_download_btn(self):
        self.find_element(self.File_filter_download_btn).click()
        time.sleep(2)


    #点击不同的变速
    def click_File_shifting_list(self):
        self.click_elements_by_scrool(self.File_shifting_list)















