# webpage.py

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from config.conf import LOCATE_MODE
from tools.times import sleep
from tools.logger import log
from appium.webdriver.common.touch_action import TouchAction
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
        self.timeout = 20
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
        sleep(0.2)
        log.info("点击元素：{}".format(locator))

    def is_exists(self, locator):
        """元素是否存在(DOM)"""
        try:
            WebPage.element_locator(lambda *args: EC.presence_of_element_located(args)(self.driver), locator)
            log.info('查找到元素', locator)
            return True
        except NoSuchElementException:
            log.info('没有查找到元素', locator)
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

    def find_toast(self, text):
        """获取弹框信息"""
        log.info('获取toast 弹框元素{},{}'.format(LOCATE_MODE['xpath'], '//*[contains(@text,"{}")]'.format((text))))
        return self.wait.until(
            EC.presence_of_element_located(('xpath', '//*[contains(@text,"{}")]'.format(text)))).text

    def element_text(self, locator):
        """获取当前的text"""
        _text = self.find_element(locator).text
        log.info("获取文本：{}".format(_text))
        return _text

    def get_attribute(self, locator, name):
        """获取元素属性"""
        return self.find_element(locator).get_attribute(name)

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

    def swipe_up(self):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        self.driver.swipe(x * 0.15, y * 0.8, x * 0.15, y * 0.3, 200)  # 向上滑动

    def swipe_down(self):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        self.driver.swipe(x * 0.15, y * 0.3, x * 0.15, y * 0.8, 200)  # 向下滑动

    def swipe_navigation_up(self):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        self.driver.swipe(x * 0.98, y * 0.8, x * 98, y * 0.2, 200)  # 导航向上滑动

    def swip_Watermark_up(self):  # 视频页向上滑动去找水印
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        self.driver.swipe(x * 0.31, y * 0.46, x * 0.17, y * 0.46, 200)

    def swip_Yuntai_up(self):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        self.driver.swipe(x * 0.19, y * 0.84, x * 0.19, y * 0.28, 200)  # 云台页向上滑动

    def swip_Bottom_navigation_up(self):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        self.driver.swipe(x * 0.96, y * 0.85, x * 0.96, y * 0.3, 200)  # 底部导航向上滑动

    def swip_Bottom_navigation_down(self):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        self.driver.swipe(x * 0.96, y * 0.3, x * 0.96, y * 0.85, 200)  # 底部导航向下滑动

    def swip_interval_up(self):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        self.driver.swipe(x * 0.35, y * 0.28, x * 0.33, y * 0.28, 200)  # 间隔秒数向上滑动

    def swip_interval_down(self):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        self.driver.swipe(x * 0.33, y * 0.43, x * 0.35, y * 0.43, 200)  # 间隔向下滑动

    def swip_Shooting_time_up(self):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        self.driver.swipe(x * 0.54, y * 0.28, x * 0.52, y * 0.28, 200)  # 拍摄时长向上滑动

    def zoom_speed(self):

        action = TouchAction(self.driver)
        action.press(x=228, y=981).move_to(x=275, y=981).move_to(x=322, y=981).move_to(x=370, y=981).move_to(x=416,
                                                                                                             y=981).move_to(
            x=464, y=981).move_to(x=511, y=981).move_to(x=558, y=981).move_to(x=605, y=981).move_to(x=652,
                                                                                                    y=981).release().perform()

    def roll_beautify(self, zong):  # 美颜滚动条华为mate30
        if zong == 1016:
            for i in range(0, 100):
                try:
                    zong = zong - 8.16
                    self.driver.tap([(632, zong)])
                except:
                    zong = zong - 9
                    self.driver.tap([(632, zong)])

    # def roll_beautify(self,zong):       #美颜滚动条华为mate40
    #     if zong == 1158:
    #         for i in range(0, 100):
    #             try:
    #                 zong = zong - 9.2
    #                 self.driver.tap([(780, zong)])
    #             except:
    #                 zong = zong - 10
    #                 self.driver.tap([(780, zong)])

    def blank_01(self):  # 点击空白区域
        self.driver.tap([(1180, 540)])

    # 返回按钮--通用
    def swip_return(self):
        self.driver.keyevent(4)

    # 封装find_elements方法
    # loc：元素的定位方法
    def find_elements2(self, locator, timeout=5):
        eles = WebDriverWait(self.driver, timeout).until(lambda driver: driver.find_elements(*locator))
        return eles

    def tap_element_coordinate(self, element=None, x=None, y=None):
        """通过trp点击元素"""
        TouchAction(self.driver).tap(element=element, x=x, y=y).perform().release()
        log.info("点击元素：{},{}".format(x, y))

    def move(self,x1,y1,x2,y2):
        TouchAction(self.driver).long_press(x=x1,y=y1).move_to(x2,y2).release().perform()

    # 点击元素，通过元素的坐标
    def tap_element(self, locator):
        ele = self.find_element(locator)
        TouchAction(self.driver).tap(ele).perform()

    # 点击元素列表，通过元素的坐标
    def tap_elements(self, loc, num):
        eles = self.find_elements(loc)
        # num = self.get_elements_num(loc)
        for i in range(num):
            TouchAction(self.driver).tap(eles[i]).perform()
            sleep(1)


    def move_seek_bar(self, locator):
        x1 = self.get_ele_x(locator)
        y1 = self.get_ele_y(locator)
        # x2 = self.get_ele_width(locator) - 10        #滑到最终的值
        x2 = x1 + self.get_ele_width(locator)     #滑动到右上角的值
        # x2 = x1+int(1.1*self.get_ele_width(loc))
        self.move(x1, y1, x2, y1)


    # 获取元素的x轴坐标的值
    def get_ele_x(self, locator):
        ele = self.find_element(locator)
        x = ele.location.get("x")
        return x


    # 获取元素的y轴坐标的值
    def get_ele_y(self, locator):
        ele = self.find_element(locator)
        y = ele.location.get("y")
        return y


    # 获取元素的宽度
    def get_ele_width(self, locator):
        ele = self.find_element(locator)
        width = ele.size['width']
        return width


    # 获取元素的高度
    def get_ele_height(self, locator):
        ele = self.find_element(locator)
        height = ele.size['height']
        return height

    # def touch_moveto(self, locator=None, x=None, y=None):
    #     """元素移动"""
    #     if locator is not None:
    #         ele = self.find_element(locator)
    #         TouchAction(self.driver).move_to(el=ele).perform().release()
    #         log.info("移动元素：{},{}".format(x, y))
    #     else:
    #         TouchAction(self.driver).move_to(x=x, y=y).perform().release()
    #         log.info("移动元素：{},{}".format(x, y))



if __name__ == "__main__":
    # def element_locator(locator):
    #     """元素定位器"""
    #     name, value = locator
    #     return (LOCATE_MODE[name], value)
    #
    #
    # print(element_locator(('css', 'com.zhiyun.cama:id/tv_login')))
    def move_seek_bar(self, locator):
        x1 = self.get_ele_x(locator)
        y1 = self.get_ele_y(locator)
        x2 = self.get_ele_width() - 10  # 滑到最终的值
        # x2 = x1 + self.get_ele_width(loc)     #滑动到右上角的值
        # x2 = x1+int(1.1*self.get_ele_width(loc))
        self.move(x1, y1, x2, y1)