import sys
from PyQt5 import QtWidgets,QtCore,Qt,QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5.QtGui import *
import sqlite3
class assigntask1(QDialog):
    def __init__(self):
        super(assigntask1, self).__init__()
        loadUi("assigntask1.ui",self)
        
        
        
     

        
a=QApplication(sys.argv)
mainwindow=assigntask1()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1230)
widget.setFixedHeight(700)
widget.show()
a.exec_()