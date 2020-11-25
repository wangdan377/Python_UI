# -*- coding: UTF-8 -*-
# Administrator
# 2020/4/21 17:41

from selenium.webdriver.common.by import By

class AddSignerLocator:

    #签署对象元素定位
    sign_object_loc = (By.XPATH,'//p[text() = "签署对象"]')

    #添加签署人按钮元素定位
    addSigner_loc = (By.XPATH,'//span[text()="添加签署人"]')

    #手机号/邮箱第一个输入框定位
    account_input_loc = (By.XPATH,'//div[@class = "info"]/ul[2]/li[2]/div[@class = "el-row"]/div[1]/div/input[1]')

    #点击指定付按钮元素定位
    Specify_button_loc = (By.XPATH,'//label[@class = "el-radio radio2"]/span')


    #选择用户元素定位
    choose_users_loc = (By.XPATH,'//div[@class ="pay"]/div[1]/div[1]/div/div[1]/input')

    #指定自己付用户元素定位
    Specify_users_loc = (By.XPATH,'//span[contains(text(),"13760495929")]')


    #下一步按钮元素定位
    nextStep_loc = (By.XPATH,'//div[@class ="sure_bottom clearfix"]/button[2]/span')