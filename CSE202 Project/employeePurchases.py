# Ritoma Sen

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
import employeeProfile
import sqlite3
import queries
import sys

class UiEmployeePurchases(QtWidgets.QMainWindow):

	def __init__(self):
		super(UiEmployeePurchases, self).__init__()
		uic.loadUi('employeePurchases.ui', self)

		# Finding components.
		self.pushButtonProfile = self.findChild(QtWidgets.QPushButton, 'pushButtonProfile')
		self.tableWidgetPurchases = self.findChild(QtWidgets.QTableWidget, 'tableWidgetPurchases')

		# Doing some magic for flawless functioning.
		self.tableStyling()
		self.displayTable()

		# Connecting components to methods.
		self.pushButtonProfile.clicked.connect(self.pushButtonProfileClicked)

		self.show()
	
	def tableStyling(self):
		css = '::section{background-color: rgb(103, 30, 189); font-family: Josefin Sans; font-size: 13px; color: rgb(151, 250, 252)}'
		self.tableWidgetPurchases.horizontalHeader().setStyleSheet(css)
		self.tableWidgetPurchases.verticalHeader().setStyleSheet(css)
	
	def displayTable(self):
		self.purchasesColumnNames = queries.columnNames(connection, cursor, 'user_purchases')
		self.tableWidgetPurchases.setColumnCount(len(self.purchasesColumnNames))
		self.tableWidgetPurchases.setHorizontalHeaderLabels(self.purchasesColumnNames)
		self.purchasesRows = queries.allRows(connection, cursor, 'user_purchases')
		self.tableWidgetPurchases.setRowCount(len(self.purchasesRows))
		for row in range(0, len(self.purchasesRows)):
			for column in range(0, len(self.purchasesColumnNames)):
				cell = str(self.purchasesRows[row][column])
				self.tableWidgetPurchases.setItem(row, column, QtWidgets.QTableWidgetItem(cell))
		self.tableWidgetPurchases.resizeColumnsToContents()
		self.tableWidgetPurchases.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

	def pushButtonProfileClicked(self):
		self.employeeProfile = QtWidgets.QMainWindow()
		self.employeeProfileUi = employeeProfile.UiEmployeeProfile()
		self.hide()

connection = sqlite3.connect('dbms_db.db')
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	window = UiEmployeePurchases()
	app.exec_()
