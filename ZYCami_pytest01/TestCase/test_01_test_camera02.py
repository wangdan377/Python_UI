#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest
from tools.times import sleep
from page_object.camerapage import CameraPage
import allure, os
from common.readelement import read_yaml
from tools.logger import log


@allure.feature("录像")
class TestCamera02:
    """测试录像"""

    def test_front(self, get_driver):
        """前置条件"""
        self.camera = CameraPage(get_driver)
        # self.camera.connect()
        # self.camera.script()
        # self.camera.actions()
        self.camera.video()

    beau_ = read_yaml('Camera')
    beautify_ = [(beau_['美颜'][0]), (beau_['美颜'][1]), (beau_['美颜'][2]),
                 (beau_['美颜'][3]), (beau_['美颜'][9]), (beau_['美颜'][4]), (beau_['美颜'][9]),
                 (beau_['美颜'][5]), (beau_['美颜'][9]), (beau_['美颜'][6]), (beau_['美颜'][9]),
                 (beau_['美颜'][7]), (beau_['美颜'][9]), (beau_['美颜'][8]), (beau_['美颜'][9]),
                 (beau_['导航栏'][2]), (beau_['导航栏'][2])]

    @allure.story("美颜")
    @allure.title("美颜")
    # @pytest.mark.skip(reason="跳过执行这条case")
    @pytest.mark.parametrize("beautify", beautify_)
    def test_camera_beautify(self, get_driver, beautify):
        self.camera = CameraPage(get_driver)
        self.camera.is_click_(beautify)
        sleep(2)

    beau_ = read_yaml('Camera')
    video_resolution_ = [(beau_['视频分辨率'][0]), (beau_['视频分辨率'][3]), (beau_['视频分辨率'][2]),
                         (beau_['视频分辨率'][1]), (beau_['相机'][6])]

    @allure.story("视频分辨率")
    @allure.title("720、1080、4k")
    @pytest.mark.parametrize("video_resolution", video_resolution_)
    def test_camera_motion_delay(self, get_driver, video_resolution):
        self.camera = CameraPage(get_driver)
        self.camera.is_click_(video_resolution)

    beau_ = read_yaml('Camera')
    flash_ = [(beau_['设置'][0]), (beau_['设置'][1]), (beau_['闪光灯'][0]), (beau_['闪光灯'][2]), (beau_['闪光灯'][1]),
              (beau_['闪光灯'][0])]

    @allure.story("闪光灯")
    @allure.title("常亮、关闭")
    @pytest.mark.parametrize("flash", flash_)
    def test_camera_flash(self, get_driver, flash):
        self.camera = CameraPage(get_driver)
        self.camera.is_click_(flash)
        sleep(2)

    beau_ = read_yaml('Camera')
    network_ = [(beau_['网络显示'][0]), (beau_['网络显示'][2]), (beau_['网络显示'][3]), (beau_['网络显示'][1]), (beau_['网络显示'][0])]

    @allure.story("网络显示")
    @allure.title("关闭、方格、对角+方格")
    @pytest.mark.parametrize("network", network_)
    def test_camera_network(self, get_driver, network):
        self.camera = CameraPage(get_driver)
        self.camera.is_click_(network)
        sleep(2)

    beau_ = read_yaml('Camera')
    white_balance_ = [(beau_['白平衡'][0]), (beau_['白平衡'][1]), (beau_['白平衡'][2]), (beau_['白平衡'][3]),
                      (beau_['白平衡'][4]), (beau_['白平衡'][5]), (beau_['相机'][6])]

    @allure.story("白平衡")
    @allure.title("自动、晴天、阴天、白炽灯、荧光灯")
    @pytest.mark.parametrize("white_balance", white_balance_)
    def test_camera_white_balance(self, get_driver, white_balance):
        self.camera = CameraPage(get_driver)
        self.camera.is_click_(white_balance)
        sleep(2)

    beau_ = read_yaml('Camera')
    gesture_control_ = [(beau_['手势控制'][0]),
                        (beau_['手势控制'][1]), (beau_['手势控制'][2]), (beau_['相机'][6]), (beau_['去水印'][0]),
                        (beau_['去水印'][0])]

    @allure.story("手势控制")
    @allure.title("跟随、拍摄")
    @pytest.mark.parametrize("gesture_control", gesture_control_)
    def test_camera_gesture_control(self, get_driver, gesture_control):
        self.camera = CameraPage(get_driver)
        self.camera.is_click_(gesture_control)
        sleep(3)

    beau_ = read_yaml('Camera')
    yun_tai_ = [(beau_['设置'][2]), (beau_['情景模式'][0]),
                (beau_['情景模式'][1]),
                (beau_['跟随模式'][0]), (beau_['相机'][6]),
                (beau_['摇杆速度'][0]), (beau_['摇杆速度'][1]), (beau_['摇杆速度'][2]),
                (beau_['摇杆速度'][3]), (beau_['反向'][0]), (beau_['反向'][0]),
                (beau_['反向'][1]), (beau_['反向'][1]),
                (beau_['M键'][0]), (beau_['M键'][1]), (beau_['M键'][2]),
                (beau_['M键'][3]), (beau_['M键'][0])]

    @allure.story("云台")
    @allure.title("各种模式")
    @pytest.mark.parametrize("yun_tai", yun_tai_)
    def test_camera_yun_tai(self, get_driver, yun_tai):
        self.camera = CameraPage(get_driver)
        self.camera.is_click_(yun_tai)
        sleep(3)

    beau_ = read_yaml('Camera')
    universal_ = [(beau_['设置'][3]), (beau_['通用'][0]),
                  (beau_['通用'][1]),
                  (beau_['通用'][2]), (beau_['通用'][4]), (beau_['通用'][2]), (beau_['通用'][5]), (beau_['通用'][1]),
                  (beau_['通用'][3]), (beau_['通用'][6]), (beau_['导航栏'][2]), (beau_['导航栏'][2])]


    @allure.story("通用")
    @allure.title("设备断开、连接")
    @pytest.mark.parametrize("universal", universal_)
    def test_camera_universal(self, get_driver, universal):
        self.camera = CameraPage(get_driver)
        self.camera.is_click_(universal)
        sleep(3)



if __name__ == '__main__':
    pytest.main(["-s", "test_01_test_camera02.py"])

