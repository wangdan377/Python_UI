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
        """前置条件"""
        self.camera = CameraPage(get_driver)
        self.camera.no_connect()
        # self.camera.connect()
        beautifys = read_yaml('Camera')

    beautifys = read_yaml('Camera')
    beautify_0 = [(beautifys['美颜'][0])]
    beautify_1 = [(beautifys['美颜'][9])]
    beautify_2 = [(beautifys['导航栏'][2])]

    @allure.story("美颜")
    @allure.title("美颜")
    # @pytest.mark.skip(reason="跳过执行这条case")
    @pytest.mark.parametrize("beautify0", beautify_0)
    @pytest.mark.parametrize("beautify1", beautify_1)
    @pytest.mark.parametrize("beautify2", beautify_2)
    def test_camera_beautify(self, get_driver, beautify0, beautify1, beautify2):
        self.camera = CameraPage(get_driver)
        self.camera.is_click_(beautify0)
        self.camera.is_click_(beautify1)
        self.camera.is_click_(beautify2)
        sleep(2)

    # beautifys = read_yaml('Camera')
    #
    # beautify_0 = [(beautifys['美颜'][0])]
    # beautify_1 = [(beautifys['美颜'][1]),(beautifys['美颜'][2]),(beautifys['美颜'][3]),(beautifys['美颜'][4]),(beautifys['美颜'][5]),(beautifys['美颜'][6]),(beautifys['美颜'][7]),(beautifys['美颜'][8])]
    # beautify_2 = [(beautifys['导航栏'][2])]
    #
    #
    # @allure.story("美颜")
    # @allure.title("美颜")
    # # @pytest.mark.skip(reason="跳过执行这条case")
    # @pytest.mark.parametrize("beautify0", beautify_0)
    # @pytest.mark.parametrize("beautify1", beautify_1)
    # @pytest.mark.parametrize("beautify2", beautify_2)
    # def test_camera_beautify(self,get_driver,beautify0,beautify1,beautify2):
    #     self.camera = CameraPage(get_driver)
    #     self.camera.is_click_(beautify0)
    #     self.camera.is_click_(beautify1)
    #     self.camera.is_click_(beautify2)
    #     sleep(2)

    # countdown_0 = [(beautifys['倒计时'][0])]
    # countdown_1 = [(beautifys['倒计时'][1]),(beautifys['倒计时'][2]),(beautifys['倒计时'][3]),(beautifys['倒计时'][4])]
    # countdown_2 = [(beautifys['导航栏'][2])]
    #
    # @allure.story("倒计时")
    # @allure.title("3、5、7、off")
    # # @pytest.mark.skip(reason="跳过执行这条case")
    # @pytest.mark.parametrize("countdown0", countdown_0)
    # @pytest.mark.parametrize("countdown1", countdown_1)
    # @pytest.mark.parametrize("countdown2", countdown_2)
    # def test_camera_countdown(self, get_driver, countdown0,countdown1,countdown2):
    #     self.camera = CameraPage(get_driver)
    #     self.camera.is_click_(countdown0)
    #     self.camera.is_click_(countdown1)
    #     self.camera.is_click_(countdown2)
    #     sleep(2)
    #
    #
    #
    # flash_ = [(beautifys['设置'][0]),(beautifys['设置'][1]),(beautifys['闪光灯'][0]),(beautifys['闪光灯'][1]),(beautifys['闪光灯'][2]),(beautifys['闪光灯'][1]),(beautifys['闪光灯'][0])]
    #
    # @allure.story("闪光灯")
    # @allure.title("关闭、常亮")
    # @pytest.mark.parametrize("flash", flash_)
    # def test_camera_flash(self, get_driver,flash):
    #     self.camera = CameraPage(get_driver)
    #     self.camera.is_click_(flash)
    #     sleep(2)

    # Network_ = [(beautifys['网络显示'][0]),(beautifys['网络显示'][1]),(beautifys['网络显示'][2]),(beautifys['网络显示'][3]),(beautifys['网络显示'][0])]

    # @allure.story("网络显示")
    # @allure.title("关闭、方格、对角+方格")
    # @pytest.mark.parametrize("Network", Network_)
    # def test_camera_Network(self, get_driver,Network):
    #     self.camera = CameraPage(get_driver)
    #     self.camera.is_click_(Network)
    #     sleep(2)
    #
    # White_balance_ = [(beautifys['白平衡'][0]),(beautifys['白平衡'][1]),(beautifys['白平衡'][2]),(beautifys['白平衡'][3]),(read_yaml('Camera')['白平衡'][4]),(beautifys['白平衡'][5]),(beautifys['相机'][6])]

    # @allure.story("白平衡")
    # @allure.title("自动、晴天、阴天、白炽灯、荧光灯")
    # @pytest.mark.parametrize("White_balance", White_balance_)
    # def test_camera_White_balance(self, get_driver,White_balance):
    #     self.camera = CameraPage(get_driver)
    #     self.camera.is_click_(White_balance)
    #     sleep(2)
    #
    #
    # Gesture_control_ = [(beautifys['手势控制'][0]),
    #                   (beautifys['手势控制'][1]), (beautifys['手势控制'][2]),(beautifys['相机'][6]), (beautifys['去水印'][0]), (read_yaml('Camera')['去水印'][0]),(read_yaml('Camera')['导航栏'][2])]
    #

    # @allure.story("手势控制")
    # @allure.title("跟随、拍摄")
    # @pytest.mark.parametrize("Gesture_control", Gesture_control_)
    # def test_camera_Gesture_control(self, get_driver, Gesture_control):
    #     self.camera = CameraPage(get_driver)
    #     self.camera.is_click_(Gesture_control)
    #     sleep(3)
    #
    #
    #
    # Yuntai_ = [(beautifys['设置'][0]), (read_yaml('Camera')['设置'][2]), (read_yaml('Camera')['情景模式'][0]),(read_yaml('Camera')['情景模式'][1]),
    #            (beautifys['跟随模式'][0]), (beautifys['跟随模式'][1]),
    #            (beautifys['跟随模式'][2]), (beautifys['跟随模式'][3]),(beautifys['相机'][6]),
    #            (beautifys['摇杆速度'][0]), (beautifys['摇杆速度'][1]), (beautifys['摇杆速度'][2]),
    #            (beautifys['摇杆速度'][3]), (beautifys['反向'][0]), (beautifys['反向'][0]),
    #            (beautifys['反向'][1]), (beautifys['反向'][1]),
    #            (beautifys['M键'][0]), (beautifys['M键'][1]), (beautifys['M键'][2]),
    #            (beautifys['M键'][3]), (beautifys['M键'][0]), (beautifys['云台自动校准'][0]),
    #            (beautifys['云台自动校准'][1])]
    #

    # @allure.story("云台")
    # @allure.title("各种模式")
    # @pytest.mark.parametrize("Yuntai", Yuntai_)
    # def test_camera_Yuntai(self, get_driver, Yuntai):
    #     self.camera = CameraPage(get_driver)
    #     self.camera.is_click_(Yuntai)
    #     sleep(3)
    #
    # Universal_ = [(beautifys['通用'][0]),
    #               (beautifys['通用'][1]),
    #               (beautifys['通用'][2]),(beautifys['通用'][4]),
    #                (beautifys['通用'][2]),(beautifys['通用'][5]),(beautifys['通用'][1]),
    #                (beautifys['通用'][3]),(beautifys['通用'][6]),(beautifys['导航栏'][2])]
    #
    #

    # @allure.story("通用")
    # @allure.title("设备连接、断开设备")
    # @pytest.mark.parametrize("Universal", Universal_)
    # def test_camera_Universal(self, get_driver, Universal):
    #     self.camera = CameraPage(get_driver)
    #     self.camera.is_click_(Universal)
    #     sleep(3)




if __name__ == '__main__':
    pytest.main(["-s","test_01_test_camera.py"])
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录zh
    # pytest.main(['--alluredir', '../report/result',r'test_02_test_login.py'])
    # # # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    # os.system('allure generate ../report/result -o ../report/html --clean')
    # # pytest.main(['--clean-alluredir', '--alluredir', './report/result'])
    # # os.system('allure generate ./report/result -o ./report/html --clean')


