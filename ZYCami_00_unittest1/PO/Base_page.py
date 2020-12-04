#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'WD'
'''
description:UI页面公共类  ---login
'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.loged import Logger

from Public import Caplictily
log = Logger('D:\ZYCami_00\logs\\error.log', level='debug')

class Base_Page(object):

    def __init__(self,driver):
        self.driver = driver


    def find_element(self,loc):

        '''重写find_element方法，显式等待'''

        try:
            WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except Exception as e:
            log.logger.error('{}元素可见失效，错误：{}'.format(loc,e))
            raise e

    def send_keys01(self, value, *loc):
        try:
            self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError as e:
            log.logger.error('{}元素可见失效，错误：{}'.format(loc,e))
            raise e

    def send_keys(self, value, *loc):
        try:
            self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError as e:
            raise e
    def find_elements(self,loc,timeout=5):      #frequency
        try:
            eles = WebDriverWait(self.driver,timeout).until(lambda driver:driver.find_elements(*loc))

        except Exception as e:
            raise e
        return eles

    """# 判断控件是否存在

    def is_element_exist(driver, element):
        source = driver.page_source
        if element in source:
            return True
        else:
            return False
"""
