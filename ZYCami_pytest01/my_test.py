


# def test1(loa = None):
#     if loa is not None:
#         print('不为空')
#     else:
#         print('为空')
#
# if __name__ == '__main__':
#
#     test1()


import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


"""class Untitled(unittest.TestCase):
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'Untitled'
    driver = None

    def setUp(self):
        self.dc['reportDirectory'] = self.reportDirectory
        self.dc['reportFormat'] = self.reportFormat
        self.dc['testName'] = self.testName
        self.dc['udid'] = '7HX0219918017044'
        self.dc['appPackage'] = 'com.zhiyun.cama'
        self.dc['appActivity'] = '.splash.SplashActivity'
        self.dc['platformName'] = 'android'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.dc)

    def testUntitled(self):
        self.driver.find_element_by_xpath("xpath=//*[@id='iv_camera']").click()

        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="ib_help"]')))
        self.driver.find_element_by_xpath("xpath=//*[@id='ib_help']").click()

        self.driver.find_element_by_xpath(
            "xpath=//*[@text='直接进入' and (./preceding-sibling::* | ./following-sibling::*)[@text='SMOOTH-X']]").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='延时摄影']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='cb_delay_set']").click()
        self.driver.find_element_by_xpath("xpath=//*[@class='android.view.ViewGroup']").click()

        self.driver.find_element_by_xpath("xpath=//*[@id='cb_path']").click()

        self.driver.find_element_by_xpath("xpath=//*[@id='cb_path']").click()


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
"""
# desired_caps ={'platformName':'Android',#手机系统
#                 'deviceName':'7HX0219918017044',
#                 'noReset':True,#防止每次启动时软件初始化
#                 'appPackage':'com.zhiyun.cama',
#                 'appActivity':'.splash.SplashActivity',
#                 'unicodeKeyboard':True,#使用unicode编码方式发送字符串
#                 'resetKeyboard':True}#将键盘隐藏起来
#
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# driver.implicitly_wait(8)
#
# time.sleep(5)
# driver.find_element_by_id("com.zhiyun.cama:id/iv_camera").click()	  #相机
# time.sleep(2)
#
#
# driver.find_element_by_id("com.zhiyun.cama:id/bt_connect").click()
# # driver.find_element_by_xpath("//*[@text='SMOOTH-X_C17F']/following-sibling::android.widget.Button']").click()
#
# time.sleep(2)
# driver.find_element_by_id("com.zhiyun.cama:id/cb_delay_set").click()
# time.sleep(2)
# driver.tap([(1300, 650)])
# driver.find_element_by_id("com.zhiyun.cama:id/cb_delay_set").click()
#
# driver.tap([(1650, 302)])
# time.sleep(2)
# driver.find_element_by_id("com.zhiyun.cama:id/cb_path").click()
# time.sleep(2)
#
# driver.tap([(1650, 302)])
# time.sleep(2)
#
# for i in range(5):
#
#     driver.find_element_by_id("com.zhiyun.cama:id/view_add_point").click()
# time.sleep(3)
# driver.find_element_by_id("com.zhiyun.cama:id/iv_delete").click()
# driver.find_element_by_id("com.zhiyun.cama:id/view_add_point").click()
# time.sleep(3)
#
# driver.find_element_by_id("com.zhiyun.cama:id/tv_delay_time").click()
# time.sleep(3)
#
# driver.find_element_by_id("com.zhiyun.cama:id/cb_action").click()
# time.sleep(3)

