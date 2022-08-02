# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 11:06:11 2020

@author: Touching tap
"""

def input_data8(sitting):
    sit = 0
    if sitting.currentText() == "1 sitting":
        sit = 0
    elif sitting.currentText() == "2 sittings":
        sit = 1
    
    return sit
 

