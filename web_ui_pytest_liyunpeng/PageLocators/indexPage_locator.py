# -*-coding:utf-8-*-
"""
============================
author:chenglei
time:2019/8/12
E-mail:461419962@qq.com
============================
"""

from selenium.webdriver.common.by import By

class IndexPageLocator:
    # user_loc=(By.XPATH,'//a[contains(text(),"我的帐户")]')
    #首页‘安全等级’元素定位
    index_loc = (By.XPATH, '//span[text()="安全等级"]')

    #首页‘发起签约’按钮元素定位
    start_sign_loc  = (By.XPATH,'//span[text() ="发起签约"]')