# conftest.py
import os
import base64
import pytest
import allure
from py._xmlgen import html
from common.readconfig import ini
from config.conf import SCREENSHOT_DIR
from tools.times import datetime_strftime, timestamp
from appium import webdriver
from common.readelement import read_yaml

read_yaml_data = read_yaml('desired_caps')


driver = None
@pytest.fixture(scope='session', autouse=True)
def get_driver(request):
    global driver
    if driver is None:
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', read_yaml('desired_caps'))
        driver.implicitly_wait(10)

        def fn():
            driver.quit()

        request.addfinalizer(fn)
        return driver
# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#     当测试失败的时候，自动截图，展示到html报告中
#     :param item:
#     """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             screen_img = _capture_screenshot()
#             if screen_img:
#                 html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:1024px;height:768px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % screen_img
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#         report.description = str(item.function.__doc__)
#         report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('用例名称'))
    cells.insert(2, html.th('Test_nodeid'))
    cells.pop(2)


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    cells.insert(2, html.td(report.nodeid))
    cells.pop(2)


@pytest.mark.optionalhook
def pytest_html_results_table_html(report, data):
    if report.passed:
        del data[:]
        data.append(html.div('通过的用例未捕获日志输出.', class_='empty log'))


@pytest.mark.optionalhook
def pytest_html_report_title(report):
    report.title = "pytest示例项目测试报告"


@pytest.mark.optionalhook
def pytest_configure(config):
    config._metadata.clear()
    config._metadata['测试项目'] = "涉外案事件通报"
    config._metadata['测试地址'] = ini.url


@pytest.mark.optionalhook
def pytest_html_results_summary(prefix, summary, postfix):
    # prefix.clear() # 清空summary中的内容
    prefix.extend([html.p("所属部门: 技术管理部")])
    prefix.extend([html.p("测试执行人: 唐雄")])


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """收集测试结果"""
    result = {
        "total": terminalreporter._numcollected,
        'passed': len(terminalreporter.stats.get('passed', [])),
        'failed': len(terminalreporter.stats.get('failed', [])),
        'error': len(terminalreporter.stats.get('error', [])),
        'skipped': len(terminalreporter.stats.get('skipped', [])),
        # terminalreporter._sessionstarttime 会话开始时间
        'total times': timestamp() - terminalreporter._sessionstarttime
    }
    print(result)
    # if result['failed'] or result['error']:
    #     send_report()


# def _capture_screenshot():
#     """
#     截图保存为base64
#     """
#     now_time = datetime_strftime("%Y%m%d%H%M%S")
#     if not os.path.exists(SCREENSHOT_DIR):
#         os.makedirs(SCREENSHOT_DIR)
#     screen_path = os.path.join(SCREENSHOT_DIR, "{}.png".format(now_time))
#     driver.save_screenshot(screen_path)
#     allure.attach.file(screen_path, "测试失败截图{}".format(
#         now_time), allure.attachment_type.PNG)
#     with open(screen_path, 'rb') as f:
#         imagebase64 = base64.b64encode(f.read())
#     return imagebase64.decode()
