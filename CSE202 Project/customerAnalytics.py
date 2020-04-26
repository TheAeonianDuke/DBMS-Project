# Ritoma Sen

from PyQt5 import QtWidgets, uic
# import homeuinew
import sqlite3
import queries
import sys

class UiCustomerAnalytics(QtWidgets.QMainWindow):

	def __init__(self):
		super(UiCustomerAnalytics, self).__init__()
		uic.loadUi('customerAnalytics.ui', self)

		self.user_id = '1'

		# Finding components.
		self.pushButtonProfile = self.findChild(QtWidgets.QPushButton, 'pushButtonProfile')
		self.tableWidgetMostFrequent = self.findChild(QtWidgets.QTableWidget, 'tableWidgetMostFrequent')
		self.labelTotalValue = self.findChild(QtWidgets.QLabel, 'labelTotalValue')
		self.labelPerTransactionValue = self.findChild(QtWidgets.QLabel, 'labelPerTransactionValue')
		self.labelDiscounts = self.findChild(QtWidgets.QLabel, 'labelDiscounts')

		# Doing some magic for flawless functioning.
		self.tableStyling()
		self.showMostFrequentProducts()
		self.showDiscounts()
		self.displayExpenditureValues()

		# Connecting components to methods.
		self.pushButtonProfile.clicked.connect(self.pushButtonProfileClicked)

		self.show()
	
	def tableStyling(self):
		css = '::section{background-color: rgb(103, 30, 189); font-family: Josefin Sans; font-size: 13px; color: rgb(151, 250, 252)}'
		self.tableWidgetMostFrequent.horizontalHeader().setStyleSheet(css)
		self.tableWidgetMostFrequent.verticalHeader().setStyleSheet(css)
	
	def showMostFrequentProducts(self):
		self.mostFrequentColumnNames = queries.columnNames(connection, cursor, 'products')
		self.tableWidgetMostFrequent.setColumnCount(len(self.mostFrequentColumnNames))
		self.tableWidgetMostFrequent.setHorizontalHeaderLabels(self.mostFrequentColumnNames)
		self.mostFrequentRows = queries.findFiveMostFrequentForUser(connection, cursor, self.user_id)
		self.tableWidgetMostFrequent.setRowCount(len(self.mostFrequentRows))
		for row in range(0, len(self.mostFrequentRows)):
			for column in range(0, len(self.mostFrequentColumnNames)):
				cell = str(self.mostFrequentRows[row][column])
				self.tableWidgetMostFrequent.setItem(row, column, QtWidgets.QTableWidgetItem(cell))
		self.tableWidgetMostFrequent.resizeColumnsToContents()
		self.tableWidgetMostFrequent.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
	
	def showDiscounts(self):
		self.discountsOn = queries.findDiscountsOnOrOff(connection, cursor, self.user_id)
		if (self.discountsOn):
			self.labelDiscounts.setText('YAY! YOUR FAVOURITE PRODUCTS ARE ON DISCOUNT.')
		else:
			self.labelDiscounts.setText('SORRY, YOUR FAVOURITE PRODUCTS ARE NOT ON DISCOUNT RIGHT NOW.')

	def displayExpenditureValues(self):
		self.totalExpenditure = queries.calculateTotalExpenditure(connection, cursor, self.user_id)
		self.averageExpenditurePerTransaction = queries.calculateAverageExpenditurePerTransaction(connection, cursor, self.user_id)
		self.labelTotalValue.setText(str(self.totalExpenditure))
		self.labelPerTransactionValue.setText(str(self.averageExpenditurePerTransaction))
	
	def pushButtonProfileClicked(self):
		# self.customerProfile = QtWidgets.QMainWindow()
		# self.customerProfileUi = homeuiunew.Ui_MainWindow()
		# self.ui.setupUi(self.customerProfile)
		# self.customerProfile.show()
		# self.hide()
		pass

connection = sqlite3.connect('dbms_db.db')
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	window = UiCustomerAnalytics()
	app.exec_()
