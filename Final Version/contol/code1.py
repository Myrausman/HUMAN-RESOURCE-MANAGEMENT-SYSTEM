import sys
from datetime import date
from PyQt5 import QtCore, QtGui, QtWidgets,Qt,QtCore
from PyQt5 import  QtWidgets , QtGui
from PyQt5.QtGui import *
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from datetime import datetime, date
import random
from docxtpl import DocxTemplate #to make a word file
import sqlite3

############################################## LOGIN ###############################################################
class page(QDialog):#mainpage hai ye
    def __init__(self):
        super( page,self).__init__()
        loadUi("main.ui",self)
        # self.label = QLabel()
        self.label.setStyleSheet("background-color:rgb(0,0,0)")
        self.label.setGeometry(0,130, 481, 151)
        
        self.label.setPixmap(QPixmap("logo.png"))
        self.HRButton.clicked.connect(self.loginn)
        self.reghereButton.clicked.connect(self.reg)
        
    def reg(self):
        c=registration()
        widget.addWidget(c)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(511)
        widget.setFixedHeight(621)  
    def loginn(self):
        createac=login()
        widget.addWidget(createac)
        widget.setCurrentIndex(widget.currentIndex()+1)
class login(QDialog):
    def __init__(self):
        super(login,self).__init__()
        loadUi("login.ui",self)
        self.label.setStyleSheet("background-color:rgb(0,0,0)")
        self.label.setGeometry(0,55, 481, 111)
        self.label.setPixmap(QPixmap("logo.png"))
        self.backbutton.clicked.connect(self.backloginnn)
        self.logbutton.clicked.connect(self.emploginfunc)#login btton click hu take me to this function
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)#password hide
        #self.createaccount.clicked.connect(self.gotcreate)
    
    def backloginnn(self):
        a=page()
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def emploginfunc(self):
        user=self.user.text() #desginer me jo hum likh raye wo yahwn connect hoga
        password= (self.password.text())
        #ass=int(password)
        
        if len(user)==0 or len(password)==0:
            self.erroremp.setText("Please inputs all fields.")
            
        else:
            
            
            conn=sqlite3.connect("empdata.db")
            # print(conn)
            cur=conn.cursor()
            
            emp='SELECT name,password ,department FROM empdat WHERE name =\''+user+"\'"
            a=cur.execute(emp)
            print([ i for i in a])
            print("password enter",password)
            for logg in cur.execute(emp):
                print("successfullyd login with an email",user,"password=",password)
                print(user,"user") 
                print(logg)
                namer=logg[0]
                print(logg[0])
                passcode=logg[1]
                departmentt=logg[2]
                print(namer,"name==",user,"   ",departmentt,"departmentt")
                print(password,"==",passcode)

                if passcode ==str(password):
                    if  str(namer).lower() ==str(user).lower() and departmentt.lower() =="finance": 
                        self.erroremp.setText("successfully logged in") 
                        print("i m in condition")
                        emppf=fin_dashboard(str(namer))
                        widget.addWidget(emppf)
                        widget.setCurrentIndex(widget.currentIndex()+1)
                        widget.setFixedWidth(1230)
                        widget.setFixedHeight(700)
                    elif passcode== password and namer.lower() == user.lower() and departmentt.lower() == "hr": 
                        print("i am in hr")
                        self.erroremp.setText("successfully logged in") 
                        
                        emppf=hr_dashboard(str(namer))
                        widget.addWidget(emppf)
                        widget.setCurrentIndex(widget.currentIndex()+1)
                        widget.setFixedWidth(1230)
                        widget.setFixedHeight(700)
                        
                    else:
                        print("i am in employee")
                        self.erroremp.setText("successfully logged in") 
                        
                        emppf=emp_dashboard(str(namer))
                        widget.addWidget(emppf)
                        widget.setCurrentIndex(widget.currentIndex()+1)
                        widget.setFixedWidth(1230)
                        widget.setFixedHeight(700)
            else:
                self.erroremp.setText("invalid password or username") 
