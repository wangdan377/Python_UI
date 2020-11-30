# -*-coding:utf-8-*-
"""
============================
author:chenglei
time:2019/8/12
E-mail:461419962@qq.com
============================
"""
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common.constant import SCREEN_SHOT
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
import datetime
import time
import os
# import win32gui
# import win32con
from selenium.webdriver.common.action_chains import ActionChains
from Common import logger # 直接执行了logger里的代码。设置日志输出。

class BasePage:
    #初始化
    def __init__(self, driver):
        self.driver = driver
    #等待元素可见
    def wait_ele_visible(self,loc,img_desc,timeout = 30,frequency = 0.5):
        start = datetime.datetime.now() #用datetime模块获取当前时间
        try:
            WebDriverWait(self.driver,timeout,frequency).until(EC.visibility_of_element_located(loc))
        except:
            logging.exception("等待元素{}可见失败!".format(loc))
            #截图
            self.save_imgs(img_desc)
            #抛出异常,让用例识别到异常
            raise
        else:
            end  = datetime.datetime.now()      #用datetime模块获取当前时间
            logging.info("等待{}元素：{}可见成功，耗时：{}".format(img_desc,loc,end-start))

    #等待元素存在
    def wait_ele_exists(self,loc,img_desc,timeout = 30,frequency = 0.5):
        start = datetime.datetime.now() #用datetime模块获取当前时间
        try:
            WebDriverWait(self.driver,timeout,frequency).until(EC.presence_of_all_elements_located(loc))
        except:
            logging.exception("等待元素：{}存在失败!".format(loc))
            #截图
            self.save_imgs(img_desc)
            #抛出异常,让用例识别到异常
            raise
        else:
            end  = datetime.datetime.now()      #用datetime模块获取当前时间
            logging.info("等待{}元素：{}存在成功，耗时：{}".format(img_desc,loc,end-start))

    #查找元素
    def get_element(self,loc,img_desc):
        try:
            ele = self.driver.find_element(*loc)
        except:
            logging.exception("等待{}元素：{}可见失败!".format(img_desc,loc))
            # 截图
            self.save_imgs(img_desc)
            # 抛出异常,让用例识别到异常
            raise
        else:
            logging.info("等待{}元素：{}可见成功!".format(img_desc, loc))
            return ele

    #点击元素
    def click_element(self,loc,img_desc,timeout = 30,frequency = 0.5):
        #先等待元素可见
        self.wait_ele_visible(loc,img_desc,timeout,frequency)
        #再查找元素
        ele = self.get_element(loc,img_desc)
        try:
            ele.click()
            logging.info("点击{}元素：{}成功!".format(img_desc, loc))
        except:
            logging.exception("点击{}元素：{}失败!".format(img_desc, loc))
            # 截图
            self.save_imgs(img_desc)
            # 抛出异常,让用例识别到异常
            raise
    #输入数据
    def input_text(self,loc,value,img_desc,timeout = 30,frequency = 0.5):
        # 先等待元素可见
        self.wait_ele_exists(loc, img_desc, timeout, frequency)
        # 再查找元素
        ele = self.get_element(loc, img_desc)
        try:
            ele.send_keys(value)
            logging.info("在{}的元素：{}上输入文本值：{}成功!".format(img_desc, loc,value))
        except:
            logging.exception("在{}的元素：{}上输入文本值：{}失败!".format(img_desc, loc,value))
            # 截图
            self.save_imgs(img_desc)
            # 抛出异常,让用例识别到异常
            raise

    def get_text(self,loc,img_desc,timeout=30,frequency = 0.5):
        #等待元素存在
        #查找元素
        #获取元素的文本值
        self.wait_ele_exists(loc, img_desc, timeout, frequency)
        ele = self.get_element(loc, img_desc)
        try:
            text= ele.text
        except:
            logging.exception("获取{}元素：{}文本失败!".format(img_desc, loc))
            # 截图
            self.save_imgs(img_desc)
            # 抛出异常,让用例识别到异常
            raise
        else:
            logging.info("获取{}元素：{} 文本成功!".format(img_desc, text))
            return text

    def get_ele_attribute(self,loc,attr_name,img_desc,timeout = 30,frequency = 0.5):
        # 等待元素存在
        # 查找元素
        # 获取元素的属性
        self.wait_ele_exists(loc, img_desc, timeout, frequency)
        ele = self.get_element(loc, img_desc)
        try:
            attr_value = ele.get_attribute(attr_name)
        except:
            logging.exception("获取{}元素：{}的属性：{}失败!".format(img_desc, loc,attr_name))
            # 截图
            self.save_imgs(img_desc)
            # 抛出异常,让用例识别到异常
            raise
        else:
            logging.info("获取{}元素：{}的{}属性成功!属性值为：{}".format(img_desc, loc,attr_name,attr_value))
            return attr_value

    #鼠标移动到目标坐标松开
    def mouse_drag_and_drop(self,loc,xoffset,yoffset,img_desc,timeout = 30,frequency = 0.5):
        #等待元素可见
        self.wait_ele_visible(loc,img_desc,timeout,frequency)
        source = self.get_element(loc,img_desc)
        try:
            ActionChains(self.driver).drag_and_drop_by_offset(source,xoffset,yoffset).perform()
        except:
            logging.exception("{}元素鼠标移动到目标位置{},{}失败".format(source,xoffset,yoffset))
            self.save_imgs(img_desc)
            raise
        else:
            logging.exception("{}元素鼠标移动到目标位置{},{}成功".format(source,xoffset,yoffset))


    # 上传操作
    def upload_file(self,filepath,img_desc):
        try:
            # 一级窗口
            dialog = win32gui.FindWindow("#32770", "打开")
            # 二级窗口
            ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
            # 三级窗口
            ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)
            # 文本输入框--四级窗口
            edit = win32gui.FindWindowEx(ComboBox, 0, "Edit", None)
            # 打开按钮--二级窗口
            button = win32gui.FindWindowEx(dialog, 0, "Button", "打开(&O)")

            # 输入文件地址
            win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filepath)
            # 点击“打开”按钮--提交文件
            win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
            logging.info("{} 文件上传操作成功".format(img_desc))
        except:
            logging.exception("文件上传失败！！！")
            # 截图
            self.save_imgs(img_desc)
            raise


    #切换到iframe
    def switch_iframe(self,refrence,img_desc,timeout = 30):
        try:
            WebDriverWait(self.driver,timeout).until(EC.frame_to_be_available_and_switch_to_it(refrence))
        except:
            logging.exception("切换到{}的iframe:{}失败".format(img_desc,refrence))
            #截图
            self.save_imgs(img_desc)
            raise
        else:
            logging.info("切换到{}的iframe:{}成功".format(img_desc, refrence))

        # windows窗口切换

    def switch_window(self,handles,doc,timeout=30, poll_frequency=0.5):
        # 使用WebDriverWait进行iframe切换
        try:
            # 等待新窗口出现
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.new_window_is_opened(handles))
            # 新窗口打开后，重新获取句柄
            handles = self.driver.window_handles
            # 切换窗口
            self.driver.switch_to.window(handles[-1])
            time.sleep(0.5)
            logging.info("window窗口切换成功")
        except:
            logging.exception("windows窗口切换失败")
            # 截图
            self.save_imgs(doc)
            raise

    #窗口滚动到当前元素的页面底部对齐
    def scroll_into_bottom(self,loc,img_desc,timeout=30, poll_frequency=0.5):
        #先等待元素存在
        self.wait_ele_exists(loc,img_desc,timeout,poll_frequency)
        #找到元素
        ele = self.get_element(loc,img_desc)
        try:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", ele)
        except:
            logging.exception("窗口滚动到当前元素页面底部对齐失败")
            self.save_imgs(img_desc)
            raise
        else:
            logging.exception("窗口滚动到当前元素页面底部对齐")



    #保存错误截图
    def save_imgs(self,img_description):
        """
        :param img_description: 图片的描述，格式：页面名称_功能名_时间戳
        :return:
        """
        #时间戳 time模块， 不要有:
        #文件路径
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        # 时间戳 time模块  不要有:
        filepath = "{}_{}.png".format(img_description, now)
        img_path = os.path.join(SCREEN_SHOT, filepath)
        try:
            self.driver.save_screenshot(img_path)
        except:
            logging.exception("当前网页截图失败")
        else:
            logging.info("截图成功，截图存放在:{}".format(img_path))


    #alert切换、下拉列表Select、windows切换


if __name__ == '__main__':
    driver = webdriver.Chrome()
    pass

    # driver.get("http://sign.oa.com")
    #
    # A = BasePage(driver)
    # B = A.get_text((By.XPATH,'//i[@class = "el-input__icon el-icon-search user_bg"]//parent::*//following-sibling::div'),'因为')
    # print(B)
    # driver.quit()