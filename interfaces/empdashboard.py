import sys
from PyQt5 import  QtWidgets , QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
class emp_profile(QDialog):  # employee ka dashboardhai ye

    def __init__(self,name):
        self.name=name
        super( emp_profile,self).__init__()
        loadUi("employee.ui",self)
        # self.conn=sqlite3.connect("empdata.db")
        # self.myprofile.clicked.connect(self.Profile)
        # self.attendance.clicked.connect(self.Attendance)
        # self.tasks.clicked.connect(self.Task)
        # self.logout.clicked.connect(self.Logout)
        # self.upload.clicked.connect(self.Upload)
        # self.savepassword.clicked.connect(self.change_pass)
        # self.saveinfo.clicked.connect(self.editProfile)
        # self.upload.clicked.connect(self.uploadPic)
        self.currentpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newpass1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newpass2.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.editprofile.setRowCount(8) 
        #Column count
        self.editprofile.setColumnCount(2) 
        keys=["ID","FULL NAME","DESIGNATION","EMAIL","ADDRESS","PHONE","TASKS","WAGE"]
        for i in range(len(keys)):
            
            label=QLabel(keys[i])
            label.setStyleSheet("background-color: darkorange;color: black ;border: 1px solid black")
            self.editprofile.setCellWidget(i,0,label)
            if keys[i]=="DESIGNATION":
                self.box=QComboBox()
                self.box.addItem("WEB DESIGNER")
                self.box.addItem("FRONT-END DEVELPER")
                self.box.addItem("BACK-END DEVELOPER")
                self.box.addItem("SEO")
                self.box.addItem("ANALYST")
                self.box.addItem("MANAGER")

                self.editprofile.setCellWidget(i,1,self.box)
        self.tableWidget.setRowCount(9)   
        #Column count
        self.tableWidget.setColumnCount(1) 
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
a=QApplication(sys.argv)
mainwindow=emp_profile("--")
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1230)
widget.setFixedHeight(700)
widget.show()
a.exec_()