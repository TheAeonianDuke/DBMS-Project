# Ritoma Sen

from PyQt5 import QtWidgets, uic
import employeeProfile, employeeTransactions, employeePurchases
import sqlite3
import queries
import sys

class UiEmployeeAnalytics(QtWidgets.QMainWindow):

	def __init__(self):
		super(UiEmployeeAnalytics, self).__init__()
		uic.loadUi('employeeAnalytics.ui', self)

		# Finding components.
		self.pushButtonProfile = self.findChild(QtWidgets.QPushButton, 'pushButtonProfile')
		self.pushButtonTransactions = self.findChild(QtWidgets.QPushButton, 'pushButtonTransactions')
		self.pushButtonPurchases = self.findChild(QtWidgets.QPushButton, 'pushButtonPurchases')
		self.tableWidgetMostFrequent = self.findChild(QtWidgets.QTableWidget, 'tableWidgetMostFrequent')
		self.labelTotalValue = self.findChild(QtWidgets.QLabel, 'labelTotalValue')
		self.labelPerTransactionValue = self.findChild(QtWidgets.QLabel, 'labelPerTransactionValue')

		# Doing some magic for flawless functioning.
		self.tableStyling()
		self.showMostFrequentProducts()
		self.displayProfitValues()

		# Connecting components to methods.
		self.pushButtonProfile.clicked.connect(self.pushButtonProfileClicked)
		self.pushButtonTransactions.clicked.connect(self.pushButtonTransactionsClicked)
		self.pushButtonPurchases.clicked.connect(self.pushButtonPurchasesClicked)

		self.show()
	
	def tableStyling(self):
		css = '::section{background-color: rgb(103, 30, 189); font-family: Josefin Sans; font-size: 13px; color: rgb(151, 250, 252)}'
		self.tableWidgetMostFrequent.horizontalHeader().setStyleSheet(css)
		self.tableWidgetMostFrequent.verticalHeader().setStyleSheet(css)
	
	def showMostFrequentProducts(self):
		self.mostFrequentColumnNames = queries.columnNames(connection, cursor, 'products')
		self.tableWidgetMostFrequent.setColumnCount(len(self.mostFrequentColumnNames))
		self.tableWidgetMostFrequent.setHorizontalHeaderLabels(self.mostFrequentColumnNames)
		self.mostFrequentRows = queries.findFiveMostFrequentAll(connection, cursor)
		self.tableWidgetMostFrequent.setRowCount(len(self.mostFrequentRows))
		for row in range(0, len(self.mostFrequentRows)):
			for column in range(0, len(self.mostFrequentColumnNames)):
				cell = str(self.mostFrequentRows[row][column])
				self.tableWidgetMostFrequent.setItem(row, column, QtWidgets.QTableWidgetItem(cell))
		self.tableWidgetMostFrequent.resizeColumnsToContents()
		self.tableWidgetMostFrequent.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
	
	def displayProfitValues(self):
		self.totalProfit = queries.calculateTotalProfit(connection, cursor)
		self.averageProfitPerTransaction = queries.calculateAverageProfitPerTransaction(connection, cursor)
		self.labelTotalValue.setText(str(self.totalProfit))
		self.labelPerTransactionValue.setText(str(self.averageProfitPerTransaction))
	
	def pushButtonProfileClicked(self):
		self.employeeProfile = QtWidgets.QMainWindow()
		self.employeeProfileUi = employeeProfile.UiEmployeeProfile()
		self.hide()
	
	def pushButtonTransactionsClicked(self):
		self.employeeTransactions = QtWidgets.QMainWindow()
		self.employeeTransactionsUi = employeeTransactions.UiEmployeeTransactions()
		self.hide()

	def pushButtonPurchasesClicked(self):
		self.employeePurchases = QtWidgets.QMainWindow()
		self.employeePurchasesUi = employeePurchases.UiEmployeePurchases()
		self.hide()

connection = sqlite3.connect('dbms_db.db')
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	window = UiEmployeeAnalytics()
	app.exec_()
