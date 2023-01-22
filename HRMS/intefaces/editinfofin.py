import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
import sqlite3
class editinfo(QDialog):
    def __init__(self):
        super(editinfo, self).__init__()
        loadUi("editinfo.ui",self)
        self.data()
    def data(self):
        
        conn=sqlite3.connect("empdata.db")
        cur=conn.cursor()
        q= 'SELECT * FROM payslips'
        cur.execute(q)
        # self.tableWidget.setRowCount(50)
        t=0
        for row in cur.execute(q):
            print(row)
            self.tableWidget.setItem(t,0,QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(t,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tableWidget.setItem(t,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.tableWidget.setItem(t,3,QtWidgets.QTableWidgetItem(str(row[10])))
            self.tableWidget.setItem(t,4,QtWidgets.QTableWidgetItem(str(row[11])))
            self.tableWidget.setItem(t,5,QtWidgets.QTableWidgetItem(str(row[12])))
        
            t=+1
        self.tableWidget.setRowCount(t+1)
    

a=QApplication(sys.argv)
mainwindow=editinfo()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1230)
widget.setFixedHeight(700)
widget.show()
a.exec_()