###############################                  CANDIDATE REGISTRATION                    #########################################
class registration(QDialog):
    def __init__(self):
        super( registration,self).__init__()
        loadUi("candidatesreg.ui",self)
        self.backbutton.clicked.connect(self.backlogin)
        self.regbutton.clicked.connect(self.adddet)
        self.resetbutton.clicked.connect(self.res)
        # self.resetbutton.clicked.connect(self.adddet)
        self.genderbox.addItem("Male")
        self.genderbox.addItem("Female")
        self.resume.clicked.connect(self.resumee)
    def res(self):
        a=registration()
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(511)
        widget.setFixedHeight(621)  
    def backlogin(self):
        a=page()
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(480)
        widget.setFixedHeight(620)  
    def resumee(self):
        resume = QFileDialog.getOpenFileName(self, 'Open file',
                                            "/home/maira/Documents/",'(*.pdf)')
        self.resume.setText(resume[0])
        
    def adddet(self):
        # a=candidate_reset()
        # widget.addWidget(a)
        # widget.setCurrentIndex(widget.currentIndex()+1)
        firstname=self.firstname.text()
        lastname=self.lastname.text()
        cnic=self.cnic.text()
        phonenumber=self.number.text()
        gender=self.genderbox.currentText()
        address=self.address.text()
        qualifications=self.qualifications.text()
        resume=self.resume.text()
        
        if firstname == "" or lastname=="" or cnic=="" or phonenumber=="" or resume=="" or address =="" or qualifications =="":
            self.erroremp.setStyleSheet("color: rgb(255,0,0);background-color: rgb(46, 52, 54)")
            self.erroremp.setText("please input all fields")
        else:
            self.erroremp.setStyleSheet("color: green ;background-color: rgb(46, 52, 54)")
            self.erroremp.setText("registered")
            q=[firstname,lastname,cnic,phonenumber,gender,address,qualifications]
            if self.resume.text() == "":
                q.append("NO reusme")
            else:
                q.append(self.resume.text())
            print(q,"i am q")
            
            conn=sqlite3.connect("empdata.db")
            cur=conn.cursor()
            cur.execute('INSERT INTO Candi (Firstname,lastName,CNIC,ContactNumber,Gender,Address,Qualification,Resume) VALUES (?,?,?,?,?,?,?,?)',q)
        conn.commit()
        conn.close()


##############################################             EMPLOYEE             ####################################################
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
        self.save.setText("SAVED")
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
        # 'UPDATE tasks SET Task =?,StartDate=?,EndDate=?,status=?,TaskNumber
        # =? WHERE EmployeeName =\''+namee+"\'"
        sqlquery = 'UPDATE tasks SET status=?  WHERE EmployeeName =\'' + self.name + "\'"
        a=self.box.currentText()
        cur.execute(sqlquery,[a])
        conn.commit()
        conn.close()
    def log_out(self):
        # self.close()
        self.saveinfo()
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
    def yess(self):
        emppf=page()
        widget.addWidget(emppf)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(480)
        widget.setFixedHeight(620)
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
        # #converting into pdf
        # pdf_file=filename.replace('.docx',".pdf")
        # convert(filename)
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
        
        keys=["NAME","TASK no.","TASK","START-DATE","END-DATE","STATUS"]
        # for i in range(len(keys)):
        #     self.tableWidget.
        self.tableWidget.setStyleSheet("border-color: rgb(255, 197, 98);selection-color: rgb(136, 138, 133);color: rgb(0,0,0)")
        self.tableWidget.setVerticalHeaderLabels(keys)
        # self.tableWidget.VerticalHeaderDefaultSectionSize(250)
        self.loaddata()
    def loaddata(self):
        self.conn = sqlite3.connect("empdata.db")
        cur = self.conn.cursor()
        sqlquery = 'SELECT   EmployeeName,TaskNumber,Task,StartDate,EndDate,status FROM tasks WHERE EmployeeName =\'' + self.name + "\'"

        # print(name)
        # path = "/home/maira/Desktop/PROJECT -/"
        for person in cur.execute(sqlquery):
            print(person,"Taks table")
            # print(person[1])
            self.tableWidget.setRowCount(6)
            self.tableWidget.setColumnCount(1)
            
            for i in range(6):
                
                if str(person[i])== "":
                    label=QLabel("------------")
                else:
                    label=QLabel(str(person[i]))
                label.setAlignment(QtCore.Qt.AlignCenter)
                label.setStyleSheet(" color: rgb(0, 0, 0);background-color: rgb(233, 185, 110);")
                
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


