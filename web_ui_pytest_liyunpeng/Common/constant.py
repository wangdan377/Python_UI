# -*-coding:utf-8-*-
"""
============================
author:chenglei
time:2019/8/12
E-mail:461419962@qq.com
============================
"""
import  os

#项目的根路径
BASE_DIR =os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


#截图的路径
SCREEN_SHOT = os.path.join(BASE_DIR,"Outputs/imgs")


# print(SCREEN_SHOT)
#log日志路径
LOGS_DIR =  os.path.join(BASE_DIR,"Outputs/logs")

#上传文件的路径
UPLOAD_DIR = os.path.join(BASE_DIR,'data')

#allure报告路径
allure_DOR = os.path.join(BASE_DIR,'Outputs/allure')
