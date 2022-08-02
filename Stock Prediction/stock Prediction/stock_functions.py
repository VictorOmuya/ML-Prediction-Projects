# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 06:03:06 2020

@author: Touching tap
"""
import pandas as pd
import pickle
import numpy as np
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from tkinter import filedialog



def pred_new(companyname):
    
    if  companyname.currentText() == 'FIRSTBANK':
        
        model = pickle.load(open('./models/svrprice_model3.sav', 'rb'))
            
    elif companyname.currentText() == 'UBA':
        model = pickle.load(open('./models/uba.sav', 'rb'))
        
    elif companyname.currentText() == 'VITAFOAM':
        model = pickle.load(open('./models/Vitafoamprice_model.sav', 'rb'))
        
    elif companyname.currentText() == 'UNILEVER':
        model = pickle.load(open('./models/Unileverprice_model.sav', 'rb'))
        
    elif companyname.currentText() == 'TOTAL':
        
        model = pickle.load(open('./models/Totalpricing_model.sav', 'rb'))
        
    elif companyname.currentText() == 'WAPCO':
        model = pickle.load(open('./models/Wapcoprice_model.sav', 'rb'))
        
    elif companyname.currentText() == 'NBC':
        model = pickle.load(open('./models/nbc.sav', 'rb'))
        
    elif companyname.currentText() == '7UP':
        model = pickle.load(open('./models/7up.sav', 'rb'))
        
    elif companyname.currentText() == 'PZ':
        model = pickle.load(open('./models/pz.sav', 'rb'))
        
    elif companyname.currentText() == 'GUINNESS':
        model = pickle.load(open('./models/guinness.sav', 'rb'))
        
    elif companyname.currentText() == 'JBERGER':
        model = pickle.load(open('./models/jberger.sav', 'rb'))
        
    elif companyname.currentText() == 'FLOURMILL':
        model = pickle.load(open('./models/flourmill.sav', 'rb'))
            
    elif companyname.currentText() == 'MOBIL':
        model = pickle.load(open('./models/mobil.sav', 'rb'))
        
    return model
pass



    


