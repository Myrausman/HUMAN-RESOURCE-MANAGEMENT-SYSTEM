import sys
# import os.path

# CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

from PyQt5 import  QtWidgets , QtGui,QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import QUrl
from PyQt5.QtWebKitWidgets import QWebView , QWebPage
from PyQt5.QtWebKit import QWebSettings
from PyQt5.QtNetwork import *
import qpageview
import sqlite3
class hr_dashboard(QDialog):
    def __init__(self, name):
        self.name = name
        self.board = "/home/maira/Desktop/PROJECT -/hr_dashboard.ui"

        super().__init__()
        loadUi(self.board, self)
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
        self.candidate_info.clicked.connect(self.candidates_info)
        self.empinfo.clicked.connect(self.employee_info)
        self.assigntask.clicked.connect(self.assign_task)
        self.emp_performance.clicked.connect(self.employee_performance)
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

        cur = self.conn.cursor()
        sqlquery = 'SELECT  id,name,department,position,email,address,phone,tasks,wage,about ,image FROM empdat WHERE name =\'' + name + "\'"

        # print(name)
        # path = "/home/maira/Desktop/PROJECT -/"
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
            for i in range(len(keys)):
                # self.editprofile.setHorizontalHeaderLabels(keys)
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

            print(password)

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

    def candidates_info(self):
        print("i have reached candidate info")
        
        a=Hrcandidate(self.name)
        # widget=QtWidgets.QStackedWidget()
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)
    def employee_info(self):
        print("EMP_INFO")
        a=EMP_INFO(self.name)
        
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)        
    def assign_task(self):

        print("assigntask")
        # self.close()
        a=assign_task(self.name)
        
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)

    def employee_performance(self):

        print("assigntask")
        # self.close()
        a=performance(self.name)
        
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)

    
    def log_out(self):
        # self.close()
        print("EMP_INFO")
        a=LOGOUT(self.name)
        
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(640)
        widget.setFixedHeight(400)   
        
        print("logged-out")

class LOGOUT(QDialog):
    def __init__(self,name):
        self.name=name
        super().__init__()
        loadUi("logout.ui",self)
        self.yes.clicked.connect(self.yess)
        self.no.clicked.connect(self.noo)
    def noo(self):
        emppf=hr_dashboard(self.name)
        widget.addWidget(emppf)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)
        print("profile")
    def yess(self):
        self.close()
        sys.exit(0)
        print("logged out")

class EMP_INFO(QDialog):
    def __init__(self,name):
        self.name=name
        super().__init__()
        print("EMP INFO CLASS")
        loadUi("emp_recordes(hr).ui",self)
        self.logo=QLabel()
        self.logo.setGeometry(0,0,218,69)
        self.logo.setPixmap(QPixmap("logo.png"))
        #buttons menu
        
        self.myprofile.clicked.connect(self.my_profile)
        self.logout.clicked.connect(self.log_out)
        self.candidate_info.clicked.connect(self.candidates_info)
        self.emp_performance.clicked.connect(self.employee_performance)
        self.assigntask.clicked.connect(self.assign_task)

        #buttons functions
        self.addemp.clicked.connect(self.add_employee)
        self.delemp.clicked.connect(self.del_employee)
        self.updemp.clicked.connect(self.update_info)

        
        conn = sqlite3.connect("empdata.db")
        cur = conn.cursor()
        sqlquery = 'SELECT   id,name,department,position,email,address,phone,image,tasks,wage FROM empdat'
        self.employeeTable.setHorizontalHeaderLabels(["ID","NAME","DEPARTMENT","DESIGNATION","E-MAIL","ADDRESS","PHONE","IMAGE","TASKS","WAGE","SALARY"])
        count=0
        self.employeeTable.setColumnCount(10)
        # self.employeeTable.setRowCount(count)
        tablerow=0
        for person in cur.execute(sqlquery):
            
            for i in range(len(person)):
                self.employeeTable.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(person[i])))
            self.image=QLabel()
            self.image.setPixmap(QPixmap(person[7]))
            self.image.setScaledContents(True)         
            self.employeeTable.setCellWidget(tablerow, 7, self.image)
            tablerow+=1
        self.employeeTable.setRowCount(tablerow)
        self.employeeTable.setRowHeight(20,50)
        
        conn.close()
    def update_info(self):
        print("updating info")
        conn = sqlite3.connect("empdata.db")
        cur=conn.cursor()
        for i in range(self.employeeTable.rowCount()):
            name=self.employeeTable.item(i,1).text()
            department=self.employeeTable.item(i,2).text()
            position=self.employeeTable.item(i,3).text()
            email=self.employeeTable.item(i,4).text()
            address=self.employeeTable.item(i,5).text()
            phone=self.employeeTable.item(i,6).text()
            # image=self.tableWidget.item(i,7).text()
            tasks=self.employeeTable.item(i,8).text()
            wage=self.employeeTable.item(i,9).text()
            q=[department,position,email,address,phone,tasks,wage]
            emp = "UPDATE empdat SET  department =?,position=?,email=?,address=?,phone=?,tasks=?,wage=?  WHERE name=\'"+name+ "\'"
            cur.execute(emp,q)
        conn.commit()
        conn.close()


    def my_profile(self):
        self.close()
        emppf=hr_dashboard(self.name)
        widget.addWidget(emppf)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)
    def candidates_info(self):
        print("i have reached candidate info")
        self.close()
        a=Hrcandidate(self.name)
        # widget=QtWidgets.QStackedWidget()
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)
    def assign_task(self):
        print("assigntask")
        # self.close()
        a=assign_task(self.name)
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)
    def employee_performance(self):

        print("assigntask")
        # self.close()
        a=performance(self.name)
        
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)
    def log_out(self):
        # self.close()
        print("EMP_INFO")
        a=LOGOUT(self.name)
        
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(640)
        widget.setFixedHeight(400)   
        
        print("logged-out")
        
        print("logged-out")
    def delete_employee(self):
        print("add employee")
    def update_employee(self):
        print("add employee")
    def add_employee(self):
        # self.close()
        a=ADD_EMPLOYEE(self.name)
        # widget=QtWidgets.QStackedWidget()
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)
        print("add employee")
    def del_employee(self):
        # self.close()
        a=DEL_EMPLOYEE(self.name)
        # widget=QtWidgets.QStackedWidget()
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)
        print("add employee")