#####################################               HR LOGIN            #####################################################
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
        print("name",name)
        sqlquery = "SELECT  id,name,department,position,email,address,phone,tasks,wage,about ,image FROM empdat WHERE name =\'" + name + "\'"

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
            if about is None:
                about=" "
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
        self.save.setText("SAVED")
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
        emppf=page()
        widget.addWidget(emppf)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(480)
        widget.setFixedHeight(620)
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
        self.updemp.clicked.connect(self.update_info)
        self.myprofile.clicked.connect(self.my_profile)
        self.logout.clicked.connect(self.log_out)
        self.candidate_info.clicked.connect(self.candidates_info)
        self.emp_performance.clicked.connect(self.employee_performance)
        self.assigntask.clicked.connect(self.assign_task)

        #buttons functions
        self.addemp.clicked.connect(self.add_employee)
        self.delemp.clicked.connect(self.del_employee)
        # self.updemp.clicked.connect(self.update_employee)
        
        conn = sqlite3.connect("empdata.db")
        cur = conn.cursor()
        sqlquery = 'SELECT   id,name,department,position,email,address,phone,image,tasks,wage FROM empdat'
        self.employeeTable.setHorizontalHeaderLabels(["ID","NAME","DEPARTMENT","DESIGNATION","E-MAIL","ADDRESS","PHONE","IMAGE","TASKS","WAGE","SALARY"])
        # self.count=0
        self.employeeTable.setColumnCount(11)
        # self.employeeTable.setRowCount(20)
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
        conn.close()
    def update_info(self):
        label=QLabel(self)
        label.setStyleSheet("color: rgb(138, 226, 52);font: 75 35pt bold")
        label.setGeometry(250,360,821,101)
        label.setAlignment(Qt.AlignCenter)
        label.setText("    Information Updated   ")
        # label.move(500,380)
        label.setFixedWidth(970)
        label.show()
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
        self.added.setText("Employee Added")
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
            self.tableWidget.setItem(tablerow, 8, item)
            tablerow+=1
        # self.count=0
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
            if self.tableWidget.item(i,8).checkState() != QtCore.Qt.Checked:
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
        self.tableWidget.setHorizontalHeaderLabels(["FIRST NAME","LAST NAME","CNIC","CONTACT NO.","GENDER","ADDRESS","QUALIFICATION","RESUME","SELECT"])
        self.tableWidget.setColumnCount(9)
        tablerow=0
        for person in cur.execute(sqlquery):
            print(person,"i am person of candidate info")
            for i in range(len(person)):
                self.tableWidget.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(person[i])))
            item = QtWidgets.QTableWidgetItem('Select')
            item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.tableWidget.setItem(tablerow, 8, item)
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
        widget.setWindowTitle("Assign TaskP")
        widget.setCurrentIndex(widget.currentIndex()+1)
    def loaddata(self):
        conn=sqlite3.connect("empdata.db")
        cur=conn.cursor()
        q= 'SELECT * FROM tasks'
        cur.execute(q)
        
        t=0
        for row in cur.execute(q):
            print(row)
            for i in range(6):
                self.tableWidget.setItem(
                    t, i, QtWidgets.QTableWidgetItem(str(row[i])))
                
            t+=1
        self.tableWidget.setRowCount(t)
        conn.close()
    def my_profile(self):
        emppf=hr_dashboard(self.name)
        widget.addWidget(emppf)
        widget.setWindowTitle("My Profile")
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)
        print("profile")
    def candidates_info(self):
        print("i have reached candidate info")
        
        a=Hrcandidate(self.name)
        # widget=QtWidgets.QStackedWidget()
        widget.addWidget(a)
        widget.setWindowTitle("Candidate Information")
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)
    def employee_info(self):
        print("EMP_INFO")
        a=EMP_INFO(self.name)
        
        widget.addWidget(a)
        widget.setWindowTitle("Employee information")
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)
    def employee_performance(self):

        print("assigntask")
        # self.close()
        a=performance(self.name)
        
        widget.addWidget(a)
        widget.setWindowTitle("Employee Performance")
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
        # self.assigned.clicked.connect(self.assigned)
    def backloginnn(self):
        a=assign_task(self.name)
        widget.addWidget(a)
        widget.setWindowTitle("Assign Task")
        widget.setCurrentIndex(widget.currentIndex()+1)
    def tas(self):
        
        conn=sqlite3.connect("empdata.db")
        cur=conn.cursor()
        emp= "SELECT name From empdat"
        
        namee=self.name.text()
        label=f"EMployee added {namee}"
        # label=f"Task Assigned to :{}",namee
        self.assigned.setText(label)
        tsk=self.task.text()
        sdate=self.startdate.text()
        edate=self.enddate.text()
        num=self.num.text()
        b="working"
        q=[namee,tsk,sdate,edate,b,num]
        a=[j for i in cur.execute(emp) for j in i]
        # print([j for i in cur.execute(emp) for j in i])
        conn.close()
        if namee not in a:
            self.error.setText("Employee doesnt exist")

            print(namee,"from assign task")
        
        
        else: 
            co=sqlite3.connect("empdata.db")
            cur=co.cursor()
            print(q,"q")
            data="INSERT INTO tasks (EmployeeName,Task,StartDate,EndDate,status,TaskNumber) VALUES (?,?,?,?,?,?)"
            
            
            print("data updating for tasks")
            cur.execute(data,q)
            co.commit()
            co.close()

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
            t+=1
        conn=sqlite3.connect("empdata.db")
        cur=conn.cursor()

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
        widget.setWindowTitle("My Profile")
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)
        print("profile")
    def candidates_info(self):
        print("i have reached candidate info",self.name)
        
        a=Hrcandidate(self.name)
        # widget=QtWidgets.QStackedWidget()
        widget.addWidget(a)
        widget.setWindowTitle("Candidates information")
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)
    def employee_info(self):
        print("EMP_INFO")
        a=EMP_INFO(self.name)
        
        widget.addWidget(a)
        widget.setWindowTitle("Employee information")
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
        widget.setWindowTitle("Assign Task")
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)

            ############################################ FINANCE LOGIN ######################################################

