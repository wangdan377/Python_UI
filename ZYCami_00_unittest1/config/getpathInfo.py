import os
#获取项目的绝对路径
def get_Path():
    # path = os.path.split(os.path.realpath(__file__))[0]


    path2 = os.path.dirname(os.path.dirname(__file__))  #
    # print(path2)  # 获取当前运行脚本的绝对路径（去掉最后一个路径）


    return path2

if __name__ == '__main__':# 执行该文件，测试下是否OK
    print('测试路径是否OK,路径为：', get_Path())
