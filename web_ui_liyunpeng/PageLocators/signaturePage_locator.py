# -*- coding: UTF-8 -*-
# Administrator
# 2020/4/27 16:09

from selenium.webdriver.common.by import By

class SingaturePageLoctor:
    #签署人标记签署位置文本定位
    signer_text_loc = (By.XPATH,'//p[text() = "给待签署人标记签署的位置"]')

    #默认云签名元素定位
    Cloud_signature_loc = (By.XPATH,'//div[@class ="cloud-box-content" ]/div[1]/ul[1]/li[1]/div/img')

    #完成签署按钮元素定位
    sign_complete_loc = (By.XPATH,'//span[text() = "完成签署"]')

    #密码验证按钮元素定位
    password_ver_loc = (By.XPATH,'//span[text() = "密码验证"]')

    #密码输入框元素定位
    password_input_loc = (By.XPATH,'//input[@type ="password"]')

    #确定按钮元素定位
    confirm_button_loc = (By.XPATH,'//div[@class ="el-dialog__wrapper ukey checkPsw" ]/div/div[3]/div/button/span')