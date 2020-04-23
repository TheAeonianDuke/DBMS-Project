# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loyalty.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
#import imm_rc
import homeuinew
import sqlite3

class Ui_MainWindow(object):
    def openWindowProfile(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = homeuinew.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.hide()
        self.window.show()
    def fillLoyalty(self,id,var): #id is the user_id and var is the type of loyalty card("gold",silver)
        db=sqlite3.connect("dbms_db.db")
        cur=db.cursor()
        #cur.execute("SELECT category FROM loyalty WHERE user_id = ?", (id,))
        # query="""IF EXISTS (select * from loyalty where user_id= 'id') THEN
        # update loyalty set category=? where user_id =?;
        # ELSE 
        # insert into loyalty (user_id,category) values (?,?);
        # """
        # query="""INSERT OR IGNORE INTO loyalty (user_id,category) VALUES (?,?)
        # UPDATE loyalty SET category =? WHERE user_id=?;"""
        query="""INSERT OR REPLACE INTO loyalty VALUES (?, ?);"""
        params=(str(id),str(var))
        cur.execute(query,params)
        # q2="ORDER BY id;"
        # cur.execute(q2)
        db.commit()
        db.close()
    def updateSilver(self): 
        id=17
        print("Silver is pressed")
        _translate = QtCore.QCoreApplication.translate
        self.confirmation_label.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">Your loyalty card has been updated to Silver</span></p></body></html>"))
        self.fillLoyalty(id,"Silver")

    def updateGold(self):
        id=17
        print("Gold is pressed")
        _translate = QtCore.QCoreApplication.translate
        self.confirmation_label.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">Your loyalty card has been updated to Gold</span></p></body></html>"))
        self.fillLoyalty(id,"Gold")
    def updatePlatinum(self):
        id=17
        print("Platinum is pressed")
        _translate = QtCore.QCoreApplication.translate
        self.confirmation_label.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">Your loyalty card has been updated to Platinum</span></p></body></html>"))
        self.fillLoyalty(id,"Platinum")
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setStyleSheet("background-color: rgb(0, 128, 128);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loyalty_title = QtWidgets.QLabel(self.centralwidget)
        self.loyalty_title.setGeometry(QtCore.QRect(590, 20, 241, 91))
        self.loyalty_title.setStyleSheet("background-color: rgb(0, 128, 128);")
        self.loyalty_title.setObjectName("loyalty_title")
        self.vertical_line = QtWidgets.QFrame(self.centralwidget)
        self.vertical_line.setGeometry(QtCore.QRect(440, 10, 20, 701))
        self.vertical_line.setStyleSheet("background-color: rgb(0, 128, 128);")
        self.vertical_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.vertical_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vertical_line.setObjectName("vertical_line")
        self.description = QtWidgets.QLabel(self.centralwidget)
        self.description.setGeometry(QtCore.QRect(80, 30, 331, 551))
        self.description.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.description.setStyleSheet("background-color: rgb(0, 128, 128);")
        self.description.setTextFormat(QtCore.Qt.AutoText)
        self.description.setScaledContents(True)
        self.description.setWordWrap(True)
        self.description.setObjectName("description")
        self.choose_label = QtWidgets.QLabel(self.centralwidget)
        self.choose_label.setGeometry(QtCore.QRect(560, 110, 621, 111))
        self.choose_label.setObjectName("choose_label")
        self.silver_button = QtWidgets.QPushButton(self.centralwidget)
        self.silver_button.setGeometry(QtCore.QRect(540, 240, 200, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.silver_button.setFont(font)
        self.silver_button.setStyleSheet("background-color: rgb(191, 191, 191);")
        self.silver_button.setObjectName("silver_button")
        self.silver_button.clicked.connect(self.updateSilver)
        self.platinum_button = QtWidgets.QPushButton(self.centralwidget)
        self.platinum_button.setGeometry(QtCore.QRect(1030, 240, 200, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.platinum_button.setFont(font)
        self.platinum_button.setStyleSheet("background-color: rgb(243, 146, 162);")
        self.platinum_button.setObjectName("platinum_button")
        self.platinum_button.clicked.connect(self.updatePlatinum)
        self.gold_button = QtWidgets.QPushButton(self.centralwidget)
        self.gold_button.setGeometry(QtCore.QRect(780, 240, 200, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gold_button.setFont(font)
        self.gold_button.setStyleSheet("background-color: rgb(255, 215, 0);")
        self.gold_button.setObjectName("gold_button")
        self.gold_button.clicked.connect(self.updateGold)
        self.profile_button = QtWidgets.QPushButton(self.centralwidget)
        self.profile_button.setGeometry(QtCore.QRect(1082, 630, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.profile_button.setFont(font)
        self.profile_button.setStyleSheet("background-color: rgb(243, 181, 255);")
        self.profile_button.setObjectName("profile_button")
        self.profile_button.clicked.connect(self.openWindowProfile)
        self.confirmation_label = QtWidgets.QLabel(self.centralwidget)
        self.confirmation_label.setGeometry(QtCore.QRect(540, 420, 681, 31))
        self.confirmation_label.setObjectName("confirmation_label")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loyalty_title.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">LOYALTY CARD</span></p></body></html>"))
        self.description.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-style:italic;\">Hey Shoppers! Tired of paying full amounts for each product you buy?</span></p><p><span style=\" font-size:12pt; font-style:italic;\">Tired of leaving some products just because the cost was going a little above board?! </span></p><p><span style=\" font-size:12pt; font-style:italic;\">Well we just have the perfect solution to your woes. We introduce to you our loyalty program wherein you can buy/upgrade your plan with us.</span></p><p><span style=\" font-size:12pt;\">Here are the 3 plans:</span></p><p><span style=\" font-size:12pt; color:#bfbfbf;\">Silver: offers 10% discounts in the whole transaction</span></p><p><span style=\" font-size:12pt; color:#ffd700;\">Gold: offers 20% discounts in the whole transaction</span></p><p><span style=\" font-size:12pt; color:#f7698f;\">Platinum: offers 30% discounts in the whole transaction </span></p></body></html>"))
        self.choose_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Click to Choose which card would you want to buy/upgrade </span></p></body></html>"))
        self.silver_button.setText(_translate("MainWindow", "Silver"))
        self.platinum_button.setText(_translate("MainWindow", "Platinum"))
        self.gold_button.setText(_translate("MainWindow", "Gold"))
        self.profile_button.setText(_translate("MainWindow", "Go back to profile"))
#         self.confirmation_label.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
# "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
# "p, li { white-space: pre-wrap; }\n"
# "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
# "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">Your selection has been made</span></p></body></html>"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    loyaltyui = Ui_MainWindow()
    loyaltyui.setupUi(window)
    window.show()
    sys.exit(app.exec_())

