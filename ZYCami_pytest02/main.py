# main.py
import pytest
import os

if __name__ == '__main__':
    # 生成allure Html 报告命令
    # allure generate ./report/result -o ./report/html  --clean

    pytest.main(['--clean-alluredir','--alluredir', './report/result'])   #存放目录
    os.system('allure generate ./report/result -o ./report/html --clean')   #生成测试报告
