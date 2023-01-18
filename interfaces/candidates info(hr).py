import sys
from PyQt5 import QtWidgets,QtCore,Qt,QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5.QtGui import *
import sqlite3
class Hrcandidate(QDialog):
    def __init__(self):
        super(Hrcandidate, self).__init__()
        loadUi("candidates.ui",self)
        
        for i in range(self.tableWidget.rowCount()):
            
                item = QtWidgets.QTableWidgetItem('Select')
                item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                item.setCheckState(QtCore.Qt.Unchecked)
                self.tableWidget.setItem(i, -1, item)
            # label=QCheckBox()
            # label.setStyleSheet("background-color: darkorange;color: black ;border: 1px solid black; color:black")
            # self.tableWidget.setCellWidget(-1,i,label)
        
        
     

        
a=QApplication(sys.argv)
mainwindow=Hrcandidate()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1230)
widget.setFixedHeight(700)
widget.show()
a.exec_()