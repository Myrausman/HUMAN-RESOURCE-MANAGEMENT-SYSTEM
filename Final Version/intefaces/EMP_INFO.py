import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
# from addemp import ADD_EMPLOYEE
import sqlite3

class EMP_INFO(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("emp_recordes(hr).ui",self)
        self.logo=QLabel()
        self.logo.setGeometry(0,0,218,69)
        self.logo.setPixmap(QPixmap("logo.png"))
        self.addemp.clicked.connect(self.add_employee)
        self.delemp.clicked.connect(self.delete_employee)
        self.updemp.clicked.connect(self.update_employee)
        
        self.conn = sqlite3.connect("empdata.db")
        cur = self.conn.cursor()
        sqlquery = 'SELECT   id,name,department,position,email,address,phone,image,tasks,wage FROM empdat'
        self.employeeTable.setHorizontalHeaderLabels(["ID","NAME","DEPARTMENT","DESIGNATION","E-MAIL","ADDRESS","PHONE","IMAGE","TASKS","WAGE","SALARY"])
        # self.count=0
        self.employeeTable.setColumnCount(11)
        self.employeeTable.setRowCount(20)
        tablerow=0
        for person in cur.execute(sqlquery):
            for i in range(len(person)):
                self.employeeTable.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(person[i])))
            self.image=QLabel()
            self.image.setPixmap(QPixmap(person[7]))
            self.image.setScaledContents(True)         
            self.employeeTable.setCellWidget(tablerow, 7, self.image)
            tablerow+=1
        

    def delete_employee(self):
        print("add employee")
    def update_employee(self):
        print("add employee")
    def add_employee(self):
        a=ADD_EMPLOYEE()
        widget=QtWidgets.QStackedWidget()
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(640)
        widget.setFixedHeight(400)
        print("add employee")
            
class ADD_EMPLOYEE(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("addemployee.ui",self)

        # self.saveinfo.clicked.connect(self.add_employee)
        # self.conn = sqlite3.connect("empdata.db")
        # cur = self.conn.cursor()
        # items = []
        # for i in range(10):
        #     rowdata = ''
        #     item = self.tableWidget.item(i, 1)
        #     # print(self.box.currentText(),"item box")
        #     if self.tabelWidget.item(i, 0) == "DESIGNATION":
        #         rowdata += self.box.currenttext()
        #     if item and item.text:

        #         rowdata += item.text()
        #         items.append(rowdata)
        #     else:
        #         rowdata += "NULL"
        # # print(items)
        # cur = self.conn.cursor()
        # emp = 'UPDATE empdat SET  position=?,department =?,email=?,address=?,phone=?,tasks=? WHERE name =\'' + self.name + "\'"
        # cur.execute(
        #     emp, (items[2], items[3], items[4], items[5], items[6], items[7]))
        # self.conn.commit()
     

        
# a=QApplication(sys.argv)
# mainwindow=EMP_INFO()
# widget=QtWidgets.QStackedWidget()
# widget.addWidget(mainwindow)
# widget.setFixedWidth(1230)
# widget.setFixedHeight(700)
# widget.show()
# a.exec_()