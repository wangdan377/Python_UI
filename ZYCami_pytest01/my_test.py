from common.readelement import read_yaml
import pytest
from appium import webdriver


"""CAMERA_ = [(read_yaml('Camera')['相机'][12]),(read_yaml('Camera')['相机'][14]),(read_yaml('Camera')['相机'][18]),(read_yaml('Camera')['相机'][19]),(read_yaml('Camera')['相机'][20])]
@pytest.mark.parametrize("condown", CAMERA_)
def test_name(condown):
    if condown['name'] =='美颜按钮':
        print((condown['type'],condown['value'])*2)
    elif condown['name'] =='磨皮':
        print('磨皮操作')
    elif condown['name'] =='美白':
        print('美白操作')
    elif condown['name'] =='眼睛放大':
        print('眼睛放大操作')
    elif condown['name'] =='光照':
        print('光照操作')


if __name__ == '__main__':
    pytest.main([r'D:\ZYCami_pytest01\my_test.py'])"""

"""driver = None
def get_driver():
    global driver
    if driver is None:
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', read_yaml('desired_caps'))
        driver.implicitly_wait(10)
        return driver


if __name__ == '__main__':
      get_driver()"""


import pytest

@pytest.mark.parametrize("a",[2,4,6])
@pytest.mark.parametrize("b",[1,3,5])
def test_1(a,b):
    print(a,b)

if __name__ == '__main__':

    pytest.main(["-s","my_test.py"])