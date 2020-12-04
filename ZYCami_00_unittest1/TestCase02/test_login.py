
# import pytest

from datetime import datetime
from appium import webdriver
import time,unittest,os,sys,HTMLTestRunner
import HTMLTestRunner
import HTMLTestRunnerCN
import HTMLTestRunnerCN3
import HTMLTestRunner2
from selenium.webdriver.support.ui import WebDriverWait

import HTMLTestRunnerCN3_pie_chart_screen

# class LoginTest(object):
#     pass

#未登录状态下去登录
class LoginTest(unittest.TestCase):
    '''未登录，去登录，我的页面退出登录'''
    def setUp(self):
        print('start test')
        """desired_caps = {}
        desired_caps['platformName'] = 'Android'  # Android系统 or IOS系统
        desired_caps['deviceName'] = '7HX0219918017044'  # 真机或模块器名
        desired_caps['platformVersion'] = '10'  # Android系统版本
        desired_caps['appPackage'] = 'com.zhiyun.cama'  # APP包名
        desired_caps['appActivity'] = '.splash.SplashActivity'  # APP启动Activity
        desired_caps['noReset'] = True  # 每次打开APP不开启重置，否则每次都进入四个欢迎页
        desired_caps['resetKeyboard'] = True  # 隐藏键盘        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 启动APP
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)"""  # 启动APP
        desired_caps ={'platformName':'Android',#手机系统
                'deviceName':'7HX0219918017044',
                'noReset':True,#防止每次启动时软件初始化
                'appPackage':'com.zhiyun.cama',
                'appActivity':'.splash.SplashActivity',
                'unicodeKeyboard':True,#使用unicode编码方式发送字符串
                'resetKeyboard':True}#将键盘隐藏起来
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    def tearDown(self):
        print('end test')
        self.driver.quit()
    def test_login(self):
        #未登录的状态下去登录
        driver = self.driver
        # 进入首页后点击我的按钮
        time.sleep(5)
        driver.find_element_by_xpath("//android.widget.FrameLayout[@content-desc=\"Me\"]/android.widget.ImageView").click() #我的按钮
        time.sleep(3)
        # x = driver.get_window_size()["width"]
        # y = driver.get_window_size()["height"]
        # driver.swipe(x * 0.3, y * 0.15, x * 0.8, y * 0.15, 1000)  # 向下滑动  x不变  y由大变小  美颜向上滑动

        driver.find_element_by_id('tv_login').click()     #点击登录按钮
        time.sleep(5)
        # 跳转到登录界面清空账号输入框并输入用户名
        # driver.find_element_by_id('LoginUserED').clear()  # APP有保存用户名功能
        driver.find_element_by_id('et_name').set_value('17195453626')
        # 清空密码输入框并输入密码
        # driver.find_element_by_id('LoginPwdED').clear()
        driver.find_element_by_id('et_pass').set_value('00000000')
        # 点击登录按钮
        driver.find_element_by_id('tv_commit').click()    #登录成功后直接进入我的页面
        driver.save_screenshot('../screen/' + sys._getframe().f_code.co_name + '.png')   #第一种方式--->正确的,实时截图,在报告中体现出来

        # driver.save_screenshot('../screen/test_login03.png')   #第二种方式--->正确的,可以用来保存截图
        # driver.get_screenshot_as_file('../screen/test_login.png')  #第三种方式,保存到指定文件路径下--->正确的,实时截图,在报告中体现出来
        # driver.save_screenshot('login.png')   #第四种方式,登录页面截图,保存当前目录下(直接保存到case下面了)
        time.sleep(1)
        # 获取登录后的昵称
        # name = driver.find_element_by_id('tv_name').text
        name = driver.find_element_by_id("tv_name").text

        # 添加断言，若昵称不正确，则打印错误信息
        try:
            assert '黄1' in name
            print('loginUser is right')
        except AssertionError as e:
            print('loginUser is Error')
        # 点击右上角设置，进入设置页面
        """driver.find_element_by_id('iv_set').click()
        # 点击退出按钮
        driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TextView").click()
        time.sleep(2)
        driver.tap([(108, 119), (587, 1359)], 500)  #点弹出框去看看
        driver.back()   #点击返回
        time.sleep(2)
        # 弹出退出提示弹框，点击确定
        # driver.find_element_by_id("com.zhiyun.cama:id/positive").click()
        # time.sleep(5)"""
#测试套件
"""def Suit():
    suite = unittest.TestSuite()
    # 构造测试集
    suite.addTest(LoginTest("test_login"))
    return suite"""
if __name__ == '__main__':
    # unittest.main()       #不需要打印报告就用这句
    # 构造测试套件
    # suite = unittest.TestSuite()
    # suite.addTest(LoginTest("test_login"))


