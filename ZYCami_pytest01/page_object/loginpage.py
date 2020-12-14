# loginpage.py
from page.webpage import WebPage
# from page.Function import BaseFun
# from common.readelement import Element
from common.readelement import read_yaml
from tools.logger import log
import allure

navigat= read_yaml('Login')['导航']
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
    '''@allure.step("我的页面")
    def me(self):
        self.is_click((login[2]['type'],login[2]['value']))
        

    @allure.step("登录按钮")
    def login_Button(self):
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
        self.is_click((login[6]['type'],login[6]['value']))'''

    # @allure.step("登录成功用例")
    # def login_test_list(self,username,password):
    #     self.is_click((navigat[2]['type'], navigat[2]['value']))
    #     self.is_click((login[0]['type'], login[0]['value']))
    #     self.input_text((login[1]['type'], login[1]['value']), username)
    #     self.input_text((login[2]['type'], login[2]['value']), password)
    #     self.is_click((login[3]['type'], login[3]['value']))
    #
    # @allure.step("登录错误用例")
    # def login_test_lists(self,username,password):
    #     self.is_click((navigat[2]['type'], navigat[2]['value']))
    #     self.is_click((login[0]['type'], login[0]['value']))
    #     self.input_text((login[1]['type'], login[1]['value']), username)
    #     self.input_text((login[2]['type'], login[2]['value']), password)
    #     self.is_click((login[3]['type'], login[3]['value']))           #登录按钮  如果是错误的就会有提示弹框   然后弹框有个确定按钮
    #     result = self.element_text((login[4]['type'], login[4]['value']))
    #     self.is_click((login[5]['type'], login[5]['value']))        #确定按钮
    #     return result

    # @allure.step("登录错误用例")
    # def login_test_lists1(self, username, password, text):
    #     self.is_click((navigat[2]['type'], navigat[2]['value']))
    #     self.is_click((login[0]['type'], login[0]['value']))
    #     self.input_text((login[1]['type'], login[1]['value']), username)
    #     self.input_text((login[2]['type'], login[2]['value']), password)
    #     self.is_click((login[3]['type'], login[3]['value']))  # 登录按钮
    #     log.info(self.find_toast(text))
    #     return self.find_toast(text)

    @allure.step("登录成功用例")
    def login_test_lists2(self, username, password):
        self.is_click((navigat[2]['type'], navigat[2]['value']))
        self.is_click((login[0]['type'], login[0]['value']))
        self.input_text((login[1]['type'], login[1]['value']), username)
        self.input_text((login[2]['type'], login[2]['value']), password)
        self.is_click((login[3]['type'], login[3]['value']))  # 登录按钮
        # self.find_toast(text)
        # return self.find_toast(text).text

if __name__ == '__main__':
    navigat = read_yaml('Login')['导航']
    print((navigat[0]))
    # print(login[3]['value'])


