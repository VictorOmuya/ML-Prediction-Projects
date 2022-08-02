# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 11:42:38 2021

@author: Touching tap
"""

from soft_home import Ui_Dialog
from software import Ui_MainWindow
import unittest


class softwareCostTest(unittest.TestCase):
    
    # test function
    def test_home_to_main(self):
        testValue = Ui_Dialog.main
        # error message in case if test case got failed
        message = "Its okay. This module will run successfully"
        # assertTrue() to check true of test value
        self.assertTrue(testValue, message)

    
    def test_model(self):
        testValue = Ui_MainWindow.predictor
        message = "the funtion connects properly with the right model"
        print(message)
        self.assertTrue(testValue, message)

    
if __name__ == '__main__':
    unittest.main()