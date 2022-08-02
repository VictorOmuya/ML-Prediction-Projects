# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 11:06:11 2020

@author: Touching tap
"""

def input_data(background):
    
    if background.currentText() == "Urban":
        bg = 1
    elif background.currentText() == "Rural":
        bg = 0
        
    return bg

def input_data2(gender):
    
    if gender.currentText() == "Male":
        gen = 1
    elif gender.currentText() == "Female":
        gen = 0
        
    return gen

def input_data3(studytime):

    if studytime.currentText() == "1":
        st = 0
    elif studytime.currentText() == "2":
        st = 1
    elif studytime.currentText() == "3":
        st = 2
    elif studytime.currentText() == "4 and above":
        st = 3
        
    return st

def input_data4(extralesson):

    if extralesson.currentText() == "Yes":
        el = 0
    elif extralesson.currentText() == "No":
        el = 1
        
    return el

def input_data5(secondary):
    
    if secondary.currentText() == "HND 2":
        sec = 0
    elif secondary.currentText() == "HND 1":
        sec = 1
    elif secondary.currentText() == "ND 2":
        sec = 0
    elif secondary.currentText() == "ND 1":
        sec = 1
        
    return sec

def input_data6(romance):

    if romance.currentText() == "Yes":
        rom = 1
    elif romance.currentText() == "No":
        rom = 0
        
    return rom

def input_data7(support):
    
    if support.currentText() == "Yes":
        sup = 1
    elif support.currentText() == "No":
        sup = 0
        
    return sup

def input_data8(health):

    if health.currentText() == "Bad":
        hlt = 4
    elif health.currentText() == "Very Bad":
        hlt = 3
    elif health.currentText() == "Good":
        hlt = 2
    elif health.currentText() == "Very Good":
        hlt = 1
    elif health.currentText() == "Excellent":
        hlt = 0
        
    return hlt

def input_data9(famsize):

    if famsize.currentText() == "Greater Than 3":
        fam = 0
    elif famsize.currentText() == "Not More Than 3":
        fam = 1
    return fam

def input_data10(internet):

    if internet.currentText() == "Yes":
        net = 1
    elif internet.currentText() == "No":
        net = 0
        
    return net

def input_data11(extracurr):

    if extracurr.currentText() == "Yes":
        ext = 1
    elif extracurr.currentText() == "No":
        ext = 0
        
    return ext

def input_data12(parental):

    if parental.currentText() == "Living Together":
        par = 1
    elif parental.currentText() == "Seperated":
        par = 0
        
    return par