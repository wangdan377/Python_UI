# -*-coding:utf-8-*-
"""
============================
author:chenglei
time:2019/8/9
E-mail:461419962@qq.com
============================
"""
#登录成功参数
success_datas = [
    {"username":"13760495929","passwd":"cl123456"},
    {"username":"461419962@qq.com","passwd":"cl123456"},
]

#账户名或密码错误
userPd_datas = [
    {"user":"13760495929","password":"cl1234561","check":"账号或密码错误，请输入正确的账号和密码。"},
    {"user":"13760495920","password":"cl1234561","check":"账号或密码错误，请输入正确的账号和密码。"},
    {"user":"461419962@qq.com","password":"cl1234561","check":"账号或密码错误，请输入正确的账号和密码。"},
]


#用户名输入错误参数
user_datas = [
    {"user": "", "password": "", "check": "请输入您注册的账户"},
    {"user": "123456798788", "password": "", "check": "请输入正确的手机号和邮箱"},
    {"user": "aa.com", "password": "", "check": "请输入正确的手机号和邮箱"},
]
#密码输入参数
passwd_datas = [
    {"user": "13760495929", "password": "", "check": "密码不能为空"},
    {"user": "13760495929", "password": "12345", "check": "请输入8~20位字符"},
    {"user": "13760495929", "password": "123452222222222121212", "check": "请输入8~20位字符"},
    {"user": "461419962@qq.com", "password": "123452222222222121212", "check": "请输入8~20位字符"},
]
