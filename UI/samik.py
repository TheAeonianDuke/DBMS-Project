from PyQt5 import QtWidgets,QtGui,Qt, QtCore

from PyQt5.QtWidgets import QApplication,QMainWindow
import sys 
import sqlite3
import first

class SamikWindow(QMainWindow):
    def __init__(self,cartList):
        super(SamikWindow,self).__init__()

        self.resize(1280,720)
        # self.setGeometry(300,300,1280,720)
        self.cartList = cartList #a 2d list of user purchases
        self.initCartUi()
        # self.setStyleSheet("background-color: rgb(220, 126, 212);")
        
        
    def profile(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = first.Ui_MainWindow(self.window)
        self.ui.setupUi(self.window)
        self.window.show()


    def initCartUi(self):
        self.font = QtGui.QFont("Josefin Sans",16, QtGui.QFont.Bold)
        self.cartCheckBox = []
         
        self.removeLabel = QtWidgets.QLabel(self)
        self.removeLabel.setFixedWidth(500)
        self.removeLabel.setText("Un-select to remove from cart")

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(0, 0, 1281, 721))
        self.label.setText("")

        self.label.setPixmap(QtGui.QPixmap("Images/storeimg.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(460, 20, 381, 61))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("color: rgb(64, 210, 231);font: 45pt \"Lemon/Milk\";")
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_2.setText("My Cart")
        
        self.removeLabel.move(300,50)
        self.removeLabel.setFont(self.font)
        self.removeLabel.setStyleSheet("background-color: rgb(220, 126, 212);")
        
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(460, 20, 381, 61))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("color: rgb(64, 210, 231);font: 15pt \"Lemon/Milk\";")
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_3.setText("Item Name")
        self.label_3.move(-10,90)


        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(460, 20, 381, 61))
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("color: rgb(64, 210, 231);font: 15pt \"Lemon/Milk\";")
        self.label_4.setTextFormat(QtCore.Qt.PlainText)
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.label_4.setText("Quantity")
        self.label_4.move(230,90)


        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(460, 20, 381, 61))
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("color: rgb(64, 210, 231);font: 15pt \"Lemon/Milk\";")
        self.label_5.setTextFormat(QtCore.Qt.PlainText)
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_4")
        self.label_5.setText("Before Discount")
        self.label_5.move(400,90)


        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(460, 20, 381, 61))
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet("color: rgb(64, 210, 231);font: 15pt \"Lemon/Milk\";")
        self.label_6.setTextFormat(QtCore.Qt.PlainText)
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_4")
        self.label_6.setText("After Discount")
        self.label_6.move(600,90)        

        self.checkoutButton = QtWidgets.QPushButton(self)
        self.checkoutButton.setFixedSize(400,60)
        self.checkoutButton.setText("Proceed to Checkout")
        self.checkoutButton.move(430,650)
        self.checkoutButton.setStyleSheet("background-color: rgb(255, 191, 93);color: rgb(247, 247, 247);font: 15pt \"Lemon/Milk\";")
        
        for i in self.cartList:
            self.checkbox = QtWidgets.QCheckBox(self)
            self.checkbox.setChecked(True)
            self.checkbox.setFixedSize(700,35)
            self.cartCheckBox.append(self.checkbox)
            
        
        x = 100
        y = 150
        count = 0
        
        for i in range(len(self.cartCheckBox)):
            print(self.cartList[i])
            self.cartCheckBox[i].setStyleSheet("background-color: rgb(103, 30, 189); font-family: Josefin Sans; font-size: 13pt; color: rgb(151, 250, 252)")
            self.cartCheckBox[i].setText(self.displayCartItem(self.cartList[i]))
            self.cartCheckBox[i].move(x,y + 50*count)
            self.cartCheckBox[i].adjustSize()
            count += 1
        self.checkoutButton.clicked.connect(self.initCheckoutGui)

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

        return "Name: " + prod_name + "                        "+ str(quantity) + "                                    "+ str(before_discount)+ "                        "+str(after_discount)


    
    def clearViewCart(self):
        for i in self.cartCheckBox:
            print("this woriking 3")
            
            i.hide()
            print(str(i) + str(i.isVisible()))
        self.removeLabel.hide()
        self.checkoutButton.hide()
        

    def addTransactions(self):
        self.label.hide()
        self.label_2.hide()
        self.label_3.hide()
        self.label_4.hide()
        self.label_5.hide()
        self.label_6.hide()
        self.label10.hide()

        print("executed")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(0, 0, 1281, 721))
        self.label.setText("")

        self.label.setPixmap(QtGui.QPixmap("Images/receipt.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.show()

        self.ExistingUserBtn_2 = QtWidgets.QPushButton(self)
        self.ExistingUserBtn_2.setGeometry(QtCore.QRect(650, 650, 281, 41))
        self.ExistingUserBtn_2.setStyleSheet("background-color: rgb(255, 191, 93);color: rgb(247, 247, 247);font: 15pt \"Lemon/Milk\";")
        self.ExistingUserBtn_2.setObjectName("ExistingUserBtn_2")
        self.ExistingUserBtn_2.setText("E X I T")
        self.ExistingUserBtn_2.clicked.connect(self.profile)
        self.ExistingUserBtn_2.show()

        try:
            add_to_transactins = (self.cartList[0][2],self.cartList[0][1],self.total_cost,self.employee_id.text(),self.employee_rating.text())
            print(add_to_transactins)
            self.c.execute("insert into transactions(receipt_id,user_id,total_cost,employee_id,satisfaction) values (?,?,?,?,?)",add_to_transactins)
            self.con.commit()
        except Exception:
            pass

        self.employee_id.hide()
        self.employee_rating.hide()
        self.checkoutLabel1.hide()
        self.checkoutLabel2.hide()
        for i in range(len(self.cartCheckBox)):
            self.cartCheckBox[i].hide()
        self.proceedButton.hide()
        self.receipt_id_label = QtWidgets.QLabel(self)



        try:
            self.receipt_id_label.setText(str(self.cartList[0][2]))

           
        except Exception:
            self.receipt_id_label.setText("0")
        
        self.receipt_id_label.setFont(QtGui.QFont("Josefin Sans",45, QtGui.QFont.Bold))
        self.receipt_id_label.adjustSize()
        # self.receipt_id_label.setAlignment(550,350)
        self.receipt_id_label.move(640,300)
        self.receipt_id_label.show()



    def initCheckoutGui(self):
        self.label.hide()
        self.label_2.hide()
        self.label_3.hide()
        self.label_4.hide()
        self.label_5.hide()
        self.label_6.hide()
        self.label10 = QtWidgets.QLabel(self)
        self.label10.setGeometry(QtCore.QRect(0, 0, 1281, 721))
        self.label10.setText("")

        self.label10.setPixmap(QtGui.QPixmap("Images/rating.jpg"))
        self.label10.setScaledContents(True)
        self.label10.setObjectName("label")

        self.label10.show()

        # self.clearViewCart()
        for i in range(len(self.cartCheckBox)):
            print("this woriking 3")
            
            self.cartCheckBox[i].hide()
            # print(str(i) + str(i.isVisible()))
        self.removeLabel.hide()
        self.checkoutButton.hide()
        
        self.checkoutLabel1 = QtWidgets.QLabel(self)
        self.checkoutLabel1.setText("Enter Employee ID: ")
        self.checkoutLabel1.setFont(QtGui.QFont("Josefin Sans",20, QtGui.QFont.Bold))

        self.checkoutLabel1.adjustSize()
        self.checkoutLabel1.move(100,200)
        self.checkoutLabel1.show()

        self.checkoutLabel2 = QtWidgets.QLabel(self)
        self.checkoutLabel2.setText("Enter Employee Rating (x.xx): ")
        self.checkoutLabel2.setFont(QtGui.QFont("Josefin Sans",20, QtGui.QFont.Bold))
        self.checkoutLabel2.adjustSize()
        self.checkoutLabel2.move(100,350)
        self.checkoutLabel2.show()

        count = 1
        x=300
        y=100
        self.employee_id = QtWidgets.QLineEdit(self)
        self.employee_id.setStyleSheet("background-color: white;")
        self.employee_id.move(100,250)
        self.employee_id.show()

        self.employee_rating = QtWidgets.QLineEdit(self)
        self.employee_rating.setStyleSheet("background-color: white;")
        self.employee_rating.move(100,400)
        self.employee_rating.show()
        
        

        self.total_cost = 0
        for i in range(len(self.cartCheckBox)):
            print(self.cartCheckBox[i].isVisible())
            if self.cartCheckBox[i].isChecked():
                self.cartCheckBox[i].move(x,y + 50*count)
                # self.cartCheckBox[i].show()
                self.total_cost+= self.cartList[i][-1]
                try:
                    self.c.execute("insert into user_purchases (purchase_id,user_id,receipt_id,product_id,quantity,discounts_id,before_discount,after_discount) values (?,?,?,?,?,?,?,?)",tuple(self.cartList[i]))
                    count += 1
                except Exception:
                    pass
        
        self.proceedButton = QtWidgets.QPushButton(self)
        self.proceedButton.setStyleSheet("background-color: rgb(255, 191, 93);color: rgb(247, 247, 247);font: 15pt \"Lemon/Milk\";")
        self.proceedButton.move(150,600)
        self.proceedButton.setText("Proceed")
        self.proceedButton.show()
        self.proceedButton.setGeometry(QtCore.QRect(150, 550, 281, 41))
        self.proceedButton.clicked.connect(self.addTransactions)
         
        
        

    
if __name__ == "__main__":
    

    app = QApplication(sys.argv)
    win = SamikWindow([[1, 1, 1, 4, 1, 1, 1, 45]])
    win.show()
    sys.exit(app.exec_())