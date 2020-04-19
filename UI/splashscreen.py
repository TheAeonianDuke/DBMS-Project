# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\splashscreen.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import newuser
import sys

class Ui_MainWindow(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = newuser.MainWindow(self.window)
        window.hide()
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1281, 701))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Images/18980.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 20, 381, 61))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("color: rgb(64, 210, 231);font: 45pt \"Lemon/Milk\";")
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(460, 70, 381, 51))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("color: rgb(86, 120, 254);font: 18pt \"Lemon/Milk\";")
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.NewUserBtn = QtWidgets.QPushButton(self.centralwidget)
        self.NewUserBtn.setGeometry(QtCore.QRect(290, 650, 281, 41))
        self.NewUserBtn.setStyleSheet("background-color: rgb(255, 191, 93);color: rgb(247, 247, 247);font: 15pt \"Lemon/Milk\";")
        self.NewUserBtn.setObjectName("NewUserBtn")
        self.NewUserBtn.clicked.connect(self.openWindow)
        self.ExistingUserBtn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.ExistingUserBtn_2.setGeometry(QtCore.QRect(650, 650, 281, 41))
        self.ExistingUserBtn_2.setStyleSheet("background-color: rgb(255, 191, 93);color: rgb(247, 247, 247);font: 15pt \"Lemon/Milk\";")
        self.ExistingUserBtn_2.setObjectName("ExistingUserBtn_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        return MainWindow

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Shopify"))
        self.label_3.setText(_translate("MainWindow", "Simply better shopping."))
        self.NewUserBtn.setText(_translate("MainWindow", "N e w  U s e r"))
        self.ExistingUserBtn_2.setText(_translate("MainWindow", "E x i s t i n g  U s e r"))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    splashui = Ui_MainWindow()
    splashui.setupUi(window)
    window.show()
    sys.exit(app.exec_())