# -*-coding:utf-8-*-
"""
============================
author:chenglei
time:2019/8/8
E-mail:461419962@qq.com
============================
"""
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.indexPage_locator import IndexPageLocator as loc
from Common.basepage import BasePage
import time

class IndexPage(BasePage):
    """首页"""

    # def __init__(self,driver:WebDriver):
    #     self.driver =driver
    #检查元素是否存在
    def check_userName_exists(self):
        try:
            self.wait_ele_exists(loc.index_loc,"首页_安全等级元素是否存在")
            return True
        except:
            return False

    def click_ele(self):
        self.click_element(loc.start_sign_loc,"首页_发起签约按钮")






















