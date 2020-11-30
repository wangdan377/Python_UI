# -*- coding: UTF-8 -*-
# Administrator
# 2020/4/20 18:08


from selenium.webdriver.common.by import By

class UploadPageLoctor:
    #上传合同元素定位
    uploadText_loc = (By.XPATH,'//div[text() = "附件上传"]')

    #添加合同元素定位
    addContract_loc = (By.XPATH,'//input[@class = "uploadinput"]')

    #上传附件元素定位
    uploadFile_loc = (By.XPATH,'//input[@class = "uploadfile"]')

    #下一步按钮元素定位
    nextStep_loc = (By.XPATH,'//span[text() = "下一步"]')

    #下一步中间提示
    error_loc = (By.XPATH,'//div[@class = "el-message__group"]/p')