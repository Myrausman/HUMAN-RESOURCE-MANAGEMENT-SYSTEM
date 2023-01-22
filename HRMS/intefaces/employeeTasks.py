import sys
from PyQt5 import  QtWidgets , QtGui,QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from myprofile import emp_profile
import sqlite3
class employee_tasks(QDialog):
    def __init__(self,name):
        super().__init__()
        self.name=name
        loadUi("/home/maira/Desktop/PROJECT -/tasks_emp.ui",self)
        self.logo = QLabel()
        self.logo.setGeometry(0, 0, 218, 69)
        self.logo.setPixmap(QPixmap("/home/maira/Desktop/PROJECT -/logo.png"))
        self.myprofile.clicked.connect(self.my_profile)
        self.logout.clicked.connect(self.log_out)
        self.loaddata()
        keys=["NAME","TASK no.","TASK","START-DATE","END-DATE","STATUS"]
        # for i in range(len(keys)):
        #     self.tableWidget.
        self.tableWidget.setStyleSheet("border-color: rgb(255, 197, 98);selection-color: rgb(136, 138, 133);color: rgb(238, 238, 236)")
        self.tableWidget.setVerticalHeaderLabels(keys)
        # self.tableWidget.VerticalHeaderDefaultSectionSize(250)

    def loaddata(self):
        self.conn = sqlite3.connect("empdata.db")
        cur = self.conn.cursor()
        sqlquery = 'SELECT   EmployeeName,TaskNumber,Task,StartDate,EndDate,status FROM tasks WHERE EmployeeName =\'' + self.name + "\'"

        # print(name)
        # path = "/home/maira/Desktop/PROJECT -/"
        for person in cur.execute(sqlquery):
            print(person)
            # print(person[1])
            self.tableWidget.setRowCount(6)
            self.tableWidget.setColumnCount(1)
            for i in range(5):
                label=QLabel(str(person[i]))
                label.setAlignment(QtCore.Qt.AlignCenter)

                # label.setStyleSheet()
                self.tableWidget.setCellWidget(i, 0, label)
            
            self.box = QComboBox()
            self.box.addItem("Working")
            self.box.addItem("Not Complete")
            self.box.addItem("Completed")
            self.tableWidget.setCellWidget(5, 0, self.box)
    
    def log_out(self):
        # self.close()
        print("EMP_INFO")
        a=LOGOUT(self.name)
        
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(640)
        widget.setFixedHeight(400)   
        # a.move(100,100)
        # a.setWindowModality(Qt.ApplicationModal)
        widget.setWindowTitle("log out")
    def my_profile(self):
        self.close()
        emppf=hr_dashboard(self.name)
        widget.addWidget(emppf)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)
            
    
a=QApplication(sys.argv)
mainwindow=employee_tasks("hadiqa")
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1230)
widget.setFixedHeight(700)
widget.show()
a.exec_()