class fin_dashboard(QDialog):
    def __init__(self, name):
        
        super().__init__()
        self.user= name
        self.board = "financedashboard.ui"
        loadUi(self.board, self)
        self.logo = QLabel()
        self.logo.setGeometry(0, 0, 218, 69)
        self.logo.setPixmap(QPixmap("/home/maira/Desktop/PROJECT -/logo.png"))
        self.placeholder.setPixmap(QPixmap("/home/maira/Desktop/PROJECT -/placeholder.png"))
        self.placeholder2.setPixmap(QPixmap("/home/maira/Desktop/PROJECT -/placeholder.png"))
        
        self.loaddata(self.user)
        self.currentpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newpass1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newpass2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.savepassword.clicked.connect(self.change_pass)
        self.saveinfo.clicked.connect(self.editProfile)
        self.upload.clicked.connect(self.uploadPic)
        self.logout.clicked.connect(self.log_out)
        # self.generatepayslip.clicked.connect(self.GENERATE)

        self.empinfo.clicked.connect(self.employee_info)
        self.generatepayslip.clicked.connect(self.GENERATE)
        self.logout.clicked.connect(self.log_out)
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
            self.ABOUTME.setStyleSheet("color:rgb(0,0,0); font:20pt bold")
            self.ABOUTME.setText(" \t\tABOUT ME \n" )
            self.ABOUTME.setStyleSheet("color:rgb(0,0,0); font:20pt bold")
            self.ABOUTME.setText( about)
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

            # print(password)

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
        emp = 'UPDATE empdat SET  department =?,position=?,email=?,address=?,phone=?,image=? WHERE name =\'' + self.user + "\'"
        cur.execute(
            emp, (self.items[2],self.items[3],self.items[4],self.items[5],self.items[6],self.items[-1]))
        conn.commit()
        print("committed changes")
        self.save.setText("SAVED")
        conn.close()
        self.loaddata(self.user)
