import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

class EMP_INFO(QDialog):
    def __init__(self):
        super(EMP_INFO, self).__init__()
        loadUi("employee recordes(hr).ui",self)
        
        for i in range(self.employeeTable.rowCount()):
            self.image=QLabel()
            a=QPixmap("placeholder.png")
            # setPixmap(scaledPixmap())
            # a.scaled(10, 10)
            # a.scaled (self, 
            #             int width, 
            #             int height, 
            #             Qt.AspectRatioMode aspectRatioMode = Qt.IgnoreAspectRatio,
            #             Qt.TransformationMode transformMode = Qt.FastTransformation)
            self.image.setPixmap(a)
            self.image.setScaledContents(True)
            # self.image.move(0, 10)
            
            
            self.employeeTable.setCellWidget(i, 6, self.image)
            # label=QCheckBox()
            # label.setStyleSheet("background-color: darkorange;color: black ;border: 1px solid black; color:black")
            # self.tableWidget.setCellWidget(-1,i,label)
        
        
     

        
a=QApplication(sys.argv)
mainwindow=EMP_INFO()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1230)
widget.setFixedHeight(700)
widget.show()
a.exec_()