#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from Public import Caplictily

from PO.Camera_Element import Beautify_Page

class Beautify_beau():
    '''是否 是会员'''
    def __init__(self):

        driver = Caplictily.Driver_Config()
        self.driver = driver.get_driver()

        self.bea = Beautify_Page(self.driver)

    def beautify_01(self):
        '''
        未登录且非会员
        :return:
        '''
        self.bea.click_File_iv_camera1()
        
   


if __name__ == '__main__':
    beaut = Beautify_beau()
    print(beaut.beautify_01())