# change passsword
    def change_pass(self):

        # print(conn)
        cur = self.conn.cursor()
        emp = 'SELECT password FROM empdat WHERE name =\'' + self.user + "\'"
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
                print("i am in chnage pass")
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
                    data = 'UPDATE empdat SET password =\'' + newpass2 + "\' WHERE name =\'" + self.user + "\'"
                    cur.execute(data)
                    self.conn.commit()
                    self.conn.close()


    def employee_info(self):
        print("EMP_INFO")
        a=emp_info(self.user)
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)        

    def GENERATE(self):
        # self.close()
        print("EMP_INFO")
        a=slip(self.user)
        
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)   
        # a.move(100,100)
        # a.setWindowModality(Qt.ApplicationModal)
        widget.setWindowTitle("GENERATE PAYSLIP")
    # def my_profile(self):
    #     self.save_info()
    #     emppf=fin_dashboard(self.user)
    #     widget.addWidget(emppf)
    #     widget.setCurrentIndex(widget.currentIndex()+1)
    #     widget.setFixedWidth(1230)
    #     widget.setFixedHeight(700)  
    
    def log_out(self):
        # self.close()
        print("EMP_INFO")
        a=LOGOUT_fin(self.user)
        
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(640)
        widget.setFixedHeight(400)   
        # a.move(100,100)
        # a.setWindowModality(Qt.ApplicationModal)
        widget.setWindowTitle("log out")

        print("logged-out")
        
class slip(QDialog):
    def __init__(self,userloggedin):
        super().__init__()
        self.user=userloggedin
        loadUi("financedashboardSLIP1.ui",self)
        self.Generate.clicked.connect(self.generate)
        self.myprofile.clicked.connect(self.my_profile)
        self.logout.clicked.connect(self.log_out)
        self.empinfo.clicked.connect(self.employee_info)
    def generate(self):
        name=self.name.text() #desginer me jo hum likh raye wo yahwn connect hoga
        if len(name)==0 :
            self.erroremp.setText("Please enter name.")
        else:
            conn=sqlite3.connect("empdata.db")
            cur = conn.cursor()
            amp=('SELECT name FROM empdat')
            # cur.execute(amp)
            c=[i for item in cur.execute(amp) for i in item]
                

            if name not in c:
                print(name, "not in ",c)
                self.erroremp.setText("User not exist.")
            else:
                emppf=slip2(name,self.user)
                widget.addWidget(emppf)
                widget.setFixedWidth(1233)
                widget.setFixedHeight(703)
                widget.setCurrentIndex(widget.currentIndex()+1)
                
                cur.close()
    def my_profile(self):
        
        emppf=fin_dashboard(self.user)
        widget.addWidget(emppf)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)  
    def log_out(self):
        # self.close()
        print("EMP_INFO")
        a=LOGOUT_fin(self.user)
        
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(640)
        widget.setFixedHeight(400)   
        # a.move(100,100)
        # a.setWindowModality(Qt.ApplicationModal)
        widget.setWindowTitle("log out")
    def employee_info(self):
        print("EMP_INFO")
        a=emp_info(self.user)
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)   
                
class slip2(QDialog):
    def __init__(self,name,userloggedin):
        super().__init__()
        self.user=userloggedin
        print("im user ",userloggedin)
        
        loadUi("financedashboardSLIP2 .ui",self)
        self.load(name)
        self.save.clicked.connect(self.savepayslip)
        self.myprofile.clicked.connect(self.my_profile)
        self.empinfo.clicked.connect(self.employee_info)
        # self.generatepayslip.clicked.connect(self.GENERATE)
        self.logout.clicked.connect(self.log_out)
    def load(self,name):

        self.nameline.setText(name)

        conn=sqlite3.connect("empdata.db")
        # print(conn)
        cur=conn.cursor()
        emp='SELECT position,wage,tasks,loan FROM empdat WHERE name =\''+name+"\'"
        for logg in cur.execute(emp):
            print("yessssss32",logg)
        cur.close()
        wage=logg[1]
        tasks=logg[2]
        if logg[3] == None:
            loan=0
        else:
            loan=logg[3]
        self.designation.setText(logg[0])
        today = date.today()
        self.Date.setText(str(today))
        if tasks <4:
            bonus=2000
            self.bonus.setText(str(bonus))
        elif 7 > tasks >=4 :
            bonus=6000
            self.bonus.setText(str(bonus))
        else:
            bonus=10000
            self.bonus.setText(str(bonus))
        self.salary.setText(str(wage))
        self.loan.setText(str(loan))
        tax=0.03*logg[1]
        self.tax.setText(str(tax))
        self.pf.setText(str(5000))
        self.internet.setText(str(2000))
        self.conveyance.setText(str(15000))
        total_add=wage+bonus+2000+15000
        total_ded=loan+tax+5000
        self.totalearn.setText(str(total_add))
        self.totalded.setText(str(total_ded))
        print(int(self.loan.text()))
        self.netsalary.setText(str(total_add+total_ded))
        #  nae hoga ese 

        conn.commit()

    def savepayslip(self):
        name=self.nameline.text()
        designation=self.designation.text()
        date=self.Date.text()
        basesalary=self.salary.text()
        bonus=self.bonus.text()
        internet=self.internet.text()
        conveyance=self.conveyance.text()
        pf=self.pf.text()
        tax=self.tax.text()
        loan=self.loan.text()
        total_add=self.totalearn.text()
        total_ded=self.totalded.text()
        net=self.netsalary.text()
        items=[name,designation,date,basesalary,bonus,internet,conveyance,pf,tax,loan,total_add,total_ded,net]
        conn=sqlite3.connect("empdata.db")
        # print(conn)
        print(items)
        cur=conn.cursor()
        sqlquery="INSERT INTO payslips ( NAME,DESIGNATION,DATE,BASESALARY,BONUS,INTERNET,CONVEYANCE,PROVIDENTFUND,TAX,LOAN,TOTALEARNINGS,TOTALDEDUCTION,NETSALARY) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"
        cur.execute(sqlquery,items)
        # sqlquery='INSERT INTO payslips '
        conn.commit()
    def my_profile(self):
        self.save_info()
        emppf=fin_dashboard(self.user)
        widget.addWidget(emppf)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)  

    def log_out(self):
        # self.close()
        print("EMP_INFO")
        a=LOGOUT_fin(self.user)
        print(self.user)
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(640)
        widget.setFixedHeight(400)   
        # a.move(100,100)
        # a.setWindowModality(Qt.ApplicationModal)
        widget.setWindowTitle("log out")
    def employee_info(self):
        print("EMP_INFO")
        a=emp_info(self.user)
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)   

