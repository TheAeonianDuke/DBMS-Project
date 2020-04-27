# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainShop.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainShopWindow(object):
    def setupUi(self, mainShopWindow):
        mainShopWindow.setObjectName("mainShopWindow")
        mainShopWindow.resize(1286, 720)
        self.centralwidget = QtWidgets.QWidget(mainShopWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonClothes = QtWidgets.QPushButton(self.centralwidget)
        self.buttonClothes.setGeometry(QtCore.QRect(160, 40, 151, 451))
        self.buttonClothes.setObjectName("buttonClothes")
        self.buttoAccessories = QtWidgets.QPushButton(self.centralwidget)
        self.buttoAccessories.setGeometry(QtCore.QRect(510, 200, 531, 131))
        self.buttoAccessories.setObjectName("buttoAccessories")
        self.buttonEatables = QtWidgets.QPushButton(self.centralwidget)
        self.buttonEatables.setGeometry(QtCore.QRect(510, 40, 531, 131))
        self.buttonEatables.setObjectName("buttonEatables")
        self.buttonDrinks = QtWidgets.QPushButton(self.centralwidget)
        self.buttonDrinks.setGeometry(QtCore.QRect(510, 360, 531, 121))
        self.buttonDrinks.setObjectName("buttonDrinks")
        self.productNameInput = QtWidgets.QTextEdit(self.centralwidget)
        self.productNameInput.setGeometry(QtCore.QRect(960, 510, 251, 30))
        self.productNameInput.setReadOnly(False)
        self.productNameInput.setObjectName("productNameInput")
        self.productLocationButton = QtWidgets.QPushButton(self.centralwidget)
        self.productLocationButton.setGeometry(QtCore.QRect(1040, 550, 93, 28))
        self.productLocationButton.setObjectName("productLocationButton")
        self.productLocationOutput = QtWidgets.QTextEdit(self.centralwidget)
        self.productLocationOutput.setGeometry(QtCore.QRect(980, 590, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.productLocationOutput.setFont(font)
        self.productLocationOutput.setReadOnly(True)
        self.productLocationOutput.setObjectName("productLocationOutput")
        self.checkoutButton = QtWidgets.QPushButton(self.centralwidget)
        self.checkoutButton.setGeometry(QtCore.QRect(380, 590, 93, 28))
        self.checkoutButton.setObjectName("checkoutButton")
        self.addPreviousToCartButton = QtWidgets.QPushButton(self.centralwidget)
        self.addPreviousToCartButton.setGeometry(QtCore.QRect(510, 590, 281, 28))
        self.addPreviousToCartButton.setObjectName("addPreviousToCartButton")
        mainShopWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainShopWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1286, 26))
        self.menubar.setObjectName("menubar")
        mainShopWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainShopWindow)
        self.statusbar.setObjectName("statusbar")
        mainShopWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainShopWindow)
        QtCore.QMetaObject.connectSlotsByName(mainShopWindow)

    def retranslateUi(self, mainShopWindow):
        _translate = QtCore.QCoreApplication.translate
        mainShopWindow.setWindowTitle(_translate("mainShopWindow", "shopMain"))
        self.buttonClothes.setText(_translate("mainShopWindow", "Clothes"))
        self.buttoAccessories.setText(_translate("mainShopWindow", "Accessories"))
        self.buttonEatables.setText(_translate("mainShopWindow", "Food"))
        self.buttonDrinks.setText(_translate("mainShopWindow", "Drinks"))
        self.productNameInput.setPlaceholderText(_translate("mainShopWindow", "Enter Product Name"))
        self.productLocationButton.setText(_translate("mainShopWindow", "Get Location"))
        self.checkoutButton.setText(_translate("mainShopWindow", "Checkout"))
        self.addPreviousToCartButton.setText(_translate("mainShopWindow", "Add previously bought items in your cart"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainShopWindow = QtWidgets.QMainWindow()
    ui = Ui_mainShopWindow()
    ui.setupUi(mainShopWindow)
    mainShopWindow.show()
    sys.exit(app.exec_())
