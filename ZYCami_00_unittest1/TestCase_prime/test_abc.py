#test_Pytest.py文件
#coding=utf-8

import pytest
import os

class Test_Pytest():

        def test_one(self):
                print("test_one方法执行" )
                assert 1==1

        def test_two(self):
                print("test_two方法执行" )
                assert "s" in "love"

        def test_three(self):
                print("test_three方法执行" )
                assert 3-2==1

# if __name__=="__main__":
#     pytest.main(['-s','test_abc.py'])

if __name__=="__main__":
    pytest.main(['-s','-q','--alluredir','report/result','test_abc.py'])

# if __name__=="__main__":
#     pytest.main(['-s','-q','--alluredir','report/result','test_abc.py'])
#     os.system("C:/python35/Lib/site-packages/allure-2.8.0/bin/allure.bat "
#               "generate "
#               "D:\ZYCami_00\\report "
#               "-o "
#               "D:\ZYCami_00\\report/html")
