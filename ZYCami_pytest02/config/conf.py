# conf.py
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


# 项目目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 配置文件
INI_PATH = os.path.join(BASE_DIR, 'config', 'config.ini')

# 页面元素目录
ELEMENT_PATH = os.path.join(BASE_DIR, 'page_element')

# 日志目录
LOG_PATH = os.path.join(BASE_DIR, 'logs')

# 报告目录
REPORT_PATH = os.path.join(BASE_DIR, 'report', 'report.html')

# 截图目录
SCREENSHOT_DIR = os.path.join(BASE_DIR, 'report', 'screen_capture')

# 元素定位的类型
LOCATE_MODE = {
    'css': By.CSS_SELECTOR,
    'xpath': By.XPATH,
    'name': By.NAME,
    'id': By.ID,
    'classname': By.CLASS_NAME,
    'link_text': By.LINK_TEXT,
    'tag_name': By.TAG_NAME
}

# 邮件信息
EMAIL_INFO = {
    'username': '1084502012@qq.com',  # 切换成你自己的地址
    'password': 'QQ邮箱授权码',
    'smtp_host': 'smtp.qq.com',
    'smtp_port': 465
}

# 收件人
ADDRESSEE = [
    '1084502012@qq.com',
]

if __name__ == '__main__':
    print(LOCATE_MODE['tag_name'])