class ADD_EMPLOYEE(QDialog):
    def __init__(self,name):
        self.name=name
        super().__init__()
        loadUi("addemployee.ui",self)
        self.save.clicked.connect(self.saveinfo)
        self.upload.clicked.connect(self.uploadPic)
        self.backbutton.clicked.connect(self.backloginnn)
        self.box = QComboBox()
        self.box.addItem("WEB DESIGNER")
        self.box.addItem("FRONT-END DEVELPER")
        self.box.addItem("BACK-END DEVELOPER")
        self.box.addItem("SEO")
        self.box.addItem("ANALYST")
        self.box.addItem("MANAGER")
        self.tableWidget.setCellWidget(3, 0, self.box)
    def saveinfo(self):
        self.conn=sqlite3.connect("empdata.db")
        self.newname=self.tableWidget.item(1, 0).text()
        print(self.newname)
        self.items=[]
        for i in range(self.tableWidget.rowCount()):
            
            id=self.tableWidget.item(0, 0).text()
            item = self.tableWidget.item(i, 0)
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
        if self.image == None:
            self.image="/home/maira/Desktop/PROJECT -/placeholder.png"
        self.items.append(self.image)
        self.items.append("12345678")
        print(self.items)
        conn=sqlite3.connect("empdata.db")
        cur=conn.cursor()
        cur.execute('INSERT INTO empdat (id , name , department,position,email,address,phone,wage,image,password) VALUES (?,?,?,?,?,?,?,?,?,?)',self.items)
        cur=conn.cursor()
        conn.commit()
        conn.close()

    def uploadPic(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            "/home/maira/Pictures/",
                                            'Images(*.png)')
        self.filename.setText(fname[0])
        self.image = fname[0]
        # conn=sqlite3.connect("empdata.db")
        self.placeholder.setPixmap(QPixmap(self.image))
    def backloginnn(self):
        a=EMP_INFO(self.name)
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
class DEL_EMPLOYEE(QDialog):
    def __init__(self,user):
        self.user=user
        super().__init__()
        loadUi("delete_emp.ui",self)
        # name=self.nameline.text()
        self.delete_2.clicked.connect(self.delete_emp)
        self.backbutton.clicked.connect(self.backloginnn)
    def backloginnn(self):
        a=EMP_INFO(self.user)
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def delete_emp(self):
        self.deleted.setText("Employee Deleted")
        con=sqlite3.connect("empdata.db")
        cur=con.cursor()
        sql="DELETE FROM empdat WHERE name=\'"+self.nameline.text()+"\'"
        cur.execute(sql)
        con.commit()
        con.close()
