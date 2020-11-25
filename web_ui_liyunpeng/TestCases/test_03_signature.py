# -*- coding: UTF-8 -*-
# Administrator
# 2020/4/30 15:31

import pytest
from PageObjects.upload_page import UploadPage as UP
from PageObjects.add_signer_page import AddSingerPage as AS
from PageObjects.signature_page import SignaturePage as SP
from PageObjects.contract_manage_page import ContractManagePage as CM
from TestDatas import upload_datas as UD


@pytest.mark.usefixtures("login_web")
class Test_Signature:
    @pytest.mark.demo
    @pytest.mark.parametrize("filepath",UD.filepath_success)
    def test_Single_signture_success(self,filepath,login_web):#单页签
        #进入上传合同页面上传合同
        login_web[1].uploadFile(filepath["filepath_1"])
        #在添加签署页面点击下一步
        AS(login_web[0]).click_signer_next()
        #在文件签署页面正常盖章签署
        SP(login_web[0]).sign_success()
        #断言是否签署成功
        # assert CM(login_web[0]).is_Sign_success()
        assert CM(login_web[0]).Sign_success_Tips() =="签署成功"


    def test_Multi_signture_success(self):#多页签
        pass
