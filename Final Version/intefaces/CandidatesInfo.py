import sys
from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
# from CandidatesInfo import Hrcandidate
from EMP_INFO import EMP_INFO
import sqlite3
class Hrcandidate(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("/home/maira/Desktop/PROJECT -/candidates.ui",self)
        self.logo=QLabel()
        self.logo.setGeometry(0,0,218,69)
        self.logo.setPixmap(QPixmap("logo.png"))
        
        self.conn= sqlite3.connect("empdata.db")
        cur = self.conn.cursor()
        sqlquery = 'SELECT  * FROM candi'
        self.tableWidget.setHorizontalHeaderLabels(["FIRST NAME","LAST NAME","CNIC","GENDER","ADDRESS","QUALIFICATION","SELECT"])
        self.tableWidget.setColumnCount(7)
        self.count=0
        for person in cur.execute(sqlquery):
            self.count+=1
            # self.tableWidget.set
            self.count+=1
        self.tableWidget.setEditTriggers(
                QtWidgets.QAbstractItemView.NoEditTriggers)
        for i in range(self.count):
            
                item = QtWidgets.QTableWidgetItem('Select')
                item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                item.setCheckState(QtCore.Qt.Unchecked)
                self.tableWidget.setItem(i, -1, item)


            # label=QCheckBox()
            # label.setStyleSheet("background-color: darkorange;color: black ;border: 1px solid black; color:black")
            # self.tableWidget.setCellWidget(-1,i,label)
        
        
     

        
# a=QApplication(sys.argv)
# mainwindow=Hrcandidate()
# widget=QtWidgets.QStackedWidget()
# widget.addWidget(mainwindow)
# widget.setFixedWidth(1230)
# widget.setFixedHeight(700)
# widget.show()
# a.exec_()