class Hrcandidate(QDialog):
    def __init__(self,name):
        super().__init__()
        self.name=name
        loadUi("/home/maira/Desktop/PROJECT -/candidates.ui",self)
        self.myprofile.clicked.connect(self.my_profile)
        self.logo=QLabel()
        self.logo.setGeometry(0,0,218,69)
        self.logo.setPixmap(QPixmap("logo.png"))
        self.updatelist.clicked.connect(self.update_list)
        #buttons menu
        self.myprofile.clicked.connect(self.my_profile)
        self.logout.clicked.connect(self.log_out)
        self.emp_performance.clicked.connect(self.employee_performance)
        # self.candidate_info.clicked.connect(self.candidates_info)
        self.empinfo.clicked.connect(self.employee_info)
        self.assigntask.clicked.connect(self.assign_task)
        self.conn= sqlite3.connect("empdata.db")
        cur = self.conn.cursor()
        sqlquery = 'SELECT  * FROM candi'
        self.tableWidget.setHorizontalHeaderLabels(["FIRST NAME","LAST NAME","CNIC","CONTACT NO.","GENDER","ADDRESS","QUALIFICATION","Resume","SELECT"])
        self.tableWidget.setColumnCount(9)
        tablerow=0
        for person in cur.execute(sqlquery):
            for i in range(len(person)):
                self.tableWidget.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(person[i])))
            item = QtWidgets.QTableWidgetItem('Select')
            item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.tableWidget.setItem(tablerow, 7, item)
            tablerow+=1
        self.count=0
        self.tableWidget.setRowCount(tablerow)
        self.tableWidget.setEditTriggers(
                QtWidgets.QAbstractItemView.NoEditTriggers)
        self.conn.close()
    def update_list(self):
        self.update.setText("Updated!")
        print("updating")
        # print(self.tableWidget.rowCount())
        con=sqlite3.connect("empdata.db")
        cur=con.cursor()
        items=[]
        for i in range (self.tableWidget.rowCount()):
            print(self.tableWidget.item(0,i).text(),"in for loop")
            if self.tableWidget.item(i,7).checkState() != QtCore.Qt.Checked:
                print("i have come here in if")
                print(self.tableWidget.item(i,0).text())
                name=self.tableWidget.item(i,0).text()
                items.append(name)
                sql="DELETE FROM Candi WHERE FirstName=\'"+name+"\'"
                cur.execute(sql)
        con.commit()
        con.close()
        print("closed")
        self.conn= sqlite3.connect("empdata.db")
        cur = self.conn.cursor()
        sqlquery = 'SELECT  * FROM candi'
        self.tableWidget.setHorizontalHeaderLabels(["FIRST NAME","LAST NAME","CNIC","CONTACT NO.","GENDER","ADDRESS","QUALIFICATION","Resume","SELECT"])
        self.tableWidget.setColumnCount(9)
        tablerow=0
        for person in cur.execute(sqlquery):
            for i in range(len(person)):
                # if i == 7:
                self.tableWidget.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(person[i])))
            item = QtWidgets.QTableWidgetItem('Select')
            item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.tableWidget.setItem(tablerow, 7, item)
            tablerow+=1
        self.count=0
        self.tableWidget.setRowCount(tablerow)
        self.tableWidget.setEditTriggers(
                QtWidgets.QAbstractItemView.NoEditTriggers)
        self.conn.close()
                

                




    def my_profile(self):
        emppf=hr_dashboard(self.name)
        widget.addWidget(emppf)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)
        print("profile")
    def employee_info(self):
        print("EMP_INFO")
        a=EMP_INFO(self.name)
        
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)
    def assign_task(self):

        print("assigntask")
        self.close()
        a=assign_task(self.name)
        
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)
    def employee_performance(self):

        print("assigntask")
        # self.close()
        a=performance(self.name)
        
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)
    def log_out(self):
        self.close()
        print("EMP_INFO")
        a=LOGOUT(self.name)
        
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(640)
        widget.setFixedHeight(400)   
        
        print("logged-out")
