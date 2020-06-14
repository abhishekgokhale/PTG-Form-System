import sys
import csv
import first
import ptg
import PTG_LOGIN
import teacher_login
import logins
import ptg2
import meet1
import untitled
import batch1
import portalT
import batchT
import listT
import report
import regforms
import units
import sppu_markss
import criticals
import cocurriculars
import ATT_RECORDS
import new as hill
import re
from PyQt5 import QtGui
from PyQt5 import QtCore, QtWidgets
import matplotlib.pyplot as plt
import numpy as np
import sqlite3
from PyQt5.QtWidgets import *

class SA1(QtWidgets.QMainWindow,first.Ui_wel):
    def __init__(self,parent=None):
        super(SA1,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.firstp)

    def firstp(self):
        self.hide()
        self.s1 = SA2()
        self.s1.show()

class SA2(QtWidgets.QMainWindow,ptg.Ui_ptg1):
    def __init__(self,parent=None):
        super(SA2,self).__init__(parent)
        self.setupUi(self)
        self.commandLinkButton.clicked.connect(self.btnone)
        self.commandLinkButton_2.clicked.connect(self.btntwo)
        self.commandLinkButton_3.clicked.connect(self.btnthree)
        self.pushButton.clicked.connect(self.back)

    def btnone(self):
        self.hide()
        self.s2 = SA3()
        self.s2.show()

    def btntwo(self):
        self.hide()
        self.s3 = SA4()
        self.s3.show()

    def btnthree(self):
        self.hide()
        self.s4 = SA5()
        self.s4.show()

    def back(self):
        self.hide()
        self.s5 = SA1()
        self.s5.show()
        
class SA3(QtWidgets.QMainWindow,PTG_LOGIN.Ui_MainWindowc):
    def __init__(self,parent=None):
        super(SA3,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btnone)
        self.pushButton_2.clicked.connect(self.back)

    def btnone(self):
        user=str(self.lineEdit.text())
        passw=str(self.lineEdit_2.text())

        if not(user and passw):
            self.s1=mes_fun()
            self.s1.message_fun("Enter proper credentials!")

        else:
            conn = sqlite3.connect("data.db")
            c=conn.cursor()
            c.execute("select password from clogin where username=?",[user])
            password = c.fetchall()
            b = list(password)
            if not b:
                self.s1=mes_fun()
                self.s1.message_fun("Wrong username entered!")
            else:    
                for a in b:
                    if passw==a[0]:
                        self.hide()
                        self.s6 = SA6()
                        self.s6.show()
                    else:
                        self.s1=mes_fun()
                        self.s1.message_fun("Wrong password entered!")
            c.close()
            conn.close()

    def back(self):
        self.hide()
        self.s7 = SA2()
        self.s7.show()

class SA4(QtWidgets.QMainWindow,teacher_login.Ui_MainWindowt):
    def __init__(self,parent=None):
        super(SA4,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.back)

    def login(self):
        passw=str(self.lineEdit_2.text())
        
        if not(str(self.lineEdit_3.text()) and passw):
            self.s1=mes_fun()
            self.s1.message_fun("Enter proper credentials!")

        else:
            conn = sqlite3.connect("data.db")
            c=conn.cursor()
            c.execute("select password from tlogin where username=?",[str(self.lineEdit_3.text())])
            password = c.fetchall()
            b = list(password)
            if not b:
                self.s1=mes_fun()
                self.s1.message_fun("Wrong username entered!")
            else:
                for a in b:
                    if passw==a[0]:
                        c.execute("INSERT INTO teacherExtra VALUES(?)",[str(self.lineEdit_3.text())])
                        conn.commit()
                        c.execute("update checklog set logged='t'")
                        conn.commit()
                        self.hide()
                        self.s6 = SA10()
                        self.s6.show()
                    else:
                        self.s1=mes_fun()
                        self.s1.message_fun("Wrong password entered!")
            c.close()
            conn.close()
                
    def back(self):
        self.hide()
        self.s7 = SA2()
        self.s7.show()

class SA5(QtWidgets.QMainWindow,logins.Ui_MainWindows):
    def __init__(self,parent=None):
        super(SA5,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.logs)
        self.pushButton_2.clicked.connect(self.back)

    def logs(self):
        username=str(self.lineEdit.text())
        passw=str(self.lineEdit_2.text())

        if not(username and passw):
            self.s1=mes_fun()
            self.s1.message_fun("Enter Proper credentials!")
        else:
            conn = sqlite3.connect("data.db")
            c=conn.cursor()
            
            c.execute("select password from slogin where username=?",[str(self.lineEdit.text())])
            password = c.fetchall()
            b = list(password)
            if not b:
                self.s1=mes_fun()
                self.s1.message_fun("Wrong username entered!")
            else:
                for a in b:
                    if passw==a[0]:
                        c.execute("INSERT INTO extra VALUES(?)",[username])
                        c.execute("update checklog set logged='s'")
                        conn.commit()
                        self.hide()
                        self.s6 = SA14()
                        self.s6.show()
                    else:
                        self.s1=mes_fun()
                        self.s1.message_fun("Wrong password entered!")
            c.close()
            conn.close()
        
    def back(self):
        self.hide()
        self.s7 = SA2()
        self.s7.show()

class SA6(QtWidgets.QMainWindow,ptg2.Ui_ptgc):
    def __init__(self,parent=None):
        super(SA6,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.lis)
        self.pushButton_2.clicked.connect(self.bat)
        self.pushButton_3.clicked.connect(self.met)
        self.pushButton_4.clicked.connect(self.back)

    def lis(self):
        self.hide()
        self.s9 = SA7()
        self.s9.show()

    def bat(self):
        self.hide()
        self.s10 = SA8()
        self.s10.show()

    def met(self):
        self.hide()
        self.s11 = SA9()
        self.s11.show()
    
    def back(self):
        self.hide()
        self.s8 = SA3()
        self.s8.show()

class SA7(QtWidgets.QMainWindow,untitled.Ui_listofs):
    def __init__(self,parent=None):
        super(SA7,self).__init__(parent)
        self.setupUi(self)
        self.filePath="a"
        self.pushButton.clicked.connect(self.pushbtn)
        self.pushButton_3.clicked.connect(self.back)
        self.pushButton_4.clicked.connect(self.done)

    def pushbtn(self):
        self.filePath = QtWidgets.QFileDialog.getOpenFileName(None,'Single File',"~/Desktop",'CSV(*.csv)')
        print(self.filePath[0])

    def done(self):
        if(self.filePath=="a"):
            self.s1=mes_fun()
            self.s1.message_fun("Select CSV file first!")
        else:
            conn = sqlite3.connect("data.db")
            c=conn.cursor()
            if self.filePath != '':
                with open(self.filePath[0]) as csv_file:
                    csv_reader = csv.reader(csv_file,delimiter=',')
                    for row in csv_reader:
                    	print(row[0])
                    	splits = row[0].split(',')
                    	c.execute("INSERT INTO slogin VALUES(?,?)",[splits[0],splits[1]])
            conn.commit()
            c.close()
            conn.close()

    def back(self):
        self.hide()
        self.s8 = SA6()
        self.s8.show()

class SA8(QtWidgets.QMainWindow,batch1.Ui_batch):
    def __init__(self,parent=None):
        super(SA8,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushbtn)
        self.pushButton_2.clicked.connect(self.back)

    def pushbtn(self):
        conn = sqlite3.connect("data.db")
        c=conn.cursor()
        batch=""
        teacher=""
        if self.checkBox.isChecked():
            batch="A1"
        elif self.checkBox_2.isChecked():
            batch="A2"
        elif self.checkBox_3.isChecked():
            batch="A3"
        elif self.checkBox_4.isChecked():
            batch="A4"
        
        if self.radioButton_5.isChecked():
            teacher="anand"
        elif self.radioButton_6.isChecked():
            teacher="swati"
        elif self.radioButton_7.isChecked():
            teacher="anuradha"
        elif self.radioButton_8.isChecked():
            teacher="rahul"
        elif self.radioButton_9.isChecked():
            teacher="shailesh"
        elif self.radioButton_10.isChecked():
            teacher="sagar"


        c.execute("select batch from allocate")
        row=c.fetchone()
        i=0
        while row is not None:
            if(batch==row[0]):
                i=1
                break
            row=c.fetchone()

        if(i==1):
            self.s1=mes_fun()
            self.s1.message_fun("Teacher already allocated for this batch!")
        else: 
            if(batch=="" or teacher==""):
                self.s1=mes_fun()
                self.s1.message_fun("Select batch and teacher!")

            else:
                c.execute("INSERT INTO allocate VALUES(?,?)",[batch,teacher])
                conn.commit()
        c.close()
        conn.close()
        
    def back(self):
        self.hide()
        self.s8 = SA6()
        self.s8.show()

