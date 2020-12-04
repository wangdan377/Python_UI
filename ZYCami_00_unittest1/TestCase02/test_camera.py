from appium import webdriver
import time,unittest,os,sys,HTMLTestRunner

"""desired_caps = {}
desired_caps['platformName'] = 'Android'  # Android系统 or IOS系统
desired_caps['deviceName'] = '7HX0219918017044'  # 真机或模块器名
desired_caps['platformVersion'] = '10'  # Android系统版本
desired_caps['appPackage'] = 'com.zhiyun.cama'  # APP包名
desired_caps['appActivity'] = '.splash.SplashActivity'  # APP启动Activity
desired_caps['noReset'] = True  # 每次打开APP不开启重置，否则每次都进入四个欢迎页
desired_caps['resetKeyboard'] = True  # 隐藏键盘        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 启动APP
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)"""  # 启动APP"""

desired_caps ={'platformName':'Android',#手机系统
                'deviceName':'7HX0219918017044',
                'noReset':True,#防止每次启动时软件初始化
                'appPackage':'com.zhiyun.cama',
                'appActivity':'.splash.SplashActivity',
                'unicodeKeyboard':True,#使用unicode编码方式发送字符串
                'resetKeyboard':True}#将键盘隐藏起来
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(5)
# driver.find_element_by_id("com.zhiyun.cama:id/positive").click()
# driver.find_element_by_id("com.zhiyun.cama:id/positive").click()
# driver.tap([(969, 539)])
# time.sleep(5)
# driver.find_element_by_id("com.zhiyun.cama:id/positive").click()
# time.sleep(5)
# driver.tap(x=969, y=539).perform()
# driver.find_element_by_xpath("//android.widget.FrameLayout[@content-desc=\"Home\"]/android.widget.ImageView").click()   #进入首页
# time.sleep(3)
# driver.find_element_by_xpath("//android.widget.FrameLayout[@content-desc=\"Me\"]/android.widget.ImageView").click() #我的按钮
# time.sleep(3)
# driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.TextView[1]").click()		#prime文字
# time.sleep(3)
# driver.keyevent(4)          #模拟返回按钮
driver.find_element_by_id("com.zhiyun.cama:id/iv_camera").click()	  #相机
time.sleep(2)
# driver.find_element_by_id("com.zhiyun.cama:id/bt_connect").click()      #连接
# time.sleep(5)
driver.find_element_by_id("com.zhiyun.cama:id/ib_help").click()	 #问号
# time.sleep(2)
driver.find_element_by_id("com.zhiyun.cama:id/enter").click()
# driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView[3]").click()  #直接进入
time.sleep(2)
# driver.find_element_by_id("com.zhiyun.cama:id/iv_setting").click()   #右上角设置的三个点
# time.sleep(2)
# driver.find_element_by_id("com.zhiyun.cama:id/enter").click()	  #不连设备,直接进入
# time.sleep(2)

# driver.find_element_by_id("com.zhiyun.cama:id/rb_stabilizer").click()  # 云台
# time.sleep(2)
# driver.find_element_by_id("com.zhiyun.cama:id/sb_zoom_speed").click()		#变焦速度
# time.sleep(2)
driver.find_element_by_id("com.zhiyun.cama:id/iv_beauty").click()    #美颜
time.sleep(2)
# driver.tap([(1180, 540)])     #美颜进度条
# time.sleep(2)

# driver.find_element_by_id("com.zhiyun.cama:id/cb_action").click()    #拍照
# time.sleep(2)
"""heng =1016
for i in range(0,100):
    try:
        heng = heng-8.16
        driver.tap([(632,heng)])
    except:
        try:
            heng = heng - 9
            driver.tap([(632, heng)])
        except:
            heng = heng - 10
            driver.tap([(632, heng)])"""

# 获取屏幕的size
# size = driver.get_window_size()
# print(size)   #{'width': 1176, 'height': 2206}  首页的宽高
              # {'width': 2328, 'height': 1128}    拍照的宽高