class assign_task(QDialog):
    def __init__(self,name):
        self.name=name
        super(assign_task, self).__init__()
        loadUi("assigntask1.ui",self)
        
        #buttons menu
        self.myprofile.clicked.connect(self.my_profile)
        self.logout.clicked.connect(self.log_out)
        self.candidate_info.clicked.connect(self.candidates_info)
        self.empinfo.clicked.connect(self.employee_info)
        self.emp_performance.clicked.connect(self.employee_performance)
        # self.assigntask.clicked.connect(self.assign_task)

        self.loaddata()
        self.assign1button.clicked.connect(self.AssignTask)
    def AssignTask(self):
        a=assign2(self.name)
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def loaddata(self):
        conn=sqlite3.connect("empdata.db")
        cur=conn.cursor()
        q= 'SELECT * FROM tasks'
        cur.execute(q)
        self.tableWidget.setRowCount(50)
        t=0
        for row in cur.execute(q):
            print(row)
            self.tableWidget.setItem(t,0,QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(t,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tableWidget.setItem(t,2,QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(t,3,QtWidgets.QTableWidgetItem(row[3]))
            self.tableWidget.setItem(t,4,QtWidgets.QTableWidgetItem(row[4]))
            self.tableWidget.setItem(t,5,QtWidgets.QTableWidgetItem(str(row[5])))
            t=+1
    def my_profile(self):
        emppf=hr_dashboard(self.name)
        widget.addWidget(emppf)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)
        print("profile")
    def candidates_info(self):
        print("i have reached candidate info")
        
        a=Hrcandidate(self.name)
        # widget=QtWidgets.QStackedWidget()
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)
    def employee_info(self):
        print("EMP_INFO")
        a=EMP_INFO(self.name)
        
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)
    def employee_performance(self):

        print("assigntask")
        # self.close()
        a=performance(self.name)
        
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)
    def log_out(self):
        # self.close()
        print("EMP_INFO")
        a=LOGOUT(self.name)
        
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(640)
        widget.setFixedHeight(400)   
        
        print("logged-out")
class assign2(QDialog):
    def __init__(self,name):
        super(assign2, self).__init__()
        self.name=name
        loadUi("assigntask2.ui",self)
        self.backbutton.clicked.connect(self.backloginnn)
        self.assignbutton.clicked.connect(self.tas)
    def backloginnn(self):
        a=assign_task(self.name)
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def tas(self):
        c=assigntk2(self.name)
        widget.addWidget(c)
        widget.setCurrentIndex(widget.currentIndex()+1)
        conn=sqlite3.connect("empdata.db")
        cur=conn.cursor()
        namee=self.name.text()
        print(namee)
        tsk=self.task.text()
        sdate=self.startdate.text()
        edate=self.enddate.text()
        num=self.num.text()
        b="working"
        data='UPDATE tasks SET Task =\''+tsk+"\' WHERE EmployeeName =\'"+namee+"\'" 
        data1='UPDATE tasks SET StartDate =\''+sdate+"\' WHERE EmployeeName =\'"+namee+"\'" 
        data2='UPDATE tasks SET EndDate =\''+edate+"\' WHERE EmployeeName =\'"+namee+"\'" 
        data3='UPDATE tasks SET status =\''+b+"\' WHERE EmployeeName =\'"+namee+"\'" 
        data4='UPDATE tasks SET tasks =\''+num+"\' WHERE EmployeeName =\'"+namee+"\'" 

        cur.execute(data)
        cur.execute(data1)
        cur.execute(data2)
        cur.execute(data3)
        cur.execute(data4)
        conn.commit()
        conn.close()
class assigntk2(QDialog):
    def __init__(self,name):
        super(assigntk2, self).__init__()
        self.name=name
        loadUi("assigntask2.ui",self)
        self.backbutton.clicked.connect(self.backloginnn)
        self.assignbutton.clicked.connect(self.tas)
    def backloginnn(self):
        a=assign_task(self.name)
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def tas(self):
        c=assign2(self.name)
        widget.addWidget(c)
        widget.setCurrentIndex(widget.currentIndex()+1)
        conn=sqlite3.connect("empdata.db")
        cur=conn.cursor()
        namee=self.name.text()
        print(namee)
        tsk=self.task.text()
        sdate=self.startdate.text()
        edate=self.enddate.text()
        num=self.num.text()
        b="working"
        query='UPDATE tasks SET Task =?,StartDate=?,EndDate=?,status=?,TaskNumber=? WHERE EmployeeName =\''+namee+"\'"
        # data='UPDATE tasks SET Task =\''+tsk+"\' WHERE EmployeeName =\'"+namee+"\'" 
        # data1='UPDATE tasks SET StartDate =\''+sdate+"\' WHERE EmployeeName =\'"+namee+"\'" 
        # data2='UPDATE tasks SET EndDate =\''+edate+"\' WHERE EmployeeName =\'"+namee+"\'" 
        # data3='UPDATE tasks SET status =\''+b+"\' WHERE EmployeeName =\'"+namee+"\'" 
        # data4='UPDATE tasks SET tasks =\''+num+"\' WHERE EmployeeName =\'"+namee+"\'" 

        cur.execute(query,(tsk,sdate,edate,b,num))
        # cur.execute(data1)
        # cur.execute(data2)
        # cur.execute(data3)
        # cur.execute(data4)
        conn.commit()
        conn.close()

