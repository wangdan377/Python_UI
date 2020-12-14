#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest
from tools.times import sleep
from page_object.camerapage import CameraPage
import allure,os
from common.readelement import read_yaml

@allure.feature("测试相机")
class Testcamera:
    """测试拍照"""
    def test_front(self,get_driver):
        '''
        前置条件
        :param get_driver:
        :return:
        '''
        self.camera = CameraPage(get_driver)
        self.camera.cameras()
        self.camera.help()
        self.camera.enter()


        sleep(3)

    # beautify_ = [(read_yaml('Camera')['美颜'][0]),(read_yaml('Camera')['美颜'][8])]
    # # @pytest.mark.skip(reason="跳过执行这条case")
    # @pytest.mark.parametrize("beautify", beautify_)
    # @allure.story("美颜")
    # @allure.title("美颜")
    # def test_camera_beautify(self,get_driver,beautify):
    #     self.camera = CameraPage(get_driver)
    #     self.camera.is_click_(beautify)
    #     sleep(2)

    # countdown_ = [(read_yaml('Camera')['倒计时'][0]),(read_yaml('Camera')['倒计时'][1])]
    #
    # @pytest.mark.skip(reason="跳过执行这条case")
    # @pytest.mark.parametrize("countdown", countdown_)
    # @allure.story("倒计时")
    # @allure.title("倒计时")
    # def test_camera_countdown(self, get_driver, countdown):
    #     self.camera = CameraPage(get_driver)
    #     self.camera.is_click_(countdown)
    #     sleep(2)

        # self.camera.setting()
        # self.camera.videos()

    # flash_ = [(read_yaml('Camera')['设置'][0]),(read_yaml('Camera')['设置'][1]),(read_yaml('Camera')['闪光灯'][0]),(read_yaml('Camera')['闪光灯'][1]),(read_yaml('Camera')['闪光灯'][2]),(read_yaml('Camera')['闪光灯'][0])]
    # @pytest.mark.parametrize("flash", flash_)
    # @allure.story("闪光灯")
    # @allure.title("关闭、常亮")
    # def test_camera_countdown(self, get_driver,flash):
    #     self.camera = CameraPage(get_driver)
    #     self.camera.is_click_(flash)
    #     sleep(2)

    # Network_ = [(read_yaml('Camera')['设置'][0]),(read_yaml('Camera')['设置'][1]),(read_yaml('Camera')['网络显示'][0]),(read_yaml('Camera')['网络显示'][1]),(read_yaml('Camera')['网络显示'][1]),(read_yaml('Camera')['网络显示'][2]),(read_yaml('Camera')['网络显示'][3]),(read_yaml('Camera')['网络显示'][0])]
    # @pytest.mark.parametrize("Network", Network_)
    # @allure.story("闪光灯")
    # @allure.title("关闭、常亮")
    # def test_camera_countdown(self, get_driver,Network):
    #     self.camera = CameraPage(get_driver)
    #     self.camera.is_click_(Network)
    #     sleep(2)

    # White_balance_ = [(read_yaml('Camera')['设置'][0]),(read_yaml('Camera')['设置'][1]),(read_yaml('Camera')['白平衡'][0]),(read_yaml('Camera')['白平衡'][1]),(read_yaml('Camera')['白平衡'][1]),(read_yaml('Camera')['白平衡'][2]),(read_yaml('Camera')['白平衡'][3]),(read_yaml('Camera')['白平衡'][4]),(read_yaml('Camera')['白平衡'][5]),(read_yaml('Camera')['白平衡'][6])]
    # @pytest.mark.parametrize("White_balance", White_balance_)
    # @allure.story("闪光灯")
    # @allure.title("关闭、常亮")
    # def test_camera_countdown(self, get_driver,White_balance):
    #     self.camera = CameraPage(get_driver)
    #     self.camera.is_click_(White_balance)
    #     sleep(2)
    Gesture_control_ = [(read_yaml('Camera')['设置'][0]), (read_yaml('Camera')['设置'][1]), (read_yaml('Camera')['手势控制'][0]),
                      (read_yaml('Camera')['手势控制'][1]), (read_yaml('Camera')['手势控制'][2]), (read_yaml('Camera')['手势控制'][3]), (read_yaml('Camera')['去水印'][0]), (read_yaml('Camera')['去水印'][0])]

    @pytest.mark.parametrize("Gesture_control", Gesture_control_)
    @allure.story("手势控制")
    @allure.title("跟随、拍摄")
    def test_camera_countdown(self, get_driver, Gesture_control):
        self.camera = CameraPage(get_driver)
        self.camera.is_click_(Gesture_control)
        sleep(10)


if __name__ == '__main__':
    pytest.main(["-s","test_01_test_camera.py"])
    # # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录zh
    # pytest.main(['--alluredir', '../report/result',r'test_02_test_login.py'])
    # # # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    # os.system('allure generate ../report/result -o ../report/html --clean')
    # # pytest.main(['--clean-alluredir', '--alluredir', './report/result'])
    # # os.system('allure generate ./report/result -o ./report/html --clean')


