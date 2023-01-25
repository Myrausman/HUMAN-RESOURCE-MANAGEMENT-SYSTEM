import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
import sqlite3
class performance(QDialog):
    def __init__(self):
        super(performance, self).__init__()
        loadUi("PERFOMANCE.ui",self)
        self.pushButton.clicked.connect(self.errorr)
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
            

a=QApplication(sys.argv)
mainwindow=performance()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1230)
widget.setFixedHeight(700)
widget.show()
a.exec_()