# HTMLTestRunner,无tester device标题,无饼图
    """suite = unittest.TestSuite()
    suite.addTest(LoginTest("test_login"))

    # 按照一定格式获取当前时间
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    ##将当前时间加入到报告文件名称中，定义测试报告存放路径
    filename = 'D:\ZY_Cami03\\report\\report' + now + 'result.html'
    # 定义测试报告
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况:')
    runner.run(suite)
    # 关闭报告
    fp.close()"""
# HTMLTestRunnerCN,有title,tester标题,无饼图
    """suite = unittest.TestSuite()
    suite.addTest(LoginTest("test_login"))
    soundbox_device = 'XYBK01011204300001'
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    ##将当前时间加入到报告文件名称中，定义测试报告存放路径
    # filename = os.getcwd() + os.sep + 'report'+ os.sep + 'report' + now + 'result.html'
    filename = 'D:\py\ZY_Cami\\report\\report' + now + 'result.html'
    # 定义测试报告
    fp = open(filename, 'wb')
    runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title='测试报告', tester='王丹', device=(soundbox_device),
                                             description='用例执行情况:')
    runner.run(suite)
    fp.close()"""

# HTMLTestRunner2,无tester device标题,有饼图
    """suite = unittest.TestSuite()
    suite.addTest(LoginTest("test_login"))
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    ##将当前时间加入到报告文件名称中，定义测试报告存放路径
    # filename = os.getcwd() + os.sep + 'report'+ os.sep + 'report' + now + 'result.html'  #第一种方法
    filename = 'D:\py\ZY_Cami\\report\\report' + now + 'result.html'    #第二种方法
    # 定义测试报告
    fp = open(filename, 'wb')
    runner = HTMLTestRunner2.HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况:')
    # runner.run(suit, rerun=0, save_last_run=False)
    runner.run(suite)
    fp.close()"""

# HTMLTestRunnerCN3,有title,tester标题+饼图
    """suite = unittest.TestSuite()
    suite.addTest(LoginTest("test_login"))
    suit = unittest.defaultTestLoader.discover(
    start_dir="D:\py\ZY_Cami\\test_case",#要执行的目录
    pattern="test_*.py"#目录下test_开头的文件
    soundbox_device = 'XYBK01011204300001'
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    ##将当前时间加入到报告文件名称中，定义测试报告存放路径
    filename = 'D:\py\ZY_Cami\\report\\report' + now + 'result.html'
    # 定义测试报告
    fp = open(filename, 'wb')
    runner = HTMLTestRunnerCN3.HTMLTestRunner(stream=fp, title='测试报告', tester='王丹', device=(soundbox_device), description='用例执行情况:')
    # runner.run(suit, rerun=0, save_last_run=False)
    runner.run(suite)
    fp.close()"""
# 这个是HTMLTestRunnerCN3_pie_chart_screen2,有title,tester标题+饼图+美观+截图
#    --------------->在test_case方法目录下面-----------
    #有问题的报告
    """soundbox_device = 'XYBK01011204300001'
    with open('my_report.html', 'wb') as fp:
        runner = HTMLTestRunnerCN3_pie_chart_screen.HTMLTestRunner(
            stream=fp,
            title='zy自动化测试报告',
            description='详情',
            tester='啊哈',
            device=(soundbox_device),
            verbosity=2  # verbosity参数可以控制执行结果的输出，0是简单报告、1是一般报告、2是详细报告
        )
        # runner = unittest.TextTestRunner()
        runner.run(Suit())
        fp.close()"""


    #可用的报告
    """suite = unittest.TestSuite()
    suite.addTest(LoginTest("test_login"))
    #可用
    soundbox_device = 'XYBK01011204300001'
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    ##将当前时间加入到报告文件名称中，定义测试报告存放路径
    filename = '../report/' + now + 'result.html'    #第一种方法,相对路径下
    '''# filename = '../report/report' + now + 'result.html'  # 第二种方法,相对路径下+report报告名字
    # filename = '../report'+ os.sep+ 'report' + now + 'result.html'    #第二种方法,相对路径下,上级目录../report文件夹下,分隔符下文件名  os.sep+ 'report'
    # filename = os.getcwd() + os.sep+ 'report' + now + 'result.html'   #相对路径下,该路径下的,所以就到test_case下面了
    # filename = os.path.dirname(os.path.dirname(__file__))+ os.sep + 'report' + now + 'result.html'  #相对路径下,该路径下的,所以就到test_case下面了
    # filename = 'D:\py\ZY_Cami\\report\\report' + now + 'result.html'   #绝对路径下
    # filename = '../' + now + 'result.html'   #../是上级目录,还是在上级目录下
    # filename = '../' + os.sep + 'report' + now + 'result.html'   #还是在上级目录下
    # filename = '../report' + now + 'result.html'  #还是在上级目录下'''
    fp = open(filename, 'wb')
    runner = HTMLTestRunnerCN3_pie_chart_screen.HTMLTestRunner(stream=fp, title='测试报告', tester='王丹', device=(soundbox_device),
                                              description='用例执行情况:')
    # runner.run(suite)
    runner.run(suite)
    fp.close()
"""




