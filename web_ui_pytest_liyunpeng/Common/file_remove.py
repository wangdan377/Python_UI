# -*- coding: UTF-8 -*-
# Administrator
# 2020/3/30 9:38

import shutil
import os

# 删除所有的文件和文件夹

def removeall(path):
    shutil.rmtree(path)
    os.mkdir(path)

#删除所有文件，有文件夹报错
# a = os.listdir(path)
# os.remove(path)
# for b in a:
#     c = path+r"\{}".format(b)
#     os.remove(c)
# # print(a)
# if os.path.exists(a):
#     os.remove(b)

if __name__ == '__main__':
    path = r"C:\Users\Administrator\Desktop\aa"
    removeall(path)