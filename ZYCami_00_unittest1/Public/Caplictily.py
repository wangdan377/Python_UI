#!/usr/bin/python
# -*- coding: utf-8 -*-

import yaml
from appium import webdriver
from common.loged import *
import os

#公共方法
"""def appium_desired():
    file = open('../yamlFile/desired_caps.yaml','r')
    data = yaml.load(file, Loader=yaml.SafeLoader)
    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['platformVersion'] = str(data['platformVersion'])
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['noReset'] = data['noReset']
    desired_caps['resetKeyboard'] = data['resetKeyboard']
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
    driver.implicitly_wait(8)
    return driver"""
class Driver_Config():

    def get_driver(self):
        log = Logger('D:\ZYCami_00\logs\\error.log', level='debug')
        try:
            file = open('../yamlFile/desired_caps.yaml', 'r')
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
            log.logger.error('错误：{}'.format(e))
