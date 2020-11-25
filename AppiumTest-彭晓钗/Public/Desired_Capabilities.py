#coding:utf-8

'''
appium启动真机的方法
'''


import yaml
from appium import webdriver


def desired_cap():
    #创建字典存放appium启动手机的desired capabilities参数
    desired_capabilities = dict()
    #获取存放在yaml文件中的desired capabilities参数
    file = open("../Config/desired_caps.yaml", 'r')
    data = yaml.load(file, Loader=yaml.FullLoader)
    file.close()
    #平台名称
    desired_capabilities["platformName"] = data["platformName"]
    #平台版本
    desired_capabilities["platformVersion"] = str(data["platformVersion"])
    #设备名称
    desired_capabilities["deviceName"] = data["deviceName"]
    #app包名
    desired_capabilities["appPackage"] = data["appPackage"]
    #app启动的activity
    desired_capabilities["appActivity"] = data["appActivity"]
    #启动应用后不重置app
    desired_capabilities["noReset"] = data["noReset"]
    desired_capabilities["newCommandTimeout"] = data["newCommandTimeout"]

    #启动真机
    driver = webdriver.Remote("http://" + str(data["ip"]) + ":" + str(data["port"]) + "/wd/hub", desired_capabilities)
    driver.implicitly_wait(8)
    # driver.start_activity(data["appPackage"], data["appActivity"])
    # time.sleep(5)
    # driver.terminate_app(data["appPackage"])
    return driver


if __name__ == '__main__':
    desired_cap()



