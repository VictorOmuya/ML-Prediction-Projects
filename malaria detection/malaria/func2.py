# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 11:06:11 2020

@author: Touching tap
"""

def input_data(age):
    age = age.text()
    return age
    

def input_data2(sex):
    
    if sex.currentText() == "Male":
        x = 1
    elif sex.currentText() == "Female":
        x = 0
        
    return x

def input_data3(cold):

    if cold.currentText() == "Yes":
        st = 0
    elif cold.currentText() == "No":
        st = 1
        
    return st

def input_data4(mosq):

    if mosq.currentText() == "Yes":
        el = 0
    elif mosq.currentText() == "No":
        el = 1
        
    return el

def input_data5(fat):
    
    if fat.currentText() == "Yes":
        sec = 0
    elif fat.currentText() == "No":
        sec = 1

        
    return sec

def input_data6(ache):

    if ache.currentText() == "Yes":
        rom = 1
    elif ache.currentText() == "No":
        rom = 0
        
    return rom

def input_data7(bitter):
    
    if bitter.currentText() == "Yes":
        sup = 1
    elif bitter.currentText() == "No":
        sup = 0        
    return sup

def input_data8(urine):

    if urine.currentText() == "Yes":
        hlt = 4
    elif urine.currentText() == "No":
        hlt = 3        
    return hlt

def input_data9(temp):

    if temp.currentText() == "Yes":
        fam = 0
    elif temp.currentText() == "No":
        fam = 1
    return fam