class LOGOUT_fin(QDialog):
    def __init__(self,name):
        self.name=name
        super().__init__()
        loadUi("logout.ui",self)
        self.yes.clicked.connect(self.yess)
        self.no.clicked.connect(self.noo)
    def noo(self):
        emppf=fin_dashboard(self.name)
        widget.addWidget(emppf)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)
        print("profile")
    def yess(self):
        emppf=page()
        widget.addWidget(emppf)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(480)
        widget.setFixedHeight(620)
        print("logged out")
class emp_info(QDialog):
    def __init__(self,user):
        self.user=user
        super(emp_info, self).__init__()
        loadUi("editinfo.ui",self)
        self.generatepayslip.clicked.connect(self.GENERATE)
        self.myprofile.clicked.connect(self.my_profile)
        self.logout.clicked.connect(self.log_out)
        self.data()
    def data(self):
        
        conn=sqlite3.connect("empdata.db")
        cur=conn.cursor()
        q= 'SELECT * FROM payslips'
        cur.execute(q)
        # self.tableWidget.setRowCount(50)
        t=0
        for row in cur.execute(q):
            print(row,t)
            self.tableWidget.setItem(t,0,QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(t,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tableWidget.setItem(t,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.tableWidget.setItem(t,3,QtWidgets.QTableWidgetItem(str(row[10])))
            self.tableWidget.setItem(t,4,QtWidgets.QTableWidgetItem(str(row[11])))
            self.tableWidget.setItem(t,5,QtWidgets.QTableWidgetItem(str(row[12])))
            
            t+=1
        self.tableWidget.setRowCount(t+1)

    def my_profile(self):
        
        emppf=fin_dashboard(self.user)
        widget.addWidget(emppf)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)  

    def log_out(self):
        # self.close()
        print("EMP_INFO")
        a=LOGOUT_fin(self.user)
        
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(640)
        widget.setFixedHeight(400)   
        # a.move(100,100)
        # a.setWindowModality(Qt.ApplicationModal)
        widget.setWindowTitle("log out")
    def GENERATE(self):
        # self.close()
        print("EMP_INFO")
        a=slip(self.user)
        
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(1230)
        widget.setFixedHeight(700)   
        # a.move(100,100)
        # a.setWindowModality(Qt.ApplicationModal)
        widget.setWindowTitle("GENERATE PAYSLIP")












a=QApplication(sys.argv)
mainwindow=page()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setWindowIcon(QIcon("/home/maira/Desktop/PROJECT -/logoicon.png"))
widget.setFixedWidth(480)
widget.setFixedHeight(620)
widget.show()
a.exec_()