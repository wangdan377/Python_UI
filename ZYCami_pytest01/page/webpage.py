# webpage.py

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from config.conf import LOCATE_MODE
from tools.times import sleep
from tools.logger import log
from selenium import webdriver

"""
selenium基类
本文件存放了selenium基类的封装方法
"""


class WebPage(object):
    """selenium基类"""

    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        # a = self.driver.find_elements_by_name("")
        #
        self.driver = driver
        self.timeout = 10
        self.wait = WebDriverWait(self.driver, self.timeout)

    def get_url(self, url):
        """打开网址并验证"""
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(60)
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
            log.info("打开网页：%s" % url)

        except TimeoutException:
            log.info("打开{}超时请检查网络或网址服务器".format(url))
            raise TimeoutException("打开{}超时请检查网络或网址服务器".format(url))

    @staticmethod
    def element_locator(func, locator):
        """元素定位器"""
        name, value = locator
        return func(LOCATE_MODE[name], value)

    def find_element(self, locator):
        """寻找单个元素"""

        return WebPage.element_locator(lambda *args: self.wait.until(
            EC.presence_of_element_located(args)), locator)

    def find_elements(self, locator):
        """查找多个相同的元素"""
        return WebPage.element_locator(lambda *args: self.wait.until(
            EC.presence_of_all_elements_located(args)), locator)

    def focus(self):
        """滚动到底部"""

        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def elements_num(self, locator):
        """获取相同元素的个数"""
        number = len(self.find_elements(locator))
        log.info("相同元素：{}".format((locator, number)))
        return number

    def input_text(self, locator, txt):
        """输入(输入前先清空)"""
        sleep(0.5)
        ele = self.find_element(locator)
        ele.clear()
        ele.send_keys(txt)
        log.info("输入文本：{}".format(txt))

    def is_click(self, locator):
        """点击"""
        self.find_element(locator).click()
        sleep()
        log.info("点击元素：{}".format(locator))

    def is_exists(self, locator):
        """元素是否存在(DOM)"""
        try:
            WebPage.element_locator(lambda *args: EC.presence_of_element_located(args)(self.driver), locator)
            return True
        except NoSuchElementException:
            return False

    def alert_exists(self):
        """判断弹框是否出现，并返回弹框的文字"""
        alert = EC.alert_is_present()(self.driver)
        if alert:
            text = alert.text
            log.info("Alert弹窗提示为：{}".format(text))
            alert.accept()
            return text
        else:
            log.info("没有Alert弹窗提示!")

    def element_text(self, locator):
        """获取当前的text"""
        _text = self.find_element(locator).text
        log.info("获取文本：{}".format(_text))
        return _text

    def get_attribute(self, locator, name):
        """获取元素属性"""
        return self.find_element(locator).get_attribute(name)

    def iframe_switch_iframe(self, locator, number):
        """切换标签"""
        try:
            iframes = self.find_elements(locator)
            self.driver.switch_to.frame(iframes[number - 1])
            log.info("共有{}个标签,切换至第{}个{}标签".format(len(iframes), number, locator[1]))
        except Exception as e:
            raise e

    def iframe_len(self, locator):
        try:
            iframes = self.find_elements(locator)
            log.info("共有{}个标签".format(len(iframes)))
            return len(iframes)
        except Exception as e:
            raise e

    def iframe_parent_frame(self):
        try:
            log.info("返回上一级iframe标签")
            self.driver.switch_to.parent_frame()
        except Exception as e:
            raise e

    def iframe_default_content(self):
        """
        退出iframe标签
        :return:
        """
        try:
            log.info("退出iframe标签")
            self.driver.switch_to.default_content()
        except Exception as e:
            raise e

    def set_select_by_value(self, locator, value):
        """
        通过value设置下拉框值
        :param value: select 标签value值
        :param locator:
        :return:
        """
        try:
            sel = self.find_element(locator)
            Select(sel).select_by_value(value)
            log.info("选择标签的value值为{}".format(value))
        except Exception as e:
            raise e

    def set_select_visible_text(self, locator, text):
        """
        通过text 设置下拉框值
        :param text:
        :param locator:
        :return:
        """
        try:
            sel = self.find_element(locator)
            Select(sel).select_by_visible_text(text)
            log.info("选择的内容为{}".format(text))
        except Exception as e:
            raise e

    def set_select_index(self, locator, index):
        """
        通过index 设置下拉框值
        :param index:
        :param locator:
        :return:
        """
        try:
            sel = self.find_element(locator)
            Select(sel).select_by_index(index)
            log.info("选择的下标为{}".format(index))
        except Exception as e:
            raise e

    def move_to_element(self, locator):
        """
        # 将鼠标悬浮在某个元素上
        :param locator:
        :return:
        """
        try:
            move_to = self.find_element(locator)
            ActionChains(self.driver).move_to_element(move_to).perform()
            log.info("将鼠标移动至{}".format(locator[1]))
        except Exception as e:
            raise e

    def move_scroll_bar(self, number):
        """
        :param number:
        :return:
        """
        try:
            js = "document.documentElement.scrollTop={}".format(number)
            self.driver.execute_script(js)
        except Exception as e:
            raise e

    @property
    def get_source(self):
        """获取页面源代码"""
        log.info("获取页面源代码")
        return self.driver.page_source

    def refresh(self):
        """刷新页面F5"""
        log.info("刷新页面")
        self.driver.refresh()
        self.driver.implicitly_wait(30)


if __name__ == "__main__":
    pass