class SA9(QtWidgets.QMainWindow,meet1.Ui_meet):
    def __init__(self,parent=None):
        super(SA9,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushbtn)
        self.pushButton_2.clicked.connect(self.back)

    def pushbtn(self):
        conn = sqlite3.connect("data.db")
        c=conn.cursor()
        batch=""
        first=""
        second=""
        third=""
        if self.radioButton.isChecked():
            batch="A1"
        elif self.radioButton_2.isChecked():
            batch="A2"
        elif self.radioButton_3.isChecked():
            batch="A3"
        elif self.radioButton_4.isChecked():
            batch="A4"
        
        first=str(self.dateEdit.text())
        second=str(self.dateEdit_2.text())
        third=str(self.dateEdit_3.text())

        c.execute("select batch from meeting")
        row=c.fetchone()
        i=0
        while row is not None:
            if(batch==row[0]):
                i=1
                break
            row=c.fetchone()

        if(i==1):
            self.s1=mes_fun()
            self.s1.message_fun("Meetings already entered for this batch!")
        else:
            if(batch=="" or first=="" or second=="" or third==""):
                self.s1=mes_fun()
                self.s1.message_fun("Select batch and meetings!")

            else:
                c.execute("INSERT INTO meeting VALUES(?,?,?,?)",[batch,first,second,third])
                conn.commit()

        c.close()
        conn.close()

    def back(self):
        self.hide()
        self.s8 = SA6()
        self.s8.show()

class SA10(QtWidgets.QMainWindow,portalT.Ui_MainWindow1):
    def __init__(self,parent=None):
        super(SA10,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.liststud)
        self.pushButton_2.clicked.connect(self.back)
        self.pushButton_3.clicked.connect(self.sch)

    def liststud(self):
        self.hide()
        self.s9 = SA11()
        self.s9.show()

    def sch(self):
        self.hide()
        self.s3 = SA12()
        self.s3.show()
        
    def back(self):
        self.hide()
        self.s8 = SA4()
        self.s8.show()

class SA11(QtWidgets.QMainWindow,listT.Ui_MainWindow):
    def __init__(self,parent=None):
        conn = sqlite3.connect("data.db")
        c=conn.cursor()
        super(SA11,self).__init__(parent)
        self.setupUi(self)
        self.sname=""
        sql = "select name from teacherExtra desc limit -1"
        c.execute(sql)
        name = c.fetchall()
        list1 = list(name)
        for a in list1:
            n=0

        c.execute("select batch from allocate where teacher=?",[a[0]])
        batch=c.fetchone()
        c.execute("select name,id from studdets where batch=?",[batch[0]])
        i=0
        row=c.fetchone()
        while row is not None:
            self.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(i,1,QtWidgets.QTableWidgetItem(str(row[1])))
            i=i+1
            row=c.fetchone()

        c.close()
        conn.close()

        self.tableWidget.cellClicked.connect(self.cell_was_clicked)
        self.pushButton.clicked.connect(self.submit)
        self.pushButton_2.clicked.connect(self.view)
        self.pushButton_3.clicked.connect(self.back)

    def submit(self):
        if(self.sname==""):
            self.s1=mes_fun()
            self.s1.message_fun("Select student first!")

        else:
            conn = sqlite3.connect("data.db")
            c=conn.cursor()
            c.execute("INSERT INTO extra VALUES(?)",[str(self.sname)])
            conn.commit()
            c.close()
            conn.close()
            self.hide()
            self.s8 = SA14()
            self.s8.show()

    def view(self):
        if(self.sname==""):
            self.s1=mes_fun()
            self.s1.message_fun("Select student first!")

        else:
            conn = sqlite3.connect("data.db")
            c=conn.cursor()
            c.execute("INSERT INTO extra VALUES(?)",[str(self.sname)])
            conn.commit()
            c.close()
            conn.close()
            self.hide()
            self.s8 = SA13()
            self.s8.show()

    def cell_was_clicked(self,row,column):
        self.sname=self.tableWidget.item(row,column).text()
        
    def back(self):
        self.hide()
        self.s8 = SA10()
        self.s8.show()

class SA12(QtWidgets.QMainWindow,batchT.Ui_MainWindow2):
    def __init__(self,parent=None):
        super(SA12,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.back)

        conn = sqlite3.connect("data.db")
        c=conn.cursor()
        sql = "select name from teacherExtra desc limit -1"
        c.execute(sql)
        name = c.fetchall()
        list1 = list(name)
        for a in list1:
            n=0

        c.execute("SELECT batch FROM allocate WHERE teacher=?",[a[0]])
        rec=c.fetchone()
        list1=list(rec)
        b=" "
        m1=" "
        m2=" "
        m3=" "
        c.execute("SELECT * FROM meeting WHERE batch=?",[str(list1[0])])
        for row in c.fetchall():
            b=row[0]
            m1=row[1]
            m2=row[2]
            m3=row[3]

        self.label_8.setText(m1)
        self.label_9.setText(m2)
        self.label_10.setText(m3)
        self.label_11.setText(b)

        c.close()
        conn.close()

    def back(self):
        self.hide()
        self.s8 = SA10()
        self.s8.show()

