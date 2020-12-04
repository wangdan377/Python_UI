#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from Public.Function import BaseFun
import os,time
class Prime_Page(BaseFun):

    # "//*[@text='扫一扫']"
    # "//*[text()='立即续费']"
    # // android.view.View[ @ text = '立即续费']
    # find_element_by_xpath("//*[@text='立即续费']")
    # self.driver.find_element_by_xpath("//*[@text='立即续费']").click()  可用
    # self.driver.find_element_by_android_uiautomator('new UiSelector().text("立即续费")').click()  可用
    File_opens01 = (By.XPATH, "//*[@text='立即开通']")
    def click_File_opens01(self):
        self.find_element(self.File_opens01).click()

    File_opens02 = (By.XPATH, "//*[@text='立即续费']")
    def click_File_opens02(self):
        self.find_element(self.File_opens02).click()

    File_meal03 = (By.XPATH, "//*[@text='一个月']")
    def click_File_meal03(self):
        self.find_element(self.File_meal03).click()

    File_meal02 = (By.XPATH, "//*[@text='连续包半年']")
    def click_File_meal02(self):
        self.find_element(self.File_meal02).click()

    File_meal01 = (By.XPATH, "//*[@text='连续包季']")
    def click_File_meal01(self):
        self.find_element(self.File_meal01).click()

    File_Service_Agreement = (By.XPATH, "//*[@text='ZHIYUN Prime服务协议']")
    def click_File_Service_Agreement(self):
        self.find_element(self.File_Service_Agreement).click()

    File_Privacy_Policy = (By.XPATH, "//*[@text='隐私协议']")
    def click_File_Privacy_Policy(self):
        self.find_element(self.File_Privacy_Policy).click()

    File_equip_buy = (By.XPATH, "//*[@text='购买']")
    def click_File_equip_buy(self):
        self.find_element(self.File_equip_buy).click()

    File_Redemption_code = (By.XPATH, "//*[@text='兑换码']")
    def click_File_Redemption_code(self):
        self.find_element(self.File_Redemption_code).click()



    #个人主页，prime文字，进入购买页面
    File_prime01 = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.TextView[1]')

    # 点击prime,进入购买页面
    def click_File_prime01(self):
        self.find_element(self.File_prime01).click()

    # 查看权益和弹框领取(包含首页)
    File_interests = (By.ID, 'com.zhiyun.cama:id/tv_get')

    # 新的权益卡待领取
    File_receive_interests = (By.XPATH,
                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.widget.Button')

    # 立即领取（我的页面里面的领取)
    File_me_receive01 = (By.XPATH,
                         '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[6]/android.widget.Button')
    # File_me_receive = (By.XPATH,'/android/ssss') ? (By.XPATH,'/android/ssss') : (By.XPATH,'/ios/ssss')

    # 确定不领取弹框
    File_positive = (By.ID, 'com.zhiyun.cama:id/positive')

    # 查看权益和弹框领取
    def click_File_interests(self):
        self.find_element(self.File_interests).click()

    # 新的权益卡待领取
    def click_File_receive_interests(self):
        self.find_element(self.File_receive_interests).click()

    # 立即领取（我的页面里面的领取)
    def click_File_me_receive(self):
        self.find_element(self.File_me_receive01).click()

    # 确定不领取弹框（首页关闭后，有一个确定按钮）
    def click_File_positive(self):
        self.find_element(self.File_positive).click()
    """#享有更多特权
    File_prime_more_prerogative = (By.ID,'com.zhiyun.cama:id/tv_prime_more_prerogative')
    
    #年
    File_meal_010 = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View/android.view.View')
    File_meal_011 = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View/android.view.View[2]')
    
    #半年
    File_meal_020 = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View')
    File_meal_021 = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View')


    #连续包月
    File_meal_030 = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[3]/android.view.View/android.view.View')
    File_meal_031 = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View/android.view.View')

    #一个月
    File_meal_04 = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[4]/android.view.View/android.view.View')

    #立即开通
    File_open_01 = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.widget.Button')
    File_open_02 = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.widget.Button')
    # self.driver.find_element_by_android_uiautomator('new UiSelector().text("立即开通")').click()
    #隐私政策
    File_Privacy_Policy = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[3]/android.view.View[2]')
    #服务协议
    File_Service_Agreement = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[3]/android.view.View[2]')
    #政策返回按钮
    File_Service_Back = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View')
    #个人页面购买第一个设备
    File_buy_equipment01 = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[6]/android.view.View[1]/android.view.View[1]/android.view.View/android.view.View[2]/android.widget.Button')
    # 个人页面购买第二个设备
    File_buy_equipment02 = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[6]/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View[2]/android.widget.Button')

    #开通返回按钮
    File_open_back = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[1]/android.view.View')
    #从有效期进入开通记录页面
    File_open_record = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[2]')
    # 立即续费
    File_Renew_01 = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[3]')
    File_Renew_02 = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[3]')

    

    

    #点击享有更多特权
    def click_File_prime_more_prerogative(self):
        self.find_element(*self.File_prime_more_prerogative).click()
        # self.find_element(self.File_prime_more_prerogative,self.File_prime_more_prerogative,self.File_prime_more_prerogative,self.File_prime_more_prerogative).click()

    # 年1
    def click_File_meal_01(self):
        self.find_element(self.File_meal_010).click()

    # 半年2
    def click_File_meal_02(self):
        self.find_element(self.File_meal_021).click()

    # 连续包月3
    def click_File_meal_03(self):
        self.find_element(self.File_meal_031).click()

    # 一个月4
    def click_File_meal_04(self):
        self.find_element(self.File_meal_04).click()

    # 立即开通
    def click_File_open01(self):
        self.find_element(self.File_open_02).click()
    # 立即续费
    def click_File_Renew(self):
        self.find_element(self.File_Renew_02).click()

    # 隐私政策
    def click_File_Privacy_Policy(self):
        self.find_element(self.File_Privacy_Policy).click()
    # 服务协议
    def click_File_Service_Agreement(self):
        self.find_element(self.File_Service_Agreement).click()
    # 政策返回按钮
    def click_File_Service_Back(self):
        self.find_element(self.File_Service_Back).click()
    # 个人页面购买第一个设备
    def click_File_buy_equipment01(self):
        self.find_element(self.File_buy_equipment01).click()

    # 个人页面购买第二个设备
    def click_File_buy_equipment02(self):
        self.find_element(self.File_buy_equipment02).click()
    # 开通返回按钮
    def click_File_open_back(self):
        self.find_element(self.File_open_back).click()
    # 从有效期进入开通记录页面
    def click_File_open_record(self):
        self.find_element(self.File_open_record).click()
    """





