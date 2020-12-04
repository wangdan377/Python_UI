# times.py
import time
import datetime


def timestamp():
    """时间戳"""
    return time.time()


def datetime_strftime(fmt="%Y%m%d"):
    """datetime格式化时间"""
    return datetime.datetime.now().strftime(fmt)


def sleep(seconds=1.0):
    """
    睡眠时间
    """
    time.sleep(seconds)


if __name__ == '__main__':
    print(datetime_strftime())