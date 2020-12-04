#!/usr/bin/python
# -*- coding: utf-8 -*-

import yaml
from appium import webdriver
from tools.logger import log
import os

#公共方法

class Driver_Config():

    def get_driver(self):

        try:
            file = open('../page_element/desired_caps.yaml', 'r')
            data = yaml.load(file, Loader=yaml.SafeLoader)
            self.desired_caps = {}
            self.desired_caps['platformName'] = data['platformName']
            self.desired_caps['deviceName'] = data['deviceName']
            self.desired_caps['platformVersion'] = str(data['platformVersion'])
            self.desired_caps['appPackage'] = data['appPackage']
            self.desired_caps['appActivity'] = data['appActivity']
            self.desired_caps['noReset'] = data['noReset']
            self.desired_caps['resetKeyboard'] = data['resetKeyboard']
            self.driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', self.desired_caps)
            self.driver.implicitly_wait(8)

            return self.driver
        except Exception as e:
            log.info('启动app错误：{}'.format(e))

