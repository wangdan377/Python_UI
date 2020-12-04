#!/usr/bin/python
# -*- coding: utf-8 -*-
from Public.Function import *
from Public import Caplictily
from PO.Camera_Element import *
from common.loged import *
from common.loged import *
import unittest
import time,os,sys
import warnings
import HTMLTestRunnerCN3_pie_chart_screen
log = Logger('D:\ZYCami_00\logs\\error.log', level='debug')

class Camera_test(unittest.TestCase):

    #初始化，使用装饰器，这样在用例执行前只初始化一次
    @classmethod
    def setUpClass(cls):
        """warnings.simplefilter("ignore", ResourceWarning)
        cls.driver = appium_desired()
        time.sleep(10)
        # cls.driver.start_activity(appPackage,appActivity)     #另外一种启动方式
        #实例化类
        cls.fun = BaseFun(cls.driver)"""
        driver = Caplictily.Driver_Config()
        cls.driver = driver.get_driver()
        cls.fun = BaseFun(cls.driver)
    #关闭驱动
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_camera(self):
        """try:
            self.fun.click(File_name)
        except AttributeError:
            log.logger.error('访问不到该对象属性')
            self.fun.saveScreenshot('camera01')
        except NoSuchElementException as a:  # 元素不存在，则调用捕获异常处理
            log.logger.error('元素不存在')
            self.fun.saveScreenshot('camera02')
        except NoAlertPresentException as b:  # 捕获意外的异常
            log.logger.warning('警告')
            self.fun.saveScreenshot('camera03')
        except Exception as result:
            log.logger.critical('严重')
            self.fun.saveScreenshot('camera04')
        else:
            pass  # 没有错的情况下执行
        finally:
            pass  # 有没有错，都会执行"""
        self.fun.clickButton(File_iv_camera1)
        # self.fun.click(File_help)
        # self.fun.click(File_enter)
        """# self.driver.get_screenshot_as_file('../screen/test_camera.png')   #直接存入报告
        self.fun.saveScreenshot('camera')
        self.fun.saveScreenshot('help')

        self.fun.click(File_enter)"""

if __name__ == '__main__':
    unittest.main()
    """suite = unittest.TestSuite()
    suite.addTest(Camera_test("test_camera"))
    soundbox_device = 'XYBK01011204300001'
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    ##将当前时间加入到报告文件名称中，定义测试报告存放路径
    filename = '../report/' + now + 'result.html'  # 第一种方法,相对路径下
    '''# filename = '../report/report' + now + 'result.html'  # 第二种方法,相对路径下+report报告名字
    # filename = '../report'+ os.sep+ 'report' + now + 'result.html'    #第二种方法,相对路径下,上级目录../report文件夹下,分隔符下文件名  os.sep+ 'report'
    # filename = os.getcwd() + os.sep+ 'report' + now + 'result.html'   #相对路径下,该路径下的,所以就到test_case下面了
    # filename = os.path.dirname(os.path.dirname(__file__))+ os.sep + 'report' + now + 'result.html'  #相对路径下,该路径下的,所以就到test_case下面了
    # filename = 'D:\py\ZY_Cami\\report\\report' + now + 'result.html'   #绝对路径下
    # filename = '../' + now + 'result.html'   #../是上级目录,还是在上级目录下
    # filename = '../' + os.sep + 'report' + now + 'result.html'   #还是在上级目录下
    # filename = '../report' + now + 'result.html'  #还是在上级目录下'''
    fp = open(filename, 'wb')
    runner = HTMLTestRunnerCN3_pie_chart_screen.HTMLTestRunner(stream=fp, title='测试报告', tester='王丹',
                                                               device=(soundbox_device),
                                                               description='用例执行情况:')
    runner.run(suite)
    # runner.run(Suit())
    fp.close()"""