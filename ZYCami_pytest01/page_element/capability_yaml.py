#!/usr/bin/python
# -*- coding: utf-8 -*-
from appium import webdriver
import yaml
file = open('desired_caps.yaml','r')
data = yaml.load(file, Loader=yaml.SafeLoader)

desired_caps = {}
desired_caps['platformName'] = data['platformName']
desired_caps['deviceName'] = data['deviceName']
desired_caps['platformVersion'] = str(data['platformVersion'])
desired_caps['appPackage'] = data['appPackage']
desired_caps['appActivity'] = data['appActivity']
desired_caps['noReset'] = data['noReset']
desired_caps['resetKeyboard'] = data['resetKeyboard']
desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub',desired_caps)

