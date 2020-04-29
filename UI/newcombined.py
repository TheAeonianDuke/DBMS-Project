from PyQt5 import QtWidgets,QtGui,Qt

from PyQt5.QtWidgets import QApplication,QMainWindow
import sys 
import sqlite3

from harsh import Ui_mainShopWindow
from samik import SamikWindow
import homeuinew
from samikharshcombined import Combined

class Final:
    def __init__(self,window,user_id):
        self.window = window
        self.user_id=user_id
        self.visheshpage = homeuinew.Ui_MainWindow(window,self.user_id)
        self.visheshpage.setupUi(self.window)
        self.visheshpage.shop_button.clicked.connect(self.goToShop)
    

    def goToShop(self):
        self.shopwindow = Combined(self.window,self.user_id)

# app = QtWidgets.QApplication(sys.argv)
# mainShopWindow = QtWidgets.QMainWindow()
# final = Final(mainShopWindow,9)
# mainShopWindow.show()
# sys.exit(app.exec_())


        