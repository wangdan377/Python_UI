#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest
from tools.times import sleep
from page_object.camerapage import CameraPage
import allure, os
from common.readelement import read_yaml
from tools.logger import log


@allure.feature("测试相机")
class TestCamera:
    """测试底部导航栏"""

    def test_front(self, get_driver):
        """前置条件"""
        self.camera = CameraPage(get_driver)
        # self.camera.no_connect()
        self.camera.connect()
        # self.camera.script()
        # self.camera.actions()
        # self.camera.video()
        # self.camera.panoramic()
        self.camera.time_lapse()
        # self.camera.motion_delay()

    # bottom_info = read_yaml('Camera')
    # Bottom_navigation_ = [ (bottom_info['底部导航栏'][0]),(bottom_info['底部导航栏'][1]),(bottom_info['底部导航栏'][2]),
    #                       (bottom_info['底部导航栏'][3]), (bottom_info['底部导航栏'][4]), (bottom_info['底部导航栏'][5]),
    #                       (bottom_info['底部导航栏'][6])]
    #
    # @allure.story("底部导航栏")
    # @allure.title("SAMRT、拍照、录像、全景、延时摄影、运动延时")
    # @pytest.mark.parametrize("Bottom_navigation", Bottom_navigation_)
    # def test_camera_Bottom_navigation(self, get_driver, Bottom_navigation):
    #     self.camera = CameraPage(get_driver)
    #     self.camera.is_click_(Bottom_navigation)

    # bottom_info = read_yaml('Camera')
    # photo_ = [(bottom_info['导航栏'][0]), (bottom_info['相册'][0]), (bottom_info['相册'][3]), (bottom_info['相册'][2]),
    #           (bottom_info['相册'][1]), (bottom_info['相册'][4]), (bottom_info['相册'][5]), (bottom_info['相册'][6]),
    #           (bottom_info['相册'][5]), (bottom_info['相册'][6]), (bottom_info['相册'][5]), (bottom_info['相册'][7]),
    #           (bottom_info['相册'][8]), (bottom_info['相册'][7]), (bottom_info['相册'][9]), (bottom_info['相册'][4]),
    #           (bottom_info['相册'][5]), (bottom_info['相册'][3]), (bottom_info['相册'][3]), (bottom_info['相册'][12]),
    #           (bottom_info['相册'][15]), (bottom_info['相册'][13]), (bottom_info['相册'][12]), (bottom_info['相册'][15]),
    #           (bottom_info['相册'][14]), (bottom_info['相册'][7]), (bottom_info['相册'][8]), (bottom_info['相册'][7]),
    #           (bottom_info['相册'][9]), (bottom_info['相册'][10]), (bottom_info['相册'][11]), (bottom_info['相机'][6]),
    #           (bottom_info['相机'][6])]

    # bottom_info = read_yaml('Camera')
    # Video_0 = [(bottom_info['视频分辨率'][0])]
    # Video_1 = [(bottom_info['视频分辨率'][3]),(bottom_info['视频分辨率'][2]), (bottom_info['视频分辨率'][1])]
    # Video_2 = [(bottom_info['导航栏'][2])]
    # Video_3 = [(bottom_info['导航栏'][2])]
    # @allure.story("录像")
    # @allure.title("录像、视频分辨率")
    # @pytest.mark.parametrize("Video0", Video_0)
    # @pytest.mark.parametrize("Video1", Video_1)
    # @pytest.mark.parametrize("Video2", Video_2)
    # @pytest.mark.parametrize("Video3", Video_3)
    # def test_camera_Video(self, get_driver, Video0,Video1,Video2,Video3):
    #     self.camera = CameraPage(get_driver)
    #     self.camera.is_click_(Video0)
    #     self.camera.is_click_(Video1)
    #     self.camera.is_click_(Video2)
    #     self.camera.is_click_(Video3)

    # bottom_info = read_yaml('Camera')
    # Motion_delay_ = [(bottom_info['视频设置'][0]),(bottom_info['视频分辨率'][1]),(bottom_info['视频分辨率'][2]),(bottom_info['视频设置'][3]),(bottom_info['视频设置'][4]), (bottom_info['视频设置'][5]), (bottom_info['视频设置'][6])]
    #
    # @allure.story("运动延时")
    # @allure.title("视频分辨率,倍数")
    # @pytest.mark.parametrize("Motion delay", Motion_delay_)
    # def test_camera_Motion_delay(self, get_driver, Motion_delay):
    #     self.camera = CameraPage(get_driver)
    #     self.camera.is_click_(Motion_delay)

    # bottom_info = read_yaml('Camera')
    # SMART_ = [(bottom_info['导航栏'][4]),
    #                            (bottom_info['SMART1'][0]),  (bottom_info['SMART3'][4]),(bottom_info['SMART3'][5]),(bottom_info['SMART1'][1]),
    #                            (bottom_info['SMART1'][0]), (bottom_info['导航栏'][2]), (bottom_info['SMART3'][1]),
    #                            (bottom_info['导航栏'][2]), (bottom_info['SMART3'][1]),
    #                            (bottom_info['导航栏'][2]), (bottom_info['SMART3'][1]),
    #                            (bottom_info['导航栏'][2]), (bottom_info['SMART3'][0]),
    #                            (bottom_info['导航栏'][2]), (bottom_info['SMART3'][1]),
    #                            (bottom_info['相机'][4]), (bottom_info['相册'][13]), (bottom_info['相机'][4]),(bottom_info['相册'][14]),
    #                             (bottom_info['SMART1'][0]),
    #                            (bottom_info['导航栏'][2]), (bottom_info['SMART3'][1]),
    #                            (bottom_info['导航栏'][2]), (bottom_info['SMART3'][1]),
    #                            (bottom_info['导航栏'][2]), (bottom_info['SMART3'][1]),
    #                            (bottom_info['导航栏'][2]), (bottom_info['SMART3'][1]),
    #                            (bottom_info['SMART1'][3]), (bottom_info['SMART1'][3]),
    #
    #                            (bottom_info['相机'][4]), (bottom_info['相册'][13]),(bottom_info['相机'][4]), (bottom_info['相册'][14]),
    #                            (bottom_info['SMART1'][0]),
    #                            (bottom_info['导航栏'][2]), (bottom_info['SMART3'][1]),
    #                            (bottom_info['导航栏'][2]), (bottom_info['SMART3'][1]),
    #                            (bottom_info['导航栏'][2]), (bottom_info['SMART3'][1]),
    #                            (bottom_info['导航栏'][2]), (bottom_info['SMART3'][1]), (bottom_info['SMART3'][2]),
    #
    #                            (bottom_info['发布'][5]), (bottom_info['发布'][5]),
    #
    #                            (bottom_info['发布'][6]),(bottom_info['发布'][7]),(bottom_info['发布'][6]),(bottom_info['发布'][7]),
    #                            (bottom_info['发布'][8]),
    #                            (bottom_info['发布'][2])
    #                            ]
    #
    # @allure.story("SMART")
    # @allure.title("使用、发布")
    # @pytest.mark.parametrize("SMART", SMART_)
    # def test_camera_bottom_navigation(self, get_driver, SMART):
    #     self.camera = CameraPage(get_driver)
    #     self.camera.is_click_(SMART)
    bottom_info = read_yaml('Camera')
    # Time_lapse_photography_ = [(bottom_info['延时摄影'][0]), (bottom_info['间隔'][0]), (bottom_info['间隔'][1]), (bottom_info['间隔'][2]),
    #                 (bottom_info['间隔'][3]), (bottom_info['间隔'][4]), (bottom_info['间隔'][8]), (bottom_info['间隔'][6]),
    #                 (bottom_info['间隔'][7]), (bottom_info['间隔'][8]), (bottom_info['间隔'][1]), (bottom_info['间隔'][9]),
    #                 (bottom_info['间隔'][10]), (bottom_info['间隔'][11]), (bottom_info['间隔'][12]), (bottom_info['间隔'][13]),
    #                 (bottom_info['间隔'][14]), (bottom_info['间隔'][15]), (bottom_info['间隔'][16]), (bottom_info['间隔'][17]),
    #                 (bottom_info['摄影时长'][0]), (bottom_info['摄影时长'][1]), (bottom_info['摄影时长'][2]),
    #                 (bottom_info['摄影时长'][3]), (bottom_info['摄影时长'][4]), (bottom_info['摄影时长'][5]),
    #                 (bottom_info['摄影时长'][6]), (bottom_info['摄影时长'][7]), (bottom_info['摄影时长'][8]),
    #                 (bottom_info['摄影时长'][9]), (bottom_info['摄影时长'][10]), (bottom_info['摄影时长'][11]),
    #                 (bottom_info['摄影时长'][12])
    time_lapse_photography_ = [(bottom_info['延时摄影'][0]),
                               (bottom_info['间隔'][0]), (bottom_info['间隔'][1])]

    @allure.story("延时摄影")
    @allure.title("视频分辨率,倍数")
    @pytest.mark.parametrize("time_lapse_photography", time_lapse_photography_)
    def test_camera_time_lapse_photography(self, get_driver, time_lapse_photography):
        self.camera = CameraPage(get_driver)
        self.camera.is_click_(time_lapse_photography)



if __name__ == '__main__':
    pytest.main(["-s", "test_01_test_camera02.py"])
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录zh
    # pytest.main(['--alluredir', '../report/result',r'test_02_test_login.py'])
    # # # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    # os.system('allure generate ../report/result -o ../report/html --clean')
    # # pytest.main(['--clean-alluredir', '--alluredir', './report/result'])
    # # os.system('allure generate ./report/result -o ./report/html --clean')
