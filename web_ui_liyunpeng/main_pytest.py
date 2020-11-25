import pytest
from Common.constant import allure_DOR
from Common.file_remove import removeall
import os
# if __name__ == '__main__':
#     pytest.main(["-s","-v","-m","login"])



if __name__ == '__main__':
    # 运行之前先删除之前的allure报告
    removeall(allure_DOR)

    pytest.main(["-s","-v","--lf","-m","demo","--html=Outputs/reports/PCUI_test.html","--alluredir=Outputs/allure"])

#生成allure报告linux命令
    os.system("allure generate Outputs/allure -o Outputs/allure_reports --clean")

#注册标签名：pytest.ini
#给用例打标签：@pytest.mark.注册的标签名
#根据标签名过滤要运行的用例：-m 标签名
#-v:可以输出用例更加详细的执行信息，比如用例所在的文件及用例名称等
#-s:输入我们用例中的调式信息，比如print的打印信息等
#--ff:运行所有的测试用例，上次运行失败的用例优先执行。
#--lf:运行上次运行失败的测试用例，如果没有失败用例则运行全部测试用例
# --html=Outputs/reports/test00.html(测试报告相对路径)
#--alluredir=Outputs/allure(allure相对路径)