#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
import os,time
import HTMLTestRunnerCN3_pie_chart_screen
Suit = unittest.defaultTestLoader.discover(
    # start_dir="D:\py\ZY_Cami\\test_case",#要执行的目录
    start_dir="../TestCase02",
    pattern="test_*.py"#目录下test_开头的文件
)
if __name__ == '__main__':
    soundbox_device = 'XYBK01011204300001'
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    ##将当前时间加入到报告文件名称中，定义测试报告存放路径
    # filename = '../Report/' + now + 'result.html'  # 第一种方法,相对路径下
    filename = '../report/' + os.sep + now + 'result.html'
    # filename = os.getcwd() + os.sep + 'report' + now + 'result.html'
    # filename = '../report' + os.sep + 'report' + now + 'result.html'
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
    # 定义测试报告
    runner.run(Suit)
    fp.close()



#一个test文件里面有多条用例
"""def Suit():
    case_path= '../TestCase_prime'
    suit=unittest.TestSuite()
    '''
    用discover方法找出目录下要执行的测试 用例脚本
    .discover方法里面有3个参数：
    case_dir:测试用例的所在目录
    pattern:这个是匹配脚本名称的规则，例如：test*.py意思是匹配所有以test开头的脚本
    top_level_dir:这个是顶级目录的名称，一般默认等于None就可以了
    '''
    # discover=unittest.defaultTestLoader.discover(case_path,pattern='test*.py',top_level_dir=None)
    discover = unittest.defaultTestLoader.discover(
        # start_dir="D:\py\ZY_Cami\\test_case",#要执行的目录
        start_dir="../TestCase02",
        pattern="test_*.py"  # 目录下test_开头的文件
    )
    for casefile in discover:
        for case in casefile:
            suit.addTest(case)
            #返回所有的测试用例
    return suit

if __name__ == '__main__':
    soundbox_device = 'XYBK01011204300001'
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    #定义测试报告的路径
    filename = '../report/' + now + 'result.html'
    #实例化测试用例
    suit=Suit()
    #定义输出报告
    fp = open(filename, 'wb')
    runner = HTMLTestRunnerCN3_pie_chart_screen.HTMLTestRunner(stream=fp, title='测试报告', tester='王丹',
                                                               device=(soundbox_device),
                                                               description='用例执行情况:')
    # 定义测试报告
    runner.run(suit)
    fp.close()
"""
