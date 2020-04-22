# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'last_transaction.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import immm_rc
import sys
import homeui


class Ui_MainWindow(object):
    def openWindowShop(self):
        self.window = QtWidgets.QMainWindow()
        # self.ui = last_transaction_ui.Ui_MainWindow() #Take from Harsh's Map/shop file
        # self.ui.setupUi(self.window)
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
        self.ui = homeui.Ui_MainWindow()
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
        self.last_transaction_image = QtWidgets.QLabel(self.centralwidget)
        self.last_transaction_image.setGeometry(QtCore.QRect(780, 10, 471, 381))
        self.last_transaction_image.setStyleSheet("background-image: url(:/newPrefix/Images/last_transaction_new.jpg);")
        self.last_transaction_image.setText("")
        self.last_transaction_image.setScaledContents(True)
        self.last_transaction_image.setObjectName("last_transaction_image")
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
        self.addlasttocart_button = QtWidgets.QPushButton(self.centralwidget)
        self.addlasttocart_button.setGeometry(QtCore.QRect(470, 570, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addlasttocart_button.setFont(font)
        self.addlasttocart_button.setStyleSheet("background-color: rgb(150, 190, 252);")
        self.addlasttocart_button.setObjectName("addlasttocart_button")
        self.addlasttocart_button.clicked.connect(self.openWindowAddLasttoCart)
        self.shop_button = QtWidgets.QPushButton(self.centralwidget)
        self.shop_button.setGeometry(QtCore.QRect(920, 570, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.shop_button.setFont(font)
        self.shop_button.setStyleSheet("background-color: rgb(150, 190, 252);")
        self.shop_button.setObjectName("shop_button")
        self.shop_button.clicked.connect(self.openWindowShop)
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
        self.last_transaction_title.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">Last Transaction</span></p></body></html>"))
        self.profile_button.setText(_translate("MainWindow", "Go back to Profile"))
        self.addlasttocart_button.setText(_translate("MainWindow", "Add last transaction to cart"))
        self.shop_button.setText(_translate("MainWindow", "Go to shop"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    last_transaction_ui = Ui_MainWindow()
    last_transaction_ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
