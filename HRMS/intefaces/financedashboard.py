import sys
from PyQt5 import  QtWidgets , QtGui,Qt,QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from myprofile import emp_profile
from datetime import date
import sqlite3
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
        self.close()
        sys.exit(0)
        print("logged out")
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
        print("im nam e",name)
        super().__init__()
        loadUi("logout.ui",self)
        # self.yes.clicked.connect(self.yess)
        self.no.clicked.connect(self.noo)
    def noo(self):
        emppf=fin_dashboard(self.name)
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
        self.tableWidget.setRowCount(50)
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
mainwindow=fin_dashboard("hadiqa")
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1230)
widget.setFixedHeight(700)
widget.show()
a.exec_()