# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1279, 720)
        MainWindow.setStyleSheet("background-color: rgb(241, 241, 241);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-40, 330, 611, 371))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Images/2749712.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 0, 251, 31))
        self.label_2.setStyleSheet("font: 20pt \"Lemon/Milk\";\n"
"color: rgb(27, 147, 164);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 280, 91, 61))
        self.label_6.setStyleSheet("font: 15pt \"Lemon/Milk\";\n"
"color: rgb(27, 147, 164);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 60, 91, 31))
        self.label_3.setStyleSheet("font: 15pt \"Lemon/Milk\";\n"
"color: rgb(27, 147, 164);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 140, 91, 31))
        self.label_4.setStyleSheet("font: 15pt \"Lemon/Milk\";\n"
"color: rgb(27, 147, 164);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 200, 91, 61))
        self.label_5.setStyleSheet("font: 15pt \"Lemon/Milk\";\n"
"color: rgb(27, 147, 164);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(450, -20, 831, 631))
        self.image_label.setStyleSheet("")
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")
        self.control_bt = QtWidgets.QPushButton(self.centralwidget)
        self.control_bt.setGeometry(QtCore.QRect(540, 620, 291, 41))
        self.control_bt.setStyleSheet("font: 12pt \"Lemon/Milk\";color: rgb(255, 255, 255);background-color: rgb(253, 142, 192);")
        self.control_bt.setObjectName("control_bt")
        self.namelabel = QtWidgets.QLabel(self.centralwidget)
        self.namelabel.setGeometry(QtCore.QRect(140, 60, 291, 31))
        self.namelabel.setStyleSheet("font: 18pt \"Lemon/Milk\";\n"
"color: rgb(0, 0, 0);")
        self.namelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.namelabel.setObjectName("namelabel")
        self.agelabel = QtWidgets.QLabel(self.centralwidget)
        self.agelabel.setGeometry(QtCore.QRect(140, 140, 291, 31))
        self.agelabel.setStyleSheet("font: 18pt \"Lemon/Milk\";\n"
"color: rgb(0, 0, 0);")
        self.agelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.agelabel.setObjectName("agelabel")
        self.phonelabel = QtWidgets.QLabel(self.centralwidget)
        self.phonelabel.setGeometry(QtCore.QRect(140, 220, 291, 31))
        self.phonelabel.setStyleSheet("font: 18pt \"Lemon/Milk\";\n"
"color: rgb(0, 0, 0);")
        self.phonelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.phonelabel.setObjectName("phonelabel")
        self.genderlabel = QtWidgets.QLabel(self.centralwidget)
        self.genderlabel.setGeometry(QtCore.QRect(140, 300, 291, 31))
        self.genderlabel.setStyleSheet("font: 18pt \"Lemon/Milk\";\n"
"color: rgb(0, 0, 0);")
        self.genderlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.genderlabel.setObjectName("genderlabel")
        self.verify_btn = QtWidgets.QPushButton(self.centralwidget)
        self.verify_btn.setGeometry(QtCore.QRect(900, 620, 291, 41))
        self.verify_btn.setStyleSheet("font: 12pt \"Lemon/Milk\";color: rgb(255, 255, 255);background-color: rgb(253, 142, 192);")
        self.verify_btn.setObjectName("verify_btn")
        self.login_btn = QtWidgets.QPushButton(self.centralwidget)
        self.login_btn.setGeometry(QtCore.QRect(140, 360, 171, 41))
        self.login_btn.setStyleSheet("font: 12pt \"Lemon/Milk\";color: rgb(255, 255, 255);background-color: rgb(253, 142, 192);")
        self.login_btn.setObjectName("login_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1279, 21))
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
        self.label_2.setText(_translate("MainWindow", "Login"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p>Gender</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Name"))
        self.label_4.setText(_translate("MainWindow", "Age"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>Phone</p><p>Number</p></body></html>"))
        self.control_bt.setText(_translate("MainWindow", "S t a r t   c a m e r a"))
        self.namelabel.setText(_translate("MainWindow", "waiting..."))
        self.agelabel.setText(_translate("MainWindow", "waiting..."))
        self.phonelabel.setText(_translate("MainWindow", "waiting..."))
        self.genderlabel.setText(_translate("MainWindow", "waiting..."))
        self.verify_btn.setText(_translate("MainWindow", "C a p t u r e   a n d   v e r i f y"))
        self.login_btn.setText(_translate("MainWindow", "L o g i n"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
