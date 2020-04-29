# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\newuser.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(16, 204, 205);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(420, 0, 861, 641))
        self.image_label.setStyleSheet("")
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")
        self.control_bt = QtWidgets.QPushButton(self.centralwidget)
        self.control_bt.setGeometry(QtCore.QRect(730, 640, 291, 41))
        self.control_bt.setStyleSheet("font: 12pt \"Lemon/Milk\";color: rgb(255, 255, 255);background-color: rgb(253, 142, 192);")
        self.control_bt.setObjectName("control_bt")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 400, 361, 311))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Images/490544-PHCFBA-7.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 10, 251, 31))
        self.label_2.setStyleSheet("font: 20pt \"Lemon/Milk\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 91, 31))
        self.label_3.setStyleSheet("font: 15pt \"Lemon/Milk\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 150, 91, 31))
        self.label_4.setStyleSheet("font: 15pt \"Lemon/Milk\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 210, 91, 61))
        self.label_5.setStyleSheet("font: 14pt \"Lemon/Milk\";\n"
"color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 290, 91, 61))
        self.label_6.setStyleSheet("font: 15pt \"Lemon/Milk\";\n"
"color: rgb(255, 255, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.nameinput = QtWidgets.QLineEdit(self.centralwidget)
        self.nameinput.setGeometry(QtCore.QRect(110, 60, 281, 51))
        self.nameinput.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 13pt \"Montserrat\";")
        self.nameinput.setObjectName("nameinput")
        self.ageinput = QtWidgets.QLineEdit(self.centralwidget)
        self.ageinput.setGeometry(QtCore.QRect(110, 140, 281, 51))
        self.ageinput.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 13pt \"Montserrat\";")
        self.ageinput.setObjectName("ageinput")
        self.phoneinput = QtWidgets.QLineEdit(self.centralwidget)
        self.phoneinput.setGeometry(QtCore.QRect(110, 220, 281, 51))
        self.phoneinput.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 13pt \"Montserrat\";")
        self.phoneinput.setObjectName("phoneinput")
        self.genderinput = QtWidgets.QLineEdit(self.centralwidget)
        self.genderinput.setGeometry(QtCore.QRect(110, 300, 281, 51))
        self.genderinput.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 13pt \"Montserrat\";")
        self.genderinput.setObjectName("genderinput")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(150, 370, 181, 31))
        self.submit.setStyleSheet("font: 12pt \"Lemon/Milk\";color: rgb(255, 255, 255);background-color: rgb(253, 142, 192);")
        self.submit.setObjectName("submit")
        self.backbtn = QtWidgets.QPushButton(self.centralwidget)
        self.backbtn.setGeometry(QtCore.QRect(10, 10, 51, 41))
        self.backbtn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.backbtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Images/3646423e2df5a8a39333e2aa8bbcc8e1_back-arrow-icon-png-image-free-download-searchpngcom_715-715.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backbtn.setIcon(icon)
        self.backbtn.setIconSize(QtCore.QSize(32, 32))
        self.backbtn.setObjectName("backbtn")
        self.control_bt.raise_()
        self.label.raise_()
        self.image_label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.nameinput.raise_()
        self.ageinput.raise_()
        self.phoneinput.raise_()
        self.genderinput.raise_()
        self.submit.raise_()
        self.backbtn.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.control_bt.setText(_translate("MainWindow", "S t a r t   C a m e r a"))
        self.label_2.setText(_translate("MainWindow", "Register User"))
        self.label_3.setText(_translate("MainWindow", "Name"))
        self.label_4.setText(_translate("MainWindow", "Age"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>Phone</p><p>Number</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p>Gender</p></body></html>"))
        self.submit.setText(_translate("MainWindow", "S u b m i t"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
