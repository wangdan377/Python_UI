#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
import os,time

#----------------------------未连接硬件，直接进入相机--------------------------
appPackage = 'com.zhiyun.cama'
appActivity = '.splash.SplashActivity'
#点击相机按钮
File_iv_camera1 = (By.ID,'com.zhiyun.cama:id/iv_camera')
#点击帮助
File_ib_help = (By.ID,'com.zhiyun.cama:id/ib_help')
#不连设备,直接进入拍照
File_enter = (By.ID,'com.zhiyun.cama:id/enter')
#连接设备
File_bt_connect = (By.ID,'com.zhiyun.cama:id/bt_connect')

#返回的按钮
File_iv_home = (By.ID,'com.zhiyun.cama:id/iv_home')

#蓝牙
File_iv_bluetooth = (By.ID,'com.zhiyun.cama:id/iv_bluetooth')

#----------------------------------倒计时---------------------------------------
#倒计时按钮
File_countdown = (By.ID, 'com.zhiyun.cama:id/iv_countdown')
# 倒计时 off
File_off = (By.XPATH, "//*[@text='off']")
# 3秒
File_three = (By.XPATH, "//*[@text='3s']")
#5秒
File_five = (By.XPATH, "//*[@text='5s']")
#7秒
File_seven = (By.XPATH, "//*[@text='7s']")

#----------------------------------美颜-------------------------------------
# 美颜

File_beauty = (By.XPATH,"//*[contains(@resource-id, 'com.zhiyun.cama:id/iv_beauty')]")
#进度条
File_sb_roll = (By.ID,'com.zhiyun.cama:id/sb_roll')
#取消美颜
File_cancel_beauty = (By.XPATH, "//[android.widget.LinearLayout[1]/android.widget.'TextView']")
#自动美颜
File_automatic_beauty = (By.XPATH, "//*[@text='自动美颜']")

#瘦脸
File_Face_lift = (By.XPATH, "//*[@text='瘦脸']")

# 磨皮
File_Microder = (By.XPATH, "//*[@text='磨皮']")


#美白
File_Whitening = (By.XPATH, "//*[@text='美白']")

#眼睛放大
File_eye = (By.XPATH, "//*[@text='眼睛放大']")

#光照
File_light = (By.XPATH, "//*[@text='光照']")
#红润
File_rosy = (By.XPATH, "//*[@text='红润']")

# ----------------------------------更多设置-----------------------------
#右边三点
File_iv_setting = (By.ID,'com.zhiyun.cama:id/iv_setting')
#视频
File_rb_video = (By.ID,'com.zhiyun.cama:id/rb_video')
# 云台
File_rb_stabilizer = (By.ID,'com.zhiyun.cama:id/rb_stabilizer')
# 通用
File_rb_general = (By.ID,'com.zhiyun.cama:id/rb_general')
#设备管理
File_Equip_manage = (By.ID,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]')
#设备关闭按钮
File_Equip_close= (By.ID,'com.zhiyun.cama:id/iv_close')
#刷新
File_Equip_scan= (By.ID,'com.zhiyun.cama:id/iv_scan')

#已连接
File_Equip_connected= (By.ID,'com.zhiyun.cama:id/iv_connected')

#取消
File_Equip_cancel= (By.ID,'com.zhiyun.cama:id/tv_cancel')

#断开
File_Equip_confirm = (By.ID,'com.zhiyun.cama:id/tv_confirm')

