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
        self.label.setGeometry(QtCore.QRect(-40, 310, 611, 371))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Images/2749712.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.nameinput = QtWidgets.QLineEdit(self.centralwidget)
        self.nameinput.setGeometry(QtCore.QRect(150, 50, 281, 51))
        self.nameinput.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 13pt \"Montserrat\";")
        self.nameinput.setObjectName("nameinput")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 0, 251, 31))
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
        self.genderinput = QtWidgets.QLineEdit(self.centralwidget)
        self.genderinput.setGeometry(QtCore.QRect(150, 290, 281, 51))
        self.genderinput.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 13pt \"Montserrat\";")
        self.genderinput.setObjectName("genderinput")
        self.ageinput = QtWidgets.QLineEdit(self.centralwidget)
        self.ageinput.setGeometry(QtCore.QRect(150, 130, 281, 51))
        self.ageinput.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 13pt \"Montserrat\";")
        self.ageinput.setObjectName("ageinput")
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
        self.phoneinput = QtWidgets.QLineEdit(self.centralwidget)
        self.phoneinput.setGeometry(QtCore.QRect(150, 210, 281, 51))
        self.phoneinput.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 13pt \"Montserrat\";")
        self.phoneinput.setObjectName("phoneinput")
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
        self.control_bt.setGeometry(QtCore.QRect(750, 620, 291, 41))
        self.control_bt.setStyleSheet("font: 12pt \"Lemon/Milk\";color: rgb(255, 255, 255);background-color: rgb(253, 142, 192);")
        self.control_bt.setObjectName("control_bt")
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
        self.label_2.setText(_translate("MainWindow", "Register User"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p>Gender</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Name"))
        self.label_4.setText(_translate("MainWindow", "Age"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>Phone</p><p>Number</p></body></html>"))
        self.control_bt.setText(_translate("MainWindow", "C a p t u r e   a n d   v e r i f y"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
