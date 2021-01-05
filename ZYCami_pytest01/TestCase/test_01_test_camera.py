#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest
from tools.times import sleep
from page_object.camerapage import CameraPage
import allure,os
from common.readelement import read_yaml


@allure.feature("拍照")
class Testcamera01:
    """测试拍照"""
    def test_front(self,get_driver):
        """前置条件"""
        self.camera = CameraPage(get_driver)
        # self.camera.no_connect()
        self.camera.connect()
        self.camera.script()
        self.camera.actions()

    beau_ = read_yaml('Camera')
    beautify_0 = [(beau_['美颜'][0])]
    beautify_1 = [(beau_['美颜'][1]), (beau_['美颜'][2]), (beau_['美颜'][3]), (beau_['美颜'][9]),
                  (beau_['美颜'][4]), (beau_['美颜'][9]), (beau_['美颜'][5]), (beau_['美颜'][9]),
                  (beau_['美颜'][6]), (beau_['美颜'][9]), (beau_['美颜'][7]), (beau_['美颜'][9]),
                  (beau_['美颜'][8]), (beau_['美颜'][9]), (beau_['美颜'][1])]
    beautify_2 = [(beau_['导航栏'][2])]

    @allure.story("美颜")
    @allure.title("美颜")
    @pytest.mark.parametrize("beautify0", beautify_0)
    @pytest.mark.parametrize("beautify1", beautify_1)
    @pytest.mark.parametrize("beautify2", beautify_2)
    def test_camera_beautify(self, get_driver, beautify0, beautify1, beautify2):
        self.camera = CameraPage(get_driver)
        self.camera.is_click_(beautify0)
        self.camera.is_click_(beautify1)
        self.camera.is_click_(beautify2)
        sleep(2)

    beau_ = read_yaml('Camera')
    countdown_0 = [(beau_['倒计时'][0])]
    countdown_1 = [(beau_['倒计时'][1]), (beau_['倒计时'][2]), (beau_['倒计时'][3]), (beau_['倒计时'][4])]
    countdown_2 = [(beau_['导航栏'][2])]
    @allure.story("倒计时")
    @allure.title("3、5、7、off")
    @pytest.mark.parametrize("countdown0", countdown_0)
    @pytest.mark.parametrize("countdown1", countdown_1)
    @pytest.mark.parametrize("countdown2", countdown_2)
    def test_camera_countdown(self, get_driver, countdown0, countdown1, countdown2):
        self.camera = CameraPage(get_driver)
        self.camera.is_click_(countdown0)
        self.camera.is_click_(countdown1)
        self.camera.is_click_(countdown2)
        sleep(2)

    beau_ = read_yaml('Camera')
    flash_ = [(beau_['设置'][0]), (beau_['设置'][1]), (beau_['闪光灯'][0]), (beau_['闪光灯'][1]), (beau_['闪光灯'][2]),
              (beau_['闪光灯'][3]), (beau_['闪光灯'][4]), (beau_['闪光灯'][0])]

    @allure.story("闪光灯")
    @allure.title("常亮、关闭")
    @pytest.mark.parametrize("flash", flash_)
    def test_camera_flash(self, get_driver,flash):
        self.camera = CameraPage(get_driver)
        self.camera.is_click_(flash)
        sleep(2)

    beau_ = read_yaml('Camera')
    network_ = [(beau_['网络显示'][0]), (beau_['网络显示'][2]), (beau_['网络显示'][3]), (beau_['网络显示'][1]), (beau_['网络显示'][0])]
    @allure.story("网络显示")
    @allure.title("关闭、方格、对角+方格")
    @pytest.mark.parametrize("network", network_)
    def test_camera_network(self, get_driver,network):
        self.camera = CameraPage(get_driver)
        self.camera.is_click_(network)
        sleep(2)

    beau_ = read_yaml('Camera')
    white_balance_ = [(beau_['白平衡'][0]), (beau_['白平衡'][1]), (beau_['白平衡'][2]), (beau_['白平衡'][3]),
                      (read_yaml('Camera')['白平衡'][4]), (beau_['白平衡'][5]),(beau_['相机'][6])]

    @allure.story("白平衡")
    @allure.title("自动、晴天、阴天、白炽灯、荧光灯")
    @pytest.mark.parametrize("white_balance", white_balance_)
    def test_camera_white_balance(self, get_driver,white_balance):
        self.camera = CameraPage(get_driver)
        self.camera.is_click_(white_balance)
        sleep(2)

    beau_ = read_yaml('Camera')
    gesture_control_ = [(beau_['手势控制'][0]), (beau_['手势控制'][1]), (beau_['手势控制'][2]), (beau_['相机'][6]), (beau_['去水印'][0]),
                        (read_yaml('Camera')['去水印'][0]), (read_yaml('Camera')['导航栏'][2])]

    @allure.story("手势控制")
    @allure.title("跟随、拍摄")
    @pytest.mark.parametrize("gesture_control", gesture_control_)
    def test_camera_gesture_control(self, get_driver, gesture_control):
        self.camera = CameraPage(get_driver)
        self.camera.is_click_(gesture_control)
        sleep(3)

    beau_ = read_yaml('Camera')
    yun_tai_ = [(beau_['设置'][0]), (read_yaml('Camera')['设置'][2]), (read_yaml('Camera')['情景模式'][0]), (read_yaml('Camera')['情景模式'][1]),
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
                  (beau_['通用'][1]), (beau_['通用'][2]), (beau_['通用'][4]), (beau_['通用'][2]), (beau_['通用'][5]),
                  (beau_['通用'][1]), (beau_['通用'][3]), (beau_['通用'][6]), (beau_['导航栏'][2])]

    @allure.story("通用")
    @allure.title("设备连接、断开设备")
    @pytest.mark.parametrize("universal", universal_)
    def test_camera_universal(self, get_driver, universal):
        self.camera = CameraPage(get_driver)
        self.camera.is_click_(universal)
        sleep(3)

    bottom_info = read_yaml('Camera')
    gesture_ = [(bottom_info['导航栏'][3]), (bottom_info['导航栏'][3]), (bottom_info['导航栏'][1]), (bottom_info['导航栏'][1]),
                (bottom_info['导航栏'][2])]

    @allure.story("照片")
    @allure.title("编辑、删除")
    @pytest.mark.parametrize("gesture", gesture_)
    def test_camera_gesture(self, get_driver, gesture):
        self.camera = CameraPage(get_driver)
        self.camera.is_click_(gesture)
        sleep(5)


if __name__ == '__main__':
    pytest.main(["-s","test_01_test_camera.py"])
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录zh
    # pytest.main(['--alluredir', '../report/result',r'test_02_test_login.py'])
    # # # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    # os.system('allure generate ../report/result -o ../report/html --clean')
    # # pytest.main(['--clean-alluredir', '--alluredir', './report/result'])
    # # os.system('allure generate ./report/result -o ./report/html --clean')


