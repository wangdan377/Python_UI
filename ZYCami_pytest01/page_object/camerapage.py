
from page.webpage import WebPage
from common.readelement import read_yaml
import allure
from tools.times import sleep

camera = read_yaml('Camera')['相机']
settings = read_yaml('Camera')['设置']
navigation = read_yaml('Camera')['导航栏']
class CameraPage(WebPage):
    """相机类"""
    @allure.step("相机按钮")
    def cameras(self):
        self.is_click((camera[0]['type'],camera[0]['value']))
        sleep(3)

    @allure.step("帮助")
    def help(self):
        self.is_click((camera[1]['type'],camera[1]['value']))

    @allure.step("直接进入")
    def enter(self):
        """直接进入"""
        self.is_click((camera[2]['type'],camera[2]['value']))

    @allure.step("连接设备")
    def connect(self):
        """连接设备"""
        self.is_click((camera[3]['type'],camera[3]['value']))
        sleep(3)

    @allure.step("返回")
    def home(self):
        """返回"""
        self.is_click((camera[4]['type'],camera[4]['value']))
    @allure.step("蓝牙")
    def bluetooth(self):
        """蓝牙"""
        self.is_click((camera[5]['type'],camera[5]['value']))

    def Universal(self):
        """通用"""
        self.is_click((settings[3]['type'], settings[3]['value']))

    def SMART(self):
        """SMART"""
        self.swipe_up()
        self.is_click((navigation[0]['type'], navigation[0]['value']))

    def AILive(self):
        """AILive"""
        self.swipe_up()
        self.is_click((navigation[1]['type'], navigation[1]['value']))

    def actions(self):
        """拍照"""
        self.swipe_up()
        self.is_click((settings[2]['type'], settings[2]['value']))

    def Video(self):
        """录像"""

        self.is_click((settings[3]['type'], settings[3]['value']))

    def panoramic(self):
        """全景"""
        self.is_click((settings[4]['type'], settings[4]['value']))

    def Time_lapse(self):
        """延时摄影"""
        self.is_click((settings[5]['type'], settings[5]['value']))

    def Motion_delay(self):
        """运动延时"""
        self.is_click((settings[6]['type'], settings[6]['value']))

    @allure.step("前置条件")
    def is_click_(self, locator):
        if locator['name'] == '美颜按钮':
            self.is_click((locator['type'], locator['value']))

        elif locator['name'] == '取消美颜':
            self.swipe_up()
            self.is_click((locator['type'],locator['value']))

        elif locator['name'] == '自动美颜':
            self.is_click((locator['type'],locator['value']))

        elif locator['name'] == '瘦脸':
            self.is_click((locator['type'],locator['value']))
            self.roll_beautify(1164)

        elif locator['name'] == '磨皮':
            self.is_click((locator['type'],locator['value']))
            self.roll_beautify(1164)

        elif locator['name'] == '美白':
            self.is_click((locator['type'],locator['value']))
            self.roll_beautify(1164)

        elif locator['name'] == '眼睛放大':
            self.swipe_down()
            self.is_click((locator['type'],locator['value']))
            self.roll_beautify(1160)

        elif locator['name'] == '光照':
            self.swipe_down()
            self.is_click((locator['type'],locator['value']))
            self.roll_beautify(1160)

        elif locator['name'] == '红润':
            self.swipe_down()
            self.is_click((locator['type'],locator['value']))
            self.roll_beautify(1158)        #滚动条
            self.blank_01()     #空白区域
            sleep(3)
        elif locator['name'] == 'action':
            self.is_click((locator['type'],locator['value']))
            self.swip_return()

        elif locator['name'] == '倒计时':
           self.is_click((locator['type'], locator['value']))

        elif locator['name'] == 'off':
           self.is_click((locator['type'], locator['value']))

        elif locator['name'] == '3s':
           self.is_click((locator['type'], locator['value']))

        elif locator['name'] == '5s':
           self.is_click((locator['type'], locator['value']))

        elif locator['name'] == '7s':
           self.is_click((locator['type'], locator['value']))

        elif locator['name'] == '设置':
           self.is_click((locator['type'], locator['value']))

        elif locator['name'] == '视频':
           self.is_click((locator['type'], locator['value']))

        elif locator['name'] == '云台':
           self.is_click((locator['type'], locator['value']))

        elif locator['name'] == '通用':
           self.is_click((locator['type'], locator['value']))

        elif locator['name'] == '闪光灯':
           self.is_click((locator['type'], locator['value']))


        elif locator['name'] == '关闭':
           self.is_click((locator['type'], locator['value']))

        elif locator['name'] == '常亮':
           self.is_click((locator['type'], locator['value']))

        elif locator['name'] == '网络显示':
           self.is_click((locator['type'], locator['value']))

        elif locator['name'] == '关闭':
           self.is_click((locator['type'], locator['value']))

        elif locator['name'] == '方格':
           self.is_click((locator['type'], locator['value']))

        elif locator['name'] == '方格+对角线':
           self.is_click((locator['type'], locator['value']))

        elif locator['name'] == '白平衡':
           self.is_click((locator['type'], locator['value']))

        elif locator['name'] == '自动':
           self.is_click((locator['type'], locator['value']))

        elif locator['name'] == '晴天':
           self.is_click((locator['type'], locator['value']))

        elif locator['name'] == '阴天':
           self.is_click((locator['type'], locator['value']))

        elif locator['name'] == '白炽灯':
           self.is_click((locator['type'], locator['value']))
        elif locator['name'] == '荧光灯':
           self.is_click((locator['type'], locator['value']))

        elif locator['name'] == '返回':
           self.is_click((locator['type'], locator['value']))

        elif locator['name'] == '手势控制':
            self.is_click((locator['type'], locator['value']))

        elif locator['name'] == '跟随+拍摄':
            self.is_click((locator['type'], locator['value']))

        elif locator['name'] == '仅拍摄':
            self.is_click((locator['type'], locator['value']))

        elif locator['name'] == '手势控制返回键':
            self.is_click((locator['type'], locator['value']))

        elif locator['name'] == '问号':
            self.is_click((locator['type'], locator['value']))

        elif locator['name'] == '去水印':

            self.is_click((locator['type'], locator['value']))

if __name__ == '__main__':
    camera = read_yaml('Camera')['手势控制'][1]
    print(camera)
    # print((camera['type'],camera['value']))
    # print((camera[11]['type'],camera[11]['value']))
    # print((camera[18]['type'], camera[18]['value']))
    # locator1 = [(read_yaml('Camera')['相机'][12]),(read_yaml('Camera')['相机'][14]),(read_yaml('Camera')['相机'][18]),(read_yaml('Camera')['相机'][19]),(read_yaml('Camera')['相机'][20])]
    # for i in locator1:
    #     print((i['type'], i['value']))