# x = driver.get_window_size()["width"]
# y = driver.get_window_size()["height"]
# z = driver.swipe(x*0.5,y*0.5,x*0.5,y*0.5,duration=2000)
# s=driver.swipe(1 / 2 * x, 1 / 2 * y, 1 / 2 * x, 1 / 3 * y, 200)#向上滑动
# time.sleep(2)
# time.sleep(2)
# driver.swipe( x*0.15, y*0.3, x*0.15, y*0.8, 200)#向下滑动  x不变  y由小变大  美颜向下滑动
# driver.tap([(500, 700)]) #变焦进度条
# driver.swipe( x*0.15, y*0.8, x*0.15, y*0.3, 1000)#向上滑动  x不变  y由大变小  美颜向上滑动
# time.sleep(10)
# driver.swipe( x*0.8, y*0.4, x*0.1, y*0.4, 1000)#向左滑动  x不变  y由大变小  美颜向上滑动
# time.sleep(10)
# driver.swipe( x*0.01, y*0.15, x*0.9, y*0.15, 1000)#向右滑动  x不变  y由大变小  美颜向上滑动
# time.sleep(10)
from appium.webdriver import Remote
# driver.keyevent(4)        #括号里填入的是手机物理按键的数字代号  4为返回键

# driver.press_keycode()        #括号里填入的是键盘按键的数字代号
# driver.keyevent(4)
# driver.swipe( x*0.09, y*0.8, x*0.09, y*0.3, 200)#向下滑动  x不变  y由大变小  云台向上滑动  #x= 220  700       y = 982         x =220 700   y=400
# time.sleep(2)
# driver.tap([(1100,265),(1150,325)],500)
# time.sleep(2)
# driver.swipe( x*0.96, y*0.52, x*0.96, y*0.58, 200)#向下滑动  x不变  y由小变大  拍照-录像，但是会记录上次的结果
# driver.swipe( x*0.96, y*0.52, x*0.96, y*0.46, 200)#向上滑动  x不变  y由大变小
# time.sleep(2)
# driver.swipe( x*0.09, y*0.8, x*0.09, y*0.3, 200)#向下滑动  x不变  y由大变小  云台向上滑动  #x= 220  700       y = 982         x =220 700   y=400
# time.sleep(2)
# driver.tap([(1100,265),(1150,325)],500)
# time.sleep(2)
# driver.swipe( x*0.96, y*0.52, x*0.96, y*0.58, 200)#向下滑动  x不变  y由小变大  拍照-录像，但是会记录上次的结果
# driver.swipe( x*0.96, y*0.52, x*0.96, y*0.46, 200)#向上滑动  x不变  y由大变小
# time.sleep(2)


# driver.tap([(1180,540)])  #点击空白区域
# driver.tap([(632, 1022)])   #横坐标632  #纵坐标1022



#     driver.swipe(1 / 2 * x, 1 / 2 * y, 1 / 2 * x, 1 / 5 * y, 200)  # 向上滑动
#     time.sleep(2)
# driver.tap([(500,1000),(500,613)],500)
# time.sleep(2)
# 向左滑动。y轴保持不变，X轴：由大变小
"""def swipe_left(driver,star_x=0.9,stop_x=0.1,duration=2000):
    x1 = int(x*star_x)
    y1 = int(y*0.5)
    x2 = int(x*stop_x)
    y2 = int(y*0.5)
    driver.swipe(x1,y1,x2,y2,duration)
    return swipe_left
print(swipe_left(driver))"""
# 向右滑动。y轴保持不变，X轴：由小变大
"""def swipe_right(driver,star_x=0.1,stop_x=0.9,duration=2000):
    x1 = int(x*star_x)
    y1 = int(y*0.5)
    x2 = int(x*stop_x)
    y2 = int(y*0.5)
    driver.swipe(x1,y1,x2,y2,duration)"""

# 向上滑动。x轴保持不变，y轴：由大变小
"""def swipe_up(driver,star_y=0.9,stop_y=0.1,duration=2000):
    x1 = int(x*0.5)
    y1 = int(y*star_y)
    x2 = int(x*0.5)
    y2 = int(y*stop_y)
    driver.swipe(x1,y1,x2,y2,duration)
    return x1,y1,x2,y2
print(swipe_up(driver))"""
# 向下滑动。x轴保持不变，y轴：由小变大
"""def swipe_down(driver,star_y=0.1,stop_y=0.9,duration=2000):
    x1 = int(x*0.5)
    y1 = int(y*star_y)
    x2 = int(x*0.5)
    y2 = int(y*stop_y)
    driver.swipe(x1,y1,x2,y2,duration)"""


"""if __name__=='__main__':
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    x = driver.get_window_size()["width"]
    y = driver.get_window_size()["height"]
    swipe_left(driver)
    swipe_right(driver)
    swipe_up(driver)
    swipe_down(driver)"""

