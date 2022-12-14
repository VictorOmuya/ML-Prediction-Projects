# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fuzzy_home.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from locate import *

class Ui_Dialog(object):
    
    def next(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_locate_image()
        self.ui.setupUi(self.window)
        self.window.show()
        Dialog.hide()
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(610, 255)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 83, 611, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(185, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        
        self.btn_next = QtWidgets.QPushButton(Dialog)
        self.btn_next.setGeometry(QtCore.QRect(533, 230, 75, 23))
        self.btn_next.setObjectName("btn_next")
        self.btn_next.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(40)
        self.btn_next.setFont(font)
        self.btn_next.clicked.connect(self.next)
        
        self.lbl_back = QtWidgets.QLabel(Dialog)
        self.lbl_back.setGeometry(QtCore.QRect(0, 2, 611, 251))
        self.lbl_back.setText("")
        self.lbl_back.setObjectName("lbl_back")
        Pixmap = QPixmap('image2.jfif')
        self.lbl_back.setPixmap(Pixmap)
        self.lbl_back.setScaledContents(True)
        
        self.lbl_back.raise_()
        self.label.raise_()
        self.btn_next.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Home"))
        self.label.setText(_translate("Dialog", "EXTRACT IMAGE LOCATION"))
        self.btn_next.setText(_translate("Dialog", "next"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
