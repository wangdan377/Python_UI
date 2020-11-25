#coding:utf-8

from selenium.webdriver.common.by import By
import os
import time

#邮箱登录链接
email_login = (By.XPATH, '//*[@text="邮箱登录"]')

#输入邮箱文本框
email_text = (By.XPATH, '//*[@text="请输入邮箱地址"]')

#输入邮箱文本框
password_text = (By.XPATH, '//*[@text="请输入密码"]')

#ZHIYUN Prime banner
zhiyun_prime_banner = (By.XPATH, '//*[@text="ZHIYUN Prime"]')

#账号或密码错误提示框信息
user_psw_incorect_tex = (By.XPATH, '//*[@text="账号或密码错误"]')

#确定按钮
confirm_btn = (By.XPATH, '//*[@text="确定"]')



