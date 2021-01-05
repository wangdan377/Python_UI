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
        width = self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()["height"]
        x = width * 0.15
        start_y = height*0.8
        end_y = height*0.3
        self.driver.swipe(x, start_y, x, end_y, 200)  # 向上滑动

    def swipe_down(self):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        self.driver.swipe(x * 0.15, y * 0.3, x * 0.15, y * 0.8, 200)  # 向下滑动

    def swipe_navigation_up(self):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        self.driver.swipe(x * 0.98, y * 0.8, x * 98, y * 0.2, 200)  # 导航向上滑动

    def swipe_watermark_up(self):  # 视频页向上滑动去找水印
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        self.driver.swipe(x * 0.31, y * 0.46, x * 0.17, y * 0.46, 200)

    def swipe_yuntai_up(self):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        self.driver.swipe(x * 0.19, y * 0.84, x * 0.19, y * 0.28, 200)  # 云台页向上滑动

    def swipe_bottom_navigation_up(self):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        self.driver.swipe(x * 0.96, y * 0.85, x * 0.96, y * 0.3, 200)  # 底部导航向上滑动

    def swipe_bottom_navigation_down(self):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        self.driver.swipe(x * 0.96, y * 0.3, x * 0.96, y * 0.85, 200)  # 底部导航向下滑动

    def swipe_interval_up(self):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        self.driver.swipe(x * 0.35, y * 0.28, x * 0.33, y * 0.28, 200)  # 间隔秒数向上滑动

    def swipe_interval_down(self):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        self.driver.swipe(x * 0.33, y * 0.28, x * 0.85, y * 0.28, 200)  # 间隔秒数向下滑动(滑动到初始值)

    def swipe_shooting_time_up(self):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        self.driver.swipe(x * 0.54, y * 0.28, x * 0.52, y * 0.28, 200)  # 拍摄时长向上滑动

    def swipe_shooting_time_down(self):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        self.driver.swipe(x * 0.54, y * 0.28, x * 0.82, y * 0.28, 200)  # 拍摄时长向下滑动(滑动到初始值)




    def gesture_move(self):
        self.driver.swipe(581, 652, 926, 888, 601)


    #美颜的滚动条
    def swipe_seek_bar_from_start_to_end(self, loc, timeout=0):
        x1 = self.get_ele_x(loc)    #左上角的x
        y1 = self.get_ele_y(loc)    #左上角的y
        y2 = self.get_phone_height()-y1     #左下角的y
        self.driver.swipe(x1, y2, x1, y1, timeout)

    #变焦速度的滚动条
    def swipe_seek_bar_from_start_to_end2(self, loc, timeout=0):
        x1 = self.get_ele_x(loc)
        y1 = self.get_ele_y(loc)
        x2 = self.get_phone_height() - 400
        self.driver.swipe(x1, y1, x2, y1, timeout)

    # 获取元素的x轴坐标的值，通过定位获取
    def get_ele_x(self, loc):
        ele = self.find_element(loc)
        x = ele.location.get("x")
        return x

    # 获取元素的y轴坐标的值，通过定位获取
    def get_ele_y(self, loc):
        ele = self.find_element(loc)
        y = ele.location.get("y")
        return y

    # 获取元素的宽度，通过定位获取
    def get_ele_width(self, loc):
        ele = self.find_element(loc)
        width = ele.size['width']
        return width

    # 获取元素的高度，通过定位获取
    def get_ele_height(self, loc):
        ele = self.find_element(loc)
        height = ele.size['height']
        return height

    # 获取手机屏幕的宽度
    def get_phone_width(self):
        width = self.driver.get_window_size()['width']
        return width

    # 获取手机屏幕的高度
    def get_phone_height(self):
        height = self.driver.get_window_size()['height']
        return height


    def blank_01(self):  # 点击空白区域
        self.driver.tap([(1300, 650)])

    def blank_02(self):  # 点击轨迹
        self.driver.tap([(1651, 313)])

    def blank_03(self):  # 点击编辑
        self.driver.tap([(936, 2316)])

    def blank_04(self):  # 点击删除
        self.driver.tap([(1061, 2314)])

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
        TouchAction(self.driver).long_press(x=x1, y=y1).move_to(x2, y2).release().perform()

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






