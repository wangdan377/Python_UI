import subprocess

import os

'''
获取ios下的硬件信息
'''


def get_ios_devices():
    devices = []
    result = subprocess.Popen("ideviceinfo -k UniqueDeviceID", shell=True, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE).stdout.readlines()
    for item in result:
        t = item.decode().split("\n")
        if len(t) >= 2:
            devices.append(t[0])
    return devices

def aaa():
    a = 2
    b = 3
    c = 4
    return a,b,c


if __name__ == "__main__":
    qqq = [3, 5 ,7,]
    print(qqq,qqq,)

