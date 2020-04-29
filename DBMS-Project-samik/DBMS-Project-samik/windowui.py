from PyQt5 import QtWidgets,QtGui,Qt

from PyQt5.QtWidgets import QApplication,QMainWindow
import sys 
import sqlite3

class SamikWindow(QMainWindow):
    def __init__(self,cartList):
        super(SamikWindow,self).__init__()
        self.setGeometry(300,300,1280,720)
        self.cartList = cartList #a 2d list of user purchases
        self.initCartUi()
        self.setStyleSheet("background-color: rgb(220, 126, 212);")
        
        

        

    def initCartUi(self):
        self.font = QtGui.QFont("Goudy Old Style",16, QtGui.QFont.Bold)
        self.cartCheckBox = []
    
    
        self.removeLabel = QtWidgets.QLabel(self)
        self.removeLabel.setFixedWidth(500)
        self.removeLabel.setText("Un-select to remove from cart")
        
        self.removeLabel.move(300,50)
        self.removeLabel.setFont(self.font)
        self.removeLabel.setStyleSheet("background-color: rgb(220, 126, 212);")
        
        
        

        self.checkoutButton = QtWidgets.QPushButton(self)
        self.checkoutButton.setFixedSize(200,50)
        self.checkoutButton.setText("Proceed to Checkout")
        self.checkoutButton.move(1000,650)
        self.checkoutButton.setStyleSheet("background-color: rgb(119, 249, 255);")
        self.checkoutButton.clicked.connect(self.initCheckoutGui)
        for i in self.cartList:
            self.checkbox = QtWidgets.QCheckBox(self)
            self.checkbox.setChecked(True)
            self.checkbox.setFixedSize(700,20)
            self.cartCheckBox.append(self.checkbox)
            
        
        x = 300
        y = 100
        count = 0
        
        for i in range(len(self.cartCheckBox)):
            print(self.cartList[i])
            self.cartCheckBox[i].setText(self.displayCartItem(self.cartList[i]))
            self.cartCheckBox[i].move(x,y + 50*count)
            count += 1


    def displayCartItem(self,l): #l is a list of user purchases type objects [purchase_id,user_id,receipt_id,product_id,quantity,discount_id,before_discount,after_discount]
        # print(l)
        self.con = sqlite3.connect("dbms_db.db")
        self.c = self.con.cursor()
        prod_name = ""
        for i in self.c.execute("select name from products where product_id = ?",(str(l[3]),)):
            prod_name = i[0]
        quantity = l[4]
        before_discount = l[6]
        after_discount = l[7]

        return "Name: " + prod_name + "     Quantity: "+ str(quantity) + "      Price Before Discount: "+ str(before_discount)+ "       Price After Discount: "+str(after_discount)


    
    def clearViewCart(self):
        for i in self.cartCheckBox:
            i.hide()
        self.removeLabel.hide()
        self.checkoutButton.hide()

    def addTransactions(self):
        print("executed")
        add_to_transactins = (self.cartList[0][2],self.cartList[0][1],self.total_cost,self.employee_id.text(),self.employee_rating.text())
        print(add_to_transactins)
        self.c.execute("insert into transactions(receipt_id,user_id,total_cost,employee_id,satisfaction) values (?,?,?,?,?)",add_to_transactins)
        self.con.commit()
        self.employee_id.hide()
        self.employee_rating.hide()
        self.checkoutLabel1.hide()
        self.checkoutLabel2.hide()
        for i in range(len(self.cartCheckBox)):
            self.cartCheckBox[i].hide()
        self.proceedButton.hide()
        self.receipt_id_label = QtWidgets.QLabel(self)
        self.receipt_id_label.setText("Your Receipt ID is: "+str(self.cartList[0][2]))
        self.receipt_id_label.setFont(self.font)
        self.receipt_id_label.adjustSize()
        # self.receipt_id_label.setAlignment(550,350)
        self.receipt_id_label.move(550,350)
        self.receipt_id_label.show()


    def initCheckoutGui(self):
        self.clearViewCart()
        
        self.checkoutLabel1 = QtWidgets.QLabel(self)
        self.checkoutLabel1.setText("Enter Employee ID: ")
        self.checkoutLabel1.setFont(self.font)

        self.checkoutLabel1.adjustSize()
        self.checkoutLabel1.move(150,55)
        self.checkoutLabel1.show()

        self.checkoutLabel2 = QtWidgets.QLabel(self)
        self.checkoutLabel2.setText("Enter Employee Rating (x.xx): ")
        self.checkoutLabel2.setFont(self.font)
        self.checkoutLabel2.adjustSize()
        self.checkoutLabel2.move(95,105)
        self.checkoutLabel2.show()

        count = 1
        x=300
        y=100
        self.employee_id = QtWidgets.QLineEdit(self)
        self.employee_id.setStyleSheet("background-color: white;")
        self.employee_id.move(350,50)
        self.employee_id.show()

        self.employee_rating = QtWidgets.QLineEdit(self)
        self.employee_rating.setStyleSheet("background-color: white;")
        self.employee_rating.move(350,100)
        self.employee_rating.show()
        
        

        self.total_cost = 0
        for i in range(len(self.cartCheckBox)):
            print(self.cartCheckBox[i].isVisible())
            if self.cartCheckBox[i].isChecked():
                self.cartCheckBox[i].move(x,y + 50*count)
                self.cartCheckBox[i].show()
                self.total_cost+= self.cartList[i][-1]
                self.c.execute("insert into user_purchases (purchase_id,user_id,receipt_id,product_id,quantity,discounts_id,before_discount,after_discount) values (?,?,?,?,?,?,?,?)",tuple(self.cartList[i]))
                count += 1
        
        self.proceedButton = QtWidgets.QPushButton(self)
        self.proceedButton.setStyleSheet("background-color: rgb(119, 249, 255);")
        self.proceedButton.move(1000,600)
        self.proceedButton.setText("Proceed")
        self.proceedButton.show()
        self.proceedButton.clicked.connect(self.addTransactions)
         
        
        

    

app = QApplication(sys.argv)
win = SamikWindow([[35, 69, 29, 4, 1, 1, 50, 45]])
win.show()
sys.exit(app.exec_())