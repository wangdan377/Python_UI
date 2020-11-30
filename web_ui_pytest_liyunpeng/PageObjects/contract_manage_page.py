# -*- coding: UTF-8 -*-
# Administrator
# 2020/4/30 14:26

from Common.basepage import BasePage
from PageLocators.contract_manage_locator import ContractManageLoactor as CM


class ContractManagePage(BasePage):
    """合同管理页面"""
    #判断签署成功之后进入该页面元素定位
    def is_Sign_success(self):
        try:
            self.wait_ele_exists(CM.sign_success,'合同管理界面_文件签署成功弹框元素定位')
            return True
        except:
            return False
    def Sign_success_Tips(self):
        return self.get_text(CM.sign_success,'合同管理界面_文件签署成功弹框')