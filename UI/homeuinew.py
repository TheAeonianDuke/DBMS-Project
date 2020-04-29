# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import last_transaction_new, loyaltyui
import sqlite3
import samikharshcombined
import customerAnalytics

class Ui_MainWindow(object):
    def __init__(self,thiswindow,id):
        self.id = id
        self.thiswindow=thiswindow
        
    
    def openWindowLogout(self):
        self.window = QtWidgets.QMainWindow()
        # self.ui = last_transaction_ui.Ui_MainWindow() #take from Abhishek's login file
        # self.ui.setupUi(self.window)
        self.thiswindow.hide()
        self.window.show()
    def openWindowLoyalty(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = loyaltyui.Ui_MainWindow(self.id,self.window)
        self.ui.setupUi(self.window)
        self.thiswindow.hide()
        self.window.show()
    def openWindowLastTransaction(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = last_transaction_new.Ui_MainWindow(self.id,self.window)
        self.ui.setupUi(self.window)
        self.thiswindow.hide()
        self.window.show()
    def openWindowInsight(self,):
        self.window = QtWidgets.QMainWindow()
        self.ui = customerAnalytics.UiCustomerAnalytics(self.id)
        self.thiswindow.hide()

    def openWindowShop(self):
        self.window = QtWidgets.QMainWindow()
        # self.ui = last_transaction_ui.Ui_MainWindow() #Take from Harsh's Map/shop file
        # self.ui.setupUi(self.window)
        self.shopwindow = samikharshcombined.Combined(self.window,self.id)
        self.thiswindow.hide()
        self.window.show()
    def fillProfile(self): # returns a tuple of all the attributes
        db=sqlite3.connect("dbms_db.db")
        cur=db.cursor()
        cur.execute("SELECT first_name,last_name,gender,age,phone FROM users WHERE user_id = ?", (self.id,))
        tup=cur.fetchone()
        #print(tup[0]+tup[1])
        # name=tup[0]+" "+tup[1]
        # gender=tup[2]
        # age=tup[3]
        # phone=tup[4]
        # self.name_input.setText(name)
        #print(name,gender,age,phone)
        #print("Passed")
        return tup
    def fillLoyalty(self):
        db=sqlite3.connect("dbms_db.db")
        cur=db.cursor()
        cur.execute("SELECT category FROM loyalty WHERE user_id = ?", (self.id,))
        tup=cur.fetchone()

        return tup
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.profile_title = QtWidgets.QLabel(self.centralwidget)
        self.profile_title.setGeometry(QtCore.QRect(440, 10, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Goudy Old Style")
        font.setPointSize(16)
        font.setItalic(True)
        self.profile_title.setFont(font)
        self.profile_title.setObjectName("profile_title")
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(160, 150, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.gender_label = QtWidgets.QLabel(self.centralwidget)
        self.gender_label.setGeometry(QtCore.QRect(160, 250, 131, 30))
        self.gender_label.setObjectName("gender_label")
        self.age_label = QtWidgets.QLabel(self.centralwidget)
        self.age_label.setGeometry(QtCore.QRect(160, 300, 90, 30))
        self.age_label.setObjectName("age_label")
        self.phone_label = QtWidgets.QLabel(self.centralwidget)
        self.phone_label.setGeometry(QtCore.QRect(160, 350, 141, 70))
        self.phone_label.setObjectName("phone_label")
        self.user_id_label = QtWidgets.QLabel(self.centralwidget)
        self.user_id_label.setGeometry(QtCore.QRect(160, 200, 131, 30))
        self.user_id_label.setObjectName("user_id_label")
        self.loyalty_label = QtWidgets.QLabel(self.centralwidget)
        self.loyalty_label.setGeometry(QtCore.QRect(160, 440, 151, 30))
        self.loyalty_label.setObjectName("loyalty_label")
        self.name_input = QtWidgets.QLabel(self.centralwidget)
        self.name_input.setGeometry(QtCore.QRect(349, 150, 281, 30))
        self.name_input.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"")
        self.name_input.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.name_input.setLineWidth(1)
        self.name_input.setText("Hello")
        self.name_input.setObjectName("name_input")
        self.user_id_input = QtWidgets.QLabel(self.centralwidget)
        self.user_id_input.setGeometry(QtCore.QRect(339, 200, 291, 30))
        self.user_id_input.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.user_id_input.setObjectName("user_id_input")
        self.gender_input = QtWidgets.QLabel(self.centralwidget)
        self.gender_input.setGeometry(QtCore.QRect(349, 250, 281, 30))
        self.gender_input.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.gender_input.setObjectName("gender_input")
        self.age_input = QtWidgets.QLabel(self.centralwidget)
        self.age_input.setGeometry(QtCore.QRect(349, 300, 281, 30))
        self.age_input.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.age_input.setObjectName("age_input")
        self.loyalty_input = QtWidgets.QLabel(self.centralwidget)
        self.loyalty_input.setGeometry(QtCore.QRect(430, 440, 200, 30))
        self.loyalty_input.setStyleSheet("")
        self.loyalty_input.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.loyalty_input.setObjectName("loyalty_input")
        self.phone_input = QtWidgets.QLabel(self.centralwidget)
        self.phone_input.setGeometry(QtCore.QRect(359, 370, 271, 30))
        self.phone_input.setStyleSheet("")
        self.phone_input.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.phone_input.setObjectName("phone_input")
        # self.logout_button = QtWidgets.QPushButton(self.centralwidget)
        # self.logout_button.setGeometry(QtCore.QRect(30, 580, 140, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        # self.logout_button.setFont(font)
        # self.logout_button.setStyleSheet("background-color: rgb(119, 249, 255);")
        # self.logout_button.setObjectName("logout_button")
        # self.logout_button.clicked.connect(self.openWindowLogout)
        self.last_transaction_button = QtWidgets.QPushButton(self.centralwidget)
        self.last_transaction_button.setGeometry(QtCore.QRect(260, 580, 161, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.last_transaction_button.setFont(font)
        self.last_transaction_button.setStyleSheet("background-color: rgb(119, 249, 255);")
        self.last_transaction_button.setObjectName("last_transaction_button")
        self.last_transaction_button.clicked.connect(self.openWindowLastTransaction)
        self.shop_button = QtWidgets.QPushButton(self.centralwidget)
        self.shop_button.setGeometry(QtCore.QRect(530, 580, 141, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.shop_button.setFont(font)
        self.shop_button.setStyleSheet("background-color: rgb(119, 249, 255);")
        self.shop_button.setObjectName("shop_button")
        self.shop_button.clicked.connect(self.openWindowShop)
        self.loyalty_button = QtWidgets.QPushButton(self.centralwidget)
        self.loyalty_button.setGeometry(QtCore.QRect(800, 580, 161, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.loyalty_button.setFont(font)
        self.loyalty_button.setStyleSheet("background-color: rgb(119, 249, 255);")
        self.loyalty_button.setObjectName("loyalty_button")
        self.loyalty_button.clicked.connect(self.openWindowLoyalty)
        self.insight_button = QtWidgets.QPushButton(self.centralwidget)
        self.insight_button.setGeometry(QtCore.QRect(1060, 580, 151, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.insight_button.setFont(font)
        self.insight_button.setStyleSheet("background-color: rgb(119, 249, 255);")
        self.insight_button.setObjectName("insight_button")
        self.insight_button.setText("View Insights")
        self.insight_button.clicked.connect(self.openWindowInsight)

        self.home_image = QtWidgets.QLabel(self.centralwidget)
        self.home_image.setGeometry(QtCore.QRect(670, 50, 601, 431))
        self.home_image.setText("")
        self.home_image.setPixmap(QtGui.QPixmap("Images/home_man.jpg"))
        self.home_image.setScaledContents(True)
        self.home_image.setObjectName("home_image")
        # self.fillProfile()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        
        tup1=self.fillProfile()
        tup2=self.fillLoyalty()
        name=str(tup1[0])
        gender=str(tup1[2])
        age=str(tup1[3])
        phone=str(tup1[4])
        loyalty=str(tup2[0])
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.profile_title.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; font-style:normal; color:#000000;\">P R O F I L E</span><span style=\" font-size:20pt; font-weight:600; color:#4677ff;\"><br/></span></p></body></html>"))
        self.name_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#000000;\">N A M E</span></p></body></html>"))
        self.gender_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#000000;\">G E N D E R</span></p></body></html>"))
        self.age_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#000000;\">A G E</span></p></body></html>"))
        self.phone_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#000000;\">P H O N E</span></p><p><span style=\" font-size:14pt; font-weight:600; color:#000000;\">N U M B E R</span></p></body></html>"))
        self.user_id_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#000000;\">U S E R I D</span></p></body></html>"))
        self.loyalty_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#000000;\">L O Y A L T Y</span></p></body></html>"))
        self.name_input.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#228B22;\">"+name+"<br/></p></body></html>"))
        self.user_id_input.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#228B22;\">"+str(self.id)+"<br/></p></body></html>"))
        self.gender_input.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#228B22;\">"+gender+"<br/></p></body></html>"))
        self.age_input.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#228B22;\">"+age+"<br/></p></body></html>"))
        self.loyalty_input.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#228B22;\">"+loyalty+"<br/></p></body></html>"))
        self.phone_input.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#228B22;\">"+phone+"<br/></p></body></html>"))
        # self.logout_button.setText(_translate("MainWindow", "L o g o u t"))
        self.last_transaction_button.setText(_translate("MainWindow", "Last Transaction"))
        self.shop_button.setText(_translate("MainWindow", "Go to Shop"))
        self.loyalty_button.setText(_translate("MainWindow", "Buy Loyalty Card"))
        # self.insight_button.setText(_translate("MainWindow", "View Insight"))

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     window = QtWidgets.QMainWindow()
#     homeuinew = Ui_MainWindow(window)
#     homeuinew.setupUi(window)
#     window.show()
#     sys.exit(app.exec_())