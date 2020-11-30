# -*- coding: UTF-8 -*-
# Administrator
# 2020/4/27 16:50

import pytest
from PageObjects.add_signer_page import AddSingerPage as AP
from PageObjects.signature_page import SignaturePage as SP
from TestDatas import upload_datas as UD
from TestDatas import add_signer_datas as ASD
import logging
import time

@pytest.mark.usefixtures("login_web")
class Test_AddSigner:
    """添加签署人"""
    # @pytest.mark.demo
    @pytest.mark.parametrize("filepath",UD.filepath_success)
    def test_access_signature(self,filepath,login_web):
        logging.info("*****************从添加签署人页面进入合同签署页面成功*********************")
        #上合同后成功进入添加签署人页面
        login_web[1].uploadFile(filepath["filepath_1"])
        # time.sleep(3)
        #点击下一步
        AP(login_web[0]).click_signer_next()
        # time.sleep(3)
        #断言正常进入下一步
        assert SP(login_web[0]).isExists_signature()

    @pytest.mark.demo
    @pytest.mark.parametrize("mobile",ASD.add_users)
    @pytest.mark.parametrize("filepath",UD.filepath_success)
    def test_Specify_user(self,mobile,filepath,login_web):
        logging.info("*****************添加签署人付款方式为指定付*********************")
        # 上合同后成功进入添加签署人页面
        login_web[1].uploadFile(filepath["filepath_1"])
        time.sleep(3)
        #新增签署人并选择指定付用户
        AP(login_web[0]).add_signer(mobile["mobile"])
        time.sleep(3)
        #断言
        assert SP(login_web[0]).isExists_signature()

