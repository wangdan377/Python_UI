#coding:utf-8
'''
基于元素操作的一些函数和方法
'''


from selenium.webdriver.support.wait import WebDriverWait
from Page.Setting_Page import *
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC

class Base_Function(object):
    def __init__(self, driver):
        self.driver = driver

    # #重写find_element方法
    def find_element(self, loc, timeout=20):
        WebDriverWait(self.driver, timeout).until(lambda driver: driver.find_element(*loc))
        return self.driver.find_element(*loc)

    # def find_element(self, loc, timeout=30):
    #     element = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located(loc))
    #     return element

    #重写clear方法
    def clear(self, loc):
        self.find_element(loc).clear()
        # time.sleep(1)

    #重写send_keys方法
    def send_keys(self, loc, value):
        self.clear(loc)
        self.find_element(loc).send_keys(value)
        # time.sleep(1)

    #重写click方法
    def click(self, loc):
        self.find_element(loc).click()
        # time.sleep(1)

    #判断元素是否存在
    def elementIsExist(self, loc):
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(loc))
            return True
        except:
            return False
        # eles = self.driver.find_elements(loc)
        # if len(eles) < 1:
        #     return False
        # else:
        #     return True

    #判断元素不存在
    def elementIsNotExist(self, loc):
        try:
            self.driver.find_element(loc)
            return False
        except:
            return True



    #从Excel表格中获取指定用例名称的测试用例数据
    #data:excel表格中的所有数据
    #exce_case_name:excel表格中的测试用例名称
    #script_case_name:自动化测试
    # 用例中的测试用例名称
    def get_expected_data(self, data, excel_case_name, script_case_name):
        expeceted_data = dict()
        for i in data:
            if i[excel_case_name] == script_case_name:
                expeceted_data = i
                print("Test data:", expeceted_data)
                break
        return expeceted_data

    #截图，默认将截图保存在//Appium//ScreenShot文件夹中，截图命名为screenshot+测试用例名+截图时间+.png
    #test_name:测试用例名称
    def get_screenshot(self, test_name, msg):
        try:
            time.sleep(1)
            timestr = time.strftime("%Y-%m-%d_%H_%M_%S")
            # self.driver.get_screenshot_as_file("././ScreenShot"+"screenshot"+test_name+timestr+".png")
            self.driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"\ScreenShot" + "screenshot" + test_name + timestr + ".png")
        finally:
            raise msg

    #向上滑动
    #time：滑动的时间
    def swipe_up(self, time=1000):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x * 0.5, y * 0.75, x * 0.5, y * 0.25, self, time)

    #向下滑动
    #time：滑动的时间
    def swipe_down(self, time=1000):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x * 0.5, y * 0.25, x * 0.5, y * 0.75, self, time)

    #向左滑动
    #time：滑动的时间
    def swipe_left(self, time=1000):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x * 0.75, y * 0.5, x * 0.25, y * 0.5, self, time)

    #向右滑动
    #time：滑动的时间
    def swipe_right(self, time=1000):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x * 0.25, y * 0.5, x * 0.75, y * 0.5, self, time)

    #封装长按方法
    #x1，y1表示坐标的x值和y值
    #time表示长按时间
    def long_press(self, x1, y1, time):
        TouchAction(self.driver).long_press(x=x1, y=y1).wait(time).release().perform()

    #封装短按方法
    #x1，y1表示坐标的x值和y值
    def short_press(self, x1, y1):
        TouchAction(self.driver).press(x=x1, y=y1).release().perform()

    #封装拖动方法
    #x1，y1表示拖动前的起始位置，x2，y2表示拖动后的终止坐标
    #time表示拖动时间
    def move(self, x1, y1, x2, y2, time):
        TouchAction(self.driver).long_press(x=x1, y=y1).move_to(x=x2, y=y2).release().perform()

















