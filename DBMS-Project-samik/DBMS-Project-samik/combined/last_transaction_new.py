# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'last_transaction.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import homeuinew
import sqlite3
import samikharshcombined

class Ui_MainWindow(object):
    def __init__(self,id):
        self.id = id
    
    def loadLastTransaction(self,id): 
        db=sqlite3.connect("dbms_db.db")
        cur=db.cursor()
        # cur.execute("SELECT receipt_id FROM transactions WHERE user_id=?;",(id,))
        # tup=cur.fetchall()
        # #print(tup[-1][0])
        # a=tup[-1][0]
        # #cur.execute("SELECT product_id,quantity,discounts_id,name,category FROM user_purchases NATURAL JOIN products WHERE receipt_id=?;",(a,))
        # cur.execute("SELECT product_id,quantity,discount_type,name,category FROM user_purchases NATURAL JOIN products NATURAL JOIN discounts WHERE receipt_id=?;",(a,))
        cur.execute("SELECT product_id,quantity,discount_type,name,category FROM user_purchases NATURAL JOIN products NATURAL JOIN discounts WHERE receipt_id=(SELECT MAX(receipt_id) FROM transactions WHERE user_id=?);",(self.id,))
        tup=cur.fetchall()
        return tup

    def fillLastTransaction(self,id):
        _translate = QtCore.QCoreApplication.translate
        solution=self.loadLastTransaction(self.id)
        print(solution)
        solution_string=""
        for i in range(len(solution)):
            solution_string+=str(solution[i][1])+" "+str(solution[i][3])+" of "+str(solution[i][4])+" category with discount "+str(solution[i][2])+"\n"
        self.last_transaction_content.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;color:#228B22\">"+" Your last transaction was <br> </span><span style=\" font-size:10pt; font-weight:600;color:#800080\">"+solution_string+"</span></p></body></html>"))
    
    def openWindowShop(self):
        self.window = QtWidgets.QMainWindow()
        # self.ui = last_transaction_ui.Ui_MainWindow() #Take from Harsh's Map/shop file
        # self.ui.setupUi(self.window)
        self.shopwindow = samikharshcombined.Combined(self.window,self.id)
        self.window.hide()
        self.window.show()
    def openWindowAddLasttoCart(self):
        self.window = QtWidgets.QMainWindow()
        # self.ui = last_transaction_ui.Ui_MainWindow() #Take from Harsh's cart file
        # self.ui.setupUi(self.window)  #Also return to Harsh a list of tuples of product ids and quantity #Do dbms things
        
        self.window.hide()
        self.window.show()
    def openWindowProfile(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = homeuinew.Ui_MainWindow(self.id)
        self.ui.setupUi(self.window)
        self.window.hide()
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.last_transaction_title = QtWidgets.QLabel(self.centralwidget)
        self.last_transaction_title.setGeometry(QtCore.QRect(420, 0, 291, 51))
        self.last_transaction_title.setObjectName("last_transaction_title")
        self.last_transaction_content = QtWidgets.QLabel(self.centralwidget)
        self.last_transaction_content.setGeometry(QtCore.QRect(20, 110, 731, 311))
        self.last_transaction_content.setText("")
        self.last_transaction_content.setObjectName("last_transaction_content")
        self.profile_button = QtWidgets.QPushButton(self.centralwidget)
        self.profile_button.setGeometry(QtCore.QRect(50, 570, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.profile_button.setFont(font)
        self.profile_button.setStyleSheet("background-color: rgb(150, 190, 252);")
        self.profile_button.setObjectName("profile_button")
        self.profile_button.clicked.connect(self.openWindowProfile)
        # self.addlasttocart_button = QtWidgets.QPushButton(self.centralwidget)
        # self.addlasttocart_button.setGeometry(QtCore.QRect(470, 570, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        # self.addlasttocart_button.setFont(font)
        # self.addlasttocart_button.setStyleSheet("background-color: rgb(150, 190, 252);")
        # self.addlasttocart_button.setObjectName("addlasttocart_button")
        # self.addlasttocart_button.clicked.connect(self.openWindowAddLasttoCart)
        self.shop_button = QtWidgets.QPushButton(self.centralwidget)
        self.shop_button.setGeometry(QtCore.QRect(920, 570, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.shop_button.setFont(font)
        self.shop_button.setStyleSheet("background-color: rgb(150, 190, 252);")
        self.shop_button.setObjectName("shop_button")
        self.shop_button.clicked.connect(self.openWindowShop)
        self.last_transaction_image = QtWidgets.QLabel(self.centralwidget)
        self.last_transaction_image.setGeometry(QtCore.QRect(800, 20, 421, 341))
        self.last_transaction_image.setText("")
        self.last_transaction_image.setPixmap(QtGui.QPixmap("Images/last_transaction_new.jpg"))
        self.last_transaction_image.setScaledContents(True)
        self.last_transaction_image.setObjectName("last_transaction_image")
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
        id=1
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.last_transaction_title.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">Last Transaction</span></p></body></html>"))
        self.fillLastTransaction(id)
        self.profile_button.setText(_translate("MainWindow", "Go back to Profile"))
        # self.addlasttocart_button.setText(_translate("MainWindow", "Add last transaction to cart"))
        self.shop_button.setText(_translate("MainWindow", "Go to shop"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    last_transaction_new = Ui_MainWindow()
    last_transaction_new.setupUi(window)
    window.show()
    sys.exit(app.exec_())