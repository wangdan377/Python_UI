from appium import webdriver
import time,unittest,os,sys,HTMLTestRunner,logging
from common.loged import Logger
from selenium.common.exceptions import  NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException




class Beautify_Fair(object):
    '''美颜'''
    """def __init__(self):
        # self.driver = self.devices()    #感觉是这里的问题
        # self.driver = 'driver'
        pass"""
    def devices(self):

        """desired_caps = {}
        desired_caps['platformName'] = 'Android'  # Android系统 or IOS系统
        desired_caps['deviceName'] = '7HX0219918017044'  # 真机或模块器名
        desired_caps['platformVersion'] = '10'  # Android系统版本
        desired_caps['appPackage'] = 'com.zhiyun.cama'  # APP包名
        desired_caps['appActivity'] = '.splash.SplashActivity'  # APP启动Activity
        desired_caps['noReset'] = True  # 每次打开APP不开启重置，否则每次都进入四个欢迎页
        desired_caps['resetKeyboard'] = True  # 隐藏键盘        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 启动APP
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)"""  # 启动APP
        desired_caps = {'platformName': 'Android',  # 手机系统
                        'deviceName': '7HX0219918017044',
                        'noReset': True,  # 防止每次启动时软件初始化
                        'appPackage': 'com.zhiyun.cama',
                        'appActivity': '.splash.SplashActivity',
                        'unicodeKeyboard': True,  # 使用unicode编码方式发送字符串
                        'resetKeyboard': True}  # 将键盘隐藏起来
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        desired_caps['newCommandTimeout'] = 6000
        self.driver.implicitly_wait(15)
        return self.driver

    """def connecting00(self):  # 不连接相机/不连接设备
        driver = self.driver
        driver.find_element_by_id("com.zhiyun.cama:id/iv_camera").click()  # 点击相机按钮
        time.sleep(5)
        driver.find_element_by_id("com.zhiyun.cama:id/ib_help").click()  # 点击帮助
        driver.find_element_by_id("com.zhiyun.cama:id/enter").click()  # 不连设备,直接进入拍照
        # driver.find_element_by_id("com.zhiyun.cama:id/bt_connect").click()  #连接设备
        try:
            driver.find_element_by_id("com.zhiyun.cama:id/iv_camera").click()#点击相机按钮
            time.sleep(5)
            driver.find_element_by_id("com.zhiyun.cama:id/ib_help").click()  # 点击帮助
            driver.find_element_by_id("com.zhiyun.cama:id/enter").click()  # 不连设备,直接进入拍照
            # driver.find_element_by_id("com.zhiyun.cama:id/bt_connect").click()  #连接设备
            time.sleep(5)
        except NoSuchElementException as a: #元素不存在，则调用捕获异常处理
            Logger('D:\ZY_Cami03\logs\error.log', level='error').logger.error(a)
        except NoAlertPresentException as b:   #捕获意外的异常
            Logger('D:\ZY_Cami03\logs\error.log', level='error').logger.error(b)
        except Exception as result:
            Logger('D:\ZY_Cami03\logs\error.log', level='error').logger.error(result)
        else:
            pass  #没有错的情况下执行
        finally:
            pass  #有没有错，都会执行
        return ''"""
    def connecting01(self):   #不连接相机/不连接设备
        driver = self.driver
        time.sleep(5)
        driver.find_element_by_id("com.zhiyun.cama:id/iv_camera").click()  # 相机
        time.sleep(5)
        driver.find_element_by_id("com.zhiyun.cama:id/ib_help").click()   #点击帮助
        driver.find_element_by_id("com.zhiyun.cama:id/enter").click()  # 不连设备,直接进入拍照
        # driver.find_element_by_id("com.zhiyun.cama:id/bt_connect").click()  #连接设备
        time.sleep(5)
        return '不连接相机/不连接设备'
    def beautify_01(self):     #美颜
        driver = self.driver
        time.sleep(5)
        driver.find_element_by_id("com.zhiyun.cama:id/iv_beauty").click()     #美颜
        time.sleep(2)
        # driver.find_element_by_id("com.zhiyun.cama:id/sb_roll").click()     #进度条	[533,150][732,1066]     199  916
        # driver.tap([(1180,540)])  #点击空白区域
        # driver.tap([(632, 1022)])   #横坐标632  #纵坐标1022
        return '点击美颜按钮'

    def slides01(self): #向上滑动
        driver = self.driver
        x = driver.get_window_size()["width"]
        y = driver.get_window_size()["height"]
        driver.swipe(x * 0.15, y * 0.8, x * 0.15, y * 0.3, 200)  # 向上滑动
        time.sleep(2)
        return '向上滑动'
    def slides02(self):
        driver = self.driver
        x = driver.get_window_size()["width"]
        y = driver.get_window_size()["height"]
        driver.swipe(x * 0.15, y * 0.3, x * 0.15, y * 0.8, 200)  # 向下滑动
        time.sleep(2)
        return '向下滑动'
    def beautify_02(self):     #自动美颜
        driver = self.driver
        self.slides01()   # 调用slides函数（向上滑动）
        driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]").click()  # 自动美颜 无进度条
        return '向上滑动，自动美颜'
    def blank_01(self):     #点击空白区域
        driver = self.driver
        driver.tap([(1180, 540)])  # 点击空白区域
        return '点击空白区域，关闭美颜'
    def beautify_03(self):     #取消美颜
        driver = self.driver
        self.beautify_01() #美颜
        self.slides01()  #向上滑动
        time.sleep(2)
        driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]").click()  # 取消美颜
        return '向上滑动，取消美颜'

    def beautify_04(self):      #瘦脸
        driver = self.driver
        self.beautify_01()     #点击美颜
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]").click()        #瘦脸
        return '瘦脸'
    def beautify_05(self):     #磨皮
        self.beautify_01()    #点击美颜
        driver = self.driver
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[4]").click()		 #磨皮
        return '磨皮'


    def beautify_06(self):  # 美白
        driver = self.driver
        self.slide()   #滑动进度条
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]").click()		  #美白
        self.slide()  # 滑动进度条

        return '美白'
    def slide(self):        #滑动
        driver = self.driver
        driver.tap([(632, 1022)])
        return '滑动'
    def beautify_07(self):  # 眼睛放大
        driver = self.driver
        self.slides02()  # 向下滑动
        time.sleep(2)
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]").click()		   #眼睛放大
        return '眼睛放大'

    def beautify_08(self):  # 光照
        driver = self.driver
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[4]").click()		 #光照
        return '光照'

    def beautify_09(self):  # 红润
        driver = self.driver
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[5]").click()		#红润
        return '红润'

    def picture_01(self):  # 点击拍照
        driver = self.driver
        self.blank_01()   #点击空白区域
        driver.find_element_by_id("com.zhiyun.cama:id/cb_action").click()		#拍照
        driver.find_element_by_id("com.zhiyun.cama:id/cb_action").click()
        # 循环
        '''num = 0
        for i in range(5):   
            try:
                num = num + 1
                driver.find_element_by_id("com.zhiyun.cama:id/cb_action").click()
            except:
                try:
                    num = num -1
                    driver.find_element_by_id("com.zhiyun.cama:id/cb_action").click()
                except:
                    num = num - 2
                    driver.find_element_by_id("com.zhiyun.cama:id/cb_action").click()'''
        return '点击拍照 '

if __name__ == '__main__':
    pic = Beautify_Fair()
    print(pic.devices())
    # print(pic.connecting00())
    print(pic.connecting01())
    print(pic.beautify_01())
    print(pic.slides01())
    print(pic.slides02())
    print(pic.beautify_02())
    print(pic.blank_01())
    print(pic.beautify_03())
    print(pic.beautify_04())
    print(pic.beautify_05())
    print(pic.beautify_06())
    print(pic.slide())    #滑动
    print(pic.beautify_07())
    print(pic.beautify_08())
    print(pic.beautify_09())
    print(pic.picture_01())
