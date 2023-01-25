import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from CandidatesInfo import Hrcandidate
from EMP_INFO import EMP_INFO
# from PyQt5.QtWidgets import  PasswordEdit

import sqlite3


class emp_profile(QDialog):  # employee ka dashboardhai ye

    def __init__(self, name, board):
        self.name = name
        self.board = board

        super().__init__()
        loadUi(board, self)
        self.logo = QLabel()
        self.logo.setGeometry(0, 0, 218, 69)
        self.logo.setPixmap(QPixmap("logo.png"))
        self.placeholder.setPixmap(QPixmap("/home/maira/Desktop/PROJECT -/placeholder.png"))
        self.placeholder2.setPixmap(QPixmap("/home/maira/Desktop/PROJECT -/placeholder.png"))
        self.conn = sqlite3.connect("empdata.db")
        self.loaddata(self.name)
        self.currentpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newpass1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newpass2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.savepassword.clicked.connect(self.change_pass)
        self.saveinfo.clicked.connect(self.editProfile)
        self.upload.clicked.connect(self.uploadPic)
        self.logout.clicked.connect(self.log_out)
        print(self.board)
        # if self.board == "/home/maira/Desktop/PROJECT -/hr_dashboard.ui":
        #     print("im in condition")
        #     self.candidate_info.clicked.connect(self.candidates_info)
        #     self.employeeinfo.clicked.connect(self.employee_info)
        #     self.assigntask.clicked.connect(self.assign_task)
        #     self.employeeperformance.clicked.connect(self.employee_performance)

        # elif self.board == "/home/maira/Desktop/PROJECT -/financedashboard.ui":
        #     self.generatepayslip.clicked.connect(self.generate_payslip)
        #     self.empinfo.clicked.connect(self.emp_info)

        # elif self.board == "/home/maira/Desktop/PROJECT -/employee.ui":
            # self.tasks.clicked.connect(self.seeTask)
            # self.generatepayslip.clicked.connect(self.generate_payslip)

    def log_out(self):
        print("logged-out")

    def uploadPic(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            "/home/maira/Pictures/",
                                            'Images(*.png)')
        self.filename.setText(fname[0])
        image = fname[0]
        cur = self.conn.cursor()
        self.placeholder2.setPixmap(QPixmap(image))
        cur.execute(image)
        self.conn.commit()

    def loaddata(self, name):

        cur = self.conn.cursor()
        sqlquery = 'SELECT  id,name,department,position,email,address,phone,tasks,wage,about ,image FROM empdat WHERE name =\'' + name + "\'"

        # print(name)
        path = "/home/maira/Desktop/PROJECT -/"
        for person in cur.execute(sqlquery):
            print(person)
            print(person[1])
            self.tableWidget.setRowCount(8)

            #Column count
            self.tableWidget.setColumnCount(1)
            self.tableWidget.setEditTriggers(
                QtWidgets.QAbstractItemView.NoEditTriggers)
            for row in range(len(person) - 3):
                self.tableWidget.setItem(
                    row - 1, 1, QtWidgets.QTableWidgetItem(str(person[row])))
            about = person[9]
            self.ABOUTME.setStyleSheet("color:rgb(0,0,0); font:25pt bold")
            self.ABOUTME.setText(" ABOUT ME \n " + about)
            image = path + person[10]
            self.placeholder.setPixmap(QPixmap(image))
            self.placeholder2.setPixmap(QPixmap(image))
            password = person[-1]

            self.editprofile.setRowCount(9)
            #Column count
            self.editprofile.setColumnCount(2)
            keys = [
                "ID", "FULL NAME", "DEPARTMENT", "DESIGNATION", "EMAIL",
                "ADDRESS", "PHONE", "TASK", "WAGE"
            ]
            for i in range(len(keys)):
                # self.editprofile.setHorizontalHeaderLabels(keys)
                label = QLabel(keys[i])
                label.setStyleSheet(
                    "background-color: white;color: black ;border: 1px solid black"
                )
                self.editprofile.setCellWidget(i, 0, label)
                if keys[i] == "DESIGNATION":
                    self.box = QComboBox()
                    self.box.addItem("WEB DESIGNER")
                    self.box.addItem("FRONT-END DEVELPER")
                    self.box.addItem("BACK-END DEVELOPER")
                    self.box.addItem("SEO")
                    self.box.addItem("ANALYST")
                    self.box.addItem("MANAGER")

                    self.editprofile.setCellWidget(i, 1, self.box)
                self.editprofile.setItem(
                    i, 1, QtWidgets.QTableWidgetItem(str(person[i])))

            print(password)

    def editProfile(self):
        items = []
        for i in range(10):
            rowdata = ''
            item = self.editprofile.item(i, 1)
            # print(self.box.currentText(),"item box")
            if self.editprofile.item(i, 0) == "DESIGNATION":
                rowdata += self.box.currentText()
            if item and item.text:

                rowdata += item.text()
                items.append(rowdata)
            else:
                rowdata += "NULL"
        # print(items)
        cur = self.conn.cursor()
        emp = 'UPDATE empdat SET  position=?,department =?,email=?,address=?,phone=?,tasks=? WHERE name =\'' + self.name + "\'"
        cur.execute(
            emp, (items[2], items[3], items[4], items[5], items[6], items[7]))
        self.conn.commit()
# change passsword
    def change_pass(self):

        # print(conn)
        cur = self.conn.cursor()
        emp = 'SELECT password FROM empdat WHERE name =\'' + self.name + "\'"
        cur.execute(emp)
        password = cur.fetchone()[0]
        print(password)

        currentpassword = self.currentpass.text()
        newpass1 = self.newpass1.text()
        newpass2 = self.newpass2.text()
        print(newpass2)
        if len(currentpassword) == 0 or len(newpass1) == 0 or len(
                newpass2) == 0:
            self.emptyerror.setText(" ! Please inputs all fields.")
        else:
            self.emptyerror.setText("")
            if currentpassword != password:
                self.incorrectpass.setText("! Incorrect Password")
                # print(currentpassword,"currentpassword")
            else:
                # self.incorrectpass.setStyleSheet("color: black; background-color:green; font:15px bold align=center")
                self.correctpass.setText("✔")
                if newpass1 != newpass2 or len(newpass1) == 0:
                    self.unmatchedpassword.setText(" ! Passowrds do not match")
                    print("error")
                else:
                    self.incorrectpass.setText("")
                    self.unmatchedpassword.setText("")
                    self.emptyerror.setText(" password changed .")
                    print("changed password succesfully")
                    print(newpass2)
                    # emp='SELECT password FROM empdat WHERE name =\''+self.name+"\'"
                    data = 'UPDATE empdat SET password =\'' + newpass2 + "\' WHERE name =\'" + self.name + "\'"
                    cur.execute(data)
                    self.conn.commit()

    # def candidates_info(self):
    #     print("i have reached candidate info")
        
    #     Hrcandidate()    
    #     # widget.addWidget(a)
    #     # widget.setCurrentIndex(widget.currentIndex()+1)
    #     # widget.setFixedWidth(1230)
    #     # widget.setFixedHeight(700)
    # def employee_info(self):
        
    #     EMP_INFO()
    #     # widget = QtWidgets.QStackedWidget()
    #     # widget.addWidget(mainwindow2)
    #     # widget.setCurrentIndex(widget.currentIndex()+1)
    #     # widget.setFixedWidth(1230)
    #     # widget.setFixedHeight(700)
    #     # widget.show()
        
    def assigntask(self):
        print("assigntask")
