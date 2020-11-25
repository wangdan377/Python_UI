# -*- coding: UTF-8 -*-
# Administrator
# 2020/4/20 17:29

import pytest
import logging
from PageObjects.upload_page import UploadPage as UP
from PageObjects.add_signer_page import AddSingerPage as AP
import time
from TestDatas import upload_datas as UD


# @pytest.mark.test
@pytest.mark.usefixtures("login_web")
class Test_Upload:
    """上传合同和附件"""

    # @pytest.mark.demo
    def test_access_upload(self, login_web):
        logging.info("*****************点击发起签约按钮，进入上传合同页面成功*********************")

        # 登录成功并点击发起签约按钮
        # login_web[1].click_ele()
        time.sleep(3)
        # 断言正常进入上传合同页面
        assert UP(login_web[0]).isExist_upload_ele()

    # @pytest.mark.demo
    @pytest.mark.parametrize("filepath", UD.filepath_success)
    def test_upload_access(self, filepath, login_web):
        logging.info("*****************上传合同并点击下一步*********************")
        # 登录成功并点击发起签约按钮
        # login_web[1].click_ele()
        # time.sleep(3)
        # 在上传合同页面上传合同，上传附件并点击下一步
        login_web[1].uploadFile(filepath["filepath_1"])
        time.sleep(3)
        assert AP(login_web[0]).isExist_addSigner_ele()

    # @pytest.mark.demo
    @pytest.mark.parametrize("file", UD.upload_error)
    def test_upload_error(self, file, login_web):
        logging.info("*****************不上传合同并点击下一步*********************")
        assert login_web[1].get_error() == file['check']


if __name__ == '__main__':
    pytest.main()
