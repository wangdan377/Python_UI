# -*- coding: UTF-8 -*-
# Administrator
# 2020/4/21 17:16

#上传文件的地址
from Common.constant import UPLOAD_DIR
import os

#上传文件路径
filepath0 = os.path.join(UPLOAD_DIR,'123.jpg')
filepath_docx = os.path.join(UPLOAD_DIR,'12.docx')


#上传图片文件
filepath_success = [{"filepath_1":filepath0}]


#不上传文件进行下一步
upload_error = [{"file":"","check":"请上传合同再进行下一步"}]