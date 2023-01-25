import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
from hrdashboard import hr_dashboard
import sqlite3
class assign_task(QDialog):
    def __init__(self):
        super(assign_task, self).__init__()
        loadUi("assigntask1.ui",self)
        self.loaddata()
        self.assign1button.clicked.connect(self.AssignTask)
    def AssignTask(self):
        a=assign2()
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
class assign2(QDialog):
    def __init__(self):
        super(assign2, self).__init__()
        loadUi("assigntask2.ui",self)
        self.backbutton.clicked.connect(self.backloginnn)
        self.assignbutton.clicked.connect(self.tas)
    def backloginnn(self):
        a=assign_task()
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def tas(self):
        c=assigntk2()
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
        data4='UPDATE tasks SET TaskNumber =\''+num+"\' WHERE EmployeeName =\'"+namee+"\'" 

        cur.execute(data)
        cur.execute(data1)
        cur.execute(data2)
        cur.execute(data3)
        cur.execute(data4)
        conn.commit()
        conn.close()
class assigntk2(QDialog):
    def __init__(self):
        super(assigntk2, self).__init__()
        loadUi("assigntask2.ui",self)
        self.backbutton.clicked.connect(self.backloginnn)
        self.assignbutton.clicked.connect(self.tas)
    def backloginnn(self):
        a=assign_task()
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def tas(self):
        c=assign2()
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
        query='UPDATE tasks SET Task =?,StartDate=?,EndDate=?,status=?,TaskNumber=?'
        data='UPDATE tasks SET Task =\''+tsk+"\' WHERE EmployeeName =\'"+namee+"\'" 
        data1='UPDATE tasks SET StartDate =\''+sdate+"\' WHERE EmployeeName =\'"+namee+"\'" 
        data2='UPDATE tasks SET EndDate =\''+edate+"\' WHERE EmployeeName =\'"+namee+"\'" 
        data3='UPDATE tasks SET status =\''+b+"\' WHERE EmployeeName =\'"+namee+"\'" 
        data4='UPDATE tasks SET TaskNumber =\''+num+"\' WHERE EmployeeName =\'"+namee+"\'" 

        cur.execute(data)
        cur.execute(data1)
        cur.execute(data2)
        cur.execute(data3)
        cur.execute(data4)
        conn.commit()
        conn.close()
        

    
    
        
        
        
        
     

        
a=QApplication(sys.argv)
mainwindow=assign_task()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1230)
widget.setFixedHeight(700)
widget.show()
a.exec_()