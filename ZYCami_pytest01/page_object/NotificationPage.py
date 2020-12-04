# NotificationOfForeign-relatedCasesPage.py
from page.webpage import WebPage, sleep
from common.readelement import Element
import allure
import time

InformationDisposal = Element('Notification')
HandleTheCase = Element('ProcessingNotice')
title = time.strftime("%Y%m%d%H%M", time.localtime()) + '流程自动化测试案例'


class NotificationPage(WebPage):
    """产品类"""

    @allure.step("点击信息处置")
    def click_dispose_of(self):
        """点击信息处置"""
        self.is_click(InformationDisposal['涉外案事件处置按钮'])

    @allure.step("点击涉外案事件通报")
    def click_information_bulletin(self):
        """点击涉外案事件通报"""
        self.is_click(InformationDisposal['涉外案事件通报按钮'])

    @allure.step("切换iframe标签")
    def switch_iframe(self):
        """切换iframe标签"""
        self.iframe_switch_iframe(InformationDisposal['切换iframe标签'], 1)
        self.iframe_switch_iframe(InformationDisposal['切换iframe标签'], 1)

    @allure.step("点击新增案事件")
    def click_new_case_event(self):
        """点击新增案事件"""
        self.is_click(InformationDisposal['点击新增案事件'])

    @allure.step("是否从警综导入案件-NO")
    def click_alert_no(self):
        """是否从警综导入案件-NO"""
        self.is_click(InformationDisposal['是否从警综导入'])

    @allure.step("采取措施时间")
    def input_happen_time(self):
        """采取措施时间"""
        self.iframe_switch_iframe(InformationDisposal['切换iframe标签'], 1)
        self.input_text(InformationDisposal['采取措施时间'], time.strftime("%Y-%m-%d", time.localtime()))

    @allure.step("输入标题")
    def input_title(self):
        """输入标题"""
        self.input_text(InformationDisposal['输入标题'], title)

    @allure.step("选择上报类型")
    def switch_report_type(self):
        """选择上报类型"""
        self.is_click(InformationDisposal['点击上报类型'])
        self.is_click(InformationDisposal['选择上报类型'])

    @allure.step("选择案件类型")
    def switch_case_type(self):
        """选择上报类型"""
        self.is_click(InformationDisposal['点击案件类型'])
        self.is_click(InformationDisposal['选择案件类型'])

    @allure.step("选择案件所属区域")
    def switch_area_of_the_case(self):
        """选择案件所属区域"""
        self.is_click(InformationDisposal['点击案件所属区域'])
        self.is_click(InformationDisposal['选择案件所属区域'])

    @allure.step("输入简要案情")
    def input_brief_case(self):
        """输入简要案情"""
        self.input_text(InformationDisposal['输入简要案情'], title)

    @allure.step("添加涉案人员")
    def add_people(self):
        """添加涉案人员"""
        self.is_click(InformationDisposal['添加涉案人员'])
        self.iframe_default_content()
        self.iframe_switch_iframe(('tag_name', 'iframe'), 3)
        self.input_text(InformationDisposal['输入英文姓名'], "Test")
        self.input_text(InformationDisposal['输入中文姓名'], "测试")
        self.set_select_visible_text(InformationDisposal['选择性别'], '男')
        self.input_text(InformationDisposal['选择国籍'], '美国/USA')
        self.is_click(InformationDisposal['点击证件类型'])
        self.is_click(InformationDisposal['选择证件类型'])
        self.move_scroll_bar(1000)
        self.move_to_element(InformationDisposal['鼠标移动强制措施'])
        self.is_click(InformationDisposal['添加强制措施'])
        self.set_select_visible_text(InformationDisposal['采取措施'], '拘留审查')
        self.input_text(InformationDisposal['处罚决定单位'], '广州市公安局')
        self.is_click(InformationDisposal['点击违法犯罪名称'])
        self.is_click(InformationDisposal['选择违法犯罪名称'])
        self.is_click(InformationDisposal['点击违法犯罪名称'])
        self.move_scroll_bar(1000)
        self.input_text(InformationDisposal['措施执行地点'], '广州市看守所')
        self.is_click(InformationDisposal['点击保存按钮'])

    @allure.step("选择接收人员")
    def switch_receiver(self):
        """选择接收人员"""
        self.focus()
        self.is_click(InformationDisposal['点击添加接收单位'])
        self.iframe_default_content()
        self.iframe_switch_iframe(('tag_name', 'iframe'), 3)
        self.is_click(InformationDisposal['选择省级接收单位'])
        self.is_click(InformationDisposal['确认省级接收单位'])

    @allure.step("切换至主页面")
    def switch_main_page(self):
        """切换至主页面"""
        self.iframe_default_content()
        self.iframe_switch_iframe(('tag_name', 'iframe'), 1)
        self.iframe_switch_iframe(('tag_name', 'iframe'), 1)
        self.iframe_switch_iframe(('tag_name', 'iframe'), 1)

    @allure.step("发送通知")
    def send_notification(self):
        """发送通知"""
        self.is_click(InformationDisposal['发送通知'])


class ProcessingNotice(WebPage):
    @allure.step("点击信息处置")
    def click_dispose_of(self):
        """点击信息处置"""
        self.is_click(InformationDisposal['涉外案事件处置按钮'])

    @allure.step("点击涉外案事件通报")
    def click_information_bulletin(self):
        """点击涉外案事件通报"""
        self.is_click(InformationDisposal['涉外案事件通报按钮'])

    @allure.step("切换iframe标签")
    def switch_iframe(self):
        """切换iframe标签"""
        self.iframe_switch_iframe(InformationDisposal['切换iframe标签'], 1)
        self.iframe_switch_iframe(InformationDisposal['切换iframe标签'], 1)
        self.iframe_switch_iframe(InformationDisposal['切换iframe标签'], 1)

    @allure.step("按标题搜索案件")
    def find_Case_title(self):
        self.input_text(HandleTheCase[''], title)
        self.is_click(HandleTheCase[''])


if __name__ == '__main__':
    print(title)