class performance(QDialog):
    def __init__(self,name):
        super(performance, self).__init__()
        self.name=name
        loadUi("PERFOMANCE.ui",self)
        self.save.clicked.connect(self.errorr)
        self.myprofile.clicked.connect(self.my_profile)
        self.logout.clicked.connect(self.log_out)
        self.candidate_info.clicked.connect(self.candidates_info)
        self.empinfo.clicked.connect(self.employee_info)
        self.assigntask.clicked.connect(self.assign_task)
        #self.errorr()
        self.loaddata()
    def loaddata(self):
        conn=sqlite3.connect("empdata.db")
        cur=conn.cursor()
        q= 'SELECT  id,name FROM empdat'
        cur.execute(q)
        self.tableWidget.setRowCount(50)
        t=0
        for row in cur.execute(q):
            print(row)
            self.tableWidget.setItem(t,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(t,1,QtWidgets.QTableWidgetItem(str(row[1])))
            # self.tableWidget.setItem(t,2,QtWidgets.QTableWidgetItem(row[2]))
            # self.tableWidget.setItem(t,3,QtWidgets.QTableWidgetItem(row[3]))
            # self.tableWidget.setItem(t,4,QtWidgets.QTableWidgetItem(row[4]))
            # self.tableWidget.setItem(t,5,QtWidgets.QTableWidgetItem(str(row[5])))
            t=+1
        # n=[self.tableWidget.item(row,2).text for row in range(self.tableWidget.rowCount())]
        # r=[self.tableWidget.item(row,3).text for row in range(self.tableWidget.rowCount())]
        # print(n)
        conn=sqlite3.connect("empdata.db")
        cur=conn.cursor()
        #data='UPDATE tasks SET Task =\''+n+"\' WHERE EmployeeName =\'"+namee+"\'"
        #cur.execute('INSERT INTO empdat(reviewdate,rating)''VALUES('%s','%s')'%(''.join(name),''.join(email)))
        #print("dta inserted")

    def errorr(self):
        self.error.setText("successfully saved info")
        rc=self.tableWidget.rowCount()
        columnCount=self.tableWidget.columnCount()
        print(columnCount) 
        for row in range(2):
            r=""
            for column in range(columnCount):
                widgetItem=self.tableWidget.item(row,column)
                if (widgetItem and widgetItem.text ):
                    r=r+' - '+widgetItem.text() 
                else:
                    r=r+' - '+'NULL'
            print(r+'\n')
        for row in range (2):
            r1=self.tableWidget.item(row,1).text()
            #r2=self.tableWidget.item(row,0).text()
            r3=self.tableWidget.item(row,2).text()
            #print("yyyyyyyyyyyyyyyyyyy",n)
            r4=self.tableWidget.item(row,3).text()
            print(r4)
            conn=sqlite3.connect("empdata.db")
            cur=conn.cursor()
            
            
            #q=[n,r]
            #cur.execute('INSERT INTO empdat (reviewdate,rating)VALUES(?,?)',q)
            print("haaaaaaaaaaaaaaaaaaaaaaaaa")
            data1='UPDATE empdat SET reviewdate=\''+r3+"\' WHERE name=\'"+r1+"\'"  
            data2='UPDATE empdat SET rating=\''+r4+"\' WHERE name=\'"+r1+"\'"  
            #data1='UPDATE empdat SET reviewdate=\''+n+"\' WHERE rating=\'"+r+"\'"  

            cur.execute(data1)
            cur.execute(data2)
            
            conn.commit()
            conn.close()
    def my_profile(self):
        emppf=hr_dashboard(self.name)
        widget.addWidget(emppf)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)
        print("profile")
    def candidates_info(self):
        print("i have reached candidate info")
        
        a=Hrcandidate(self.name)
        # widget=QtWidgets.QStackedWidget()
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)
    def employee_info(self):
        print("EMP_INFO")
        a=EMP_INFO(self.name)
        
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)
    def log_out(self):
        # self.close()
        print("EMP_INFO")
        a=LOGOUT(self.name)
        
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(640)
        widget.setFixedHeight(400)   
    def assign_task(self):

        print("assigntask")
        self.close()
        a=assign_task(self.name)
        
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)


a=QApplication(sys.argv)
mainwindow=hr_dashboard("Maira Usman")
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1230)
widget.setFixedHeight(700)
widget.show()
a.exec_()