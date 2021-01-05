# import unittest
# import time
# from appium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
#
#
# class Untitled(unittest.TestCase):
#     reportDirectory = 'reports'
#     reportFormat = 'xml'
#     dc = {}
#     testName = 'Untitled'
#     driver = None
#
#     def setUp(self):
#         self.dc['reportDirectory'] = self.reportDirectory
#         self.dc['reportFormat'] = self.reportFormat
#         self.dc['testName'] = self.testName
#         self.dc['udid'] = '7HX0219918017044'
#         self.dc['appPackage'] = 'com.zhiyun.cama'
#         self.dc['appActivity'] = '.splash.SplashActivity'
#         self.dc['platformName'] = 'android'
#         self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.dc)
#
#     def testUntitled(self):
#         self.driver.find_element_by_xpath("xpath=//*[@id='iv_camera']").click()
#         WebDriverWait(self.driver, 10).until(
#             expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="ib_help"]')))
#         self.driver.find_element_by_xpath("xpath=//*[@id='ib_help']").click()
#
#         self.driver.find_element_by_xpath("xpath=//*[@id='texture_view']").click()
#         self.driver.find_element_by_xpath("xpath=//*[@id='cb_delay_set']").click()
#         WebDriverWait(self.driver, 30).until(
#             expected_conditions.presence_of_element_located((By.XPATH, '//*[@class="android.view.ViewGroup"]')))
#         self.driver.find_element_by_xpath("xpath=//*[@class='android.view.ViewGroup']").click()
#         self.driver.find_element_by_xpath("xpath=//*[@id='cb_path']").click()
#         self.driver.find_element_by_xpath("xpath=//*[@class='android.view.ViewGroup']").click()
#         self.driver.find_element_by_xpath("xpath=//*[@id='cb_path']").click()
#         self.driver.find_element_by_xpath("xpath=//*[@class='android.view.ViewGroup']").click()
#         self.driver.find_element_by_xpath("xpath=//*[@id='cb_path']").click()
#
#     def tearDown(self):
#         self.driver.quit()
#
#
# if __name__ == '__main__':
#     unittest.main()
