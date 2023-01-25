import sys
# import os.path

# CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

from PyQt5 import  QtWidgets , QtGui,Qt,QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from datetime import datetime, date
import random
from docxtpl import DocxTemplate #to make a word file
from docx2pdf import convert #to converr into pdf (pip install docx2pdf)
from pdf2image import convert_from_path #to convert into image from pdf (pip install pdf2image, downlode Poppler for Windows)
import os #to remove unwanted file
import sqlite3
class emp_dashboard(QDialog):
    def __init__(self, name):
        self.name = name
        self.board = "/home/maira/Desktop/PROJECT -/employee.ui"
        super().__init__()
        loadUi(self.board, self)
        self.logo = QLabel()
        self.logo.setGeometry(0, 0, 218, 69)
        self.logo.setPixmap(QPixmap("/home/maira/Desktop/PROJECT -/logo.png"))
        self.placeholder.setPixmap(QPixmap("/home/maira/Desktop/PROJECT -/placeholder.png"))
        self.placeholder2.setPixmap(QPixmap("/home/maira/Desktop/PROJECT -/placeholder.png"))
        
        self.loaddata(self.name)
        self.currentpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newpass1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newpass2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.savepassword.clicked.connect(self.change_pass)
        self.saveinfo.clicked.connect(self.editProfile)
        self.upload.clicked.connect(self.uploadPic)
        self.logout.clicked.connect(self.log_out)
        # self.candidate_info.clicked.connect(self.candidates_info)
        self.generatepayslip.clicked.connect(self.payslip)
        self.tasks.clicked.connect(self.task)
        # self.emp_performance.clicked.connect(self.employee_performance)
        print(self.board)
    def uploadPic(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            "/home/maira/Pictures/",
                                            'Images(*.png)')
        self.filename.setText(fname[0])
        self.image = fname[0]
        self.placeholder.setPixmap(QPixmap(self.image))
        self.placeholder2.setPixmap(QPixmap(self.image))
        
    def loaddata(self, name):
        self.conn = sqlite3.connect("empdata.db")
        cur = self.conn.cursor()
        sqlquery = 'SELECT  id,name,department,position,email,address,phone,tasks,wage,about ,image FROM empdat WHERE name =\'' + name + "\'"
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
            self.ABOUTME.setText(" \t\tABOUT ME \n" + about)
            image =person[10]
            print(image)
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
            # self.editprofile.setVerticalHeaderLabels(keys)
            for i in range(len(keys)):
                # 
                label = QLabel(keys[i])
                
                label.setStyleSheet(
                    "color:rgb(0,0,0) ;background-color: rrgb(255, 197, 98) ;border: 1px solid black"
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

    def editProfile(self):
        self.items=[]
        for i in range(self.editprofile.rowCount()):
            
            id=self.editprofile.item(0, 1).text()
            item = self.editprofile.item(i, 1)
            rowdata=""
            if i== 3:
                # box=self.box.currentText()
                rowdata+=self.box.currentText()
            elif item.text():
                
                rowdata += item.text()
                
            else:
                rowdata += "NULL"
            print(rowdata,i)
            self.items.append(rowdata)
        if self.filename.text() == "":
            self.items.append("/home/maira/Desktop/PROJECT -/placeholder.png")
        else:
            self.items.append(self.filename.text())
        print(self.items)
        conn = sqlite3.connect("empdata.db")
        cur = conn.cursor()
        emp = 'UPDATE empdat SET  department =?,position=?,email=?,address=?,phone=?,image=? WHERE name =\'' + self.name + "\'"
        cur.execute(
            emp, (self.items[2],self.items[3],self.items[4],self.items[5],self.items[6],self.items[-1]))
        conn.commit()
        print("committed changes")
        conn.close()
        self.loaddata(self.name)
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
                self.correctpass.setStyleSheet("color: red")
                self.correctpass.setText("X")

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
                    self.conn.close()

    def save_info(self):
        conn = sqlite3.connect("empdata.db")
        cur = conn.cursor()
        # 'UPDATE tasks SET Task =?,StartDate=?,EndDate=?,status=?,tasks=? WHERE EmployeeName =\''+namee+"\'"
        sqlquery = 'UPDATE tasks SET status=?  WHERE EmployeeName =\'' + self.name + "\'"
        a=self.box.currentText()
        cur.execute(sqlquery,[a])
        conn.commit()
        conn.close()
    def log_out(self):
        # self.close()
        self.saveinfo()
        print("EMP_INFO")
        a=LOGOUT_emp(self.name)
        
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(640)
        widget.setFixedHeight(400)   
        # a.move(100,100)
        # a.setWindowModality(Qt.ApplicationModal)
        widget.setWindowTitle("log out")
    def my_profile(self):
        self.save_info()
        emppf=emp_dashboard(self.name)
        widget.addWidget(emppf)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)  
    def task(self):

        print("assigntask")
        # self.close()
        a=employee_tasks(self.name)
        
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)

    def payslip(self):
        self.close
        print("im here")
        emppf=employee_slip(self.name)
        widget.addWidget(emppf)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)

    
    def log_out(self):
        # self.close()
        print("EMP_INFO")
        a=LOGOUT_emp(self.name)
        
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(640)
        widget.setFixedHeight(400)   
        # a.move(100,100)
        # a.setWindowModality(Qt.ApplicationModal)
        widget.setWindowTitle("log out")

        print("logged-out")
