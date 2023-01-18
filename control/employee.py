import sys
from PyQt5 import  QtWidgets , QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
# from PyQt5.QtWidgets import  PasswordEdit

import sqlite3

class emp_profile(QDialog):  # employee ka dashboardhai ye

    def __init__(self,name):
        self.name=name
        super( emp_profile,self).__init__()
        loadUi("employee.ui",self)
        self.conn=sqlite3.connect("empdata.db")
        self.currentpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newpass1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newpass2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.myprofile.clicked.connect(self.Profile)
        self.attendance.clicked.connect(self.Attendance)
        self.tasks.clicked.connect(self.Task)
        self.logout.clicked.connect(self.Logout)
        self.upload.clicked.connect(self.Upload)
        
        self.loaddata(self.name)
        # self.name.clicked.connect(self.name)
        # self.about.clicked.connect(self.name)
        # self.job.clicked.connect(self.name)
        # self.phone.clicked.connect(self.name)
        # self.address.clicked.connect(self.name)
        # self.email.clicked.connect(self.name)
    def loaddata(self,name):
        
        cur=self.conn.cursor()
        sqlquery='SELECT  id,name,position,email,address,phone,about ,image FROM empdat WHERE name =\''+name+"\'"
        
        
        # print(name)
        path="/home/maira/Desktop/PROJECT -/"
        for person in cur.execute(sqlquery):
            print(person)
            print(person[1])
            self.tableWidget.setRowCount(6) 
            
            #Column count
            self.tableWidget.setColumnCount(1) 
            self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            for row in range(len(person)-3):
                self.tableWidget.setItem(row-1,1,QtWidgets.QTableWidgetItem(str(person[row])))
            about=person[6]
            self.ABOUTME.setStyleSheet("color:rgb(0,0,0); font:25pt bold")
            self.ABOUTME.setText(" ABOUT ME \n "+about)
            image=path+person[7]
            self.placeholder.setPixmap(QPixmap(image))
            self.placeholder2.setPixmap(QPixmap(image))
            password=person[-1]
            
           
            self.editprofile.setRowCount(6) 
            #Column count
            self.editprofile.setColumnCount(2) 
            keys=["ID","FULL NAME","DESIGNATION","EMAIL","ADDRESS","PHONE"]
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
                self.editprofile.setItem(i,1,QtWidgets.QTableWidgetItem(str(person[i])))
                
                
            print(password)
            self.savepassword.clicked.connect(self.change_pass)
            self.saveinfo.clicked.connect(self.editProfile)
            self.upload.clicked.connect(self.uploadPic)
    def uploadPic(self):
        fname=QFileDialog.getOpenFileName(self,'Open file',"/home/maira/Pictures/",'Images(*.png)')
        self.filename.setText(fname[0])
        image=fname[0]
        cur=self.conn.cursor()

        cur.execute(image)
        self.conn.commit()
        

    def editProfile(self):
        
        # print(conn)
        
        
        items=[]
        for i in range(7):
            rowdata=''
            item=self.editprofile.item(i,1)
            if item and item.text:

                rowdata+= item.text()
            
                items.append(rowdata)
                print(rowdata)
            else:
                rowdata+= "NULL"
        print(items)
        cur=self.conn.cursor()
        emp='UPDATE empdat SET  name=?,position=?,email=?,address=?,phone=? WHERE name =\''+self.name+"\'"
        cur.execute(emp,(items[1],items[2],items[3],items[4],items[5]))
        # for i in cur.execute(emp,(items[1],items[2],items[3],items[4],items[5])):
        #     print(i)
        self.conn.commit()
        emp_profile(self.name)
    def change_pass(self):
        
        # print(conn)
        cur=self.conn.cursor()
        emp='SELECT password FROM empdat WHERE name =\''+self.name+"\'"
        cur.execute(emp)
        password=cur.fetchone()[0]
        print(password)
        
        currentpassword= self.currentpass.text()
        newpass1= self.newpass1.text()
        newpass2=self.newpass2.text()
        print(newpass2)
        if len(currentpassword) == 0 or len(newpass1) == 0 or len(newpass2) == 0:
            self.emptyerror.setText(" ! Please inputs all fields.")
        else:       
            self.emptyerror.setText("")
            if currentpassword != password:
                self.incorrectpass.setText("! Incorrect Password")
                # print(currentpassword,"currentpassword")
            else:
                # self.incorrectpass.setStyleSheet("color: black; background-color:green; font:15px bold align=center")
                self.correctpass.setText("✔")
                if newpass1 !=newpass2 or len(newpass1) ==0 : 
                    self.unmatchedpassword.setText(" ! Passowrds do not match")
                    print("error")
                else:
                    self.incorrectpass.setText("")
                    self.unmatchedpassword.setText("")
                    self.emptyerror.setText(" password changed .")
                    print("changed password succesfully")
                    print(newpass2)
                    # emp='SELECT password FROM empdat WHERE name =\''+self.name+"\'"
                    data='UPDATE empdat SET password =\''+newpass2+"\' WHERE name =\'"+self.name+"\'"
                    cur.execute(data)
                    self.conn.commit()

        


           



            

    def Profile(self):
        print("my profile ")
    def Attendance(self):
        print("attendance ")
    def Task(self):
        print("tasks  ")
    def Logout(self):
        print("logout ")
    def Upload(self):
        print("upload")   

a=QApplication(sys.argv)
mainwindow=emp_profile("Hadiqa")
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1230)
widget.setFixedHeight(700)
widget.show()
a.exec_()