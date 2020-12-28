from page.webpage import WebPage
from common.readelement import read_yaml
import allure
from tools.times import sleep
from tools.logger import log

camera = read_yaml('Camera')['相机']
settings = read_yaml('Camera')['设置']
bot_navigation = read_yaml('Camera')['底部导航栏']
navigation = read_yaml('Camera')['导航栏']
beauti = read_yaml('Camera')['美颜']
release = read_yaml('Camera')['发布']


class CameraPage(WebPage):
    """相机类"""

    @allure.step("不连接设备")
    def no_connect(self):
        self.is_click((camera[0]['type'], camera[0]['value']))
        self.is_click((camera[1]['type'], camera[1]['value']))
        self.is_click((camera[2]['type'], camera[2]['value']))
        sleep(3)

    @allure.step("连接设备")
    def connect(self):
        """连接设备"""
        self.is_click((camera[0]['type'], camera[0]['value']))
        self.is_click((camera[3]['type'], camera[3]['value']))
        sleep(3)

    @allure.step("导航栏")
    def photo(self):
        """切换smart"""
        self.is_click((navigation[0]['type'], navigation[0]['value']))

    def gesture(self):
        self.is_click((navigation[1]['type'], navigation[1]['value']))

    def action(self):
        self.is_click((navigation[2]['type'], navigation[2]['value']))

    def flip(self):
        self.is_click((navigation[3]['type'], navigation[3]['value']))

    def script(self):
        self.is_click((navigation[4]['type'], navigation[4]['value']))

    @allure.step("底部导航栏")
    def smart(self):
        """SMART"""
        self.is_click((bot_navigation[0]['type'], bot_navigation[0]['value']))

    def ai_live(self):
        """AILive"""
        self.is_click((bot_navigation[1]['type'], bot_navigation[1]['value']))

    def actions(self):
        """拍照"""
        sleep(3)
        self.is_click((bot_navigation[2]['type'], bot_navigation[2]['value']))

    def video(self):
        """录像"""
        sleep(3)
        self.is_click((bot_navigation[3]['type'], bot_navigation[3]['value']))

    def panoramic(self):
        """全景"""
        sleep(3)
        self.is_click((bot_navigation[4]['type'], bot_navigation[4]['value']))

    def time_lapse(self):
        """延时摄影"""
        sleep(3)
        self.is_click((bot_navigation[5]['type'], bot_navigation[5]['value']))

    def motion_delay(self):
        """运动延时"""
        sleep(3)
        self.is_click((bot_navigation[6]['type'], bot_navigation[6]['value']))

    def description(self, reals):
        """作品描述"""
        self.input_text((release[1]['type'], release[1]['value']), reals)

    @allure.step("前置条件")
    def is_click_(self, locator):
        if locator['name'] == '美颜按钮':
            self.is_click((locator['type'], locator['value']))

        elif locator['name'] == '取消美颜':
            self.swipe_up()
            # self.touch_moveto(locator=(locator['type'], locator['value']))    #没有滑动  找不到元素 所以报错
            self.is_click((locator['type'], locator['value']))

        elif locator['name'] == '自动美颜':
            self.is_click((locator['type'], locator['value']))

        elif locator['name'] == '瘦脸':
            self.is_click((locator['type'], locator['value']))
            # self.roll_beautify(1016)

        elif locator['name'] == '美颜滚动条':
            self.move_seek_bar((locator['type'], locator['value']))
            # self.tap_element((locator['type'], locator['value']))
            self.is_click((locator['type'], locator['value']))


        elif locator['name'] == '磨皮':
            self.is_click((locator['type'], locator['value']))
            self.roll_beautify(1016)

        elif locator['name'] == '美白':
            self.is_click((locator['type'], locator['value']))
            self.roll_beautify(1016)

        elif locator['name'] == '眼睛放大':
            self.swipe_down()
            self.is_click((locator['type'], locator['value']))
            self.roll_beautify(1016)

        elif locator['name'] == '光照':
            self.swipe_down()
            self.is_click((locator['type'], locator['value']))
            self.roll_beautify(1016)

        elif locator['name'] == '红润':
            self.swipe_down()
            self.is_click((locator['type'], locator['value']))
            self.roll_beautify(1016)  # 滚动条

        elif locator['name'] == 'action':
            self.blank_01()  # 空白区域
            self.is_click((locator['type'], locator['value']))
            sleep(2)
            # self.swip_return()
        elif locator['name'] == '去水印':
            self.swip_Watermark_up()  # 横屏向上滑动
            self.is_click((locator['type'], locator['value']))

        elif locator['name'] == '变焦速度':
            self.zoom_speed()
            self.is_click((locator['type'], locator['value']))

        elif locator['name'] == '水平反向':
            self.swip_Yuntai_up()
            self.is_click((locator['type'], locator['value']))

        elif locator['name'] == '默认':
            self.swip_Yuntai_up()
            self.is_click((locator['type'], locator['value']))

        elif locator['name'] == '关闭':
            self.is_click((locator['type'], locator['value']))
            self.swip_return()

        elif locator['name'] == '1秒':

            self.swip_interval_up()
            # self.is_click((locator['type'], locator['value']))

        elif locator['name'] == '1min':
            self.swip_Shooting_time_up()
            self.is_click((locator['type'], locator['value']))

        elif locator['name'] == '倒计时' or \
                locator['name'] == 'off' or \
                locator['name'] == '3s' or \
                locator['name'] == '5s' or \
                locator['name'] == '7s' or \
                locator['name'] == '设置' or \
                locator['name'] == '视频' or \
                locator['name'] == '云台' or \
                locator['name'] == '通用' or \
                locator['name'] == '闪光灯' or \
                locator['name'] == '关闭' or \
                locator['name'] == '常亮' or \
                locator['name'] == '网络显示' or \
                locator['name'] == '方格' or \
                locator['name'] == '方格+对角线' or \
                locator['name'] == '白平衡' or \
                locator['name'] == '自动' or \
                locator['name'] == '晴天' or \
                locator['name'] == '阴天' or \
                locator['name'] == '白炽灯' or \
                locator['name'] == '荧光灯' or \
                locator['name'] == '返回' or \
                locator['name'] == '手势控制' or \
                locator['name'] == '跟随+拍摄' or \
                locator['name'] == '问号' or \
                locator['name'] == '行走' or \
                locator['name'] == '运动' or \
                locator['name'] == '跟随' or \
                locator['name'] == '左右跟随' or \
                locator['name'] == '全锁定' or \
                locator['name'] == '横滚航向跟随' or \
                locator['name'] == '快' or \
                locator['name'] == '中' or \
                locator['name'] == '慢' or \
                locator['name'] == '垂直反向' or \
                locator['name'] == 'M键开关' or \
                locator['name'] == '切换拍照/录像' or \
                locator['name'] == '快捷菜单' or \
                locator['name'] == '云台自动校准' or \
                locator['name'] == '通用页取消' or \
                locator['name'] == '相册页取消' or \
                locator['name'] == '开始' or \
                locator['name'] == '确定' or \
                locator['name'] == '设备管理' or \
                locator['name'] == 'C17F设备' or \
                locator['name'] == 'C17F设备Button' or \
                locator['name'] == '分辨率' or \
                locator['name'] == 'resolution_720' or \
                locator['name'] == 'resolution_1080' or \
                locator['name'] == 'resolution_4k' or \
                locator['name'] == '5x' or \
                locator['name'] == '10x' or \
                locator['name'] == '15x' or \
                locator['name'] == '30x' or \
                locator['name'] == '运动延时' or \
                locator['name'] == '延时摄影' or \
                locator['name'] == '全景' or \
                locator['name'] == '录像' or \
                locator['name'] == '拍照' or \
                locator['name'] == 'SMART':
            self.is_click((locator['type'], locator['value']))
        # elif locator['name'] == '编辑':
        #     self.tap_element_coordinate(925, 2300)

        elif locator['name'] == '相册' or \
                locator['name'] == '手势' or \
                locator['name'] == '切换摄像头' or \
                locator['name'] == '切换SMART' or \
                locator['name'] == '全部' or \
                locator['name'] == '视频' or \
                locator['name'] == '照片' or \
                locator['name'] == '喜欢' or \
                locator['name'] == '图' or \
                locator['name'] == '选择' or \
                locator['name'] == 'favorite' or \
                locator['name'] == '编辑' or \
                locator['name'] == '删除' or \
                locator['name'] == '关闭' or \
                locator['name'] == '图片信息' or \
                locator['name'] == '剪辑返回' or \
                locator['name'] == '退出/取消' or \
                locator['name'] == '保存并退出/确定' or \
                locator['name'] == '确定删除':
            self.is_click((locator['type'], locator['value']))

        elif locator['name'] == '0.5秒' or \
                locator['name'] == '2秒' or \
                locator['name'] == '3秒' or \
                locator['name'] == '4秒' or \
                locator['name'] == '5秒' or \
                locator['name'] == '6秒' or \
                locator['name'] == '7秒' or \
                locator['name'] == '8秒' or \
                locator['name'] == '9秒' or \
                locator['name'] == '10秒' or \
                locator['name'] == '13秒' or \
                locator['name'] == '15秒' or \
                locator['name'] == '20秒' or \
                locator['name'] == '25秒' or \
                locator['name'] == '30秒' or \
                locator['name'] == '40秒' or \
                locator['name'] == '60秒' or \
                locator['name'] == '∞' or \
                locator['name'] == '1min' or \
                locator['name'] == '2min' or \
                locator['name'] == '3min' or \
                locator['name'] == '4min' or \
                locator['name'] == '5min' or \
                locator['name'] == '10min' or \
                locator['name'] == '20min' or \
                locator['name'] == '30min' or \
                locator['name'] == '1h' or \
                locator['name'] == '3h' or \
                locator['name'] == '5h' or \
                locator['name'] == '间隔' or \
                locator['name'] == '第一时长' or \
                locator['name'] == '第二时长' or \
                locator['name'] == '箭头' or \
                locator['name'] == '轨迹_path' or \
                locator['name'] == '添加视频' or \
                locator['name'] == '删除视频':
            self.is_click((locator['type'], locator['value']))

        elif locator['name'] == '使用' or \
                locator['name'] == '使用后返回' or \
                locator['name'] == '草稿箱' or \
                locator['name'] == '重拍' or \
                locator['name'] == '拍下一段' or \
                locator['name'] == '草稿' or \
                locator['name'] == 'SMART3保存' or \
                locator['name'] == 'smart蓝牙' or \
                locator['name'] == '拍摄教程缩小' or \
                locator['name'] == '拍摄教程放大' or \
                locator['name'] == '预览后保存' or \
                locator['name'] == '发布的返回键' or \
                locator['name'] == '为你的作品写一段描述吧' or \
                locator['name'] == '快手按钮' or \
                locator['name'] == '同步发布按钮' or \
                locator['name'] == '同步发布' or \
                locator['name'] == '发布' or \
                locator['name'] == '定位' or \
                locator['name'] == '添加标签' or \
                locator['name'] == '标签2' or \
                locator['name'] == '删除标签1' or \
                locator['name'] == '视频开/关' or \
                locator['name'] == '1min' or \
                locator['name'] == '2min' or \
                locator['name'] == '3min' or \
                locator['name'] == '4min' or \
                locator['name'] == '5min' or \
                locator['name'] == '10min' or \
                locator['name'] == '20min' or \
                locator['name'] == '30min' or \
                locator['name'] == '1h' or \
                locator['name'] == '3h' or \
                locator['name'] == '5h' or \
                locator['name'] == '间隔' or \
                locator['name'] == '第一时长' or \
                locator['name'] == '第二时长' or \
                locator['name'] == '箭头' or \
                locator['name'] == '轨迹_path' or \
                locator['name'] == '添加视频' or \
                locator['name'] == '删除视频':
            self.is_click((locator['type'], locator['value']))


if __name__ == '__main__':
    beauti = read_yaml('Camera')['美颜']
    print((beauti[9]['type'], beauti[9]['value']))
    # print((camera[0]['type'], camera[0]['value']))
    # print((navigation['type'], navigation['value']))
    # print((camera[11]['type'],camera[11]['value']))
    # print((camera[18]['type'], camera[18]['value']))
    # locator1 = [(read_yaml('Camera')['相机'][0]),(read_yaml('Camera')['相机'][1]),(read_yaml('Camera')['相机'][2]),(read_yaml('Camera')['相机'][3]),(read_yaml('Camera')['相机'][4])]
    # for i in locator1:
    #     print((i['type'], i['value']))