class LOGOUT_emp(QDialog):
    def __init__(self,name):
        self.name=name
        super().__init__()
        loadUi("logout.ui",self)
        self.yes.clicked.connect(self.yess)
        self.no.clicked.connect(self.noo)
    def noo(self):
        emppf=emp_dashboard(self.name)
        widget.addWidget(emppf)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)
        print("profile")
    # def yess(self):
    #     emppf=page()
    #     widget.addWidget(emppf)
    #     widget.setCurrentIndex(widget.currentIndex()+1)
    #     widget.setFixedWidth(1230)
    #     widget.setFixedHeight(700)
        print("logged out")
class employee_slip(QDialog):
    def __init__(self,userloggedin):
        super().__init__()
        self.user=userloggedin
        loadUi("emp_slip.ui",self)
        self.load(self.user)
        self.save.clicked.connect(self.creating)
        self.myprofile.clicked.connect(self.my_profile)
        self.logout.clicked.connect(self.log_out)
        self.tasks.clicked.connect(self.task)

    def load(self,name):

        self.nameline.setText(name)

        conn=sqlite3.connect("empdata.db")
        # print(conn)
        cur=conn.cursor()
        emp='SELECT position,wage,tasks,loan FROM empdat WHERE name =\''+self.user+"\'"
        for logg in cur.execute(emp):
            print("yessssss32",logg)
        cur.close()
        self.basic=logg[1]
        tasks=logg[2]
        if logg[3] == None:
            loan=0
        else:
            loan=logg[3]
        self.designation.setText(logg[0])
        self.today = date.today()
        self.Date.setText(str(self.today))
        if tasks <4:
            self.bonus1=2000
            self.bonus.setText(str(self.bonus1))
        elif 7 > tasks >=4 :
            self.bonus1=6000
            self.bonus.setText(str(self.bonus1))
        else:
            self.bonus1=10000
            self.bonus.setText(str(self.bonus1))
        self.salary.setText(str(self.basic))
        self.loan.setText(str(loan))
        tax=0.03*logg[1]
        self.tax.setText(str(tax))
        self.pf.setText(str(5000))
        self.internet.setText(str(2000))
        self.conveyance.setText(str(15000))
        self.total_add=self.basic+self.bonus1+2000+15000
        self.total_ded=loan+tax+5000
        self.totalearn.setText(str(self.total_add))
        self.totalded.setText(str(self.total_ded))
        print(int(self.loan.text()))
        self.netsalary.setText(str(self.total_add+self.total_ded))
        #  nae hoga ese 

        conn.commit()
    def log_out(self):
        a=LOGOUT_emp(self.user)
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(640)
        widget.setFixedHeight(400)   
        # a.move(100,100)
        # a.setWindowModality(Qt.ApplicationModal)
        widget.setWindowTitle("log out")
    def my_profile(self):
        self.close()
        emppf=emp_dashboard(self.user)
        widget.addWidget(emppf)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)
    def task(self):
        print("assigntask")
        # self.close()
        a=employee_tasks(self.user)
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)
    def creating(self):
        self.downloaded.setText("DOwnloaded")
        self.service=self.designation.text()
        # date=self.today
        self.inter1=self.internet.text()

        #making word file
        now =datetime.now()
        date=f'{now.day}/{now.month}/{now.year}'
        filename=f'salaryslip#{random.randint(100,999)}.docx'

        doc=DocxTemplate('salarysliptemp.docx')
        context={'Emp_name':self.user,
        'Emp_service':self.service,
        'slip_date':date,
        'basic':self.basic,
        'bonus1':self.bonus1,
        'inter1':self.inter1,
        'conv':self.conveyance.text(),
        'loan1':self.loan.text(),
        'fund1':self.pf.text(),
        'tax1':self.tax.text(),
        'total_add':self.total_add,
        'total__ded':self.total_ded,
        'total1':self.netsalary.text()
        }
        doc.render(context)
        doc.save(filename) 
        
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
        self.save.clicked.connect(self.savestat)
        self.generatepayslip.clicked.connect(self.payslip)
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
        self.conn.close()
    

    def savestat(self):
        self.saved.setText("SAVED")
        print("im here")
        con=sqlite3.connect("empdata.db")
        cur=con.cursor()
        a=self.box.currentText()
        query='Update tasks Set status=\''+a+"\'" ' where EmployeeName=\'' + self.name + "\'"
        cur.execute(query)
        con.commit()
        con.close()
    def log_out(self):
        a=LOGOUT_emp(self.name)
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(640)
        widget.setFixedHeight(400)   
        # a.move(100,100)
        # a.setWindowModality(Qt.ApplicationModal)
        widget.setWindowTitle("log out")
    def payslip(self):
        self.close()
        emppf=employee_slip(self.name)
        widget.addWidget(emppf)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)
    def my_profile(self):
        self.close()
        emppf=emp_dashboard(self.name)
        widget.addWidget(emppf)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)

a=QApplication(sys.argv)
mainwindow=emp_dashboard("abdullah")
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1230)
widget.setFixedHeight(700)
widget.show()
a.exec_()