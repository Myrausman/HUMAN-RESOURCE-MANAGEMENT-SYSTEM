import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
from datetime import date
import sqlite3
class slip(QDialog):
    def __init__(self,userloggedin):
        super().__init__()
        self.user=userloggedin
        loadUi("financedashboardSLIP1.ui",self)
        self.Generate.clicked.connect(self.generate)
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
        
                
class slip2(QDialog):
    def __init__(self,name,userloggedin):
        super().__init__()
        self.user=userloggedin

        
        loadUi("financedashboardSLIP2 .ui",self)
        self.load(name)
        self.save.clicked.connect(self.savepayslip)
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


a=QApplication(sys.argv)
mainwindow=slip("myra")
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1230)
widget.setFixedHeight(700)
widget.show()
a.exec_()