class SA13(QtWidgets.QMainWindow,report.Ui_MainWindowr):
    def __init__(self,parent=None):
        super(SA13,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.back)
        self.pushButton_3.clicked.connect(self.pushatt)
        self.pushButton_2.clicked.connect(self.pushper)

    def pushatt(self):
        conn = sqlite3.connect("data.db")
        c=conn.cursor()
        sql = "select name from extra desc limit -1"
        c.execute(sql)
        name = c.fetchall()
        list1 = list(name)
        for a in list1:
            n=0

        c.execute("SELECT a1,a2,a3,a4,a5 FROM acca where name=?",[a[0]])
        row=c.fetchone()
        i=0
        fe=[[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
        att=[1,1,1,1,1,1,1,1]
        sem=[1,2,3,4,5,6,7,8]
        while row is not None:
            fe[i][0]=row[0]
            fe[i][1]=row[1]
            fe[i][2]=row[2]
            fe[i][3]=row[3]
            fe[i][4]=row[4]
            att[i]=(fe[i][0]+fe[i][1]+fe[i][2]+fe[i][3]+fe[i][4])/5
            i=i+1
            row=c.fetchone()

        c.close()
        conn.close()
            
        index = np.arange(len(sem))
        plt.bar(index, att)
        plt.xlabel('Semester', fontsize=15)
        plt.ylabel('Attendance', fontsize=15)
        plt.xticks(index, sem, fontsize=10, rotation=30)
        plt.title('Attendance record')
        plt.show()

    def pushper(self):
        conn = sqlite3.connect("data.db")
        c=conn.cursor()
        sql = "select name from extra desc limit -1"
        c.execute(sql)
        name = c.fetchall()
        list1 = list(name)
        for a in list1:
            n=0
        c.execute("SELECT agg FROM sppuper WHERE name=?",[a[0]])
        row=c.fetchone()
        agg=[1,1,1,1,1,1,1,1]
        sem=[1,2,3,4,5,6,7,8]
        i=0
        while row is not None:
            agg[i]=row[0]
            i=i+1
            row=c.fetchone()

        c.close()
        conn.close()
        
        index = np.arange(len(sem))
        plt.bar(index, agg)
        plt.xlabel('Semester', fontsize=15)
        plt.ylabel('Aggregate marks', fontsize=15)
        plt.xticks(index, sem, fontsize=10, rotation=30)
        plt.title('SPPU Performance')
        plt.show()

    def back(self):
        self.hide()
        self.s8 = SA11()
        self.s8.show()

class SA14(QtWidgets.QMainWindow,regforms.Ui_MainWindow2):
    def __init__(self,parent=None):
        super(SA14,self).__init__(parent)
        self.setupUi(self)
        conn = sqlite3.connect("data.db")
        c=conn.cursor()
        global a
        sql = "select name from extra desc limit -1"
        c.execute(sql)
        name = c.fetchall()
        list1 = list(name)
        for a in list1:
            n=0
        c.close()
        conn.close()
        
        self.pushButton.clicked.connect(self.regs)
        self.pushButton_2.clicked.connect(self.view)
        self.pushButton_3.clicked.connect(self.back)

    def regs(self):
        conn = sqlite3.connect("data.db")
        c=conn.cursor()
        name=str(self.lineEdit_15.text())
        sid=str(self.lineEdit_14.text())
        branch=str(self.lineEdit_13.text())
        yoa=str(self.lineEdit.text())
        shift=str(self.lineEdit_3.text())
        dob=str(self.lineEdit_4.text())
        phno=str(self.lineEdit_5.text())
        ladd=str(self.lineEdit_7.text())
        padd=str(self.lineEdit_6.text())
        email=str(self.lineEdit_10.text())
        fname=str(self.lineEdit_11.text())
        mname=str(self.lineEdit_12.text())
        focc=str(self.lineEdit_8.text())
        mocc=str(self.lineEdit_9.text())

        # if(re.match("^[A-Za-z]*$",name)):
        # 	print ("valid name")
        # else:
        # 	print ("invalid name")
        # 	QtWidgets.QMessageBox.warning(self, 'ERROR','!!! INVALID NAME !!!')
        # if(re.match("^[A-Za-z]*$",sid)):
        # 	print ("invalid Student id")
        # 	QtWidgets.QMessageBox.warning(self, 'ERROR','!!! INVALID STUDENT ID !!!')
        # else:
        # 	print ("valid sid")
        # 	if(re.match("^[A-Za-z]*$",branch)):
        # 		print ("valid name")
        # 	else:
        # 		print ("invalid branch")
        # 		QtWidgets.QMessageBox.warning(self, 'ERROR','!!! INVALID BRANCH !!!')
        # if(re.match("^[A-Za-z]*$",shift)):
        # 	print ("invalid Student id")
        # 	QtWidgets.QMessageBox.warning(self, 'ERROR','!!! INVALID SHIFT !!!')
        # else:
        # 	print ("valid SHIFT")
        # checkm=re.match('\d{10}',phno)
        # if checkm:
        # 	mobile1=int(mb)
        # 	if(mobile1>6999999999 and mobile1<10000000000):
        # 		print('valid mobile')
        # 	else :
        # 		QtWidgets.QMessageBox.warning( self, 'Error','!!!  INVALID MOBILE NUMBER !!!')
        # else :
        # 	QtWidgets.QMessageBox.warning(self, 'Error','!!!  ENTER 10 DIGIT NUMBER ONLY !!!')
        # checke3=re.match('[^@]+@[^@]+\.[^@]+',email)
        # if checke3 :
        # 	print('valid email')
        # else :
        # 	QtWidgets.QMessageBox.warning( self, 'Error','!!! INVALID EMAIL-ID !!!')
        # 	if(re.match("^[A-Za-z]*$",fname)):
        # 		print ("valid name")
        # 	else:
        # 		print ("invalid branch")
        # 		QtWidgets.QMessageBox.warning(self, 'ERROR','!!! INVALID NAME !!!')
        # 		if(re.match("^[A-Za-z]*$",mname)):
        # 			print ("valid name")
        # 		else:
        # 			print ("invalid branch")
        # 			QtWidgets.QMessageBox.warning(self, 'ERROR','!!! INVALID NAME !!!')
        if int(self.lineEdit_14.text())>60:
            batch="A4"
        elif int(self.lineEdit_14.text())>40:
            batch="A3"
        elif int(self.lineEdit_14.text())>20:
            batch="A2"
        else:
            batch="A1"

        c.execute("SELECT id FROM studdets WHERE name=?",[a[0]])
        get=c.fetchall()
        list1=list(get)

        if not list1:
            c.execute("INSERT INTO studdets values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",[name,sid,branch,yoa,shift,dob,phno,ladd,padd,email,fname,mname,focc,mocc,batch])
        else:
            c.execute("""UPDATE studdets SET name=?,
                        id=?,branch=?,
                        yoa=?,shift=?,
                        dob=?,phno=?,
                        ladd=?,padd=?,
                        email=?,fname=?,
                        mname=?,focc=?,
                        mocc=?,batch=?
                        WHERE name=?""",[name,sid,branch,yoa,shift,dob,phno,ladd,padd,email,fname,mname,focc,mocc,batch,a[0]])
        conn.commit()
        c.close()
        conn.close()

        
        # counter=1
        # cipher_text = ""
        # plain_text = ""

        # f = open("encrypt.txt", "w+")
        # msg = name+branch+shift+email
        # print(len(msg))

        # for i in range(0,len(msg),4):
        #     PT = msg[i]+msg[i+1]+msg[i+2]+msg[i+3]
        #     encrypted_msg = hill.encrypt(PT,counter)
        #     cipher_text = cipher_text+encrypted_msg
        #     counter = counter + 1
        # f.write(cipher_text)

        # counter=1

        # f = open("decrypt.txt","w+")

        # for i in range(0,len(cipher_text),4):
        #     CT = cipher_text[i]+cipher_text[i+1]+cipher_text[i+2]+cipher_text[i+3]
        #     decrypted_msg = hill.decrypt(CT, counter)
        #     plain_text = plain_text+decrypted_msg
        #     counter = counter + 1

        # f.write(plain_text)

        
        self.hide()
        self.s8 = SA15()
        self.s8.show()

    def view(self):
        conn = sqlite3.connect("data.db")
        c=conn.cursor()
        sql = "select name from extra desc limit -1"
        c.execute(sql)
        name = c.fetchall()
        list1 = list(name)
        for a in list1:
            n=0
            
        c.execute("SELECT * FROM studdets WHERE name=?",[a[0]])
        for row in c.fetchall():
            name=row[0]
            sid=row[1]
            branch=row[2]
            yoa=row[3]
            shift=row[4]
            dob=row[5]
            phno=row[6]
            ladd=row[7]
            padd=row[8]
            email=row[9]
            fname=row[10]
            mname=row[11]
            focc=row[12]
            mocc=row[13]

        self.lineEdit_15.setText(name)
        self.lineEdit_14.setText(str(sid))
        self.lineEdit_13.setText(branch)
        self.lineEdit.setText(yoa)
        self.lineEdit_3.setText(shift)
        self.lineEdit_4.setText(dob)
        self.lineEdit_5.setText(str(phno))
        self.lineEdit_7.setText(ladd)
        self.lineEdit_6.setText(padd)
        self.lineEdit_10.setText(email)
        self.lineEdit_11.setText(fname)
        self.lineEdit_12.setText(mname)
        self.lineEdit_8.setText(focc)
        self.lineEdit_9.setText(mocc)
        self.lineEdit_2.setText(branch)
        
        c.close()
        conn.close()

    def back(self):
        conn = sqlite3.connect("data.db")
        c=conn.cursor()

        c.execute("select logged from checklog")
        check=c.fetchone()
        
        if check[0]=='s':
            c.close()
            conn.close()
            self.hide()
            self.s8 = SA5()
            self.s8.show()
        else:
            c.close()
            conn.close()
            self.hide()
            self.s8 = SA11()
            self.s8.show()

class SA15(QtWidgets.QMainWindow,units.Ui_MainWindow3):
    def __init__(self,parent=None):
        super(SA15,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.uni)
        self.pushButton_2.clicked.connect(self.back)
        self.pushButton_3.clicked.connect(self.viewbtn)

    def uni(self):
        conn = sqlite3.connect("data.db")
        c=conn.cursor()
        
        fe11_tot=str(self.lineEdit.text())
        fe11_app=str(self.lineEdit_2.text())
        fe11_pass=str(self.lineEdit_3.text())
        fe11_fail=str(self.lineEdit_4.text())
        fe11_sug=str(self.lineEdit_5.text())
        fe11_mua=str(self.lineEdit_6.text())

        fe12_tot=str(self.lineEdit_7.text())
        fe12_app=str(self.lineEdit_8.text())
        fe12_pass=str(self.lineEdit_9.text())
        fe12_fail=str(self.lineEdit_11.text())
        fe12_sug=str(self.lineEdit_10.text())
        fe12_mua=str(self.lineEdit_12.text())

        fe21_tot=str(self.lineEdit_13.text())
        fe21_app=str(self.lineEdit_15.text())
        fe21_pass=str(self.lineEdit_18.text())
        fe21_fail=str(self.lineEdit_24.text())
        fe21_sug=str(self.lineEdit_21.text())
        fe21_mua=str(self.lineEdit_16.text())

        fe22_tot=str(self.lineEdit_19.text())
        fe22_app=str(self.lineEdit_17.text())
        fe22_pass=str(self.lineEdit_14.text())
        fe22_fail=str(self.lineEdit_23.text())
        fe22_sug=str(self.lineEdit_20.text())
        fe22_mua=str(self.lineEdit_22.text())

        se11_tot=str(self.lineEdit_29.text())
        se11_app=str(self.lineEdit_35.text())
        se11_pass=str(self.lineEdit_33.text())
        se11_fail=str(self.lineEdit_27.text())
        se11_sug=str(self.lineEdit_42.text())
        se11_mua=str(self.lineEdit_40.text())

        se12_tot=str(self.lineEdit_30.text())
        se12_app=str(self.lineEdit_26.text())
        se12_pass=str(self.lineEdit_38.text())
        se12_fail=str(self.lineEdit_46.text())
        se12_sug=str(self.lineEdit_32.text())
        se12_mua=str(self.lineEdit_44.text())

        se21_tot=str(self.lineEdit_45.text())
        se21_app=str(self.lineEdit_31.text())
        se21_pass=str(self.lineEdit_36.text())
        se21_fail=str(self.lineEdit_41.text())
        se21_sug=str(self.lineEdit_48.text())
        se21_mua=str(self.lineEdit_34.text())

        se22_tot=str(self.lineEdit_28.text())
        se22_app=str(self.lineEdit_47.text())
        se22_pass=str(self.lineEdit_39.text())
        se22_fail=str(self.lineEdit_25.text())
        se22_sug=str(self.lineEdit_43.text())
        se22_mua=str(self.lineEdit_37.text())

        te11_tot=str(self.lineEdit_88.text())
        te11_app=str(self.lineEdit_83.text())
        te11_pass=str(self.lineEdit_75.text())
        te11_fail=str(self.lineEdit_70.text())
        te11_sug=str(self.lineEdit_55.text())
        te11_mua=str(self.lineEdit_59.text())

        te12_tot=str(self.lineEdit_49.text())
        te12_app=str(self.lineEdit_80.text())
        te12_pass=str(self.lineEdit_65.text())
        te12_fail=str(self.lineEdit_91.text())
        te12_sug=str(self.lineEdit_96.text())
        te12_mua=str(self.lineEdit_66.text())

        te21_tot=str(self.lineEdit_77.text())
        te21_app=str(self.lineEdit_90.text())
        te21_pass=str(self.lineEdit_76.text())
        te21_fail=str(self.lineEdit_61.text())
        te21_sug=str(self.lineEdit_72.text())
        te21_mua=str(self.lineEdit_92.text())

        te22_tot=str(self.lineEdit_86.text())
        te22_app=str(self.lineEdit_87.text())
        te22_pass=str(self.lineEdit_95.text())
        te22_fail=str(self.lineEdit_63.text())
        te22_sug=str(self.lineEdit_54.text())
        te22_mua=str(self.lineEdit_58.text())

        be11_tot=str(self.lineEdit_68.text())
        be11_app=str(self.lineEdit_69.text())
        be11_pass=str(self.lineEdit_64.text())
        be11_fail=str(self.lineEdit_82.text())
        be11_sug=str(self.lineEdit_67.text())
        be11_mua=str(self.lineEdit_71.text())

        be12_tot=str(self.lineEdit_85.text())
        be12_app=str(self.lineEdit_81.text())
        be12_pass=str(self.lineEdit_62.text())
        be12_fail=str(self.lineEdit_51.text())
        be12_sug=str(self.lineEdit_73.text())
        be12_mua=str(self.lineEdit_50.text())

        be21_tot=str(self.lineEdit_57.text())
        be21_app=str(self.lineEdit_74.text())
        be21_pass=str(self.lineEdit_93.text())
        be21_fail=str(self.lineEdit_56.text())
        be21_sug=str(self.lineEdit_60.text())
        be21_mua=str(self.lineEdit_89.text())

        be22_tot=str(self.lineEdit_52.text())
        be22_app=str(self.lineEdit_84.text())
        be22_pass=str(self.lineEdit_79.text())
        be22_fail=str(self.lineEdit_94.text())
        be22_sug=str(self.lineEdit_78.text())
        be22_mua=str(self.lineEdit_53.text())

        c.execute("SELECT tsub FROM utmarks WHERE name=?",[a[0]])
        get=c.fetchall()
        list1=list(get)

        if not list1:
            c.execute("INSERT INTO utmarks values(?,?,?,?,?,?,?,1)",[fe11_tot,fe11_app,fe11_pass,fe11_fail,fe11_sug,fe11_mua,a[0]])
            c.execute("INSERT INTO utmarks values(?,?,?,?,?,?,?,2)",[fe12_tot,fe12_app,fe12_pass,fe12_fail,fe12_sug,fe12_mua,a[0]])
            c.execute("INSERT INTO utmarks values(?,?,?,?,?,?,?,3)",[fe21_tot,fe21_app,fe21_pass,fe21_fail,fe21_sug,fe21_mua,a[0]])
            c.execute("INSERT INTO utmarks values(?,?,?,?,?,?,?,4)",[fe22_tot,fe22_app,fe22_pass,fe22_fail,fe22_sug,fe22_mua,a[0]])
            
            c.execute("INSERT INTO utmarks values(?,?,?,?,?,?,?,5)",[se11_tot,se11_app,se11_pass,se11_fail,se11_sug,se11_mua,a[0]])
            c.execute("INSERT INTO utmarks values(?,?,?,?,?,?,?,6)",[se12_tot,se12_app,se12_pass,se12_fail,se12_sug,se12_mua,a[0]])
            c.execute("INSERT INTO utmarks values(?,?,?,?,?,?,?,7)",[se21_tot,se21_app,se21_pass,se21_fail,se21_sug,se21_mua,a[0]])
            c.execute("INSERT INTO utmarks values(?,?,?,?,?,?,?,8)",[se22_tot,se22_app,se22_pass,se22_fail,se22_sug,se22_mua,a[0]])

            c.execute("INSERT INTO utmarks values(?,?,?,?,?,?,?,9)",[te11_tot,te11_app,te11_pass,te11_fail,te11_sug,te11_mua,a[0]])
            c.execute("INSERT INTO utmarks values(?,?,?,?,?,?,?,10)",[te12_tot,te12_app,te12_pass,te12_fail,te12_sug,te12_mua,a[0]])
            c.execute("INSERT INTO utmarks values(?,?,?,?,?,?,?,11)",[te21_tot,te21_app,te21_pass,te21_fail,te21_sug,te21_mua,a[0]])
            c.execute("INSERT INTO utmarks values(?,?,?,?,?,?,?,12)",[te22_tot,te22_app,te22_pass,te22_fail,te22_sug,te22_mua,a[0]])
            
            c.execute("INSERT INTO utmarks values(?,?,?,?,?,?,?,13)",[be11_tot,be11_app,be11_pass,be11_fail,be11_sug,be11_mua,a[0]])
            c.execute("INSERT INTO utmarks values(?,?,?,?,?,?,?,14)",[be12_tot,be12_app,be12_pass,be12_fail,be12_sug,be12_mua,a[0]])
            c.execute("INSERT INTO utmarks values(?,?,?,?,?,?,?,15)",[be21_tot,be21_app,be21_pass,be21_fail,be21_sug,be21_mua,a[0]])
            c.execute("INSERT INTO utmarks values(?,?,?,?,?,?,?,16)",[be22_tot,be22_app,be22_pass,be22_fail,be22_sug,be22_mua,a[0]])

        else:
            c.execute("""UPDATE utmarks SET tsub=?,app=?,passed=?,failed=?,sugg=?,makeupact=? WHERE name=? and sub=1""",[fe11_tot,fe11_app,fe11_pass,fe11_fail,fe11_sug,fe11_mua,a[0]])
            c.execute("""UPDATE utmarks SET tsub=?,app=?,passed=?,failed=?,sugg=?,makeupact=? WHERE name=? and sub=2""",[fe12_tot,fe12_app,fe12_pass,fe12_fail,fe12_sug,fe12_mua,a[0]])
            c.execute("""UPDATE utmarks SET tsub=?,app=?,passed=?,failed=?,sugg=?,makeupact=? WHERE name=? and sub=3""",[fe21_tot,fe21_app,fe21_pass,fe21_fail,fe21_sug,fe21_mua,a[0]])
            c.execute("""UPDATE utmarks SET tsub=?,app=?,passed=?,failed=?,sugg=?,makeupact=? WHERE name=? and sub=4""",[fe22_tot,fe22_app,fe22_pass,fe22_fail,fe22_sug,fe22_mua,a[0]])

            c.execute("""UPDATE utmarks SET tsub=?,app=?,passed=?,failed=?,sugg=?,makeupact=? WHERE name=? and sub=5""",[se11_tot,se11_app,se11_pass,se11_fail,se11_sug,se11_mua,a[0]])
            c.execute("""UPDATE utmarks SET tsub=?,app=?,passed=?,failed=?,sugg=?,makeupact=? WHERE name=? and sub=6""",[se12_tot,se12_app,se12_pass,se12_fail,se12_sug,se12_mua,a[0]])
            c.execute("""UPDATE utmarks SET tsub=?,app=?,passed=?,failed=?,sugg=?,makeupact=? WHERE name=? and sub=7""",[se21_tot,se21_app,se21_pass,se21_fail,se21_sug,se21_mua,a[0]])
            c.execute("""UPDATE utmarks SET tsub=?,app=?,passed=?,failed=?,sugg=?,makeupact=? WHERE name=? and sub=8""",[se22_tot,se22_app,se22_pass,se22_fail,se22_sug,se22_mua,a[0]])

            c.execute("""UPDATE utmarks SET tsub=?,app=?,passed=?,failed=?,sugg=?,makeupact=? WHERE name=? and sub=9""",[te11_tot,te11_app,te11_pass,te11_fail,te11_sug,te11_mua,a[0]])
            c.execute("""UPDATE utmarks SET tsub=?,app=?,passed=?,failed=?,sugg=?,makeupact=? WHERE name=? and sub=10""",[te12_tot,te12_app,te12_pass,te12_fail,te12_sug,te12_mua,a[0]])
            c.execute("""UPDATE utmarks SET tsub=?,app=?,passed=?,failed=?,sugg=?,makeupact=? WHERE name=? and sub=11""",[te21_tot,te21_app,te21_pass,te21_fail,te21_sug,te21_mua,a[0]])
            c.execute("""UPDATE utmarks SET tsub=?,app=?,passed=?,failed=?,sugg=?,makeupact=? WHERE name=? and sub=12""",[te22_tot,te22_app,te22_pass,te22_fail,te22_sug,te22_mua,a[0]])

            c.execute("""UPDATE utmarks SET tsub=?,app=?,passed=?,failed=?,sugg=?,makeupact=? WHERE name=? and sub=13""",[be11_tot,be11_app,be11_pass,be11_fail,be11_sug,be11_mua,a[0]])
            c.execute("""UPDATE utmarks SET tsub=?,app=?,passed=?,failed=?,sugg=?,makeupact=? WHERE name=? and sub=14""",[be12_tot,be12_app,be12_pass,be12_fail,be12_sug,be12_mua,a[0]])
            c.execute("""UPDATE utmarks SET tsub=?,app=?,passed=?,failed=?,sugg=?,makeupact=? WHERE name=? and sub=15""",[be21_tot,be21_app,be21_pass,be21_fail,be21_sug,be21_mua,a[0]])
            c.execute("""UPDATE utmarks SET tsub=?,app=?,passed=?,failed=?,sugg=?,makeupact=? WHERE name=? and sub=16""",[be22_tot,be22_app,be22_pass,be22_fail,be22_sug,be22_mua,a[0]])

        conn.commit()
        c.close()
        conn.close()
        
        self.hide()
        self.s8 = SA16()
        self.s8.show()

    def viewbtn(self):
        conn = sqlite3.connect("data.db")
        c=conn.cursor()
        
        tsub=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        app=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        passed=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        failed=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        sugg=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        makeup=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        i=0
        sql = "select name from extra desc limit -1"
        c.execute(sql)
        name = c.fetchall()
        list1 = list(name)
        for a in list1:
            n=0
        c.execute("SELECT tsub,app,passed,failed,sugg,makeupact FROM utmarks WHERE name=?",[a[0]])
        row=c.fetchone()
        for j in range(0,16):
            tsub[i]=str(row[0])
            app[i]=str(row[1])
            passed[i]=str(row[2])
            failed[i]=str(row[3])
            sugg[i]=str(row[4])
            makeup[i]=str(row[5])
            i=i+1
            row=c.fetchone()

        c.close()
        conn.close()

        self.lineEdit.setText(tsub[0])
        self.lineEdit_2.setText(app[0])
        self.lineEdit_3.setText(passed[0])
        self.lineEdit_4.setText(failed[0])
        self.lineEdit_5.setText(sugg[0])
        self.lineEdit_6.setText(makeup[0])
        
        self.lineEdit_7.setText(tsub[1])
        self.lineEdit_8.setText(app[1])
        self.lineEdit_9.setText(passed[1])
        self.lineEdit_11.setText(failed[1])
        self.lineEdit_10.setText(sugg[1])
        self.lineEdit_12.setText(makeup[1])
        
        self.lineEdit_13.setText(tsub[2])
        self.lineEdit_15.setText(app[2])
        self.lineEdit_18.setText(passed[2])
        self.lineEdit_24.setText(failed[2])
        self.lineEdit_21.setText(sugg[2])
        self.lineEdit_16.setText(makeup[2])
        
        self.lineEdit_19.setText(tsub[3])
        self.lineEdit_17.setText(app[3])
        self.lineEdit_14.setText(passed[3])
        self.lineEdit_23.setText(failed[3])
        self.lineEdit_20.setText(sugg[3])
        self.lineEdit_22.setText(makeup[3])
        
        self.lineEdit_29.setText(tsub[4])
        self.lineEdit_35.setText(app[4])
        self.lineEdit_33.setText(passed[4])
        self.lineEdit_27.setText(failed[4])
        self.lineEdit_42.setText(sugg[4])
        self.lineEdit_40.setText(makeup[4])
        
        self.lineEdit_30.setText(tsub[5])
        self.lineEdit_26.setText(app[5])
        self.lineEdit_38.setText(passed[5])
        self.lineEdit_46.setText(failed[5])
        self.lineEdit_32.setText(sugg[5])
        self.lineEdit_44.setText(makeup[5])
        
        self.lineEdit_45.setText(tsub[6])
        self.lineEdit_31.setText(app[6])
        self.lineEdit_36.setText(passed[6])
        self.lineEdit_41.setText(failed[6])
        self.lineEdit_48.setText(sugg[6])
        self.lineEdit_34.setText(makeup[6])
        
        self.lineEdit_28.setText(tsub[7])
        self.lineEdit_47.setText(app[7])
        self.lineEdit_39.setText(passed[7])
        self.lineEdit_25.setText(failed[7])
        self.lineEdit_43.setText(sugg[7])
        self.lineEdit_37.setText(makeup[7])
        
        self.lineEdit_88.setText(tsub[8])
        self.lineEdit_83.setText(app[8])
        self.lineEdit_75.setText(passed[8])
        self.lineEdit_70.setText(failed[8])
        self.lineEdit_55.setText(sugg[8])
        self.lineEdit_59.setText(makeup[8])
        
        self.lineEdit_49.setText(tsub[9])
        self.lineEdit_80.setText(app[9])
        self.lineEdit_65.setText(passed[9])
        self.lineEdit_91.setText(failed[9])
        self.lineEdit_96.setText(sugg[9])
        self.lineEdit_66.setText(makeup[9])
        
        self.lineEdit_77.setText(tsub[10])
        self.lineEdit_90.setText(app[10])
        self.lineEdit_76.setText(passed[10])
        self.lineEdit_61.setText(failed[10])
        self.lineEdit_72.setText(sugg[10])
        self.lineEdit_92.setText(makeup[10])
        
        self.lineEdit_86.setText(tsub[11])
        self.lineEdit_87.setText(app[11])
        self.lineEdit_95.setText(passed[11])
        self.lineEdit_63.setText(failed[11])
        self.lineEdit_54.setText(sugg[11])
        self.lineEdit_58.setText(makeup[11])
        
        self.lineEdit_68.setText(tsub[12])
        self.lineEdit_69.setText(app[12])
        self.lineEdit_64.setText(passed[12])
        self.lineEdit_82.setText(failed[12])
        self.lineEdit_67.setText(sugg[12])
        self.lineEdit_71.setText(makeup[12])
        
        self.lineEdit_85.setText(tsub[13])
        self.lineEdit_81.setText(app[13])
        self.lineEdit_62.setText(passed[13])
        self.lineEdit_51.setText(failed[13])
        self.lineEdit_73.setText(sugg[13])
        self.lineEdit_50.setText(makeup[13])
        
        self.lineEdit_57.setText(tsub[14])
        self.lineEdit_74.setText(app[14])
        self.lineEdit_93.setText(passed[14])
        self.lineEdit_56.setText(failed[14])
        self.lineEdit_60.setText(sugg[14])
        self.lineEdit_89.setText(makeup[14])
        
        self.lineEdit_52.setText(tsub[15])
        self.lineEdit_84.setText(app[15])
        self.lineEdit_79.setText(passed[15])
        self.lineEdit_94.setText(failed[15])
        self.lineEdit_78.setText(sugg[15])
        self.lineEdit_53.setText(makeup[15])

    def back(self):
        self.hide()
        self.s8 = SA14()
        self.s8.show()

class SA16(QtWidgets.QMainWindow,sppu_markss.Ui_sppu):
    def __init__(self,parent=None):
        super(SA16,self).__init__(parent)
        self.setupUi(self)
        self.btn_SUBMIT.clicked.connect(self.sppu)
        self.btn_SUBMIT_2.clicked.connect(self.back)
        self.btn_SUBMIT_3.clicked.connect(self.view)

    def sppu(self):

        mandy=["","","","","","","",""]
        seatno=["","","","","","","",""]
        result=["","","","","","","",""]
        sugg=["","","","","","","",""]
        agg=[1,1,1,1,1,1,1,1]
        years=["FE","FE","SE","SE","TE","TE","BE","BE"]

        mandy[0]=str(self.lineEdit.text())
        mandy[1]=str(self.lineEdit_9.text())
        mandy[2]=str(self.lineEdit_14.text())
        mandy[3]=str(self.lineEdit_19.text())
        mandy[4]=str(self.lineEdit_24.text())
        mandy[5]=str(self.lineEdit_29.text())
        mandy[6]=str(self.lineEdit_34.text())
        mandy[7]=str(self.lineEdit_39.text())

        seatno[0]=str(self.lineEdit_2.text())
        seatno[1]=str(self.lineEdit_6.text())
        seatno[2]=str(self.lineEdit_11.text())
        seatno[3]=str(self.lineEdit_16.text())
        seatno[4]=str(self.lineEdit_21.text())
        seatno[5]=str(self.lineEdit_26.text())
        seatno[6]=str(self.lineEdit_31.text())
        seatno[7]=str(self.lineEdit_36.text())

        result[0]=str(self.lineEdit_3.text())
        result[1]=str(self.lineEdit_10.text())
        result[2]=str(self.lineEdit_15.text())
        result[3]=str(self.lineEdit_20.text())
        result[4]=str(self.lineEdit_25.text())
        result[5]=str(self.lineEdit_30.text())
        result[6]=str(self.lineEdit_35.text())
        result[7]=str(self.lineEdit_40.text())

        sugg[0]=str(self.lineEdit_4.text())
        sugg[1]=str(self.lineEdit_7.text())
        sugg[2]=str(self.lineEdit_12.text())
        sugg[3]=str(self.lineEdit_17.text())
        sugg[4]=str(self.lineEdit_22.text())
        sugg[5]=str(self.lineEdit_27.text())
        sugg[6]=str(self.lineEdit_32.text())
        sugg[7]=str(self.lineEdit_37.text())

        agg[0]=str(self.lineEdit_5.text())
        agg[1]=str(self.lineEdit_8.text())
        agg[2]=str(self.lineEdit_13.text())
        agg[3]=str(self.lineEdit_18.text())
        agg[4]=str(self.lineEdit_23.text())
        agg[5]=str(self.lineEdit_28.text())
        agg[6]=str(self.lineEdit_33.text())
        agg[7]=str(self.lineEdit_38.text())
        
        conn = sqlite3.connect("data.db")
        c=conn.cursor()

        sql = "select name from extra desc limit -1"
        c.execute(sql)
        name = c.fetchall()
        list1 = list(name)
        for a in list1:
            n=0

        c.execute("SELECT mandy FROM sppuper WHERE name=?",[a[0]])
        get=c.fetchall()
        list1=list(get)

        if not list1:
            c.execute("insert into sppuper values(1,?,?,?,?,?,?,?)",[years[0],mandy[0],seatno[0],result[0],sugg[0],agg[0],a[0]])
            c.execute("insert into sppuper values(2,?,?,?,?,?,?,?)",[years[1],mandy[1],seatno[1],result[1],sugg[1],agg[1],a[0]])
            c.execute("insert into sppuper values(3,?,?,?,?,?,?,?)",[years[2],mandy[2],seatno[2],result[2],sugg[2],agg[2],a[0]])
            c.execute("insert into sppuper values(4,?,?,?,?,?,?,?)",[years[3],mandy[3],seatno[3],result[3],sugg[3],agg[3],a[0]])
            c.execute("insert into sppuper values(5,?,?,?,?,?,?,?)",[years[4],mandy[4],seatno[4],result[4],sugg[4],agg[4],a[0]])
            c.execute("insert into sppuper values(6,?,?,?,?,?,?,?)",[years[5],mandy[5],seatno[5],result[5],sugg[5],agg[5],a[0]])
            c.execute("insert into sppuper values(7,?,?,?,?,?,?,?)",[years[6],mandy[6],seatno[6],result[6],sugg[6],agg[6],a[0]])
            c.execute("insert into sppuper values(8,?,?,?,?,?,?,?)",[years[7],mandy[7],seatno[7],result[7],sugg[7],agg[7],a[0]])
            conn.commit()

        else:
            c.execute("update sppuper set mandy=?,seatno=?,result=?,sugg=?,agg=? where srno=1 and name=?",[mandy[0],seatno[0],result[0],sugg[0],agg[0],a[0]])
            c.execute("update sppuper set mandy=?,seatno=?,result=?,sugg=?,agg=? where srno=2 and name=?",[mandy[1],seatno[1],result[1],sugg[1],agg[1],a[0]])
            c.execute("update sppuper set mandy=?,seatno=?,result=?,sugg=?,agg=? where srno=3 and name=?",[mandy[2],seatno[2],result[2],sugg[2],agg[2],a[0]])
            c.execute("update sppuper set mandy=?,seatno=?,result=?,sugg=?,agg=? where srno=4 and name=?",[mandy[3],seatno[3],result[3],sugg[3],agg[3],a[0]])
            c.execute("update sppuper set mandy=?,seatno=?,result=?,sugg=?,agg=? where srno=5 and name=?",[mandy[4],seatno[4],result[4],sugg[4],agg[4],a[0]])
            c.execute("update sppuper set mandy=?,seatno=?,result=?,sugg=?,agg=? where srno=6 and name=?",[mandy[5],seatno[5],result[5],sugg[5],agg[5],a[0]])
            c.execute("update sppuper set mandy=?,seatno=?,result=?,sugg=?,agg=? where srno=7 and name=?",[mandy[6],seatno[6],result[6],sugg[6],agg[6],a[0]])
            c.execute("update sppuper set mandy=?,seatno=?,result=?,sugg=?,agg=? where srno=8 and name=?",[mandy[7],seatno[7],result[7],sugg[7],agg[7],a[0]])
            conn.commit()

        c.close()
        conn.close()
        
        self.hide()
        self.s8 = SA17()
        self.s8.show()

    def view(self):
        conn = sqlite3.connect("data.db")
        c=conn.cursor()

        sql = "select name from extra desc limit -1"
        c.execute(sql)
        name = c.fetchall()
        list1 = list(name)
        for a in list1:
            n=0

        mandy=["","","","","","","",""]
        seatno=["","","","","","","",""]
        result=["","","","","","","",""]
        sugg=["","","","","","","",""]
        agg=[1,1,1,1,1,1,1,1]

        c.execute("select mandy,seatno,result,sugg,agg from sppuper where name=?",[a[0]])
        row=c.fetchone()
        i=0
        while row is not None:
           mandy[i]=row[0]
           seatno[i]=row[1]
           result[i]=row[2]
           sugg[i]=row[3]
           agg[i]=row[4]
           i=i+1
           row=c.fetchone()

        c.close()
        conn.close()

        self.lineEdit.setText(mandy[0])
        self.lineEdit_9.setText(mandy[1])
        self.lineEdit_14.setText(mandy[2])
        self.lineEdit_19.setText(mandy[3])
        self.lineEdit_24.setText(mandy[4])
        self.lineEdit_29.setText(mandy[5])
        self.lineEdit_34.setText(mandy[6])
        self.lineEdit_39.setText(mandy[7])

        self.lineEdit_2.setText(seatno[0])
        self.lineEdit_6.setText(seatno[1])
        self.lineEdit_11.setText(seatno[2])
        self.lineEdit_16.setText(seatno[3])
        self.lineEdit_21.setText(seatno[4])
        self.lineEdit_26.setText(seatno[5])
        self.lineEdit_31.setText(seatno[6])
        self.lineEdit_36.setText(seatno[7])

        self.lineEdit_3.setText(result[0])
        self.lineEdit_10.setText(result[1])
        self.lineEdit_15.setText(result[2])
        self.lineEdit_20.setText(result[3])
        self.lineEdit_25.setText(result[4])
        self.lineEdit_30.setText(result[5])
        self.lineEdit_35.setText(result[6])
        self.lineEdit_40.setText(result[7])

        self.lineEdit_4.setText(sugg[0])
        self.lineEdit_7.setText(sugg[1])
        self.lineEdit_12.setText(sugg[2])
        self.lineEdit_17.setText(sugg[3])
        self.lineEdit_22.setText(sugg[4])
        self.lineEdit_27.setText(sugg[5])
        self.lineEdit_32.setText(sugg[6])
        self.lineEdit_37.setText(sugg[7])

        self.lineEdit_5.setText(agg[0])
        self.lineEdit_8.setText(agg[1])
        self.lineEdit_13.setText(agg[2])
        self.lineEdit_18.setText(agg[3])
        self.lineEdit_23.setText(agg[4])
        self.lineEdit_28.setText(agg[5])
        self.lineEdit_33.setText(agg[6])
        self.lineEdit_38.setText(agg[7])

    def back(self):
        self.hide()
        self.s8 = SA15()
        self.s8.show()

class SA17(QtWidgets.QMainWindow,criticals.Ui_cri):
    def __init__(self,parent=None):
        super(SA17,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.back)
        self.pushButton_3.clicked.connect(self.view)

    def login(self):
        analysis=["","","","","","","",""]
        years=["FE","FE","SE","SE","TE","TE","BE","BE"]

        analysis[0]=str(self.lineEdit.text())
        analysis[1]=str(self.lineEdit_2.text())
        analysis[2]=str(self.lineEdit_3.text())
        analysis[3]=str(self.lineEdit_4.text())
        analysis[4]=str(self.lineEdit_7.text())
        analysis[5]=str(self.lineEdit_8.text())
        analysis[6]=str(self.lineEdit_5.text())
        analysis[7]=str(self.lineEdit_6.text())

        conn = sqlite3.connect("data.db")
        c=conn.cursor()

        sql = "select name from extra desc limit -1"
        c.execute(sql)
        name = c.fetchall()
        list1 = list(name)
        for a in list1:
            n=0

        c.execute("SELECT analysis FROM acca WHERE name=?",[a[0]])
        get=c.fetchall()
        list1=list(get)

        if not list1:
            c.execute("insert into acca(class,sem,analysis,name) values(?,1,?,?)",[years[0],analysis[0],a[0]])
            c.execute("insert into acca(class,sem,analysis,name) values(?,2,?,?)",[years[1],analysis[1],a[0]])
            c.execute("insert into acca(class,sem,analysis,name) values(?,3,?,?)",[years[2],analysis[2],a[0]])
            c.execute("insert into acca(class,sem,analysis,name) values(?,4,?,?)",[years[3],analysis[3],a[0]])
            c.execute("insert into acca(class,sem,analysis,name) values(?,5,?,?)",[years[4],analysis[4],a[0]])
            c.execute("insert into acca(class,sem,analysis,name) values(?,6,?,?)",[years[5],analysis[5],a[0]])
            c.execute("insert into acca(class,sem,analysis,name) values(?,7,?,?)",[years[6],analysis[6],a[0]])
            c.execute("insert into acca(class,sem,analysis,name) values(?,8,?,?)",[years[7],analysis[7],a[0]])
            conn.commit()

        else:
            c.execute("update acca set analysis=? where sem=1 and name=?",[analysis[0],a[0]])
            c.execute("update acca set analysis=? where sem=2 and name=?",[analysis[1],a[0]])
            c.execute("update acca set analysis=? where sem=3 and name=?",[analysis[2],a[0]])
            c.execute("update acca set analysis=? where sem=4 and name=?",[analysis[3],a[0]])
            c.execute("update acca set analysis=? where sem=5 and name=?",[analysis[4],a[0]])
            c.execute("update acca set analysis=? where sem=6 and name=?",[analysis[5],a[0]])
            c.execute("update acca set analysis=? where sem=7 and name=?",[analysis[6],a[0]])
            c.execute("update acca set analysis=? where sem=8 and name=?",[analysis[7],a[0]])
            conn.commit()
            
        c.close()
        conn.close()
        
        self.hide()
        self.s8 = SA18()
        self.s8.show()

    def view(self):
        conn = sqlite3.connect("data.db")
        c=conn.cursor()

        sql = "select name from extra desc limit -1"
        c.execute(sql)
        name = c.fetchall()
        list1 = list(name)
        for a in list1:
            n=0

        analysis=["","","","","","","",""]

        c.execute("select analysis from acca where name=?",[a[0]])  
        row=c.fetchone()
        i=0
        while row is not None:
            analysis[i]=row[0]
            i=i+1
            row=c.fetchone()

        self.lineEdit.setText(analysis[0])
        self.lineEdit_2.setText(analysis[1])
        self.lineEdit_3.setText(analysis[2])
        self.lineEdit_4.setText(analysis[3])
        self.lineEdit_7.setText(analysis[4])
        self.lineEdit_8.setText(analysis[5])
        self.lineEdit_5.setText(analysis[6])
        self.lineEdit_6.setText(analysis[7])

        c.close()
        conn.close()

    def back(self):
        self.hide()
        self.s8 = SA16()
        self.s8.show()

class SA18(QtWidgets.QMainWindow,cocurriculars.Ui_coc):
    def __init__(self,parent=None):
        super(SA18,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.view)
        self.pushButton_3.clicked.connect(self.back)

    def login(self):

        activities=["","","","","","","",""]
        performance=["","","","","","","",""]

        activities[0]=str(self.lineEdit.text())
        activities[1]=str(self.lineEdit_3.text())
        activities[2]=str(self.lineEdit_5.text())
        activities[3]=str(self.lineEdit_6.text())
        activities[4]=str(self.lineEdit_7.text())
        activities[5]=str(self.lineEdit_8.text())
        activities[6]=str(self.lineEdit_9.text())
        activities[7]=str(self.lineEdit_10.text())

        performance[0]=str(self.lineEdit_2.text())
        performance[1]=str(self.lineEdit_4.text())
        performance[2]=str(self.lineEdit_11.text())
        performance[3]=str(self.lineEdit_12.text())
        performance[4]=str(self.lineEdit_13.text())
        performance[5]=str(self.lineEdit_14.text())
        performance[6]=str(self.lineEdit_15.text())
        performance[7]=str(self.lineEdit_16.text())

        conn = sqlite3.connect("data.db")
        c=conn.cursor()

        sql = "select name from extra desc limit -1"
        c.execute(sql)
        name = c.fetchall()
        list1 = list(name)
        for a in list1:
            n=0

        c.execute("SELECT activities FROM acca WHERE name=?",[a[0]])
        get=c.fetchall()
        list1=list(get)

        if not list1:
            c.execute("insert into acca(activities,performance) values(?,?) where sem=1 and name=?",[activities[0],performance[0],a[0]])
            c.execute("insert into acca(activities,performance) values(?,?) where sem=2 and name=?",[activities[1],performance[1],a[0]])
            c.execute("insert into acca(activities,performance) values(?,?) where sem=3 and name=?",[activities[2],performance[2],a[0]])
            c.execute("insert into acca(activities,performance) values(?,?) where sem=4 and name=?",[activities[3],performance[3],a[0]])
            c.execute("insert into acca(activities,performance) values(?,?) where sem=5 and name=?",[activities[4],performance[4],a[0]])
            c.execute("insert into acca(activities,performance) values(?,?) where sem=6 and name=?",[activities[5],performance[5],a[0]])
            c.execute("insert into acca(activities,performance) values(?,?) where sem=7 and name=?",[activities[6],performance[6],a[0]])
            c.execute("insert into acca(activities,performance) values(?,?) where sem=8 and name=?",[activities[7],performance[7],a[0]])
            conn.commit()

        else:
            c.execute("update acca set activities=?,performance=? where sem=1 and name=?",[activities[0],performance[0],a[0]])
            c.execute("update acca set activities=?,performance=? where sem=2 and name=?",[activities[1],performance[1],a[0]])
            c.execute("update acca set activities=?,performance=? where sem=3 and name=?",[activities[2],performance[2],a[0]])
            c.execute("update acca set activities=?,performance=? where sem=4 and name=?",[activities[3],performance[3],a[0]])
            c.execute("update acca set activities=?,performance=? where sem=5 and name=?",[activities[4],performance[4],a[0]])
            c.execute("update acca set activities=?,performance=? where sem=6 and name=?",[activities[5],performance[5],a[0]])
            c.execute("update acca set activities=?,performance=? where sem=7 and name=?",[activities[6],performance[6],a[0]])
            c.execute("update acca set activities=?,performance=? where sem=8 and name=?",[activities[7],performance[7],a[0]])
            conn.commit()

        c.close()
        conn.close()
        
        self.hide()
        self.s8 = SA19()
        self.s8.show()
        
    def view(self):
        
        conn = sqlite3.connect("data.db")
        c=conn.cursor()

        sql = "select name from extra desc limit -1"
        c.execute(sql)
        name = c.fetchall()
        list1 = list(name)
        for a in list1:
            n=0

        activities=["","","","","","","",""]
        performance=["","","","","","","",""]

        c.execute("select activities,performance from acca where name=?",[a[0]])  
        row=c.fetchone()
        i=0
        while row is not None:
            activities[i]=row[0]
            performance[i]=row[1]
            i=i+1
            row=c.fetchone()

        self.lineEdit.setText(activities[0])
        self.lineEdit_3.setText(activities[1])
        self.lineEdit_5.setText(activities[2])
        self.lineEdit_6.setText(activities[3])
        self.lineEdit_7.setText(activities[4])
        self.lineEdit_8.setText(activities[5])
        self.lineEdit_9.setText(activities[6])
        self.lineEdit_10.setText(activities[7])
        
        self.lineEdit_2.setText(performance[0])
        self.lineEdit_4.setText(performance[1])
        self.lineEdit_11.setText(performance[2])
        self.lineEdit_12.setText(performance[3])
        self.lineEdit_13.setText(performance[4])
        self.lineEdit_14.setText(performance[5])
        self.lineEdit_15.setText(performance[6])
        self.lineEdit_16.setText(performance[7])
        
        c.close()
        conn.close()

    def back(self):
        self.hide()
        self.s8 = SA17()
        self.s8.show()

class SA19(QtWidgets.QMainWindow,ATT_RECORDS.Ui_MainWindowAtt):
    def __init__(self,parent=None):
        super(SA19,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushbtn)
        self.pushButton_2.clicked.connect(self.view)
        self.pushButton_3.clicked.connect(self.back)

    def pushbtn(self):
        fe=[[1,1,1,1,1],[1,1,1,1,1]]
        se=[[1,1,1,1,1],[1,1,1,1,1]]
        te=[[1,1,1,1,1],[1,1,1,1,1]]
        be=[[1,1,1,1,1],[1,1,1,1,1]]

        fe[0][0]=self.lineEdit.text()
        fe[0][1]=self.lineEdit_5.text()
        fe[0][2]=self.lineEdit_4.text()
        fe[0][3]=self.lineEdit_2.text()
        fe[0][4]=self.lineEdit_3.text()
        fe[1][0]=self.lineEdit_9.text()
        fe[1][1]=self.lineEdit_7.text()
        fe[1][2]=self.lineEdit_8.text()
        fe[1][3]=self.lineEdit_10.text()
        fe[1][4]=self.lineEdit_6.text()
        
        se[0][0]=self.lineEdit_14.text()
        se[0][1]=self.lineEdit_12.text()
        se[0][2]=self.lineEdit_13.text()
        se[0][3]=self.lineEdit_15.text()
        se[0][4]=self.lineEdit_11.text()
        se[1][0]=self.lineEdit_19.text()
        se[1][1]=self.lineEdit_17.text()
        se[1][2]=self.lineEdit_18.text()
        se[1][3]=self.lineEdit_20.text()
        se[1][4]=self.lineEdit_16.text()

        te[0][0]=self.lineEdit_24.text()
        te[0][1]=self.lineEdit_22.text()
        te[0][2]=self.lineEdit_23.text()
        te[0][3]=self.lineEdit_21.text()
        te[0][4]=self.lineEdit_25.text()
        te[1][0]=self.lineEdit_29.text()
        te[1][1]=self.lineEdit_27.text()
        te[1][2]=self.lineEdit_28.text()
        te[1][3]=self.lineEdit_26.text()
        te[1][4]=self.lineEdit_30.text()

        be[0][0]=self.lineEdit_34.text()
        be[0][1]=self.lineEdit_32.text()
        be[0][2]=self.lineEdit_33.text()
        be[0][3]=self.lineEdit_31.text()
        be[0][4]=self.lineEdit_35.text()
        be[1][0]=self.lineEdit_39.text()
        be[1][1]=self.lineEdit_37.text()
        be[1][2]=self.lineEdit_38.text()
        be[1][3]=self.lineEdit_36.text()
        be[1][4]=self.lineEdit_40.text()

        conn = sqlite3.connect("data.db")
        c=conn.cursor()

        sql = "select name from extra desc limit -1"
        c.execute(sql)
        name = c.fetchall()
        list1 = list(name)
        for a in list1:
            n=0

        c.execute("SELECT a1 FROM acca WHERE name=?",[a[0]])
        get=c.fetchall()
        list1=list(get)

        if not list1:
            c.execute("insert into acca(a1,a2,a3,a4,a5) values(?,?,?,?,?) where sem=1 and name=?",[str(fe[0][0]),str(fe[0][1]),str(fe[0][2]),str(fe[0][3]),str(fe[0][4]),a[0]])
            c.execute("insert into acca(a1,a2,a3,a4,a5) values(?,?,?,?,?) where sem=1 and name=?",[str(fe[1][0]),str(fe[1][1]),str(fe[1][2]),str(fe[1][3]),str(fe[1][4]),a[0]])
            c.execute("insert into acca(a1,a2,a3,a4,a5) values(?,?,?,?,?) where sem=1 and name=?",[str(se[0][0]),str(se[0][1]),str(se[0][2]),str(se[0][3]),str(se[0][4]),a[0]])
            c.execute("insert into acca(a1,a2,a3,a4,a5) values(?,?,?,?,?) where sem=1 and name=?",[str(se[1][0]),str(se[1][1]),str(se[1][2]),str(se[1][3]),str(se[1][4]),a[0]])
            c.execute("insert into acca(a1,a2,a3,a4,a5) values(?,?,?,?,?) where sem=1 and name=?",[str(te[0][0]),str(te[0][1]),str(te[0][2]),str(te[0][3]),str(te[0][4]),a[0]])
            c.execute("insert into acca(a1,a2,a3,a4,a5) values(?,?,?,?,?) where sem=1 and name=?",[str(te[1][0]),str(te[1][1]),str(te[1][2]),str(te[1][3]),str(te[1][4]),a[0]])
            c.execute("insert into acca(a1,a2,a3,a4,a5) values(?,?,?,?,?) where sem=1 and name=?",[str(be[0][0]),str(be[0][1]),str(be[0][2]),str(be[0][3]),str(be[0][4]),a[0]])
            c.execute("insert into acca(a1,a2,a3,a4,a5) values(?,?,?,?,?) where sem=1 and name=?",[str(be[1][0]),str(be[1][1]),str(be[1][2]),str(be[1][3]),str(be[1][4]),a[0]])
            conn.commit()

        else:
            c.execute("update acca set a1=?,a2=?,a3=?,a4=?,a5=? where sem=1 and name=?",[str(fe[0][0]),str(fe[0][1]),str(fe[0][2]),str(fe[0][3]),str(fe[0][4]),a[0]])
            c.execute("update acca set a1=?,a2=?,a3=?,a4=?,a5=? where sem=2 and name=?",[str(fe[1][0]),str(fe[1][1]),str(fe[1][2]),str(fe[1][3]),str(fe[1][4]),a[0]])
            c.execute("update acca set a1=?,a2=?,a3=?,a4=?,a5=? where sem=3 and name=?",[str(se[0][0]),str(se[0][1]),str(se[0][2]),str(se[0][3]),str(se[0][4]),a[0]])
            c.execute("update acca set a1=?,a2=?,a3=?,a4=?,a5=? where sem=4 and name=?",[str(se[1][0]),str(se[1][1]),str(se[1][2]),str(se[1][3]),str(se[1][4]),a[0]])
            c.execute("update acca set a1=?,a2=?,a3=?,a4=?,a5=? where sem=5 and name=?",[str(te[0][0]),str(te[0][1]),str(te[0][2]),str(te[0][3]),str(te[0][4]),a[0]])
            c.execute("update acca set a1=?,a2=?,a3=?,a4=?,a5=? where sem=6 and name=?",[str(te[1][0]),str(te[1][1]),str(te[1][2]),str(te[1][3]),str(te[1][4]),a[0]])
            c.execute("update acca set a1=?,a2=?,a3=?,a4=?,a5=? where sem=7 and name=?",[str(be[0][0]),str(be[0][1]),str(be[0][2]),str(be[0][3]),str(be[0][4]),a[0]])
            c.execute("update acca set a1=?,a2=?,a3=?,a4=?,a5=? where sem=8 and name=?",[str(be[1][0]),str(be[1][1]),str(be[1][2]),str(be[1][3]),str(be[1][4]),a[0]])
            conn.commit()

        c.close()
        conn.close()

    def view(self):
        conn = sqlite3.connect("data.db")
        c=conn.cursor()

        sql = "select name from extra desc limit -1"
        c.execute(sql)
        name = c.fetchall()
        list1 = list(name)
        for a in list1:
            n=0

        fe=[[1,1,1,1,1],[1,1,1,1,1]]
        se=[[1,1,1,1,1],[1,1,1,1,1]]
        te=[[1,1,1,1,1],[1,1,1,1,1]]
        be=[[1,1,1,1,1],[1,1,1,1,1]]

        c.execute("select a1,a2,a3,a4,a5 from acca where name=?",[a[0]])  
        row=c.fetchone()
        i=0
        while row is not None:
            if i<2:
                fe[i][0]=row[0]
                fe[i][1]=row[1]
                fe[i][2]=row[2]
                fe[i][3]=row[3]
                fe[i][4]=row[4]
            elif i<4:
                se[i-2][0]=row[0]
                se[i-2][1]=row[1]
                se[i-2][2]=row[2]
                se[i-2][3]=row[3]
                se[i-2][4]=row[4]
            elif i<6:
                te[i-4][0]=row[0]
                te[i-4][1]=row[1]
                te[i-4][2]=row[2]
                te[i-4][3]=row[3]
                te[i-4][4]=row[4]
            else:
                be[i-6][0]=row[0]
                be[i-6][1]=row[1]
                be[i-6][2]=row[2]
                be[i-6][3]=row[3]
                be[i-6][4]=row[4]
            i=i+1
            row=c.fetchone()

        self.lineEdit.setText(str(fe[0][0]))
        self.lineEdit_5.setText(str(fe[0][1]))
        self.lineEdit_4.setText(str(fe[0][2]))
        self.lineEdit_2.setText(str(fe[0][3]))
        self.lineEdit_3.setText(str(fe[0][4]))
        self.lineEdit_9.setText(str(fe[1][0]))
        self.lineEdit_7.setText(str(fe[1][1]))
        self.lineEdit_8.setText(str(fe[1][2]))
        self.lineEdit_10.setText(str(fe[1][3]))
        self.lineEdit_6.setText(str(fe[1][4]))
        
        self.lineEdit_14.setText(str(se[0][0]))
        self.lineEdit_12.setText(str(se[0][1]))
        self.lineEdit_13.setText(str(se[0][2]))
        self.lineEdit_15.setText(str(se[0][3]))
        self.lineEdit_11.setText(str(se[0][4]))
        self.lineEdit_19.setText(str(se[1][0]))
        self.lineEdit_17.setText(str(se[1][1]))
        self.lineEdit_18.setText(str(se[1][2]))
        self.lineEdit_20.setText(str(se[1][3]))
        self.lineEdit_16.setText(str(se[1][4]))
        
        self.lineEdit_24.setText(str(te[0][0]))
        self.lineEdit_22.setText(str(te[0][1]))
        self.lineEdit_23.setText(str(te[0][2]))
        self.lineEdit_21.setText(str(te[0][3]))
        self.lineEdit_25.setText(str(te[0][4]))
        self.lineEdit_29.setText(str(te[1][0]))
        self.lineEdit_27.setText(str(te[1][1]))
        self.lineEdit_28.setText(str(te[1][2]))
        self.lineEdit_26.setText(str(te[1][3]))
        self.lineEdit_30.setText(str(te[1][4]))
        
        self.lineEdit_34.setText(str(be[0][0]))
        self.lineEdit_32.setText(str(be[0][1]))
        self.lineEdit_33.setText(str(be[0][2]))
        self.lineEdit_31.setText(str(be[0][3]))
        self.lineEdit_35.setText(str(be[0][4]))
        self.lineEdit_39.setText(str(be[1][0]))
        self.lineEdit_37.setText(str(be[1][1]))
        self.lineEdit_38.setText(str(be[1][2]))
        self.lineEdit_36.setText(str(be[1][3]))
        self.lineEdit_40.setText(str(be[1][4]))
        
        c.close()
        conn.close()

    def back(self):
        self.hide()
        self.s8 = SA18()
        self.s8.show()

class mes_fun():
	def message_fun(self,ms):
		msgBox = QMessageBox()
		msgBox.setIcon(QMessageBox.Warning)
		msgBox.setWindowTitle("Attention!")
		msgBox.setText("ERROR                                                     ")
		msgBox.setInformativeText(ms)
		msgBox.setStandardButtons(QMessageBox.Ok)
		msgBox.setDefaultButton(QMessageBox.Ok)
		retval = msgBox.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    s1 = SA1()
    s1.show()
    sys.exit(app.exec_())
