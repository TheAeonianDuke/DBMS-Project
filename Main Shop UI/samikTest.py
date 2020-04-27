# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'samikTestUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from mainShop import Ui_mainShopWindow

# import mainShop


class Ui_MainWindow(object):

    def __init__(self):
        super().__init__()
        self.cart = []


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.goToShopButton = QtWidgets.QPushButton(self.centralwidget)
        self.goToShopButton.setGeometry(QtCore.QRect(260, 207, 261, 71))
        self.goToShopButton.setObjectName("goToShopButton")

        self.showCartButton = QtWidgets.QPushButton(self.centralwidget)
        self.showCartButton.setGeometry(QtCore.QRect(300, 207, 261, 71))
        self.showCartButton.setObjectName("showCartButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.goToShopButton.clicked.connect(self.goToShop)
        self.showCartButton.clicked.connect(self.showCart)

    def showCart(self):
        print (self.cart)

    def goToShop(self):
        print("clicked")
        self.shopWindow = QtWidgets.QMainWindow()
        self.user_id = 69 # change it according to the user_id
        self.ui = Ui_mainShopWindow(self.shopWindow, self.cart ,self.user_id) # in your __init__ , initialize the self.cart = []
        self.ui.setupUi(self.shopWindow)
        self.shopWindow.show()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.goToShopButton.setText(_translate("MainWindow", "Go to shop!"))
        self.showCartButton.setText(_translate("MainWindow", "Show Cart!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