# -------------------------------------------------------------------闪光灯-------------------------------------------------------------------
#闪光灯
File_flash = (By.ID,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout')
#闪光灯关闭
File_flash_close = (By.ID,'com.zhiyun.cama:id/rb_flash_close')
#闪光灯常亮
File_flash_torch = (By.ID,'com.zhiyun.cama:id/rb_flash_torch')
#闪光灯下拉框回收按钮
File_flash_Recycle = (By.ID,'com.zhiyun.cama:id/cb_video_flash')

# ------------------------------------------------------------网络显示---------------------------------------------------------------
#网络显示大框
File_video = (By.ID,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout')
#网络下拉框回收按钮
File_video_Recycle = (By.ID,'com.zhiyun.cama:id/cb_video_grid')

#方格
File_Checkered = (By.ID,'com.zhiyun.cama:id/rb_grid')
#对角线
File_diagonal = (By.ID,'com.zhiyun.cama:id/rb_grid_and_diagonal')

# -----------------------------------------------------------白平衡---------------------------------------------------------------------
#白平衡打开按钮
File_white_balance = (By.ID,'com.zhiyun.cama:id/tv_white_balance')
#白平衡返回按钮
File_white_back = (By.ID,'com.zhiyun.cama:id/iv_back')
#自动 [96,209][834,329]
File_white_automatic = (By.ID,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RadioGroup/android.widget.RadioButton[1]')
#晴天 [96,329][834,449]
File_white_sunny = (By.ID,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RadioGroup/android.widget.RadioButton[2]')
#阴天		[96,449][834,569]
File_white_cloudy = (By.ID,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RadioGroup/android.widget.RadioButton[3]')
#白炽灯		[96,569][834,689]
File_white_fabric_lamp = (By.ID,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RadioGroup/android.widget.RadioButton[4]')
#荧光灯		[96,689][834,809]
File_white_Fluorescent = (By.ID,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RadioGroup/android.widget.RadioButton[5]')
#返回按钮
File_white_back = (By.ID,'com.zhiyun.cama:id/iv_back')


# --------------------------------------------------------------------手势控制--------------------------------------------------------------------
#手势控制
File_gesture = (By.ID,'com.zhiyun.cama:id/tv_gesture')
#跟随+拍摄
File_gesture_follow = (By.ID,'com.zhiyun.cama:id/fl_follow_take')
#仅拍摄
File_gesture_only_take = (By.ID,'com.zhiyun.cama:id/fl_only_take')
# 返回按钮
File_gesture_back = (By.ID,'com.zhiyun.cama:id/iv_back')

# ---------------------------------------------------------------------水印------------------------------------------------------------------
#开关
File_watermark_open = (By.ID,'com.zhiyun.cama:id/cb_watermark')
#水印文本
File_watermark_text = (By.ID,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.TextView')
#水印大框
File_name_watermark = (By.ID,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[3]')

# ---------------------------------------------------------------------权限------------------------------------------------------------------
#取消
File_button2_recly = (By.ID,'android:id/button2')
#去设置
File_button1_recly = (By.ID,'android:id/button1')
#权限
File_Authority = (By.ID,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.ImageView')
#存储
File_storage = (By.ID,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.ImageView')
#允许
File_allow_radio = (By.ID,'com.android.permissioncontroller:id/allow_radio_button')
#禁止
File_deny_radio = (By.ID,'com.android.permissioncontroller:id/deny_radio_button')
#电话
File_phone = (By.ID,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[4]/android.widget.LinearLayout/android.widget.LinearLayout[3]')
# 返回  然后再返回
File_navigation = (By.ID,'向上导航')
#位置权限信息
File_name = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[5]/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.ImageView')
#仅使用期间允许
File_foreground_only_radio = (By.ID,'com.android.permissioncontroller:id/foreground_only_radio_button')

#相机权限
File_Camera_permissions = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[6]/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.ImageView')
#麦克风权限
File_Microphone_permissions = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[7]/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.ImageView')
#应用内安装其他应用权限
File_Other_applications = (By.ID,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[8]/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.ImageView')


# --------------------------------------------------------------------视频帧率------------------------------------------------------------------
#视频设置
File_Video_settings = (By.ID,'com.zhiyun.cama:id/iv_dpi')
#720P
File_720p = (By.ID,'com.zhiyun.cama:id/rb_resolution_720')
#1080P
File_1080p = (By.ID,'com.zhiyun.cama:id/rb_resolution_1080')
#4k
File_4k = (By.ID,'com.zhiyun.cama:id/rb_resolution_4k')
#返回
File_Video_back = (By.ID,'com.zhiyun.cama:id/iv_back')



# -----------------------------------------------------------------从右到左--------------------------------------------------------------
#SMART
File_script_smart = (By.ID,'com.zhiyun.cama:id/iv_script')
#翻转
File_flip = (By.ID,'com.zhiyun.cama:id/iv_flip')
#拍照
File_action = (By.ID,'com.zhiyun.cama:id/cb_action')
#手势
File_cb_gesture = (By.ID,'com.zhiyun.cama:id/cb_gesture')
#相册
File_photo = (By.ID,'com.zhiyun.cama:id/iv_photo')


# -----------------------------------------------------------------云台------------------------------------------------------------------
#情景模式
File_Scene_mode = (By.ID,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]')
#行走
File_walk = (By.ID,'com.zhiyun.cama:id/rb_walk')
#运动
File_sport = (By.ID,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/com.zhiyun.cama.camera.widget.CheckedGroup/android.widget.RadioButton[2]')


# -----------------------------------------------------------------跟随模式-----------------------------------------------------------------
#进入跟随模式
File_rb_walk = (By.ID,'com.zhiyun.cama:id/rb_walk')
# 左右跟随
File_follow_walk = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/com.zhiyun.cama.camera.widget.CheckedGroup/android.widget.RadioButton[1]')
# 全锁定
File_Full_lock = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/com.zhiyun.cama.camera.widget.CheckedGroup/android.widget.RadioButton[2]')
# 横滚航向跟随
File_Roll_heading_follow = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/com.zhiyun.cama.camera.widget.CheckedGroup/android.widget.RadioButton[3]')
#返回按钮
File_walk_back = (By.ID,'com.zhiyun.cama:id/iv_back')
#变焦速度
File_zoom_speed = (By.ID,'com.zhiyun.cama:id/sb_zoom_speed')

# -----------------------------------------------------------------摇杆速度-----------------------------------------------------------------
#快
File_fast = (By.ID,'com.zhiyun.cama:id/rb_high')
#中
File_in = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/com.zhiyun.cama.camera.widget.CheckedGroup/android.widget.RadioButton[2]')
#慢
File_slow = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/com.zhiyun.cama.camera.widget.CheckedGroup/android.widget.RadioButton[3]')


# -----------------------------------------------------------------水平反向-----------------------------------------------------------------
#大的边框
File_ctv_yaw01 = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]')
#水平反向
File_ctv_yaw02 = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView')
#水平开关
File_ctv_yaw_reverse = (By.ID,'com.zhiyun.cama:id/ctv_yaw_reverse')

# ----------------------------------------------------------------垂直反向-----------------------------------------------------------------
#大框
File_ctv_roll01 = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]')
#垂直反向
File_ctv_roll02 = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView')
#垂直开关
File_ctv_roll_reverse = (By.ID,'com.zhiyun.cama:id/ctv_roll_reverse')

# ----------------------------------------------------------------单击M键-----------------------------------------------------------------
#点击单击M键按钮
File_click_m = (By.ID,'com.zhiyun.cama:id/cb_video_click_m')
#默认
File_default = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/com.zhiyun.cama.camera.widget.CheckedGroup/android.widget.RadioButton[1]')
#切换拍照/录像
File_Switch = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/com.zhiyun.cama.camera.widget.CheckedGroup/android.widget.RadioButton[2]')
#快捷键菜单
File_Shortcut_menu = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/com.zhiyun.cama.camera.widget.CheckedGroup/android.widget.RadioButton[3]')

# ----------------------------------------------------------------云台自动校准-----------------------------------------------------------------
#大框
File_pan = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[3]')

#取消
File_pan_negative = (By.ID,'com.zhiyun.cama:id/negative')

#按钮
File_pan_Button = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.TextView[2]')

#开始
File_pan_begin = (By.ID,'com.zhiyun.cama:id/positive')


# ----------------------------------------------------------------通用-----------------------------------------------------------------
#设备管理
File_equip_Universal = (By.ID,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]')

#关闭
File_equip_close = (By.ID,'com.zhiyun.cama:id/iv_close')

#刷新
File_equip_Refresh = (By.ID,'com.zhiyun.cama:id/iv_scan')

#已连接
File_equip_connected = (By.ID,'com.zhiyun.cama:id/iv_connected')

#取消
File_equip_cancel = (By.ID,'com.zhiyun.cama:id/tv_cancel')

#断开
File_equip_disconnect = (By.ID,'com.zhiyun.cama:id/tv_confirm')

#连接
File_equip_connect = (By.ID,'com.zhiyun.cama:id/bt_connect')
