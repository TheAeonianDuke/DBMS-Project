# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\first.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import splashscreen
import employeesplashscreen 


class Ui_MainWindow(object):

    def __init__(self,thiswindow):
        self.thiswindow = thiswindow

    def openWindowEmployee(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = employeesplashscreen.Ui_MainWindow(self.window)
        self.ui.setupUi(self.window)
        self.thiswindow.close()
        self.window.show()


    def openWindowUser(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = splashscreen.Ui_MainWindow(self.window)
        self.ui.setupUi(self.window)
        self.thiswindow.close()
        self.window.show()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1281, 721))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Images/Mesa de trabajo 1.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 250, 381, 61))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("font: 45pt \"Lemon/Milk\";\n"
"color: rgb(243, 75, 150);")
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(460, 300, 381, 51))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet(";font: 18pt \"Lemon/Milk\";\n"
"color: rgb(255, 206, 149);")
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.NewUserBtn = QtWidgets.QPushButton(self.centralwidget)
        self.NewUserBtn.setGeometry(QtCore.QRect(350, 360, 281, 41))
        self.NewUserBtn.setStyleSheet("background-color: rgb(255, 191, 93);color: rgb(247, 247, 247);font: 15pt \"Lemon/Milk\";")
        self.NewUserBtn.setObjectName("NewUserBtn")
        self.NewUserBtn.clicked.connect(self.openWindowUser)
        self.ExistingUserBtn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.ExistingUserBtn_2.setGeometry(QtCore.QRect(690, 360, 281, 41))
        self.ExistingUserBtn_2.setStyleSheet("background-color: rgb(255, 191, 93);color: rgb(247, 247, 247);font: 15pt \"Lemon/Milk\";")
        self.ExistingUserBtn_2.setObjectName("ExistingUserBtn_2")
        self.ExistingUserBtn_2.clicked.connect(self.openWindowEmployee)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Shopify"))
        self.label_3.setText(_translate("MainWindow", "Simply better shopping."))
        self.NewUserBtn.setText(_translate("MainWindow", "C u s t o m e r "))
        self.ExistingUserBtn_2.setText(_translate("MainWindow", "E m p l o y e e "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
