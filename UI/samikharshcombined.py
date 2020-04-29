from PyQt5 import QtWidgets,QtGui,Qt

from PyQt5.QtWidgets import QApplication,QMainWindow
import sys 
import sqlite3

from harsh import Ui_mainShopWindow
from samik import SamikWindow

class Combined:
    def __init__(self,window1,user_id):
        
        self.harshwindow = window1
        self.user_id = user_id
        self.cart = []
        self.ui = Ui_mainShopWindow(window1,self.cart,self.user_id)
        self.ui.setupUi(window1)
        self.ui.checkoutButton.clicked.connect(self.checkout)
        
        

    def checkout(self):
        print("this working")
        self.samikwindow = SamikWindow(self.cart)
        # self.samikwindow.initCartUi()
        
        self.samikwindow.show()
        print("this working 2")
           

    

if __name__ == "__main__":
    

    app = QtWidgets.QApplication(sys.argv)
    mainShopWindow = QtWidgets.QMainWindow()
    c = Combined(mainShopWindow,9,)




    mainShopWindow.show()
    sys.exit(app.exec_())

