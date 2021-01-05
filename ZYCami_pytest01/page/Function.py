#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
import time, os
from tools.logger import log


class BaseFun(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, loc, timeout=5):
        # driver表示驱动；timeout表示最长超时的时间，以秒为单位
        # 一般与until()或者until_not()组合使用
        # is_displayed 是用来判断元素是否显
        try:
            WebDriverWait(self.driver, timeout).until(lambda driver: driver.find_element(*loc))
            return self.driver.find_element(*loc)
        except Exception as e:
            log.info('{}元素可见失效，错误：{}'.format(loc, e))
            raise e

    # 多个元素
    def find_elements(self, loc, timeout=5):  # frequency
        try:
            eles = WebDriverWait(self.driver, timeout).until(lambda driver: driver.find_elements(*loc))

        except Exception as e:
            raise e
        return eles

    # 多个元素，根据列表查找
    def get_elements_num(self, loc, timeout=5):
        # 用find_elements查找元素，返回的是列表
        eles = WebDriverWait(self.driver, timeout).until(lambda driver: driver.find_elements(*loc))
        # length = len(eles)
        # return length
        return eles

    # 判断元素是否存在
    def is_element_exist(self, loc):
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(loc))
            return True
        except:
            return False

    # 重写clear方法
    def clear(self, loc):
        self.find_element(loc).clear()

    # 重写send_keys()方法
    def send_keys(self, loc, value):
        self.clear(loc)  # 先清除文本框的内容
        self.find_element(loc).send_keys(value)  # 输入内容，value是传入要输入的内容
        log.info("点击元素：{}".format(loc))

    # 重写click()方法
    def click(self, loc):
        self.find_element(loc).click()
        time.sleep(2)
        log.info("点击元素：{}".format(loc))

    def clickButton(self, loc, find_first=True):

        try:
            if find_first:
                self.find_element(loc)
            self.find_element(loc).click()
        except Exception as e:
            log.logger.error(e)

    # 重新封装按钮点击方法
    # 向上滑动(美颜向上)
    def swip_up(self, time=200):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        self.driver.swipe(x * 0.15, y * 0.8, x * 0.15, y * 0.3, time)  # 向上滑动

    # 向下滑动(美颜向下)
    def swip_down(self, time=200):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        self.driver.swipe(x * 0.15, y * 0.3, x * 0.15, y * 0.8, time)  # 向上滑动

    # 页面向左滑动
    def swip_left(self, time=200):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        self.driver.swipe(x * 0.8, y * 0.15, x * 0.3, y * 0.15, time)

    # 向右滑动
    def swip_right(self, time=200):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        self.driver.swipe(x * 0.3, y * 0.15, x * 0.8, y * 0.15, time)  # 向右滑动

    # prime页面购买设备向左滑动
    def swip_prime_left01(self, time=200):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        self.driver.swipe(x * 0.5, y * 0.8, x * 0.1, y * 0.8, time)  # 向左滑动

    # prime页面购买设备向右滑动
    def swip_prime_right01(self, time=200):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        self.driver.swipe(x * 0.1, y * 0.8, x * 0.5, y * 0.8, time)  # 向左滑动

    # prime页面素材向左滑动
    def swip_material_left01(self, time=200):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        self.driver.swipe(x * 0.45, y * 0.65, x * 0.1, y * 0.65, time)  # 向左滑动

    # prime页面素材向右滑动
    def swip_material_right01(self, time=200):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        self.driver.swipe(x * 0.1, y * 0.65, x * 0.45, y * 0.65, time)  # 向左滑动

    # prime 待领取页面素材向左滑动
    def swip_material_left02(self, time=200):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        self.driver.swipe(x * 0.54, y * 0.48, x * 0.1, y * 0.48, time)  # 向左滑动

    # prime页面素材向右滑动
    def swip_material_right02(self, time=200):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        self.driver.swipe(x * 0.1, y * 0.48, x * 0.54, y * 0.48, time)  # 向左滑动

    # 向左滑动-找到特定元素停止滑动
    # time：滑动的时间
    def swipe_left_find_ele(self, loc, timeout=1000):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        flag = True
        i = 0
        while flag:
            if self.is_element_exist(loc):
                break
            else:
                self.driver.swipe(x * 0.5, y * 0.98, x * 0.25, y * 0.98, timeout)
                i = i + 1
            if i == 3:
                flag = False

    # 点击元素，通过元素的坐标
    def tap_element(self, loc):
        ele = self.find_element(loc)
        TouchAction(self.driver).tap(ele).perform()

    # 返回按钮--通用
    def swip_return(self):
        self.driver.keyevent(4)

    # prime弹框关闭，用坐标
    def swip_prime_closed(self):
        self.driver.tap([(969, 539)])

    # 云剪辑-制作，用坐标
    def swip_yun_Make(self):
        self.driver.tap([(291, 1104)])

    # 套餐1，用坐标
    def swip_meal01(self):
        self.driver.tap([(204, 724)])

    # 套餐2，用坐标
    def swip_meal02(self):
        self.driver.tap([(551, 724)])

    # 套餐3，用坐标
    def swip_meal03(self):
        self.driver.tap([(859, 724)])

    # 有效期，用坐标
    def swip_open_record(self):
        self.driver.tap([(262, 777)])

    # 微信支付
    def swip_wx_pay(self):
        self.driver.tap([(955, 1325)])

    # 关闭微信支付
    def swip_wx_closed(self):
        self.driver.tap([(981, 1099)])

    # 封装长按方法，te表示长按的时间
    def long_press(self, x1, y1, te):
        TouchAction(self.driver).press(x=x1, y=y1).release().perform()

    # 拖动，x1,y1表示拖动前的初始位置；x2,y2表示拖动后的终止坐标；te表示时间
    def move(self, x1, y1, x2, y2):
        TouchAction(self.driver).long_press(x=x1, y=y1).move_to(x2, y2).release().perform()

    # 判断控件是否存在
    def elementIsExit(self, loc):
        if self.find_element(loc) == 0:
            print(0)
            return 0
        else:
            print(1)
            return 1

    # savePngName:生成图片的名称
    def savePngName(self, name):
        """name：自定义图片的名称"""
        day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        fp = "Result\\" + day + "\\image\\" + day
        tm = self.saveTime()
        type = ".png"
        if os.path.exists(fp):
            filename = fp + "\\" + tm + "_" + name + type
            print(filename)
            # print "True"
            return filename
        else:
            os.makedirs(fp)
            filename = fp + "\\" + tm + "_" + name + type
            print(filename)
            # print "False"
            return filename

        # 获取系统当前时间

    def saveTime(self):
        """返回当前系统时间以括号中（2014-08-29-15_21_55）展示"""
        return time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))

    def saveScreenshot(self, name):
        """
    快照截图   saveScreenshot:通过图片名称，进行截图保存
    name:图片名称
    """
        # 获取当前路径
        # print os.getcwd()
        image = self.driver.save_screenshot(self.savePngName(name))
        return image

    # 封装find_elements方法
    # loc：元素的定位方法
    def find_elements(self, loc, timeout=5):
        eles = WebDriverWait(self.driver, timeout).until(lambda driver: driver.find_elements(*loc))
        return eles

    # 点击坐标
    def tap_coordinate(self, x, y):
        self.driver.tap([(x, y)])

    # 先定位元素 通过tap方法操作元素
    def tap_element(self, loc):
        ele = self.find_element(loc)
        TouchAction(self.driver).tap(ele).perform()

    # 获取元素的x,y轴坐标的值
    def get_xy_click(self, loc):
        """通过元素获取坐标，然后使用tap坐标点击  """
        ele = self.find_element(loc)
        x = ele.location.get("x")
        y = ele.location.get("y")
        self.driver.tap([(x, y)])

    # 点击元素列表，通过元素的坐标
    def tap_elements(self, loc, num):
        eles = self.find_elements(loc)
        # num = self.get_elements_num(loc)
        for i in range(num):
            TouchAction(self.driver).tap(eles[i]).perform()
            time.sleep(1)

    def move_seek_bar(self, loc):
        x1 = self.get_ele_x(loc)
        y1 = self.get_ele_y(loc)
        x2 = self.get_ele_width() - 10  # 滑到最终的值
        # x2 = x1 + self.get_ele_width(loc)     #滑动到右上角的值
        # x2 = x1+int(1.1*self.get_ele_width(loc))
        self.move(x1, y1, x2, y1)

    # 获取元素的x轴坐标的值
    def get_ele_x(self, loc):
        ele = self.find_element(loc)
        x = ele.location.get("x")
        return x

    # 获取元素的y轴坐标的值
    def get_ele_y(self, loc):
        ele = self.find_element(loc)
        y = ele.location.get("y")
        return y

    # 获取元素的宽度
    def get_ele_width(self, loc):
        ele = self.find_element(loc)
        width = ele.size['width']
        return width

    # 获取元素的高度
    def get_ele_height(self, loc):
        ele = self.find_element(loc)
        height = ele.size['height']
        return height

if __name__ == '__main__':
    # from selenium import webdriver
    # driver = webdriver.Remote()
    # driver.find_element().location.get()
    # 以后看到不懂的方法可以这样操作 去看下他的源码注释
    pass