#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest
from tools.times import sleep
from page_object.camerapage import CameraPage
import allure, os
from common.readelement import read_yaml
from tools.logger import log


@allure.feature("相册")
class TestCamera06:
    """测试相册"""

    def test_front(self, get_driver):
        """前置条件"""
        self.camera = CameraPage(get_driver)
        # self.camera.no_connect()
        # self.camera.actions()
        # self.camera.panoramic()
        self.camera.photo()


    bottom_info = read_yaml('Camera')
    choose_ = [(bottom_info['相册'][3]),(bottom_info['相册'][2]),(bottom_info['相册'][1]),
                     (bottom_info['相册'][4]),
                     (bottom_info['相册'][6]), (bottom_info['相册'][8]),
                     (bottom_info['相册'][6]), (bottom_info['相册'][8]),
                     (bottom_info['相册'][6]), (bottom_info['相册'][9]), (bottom_info['相册'][10]),
                     (bottom_info['相册'][9]), (bottom_info['相册'][11]),
                     (bottom_info['相册'][5]), (bottom_info['相册'][8]),
                     (bottom_info['相册'][5]), (bottom_info['相册'][8]),
                     (bottom_info['相册'][5]), (bottom_info['相册'][9]), (bottom_info['相册'][10]),
                     (bottom_info['相册'][9]), (bottom_info['相册'][11]), (bottom_info['相册'][4])]


    @allure.story("选择、全选")
    @allure.title("选择后点赞或者删除")
    @pytest.mark.parametrize("choose", choose_)
    def test_camera_photo_choose(self, get_driver, choose):
        self.camera = CameraPage(get_driver)
        self.camera.is_click_(choose)
        sleep(2)

    bottom_info = read_yaml('Camera')
    video_ = [(bottom_info['相册'][6]), (bottom_info['相册'][18]), (bottom_info['相册'][19]),
              (bottom_info['相册'][7]), (bottom_info['相册'][10]), (bottom_info['相册'][7]), (bottom_info['相册'][11]),
               (bottom_info['相册'][12]), (bottom_info['相册'][13]), (bottom_info['相册'][17]), (bottom_info['相册'][15]),
               (bottom_info['相册'][20])]

    @allure.story("视频")
    @allure.title("编辑、删除")
    @pytest.mark.parametrize("video", video_)
    def test_camera_photo_video(self, get_driver, video):
        self.camera = CameraPage(get_driver)
        self.camera.is_click_(video)
        sleep(5)

    bottom_info = read_yaml('Camera')
    photos_ = [(bottom_info['相册'][2]), (bottom_info['相册'][6]), (bottom_info['相册'][7]), (bottom_info['相册'][10]),
               (bottom_info['相册'][7]), (bottom_info['相册'][11]),
               (bottom_info['相册'][20]), (bottom_info['相册'][20])]

    @allure.story("照片")
    @allure.title("编辑、删除")
    @pytest.mark.parametrize("photos", photos_)
    def test_camera_photo_photos(self, get_driver, photos):
        self.camera = CameraPage(get_driver)
        self.camera.is_click_(photos)
        sleep(5)



if __name__ == '__main__':
    pytest.main(["-s", "test_01_test_camera06.py"])

