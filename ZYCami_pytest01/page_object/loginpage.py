# loginpage.py
from page.webpage import WebPage
# from page.Function import BaseFun
# from common.readelement import Element
from common.readelement import read_yaml
import allure

login = read_yaml('Login')['登录']

'''class LoginPage(WebPage):
    """登录类"""
    @allure.step("我的页面")
    def me(self):
        self.is_click(login['me'])

    @allure.step("登录按钮")
    def logins(self):
        self.is_click(login['登录按钮'])

    @allure.step("输入用户名")
    def username(self, name):
        """用户名"""
        self.input_text(login['输入用户名'], name)

    @allure.step("输入密码")
    def password(self, pwd):
        """密码"""
        self.input_text(login['输入密码'], pwd)

    @allure.step("点击登录")
    def submit(self):
        """登录"""
        self.is_click(login['登录提交按钮'])


if __name__ == '__main__':
    login = Element('Login')
    print(login['me'])'''
class LoginPage(WebPage):
    """登录类"""
    @allure.step("我的页面")
    def me(self):
        self.is_click((login[2]['type'],login[2]['value']))
        # self.is_click(('xpath', "//*[@content-desc='Me']"))

    @allure.step("登录按钮")
    def logins(self):
        self.is_click((login[3]['type'],login[3]['value']))

    @allure.step("输入用户名")
    def username(self, name):
        """用户名"""
        self.input_text((login[4]['type'],login[4]['value']),name)

    @allure.step("输入密码")
    def password(self, pwd):
        """密码"""
        self.input_text((login[5]['type'],login[5]['value']),pwd)

    @allure.step("点击登录")
    def submit(self):
        """登录"""
        self.is_click((login[6]['type'],login[6]['value']))


if __name__ == '__main__':
    login = read_yaml('Login')['登录']
    print((login[2]['type'],login[2]['value']))

