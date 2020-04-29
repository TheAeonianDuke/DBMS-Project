# Ritoma Sen

from PyQt5 import QtWidgets, uic
import employeeProfile
import sqlite3
import queries
import sys

class UiEmployeeCustomers(QtWidgets.QMainWindow):

	def __init__(self):
		super(UiEmployeeCustomers, self).__init__()
		uic.loadUi('employeeCustomers.ui', self)

		# Finding components.
		self.pushButtonProfile = self.findChild(QtWidgets.QPushButton, 'pushButtonProfile')
		self.tableWidgetCustomers = self.findChild(QtWidgets.QTableWidget, 'tableWidgetCustomers')
		self.lineEditSearchByName = self.findChild(QtWidgets.QLineEdit, 'lineEditSearchByName')
		self.lineEditSearchById = self.findChild(QtWidgets.QLineEdit, 'lineEditSearchById')

		# Doing some magic for flawless functioning.
		self.tableStyling()
		self.displayTable()

		# Connecting components to methods.
		self.pushButtonProfile.clicked.connect(self.pushButtonProfileClicked)
		self.lineEditSearchByName.returnPressed.connect(self.searchByName)
		self.lineEditSearchById.returnPressed.connect(self.searchByID)

		self.show()
	
	def tableStyling(self):
		css = '::section{background-color: rgb(103, 30, 189); font-family: Josefin Sans; font-size: 13px; color: rgb(151, 250, 252)}'
		self.tableWidgetCustomers.horizontalHeader().setStyleSheet(css)
		self.tableWidgetCustomers.verticalHeader().setStyleSheet(css)
		
	def displayTable(self):
		self.customersColumnNames = queries.columnNames(connection, cursor, 'users')
		self.tableWidgetCustomers.setColumnCount(len(self.customersColumnNames))
		self.tableWidgetCustomers.setHorizontalHeaderLabels(self.customersColumnNames)
		self.customersRows = queries.allRows(connection, cursor, 'users')
		self.tableWidgetCustomers.setRowCount(len(self.customersRows))
		for row in range(0, len(self.customersRows)):
			for column in range(0, len(self.customersColumnNames)):
				cell = str(self.customersRows[row][column])
				self.tableWidgetCustomers.setItem(row, column, QtWidgets.QTableWidgetItem(cell))
		self.tableWidgetCustomers.resizeColumnsToContents()
		self.tableWidgetCustomers.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
	
	def searchByName(self):
		self.customersColumnNames = queries.columnNames(connection, cursor, 'users')
		self.tableWidgetCustomers.setColumnCount(len(self.customersColumnNames))
		self.tableWidgetCustomers.setHorizontalHeaderLabels(self.customersColumnNames)
		self.searchString = self.lineEditSearchByName.text()
		if (self.searchString != ''):
			self.searchedRows = queries.searchInRowsTwoColumns(connection, cursor, 'users', 'first_name', 'last_name', self.searchString)
			self.tableWidgetCustomers.setRowCount(len(self.searchedRows))
			for row in range(0, len(self.searchedRows)):
				for column in range(0, len(self.customersColumnNames)):
					cell = str(self.searchedRows[row][column])
					self.tableWidgetCustomers.setItem(row, column, QtWidgets.QTableWidgetItem(cell))
			self.tableWidgetCustomers.resizeColumnsToContents()
			self.tableWidgetCustomers.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
		else:
			self.displayTable()
	
	def searchByID(self):
		self.customersColumnNames = queries.columnNames(connection, cursor, 'users')
		self.tableWidgetCustomers.setColumnCount(len(self.customersColumnNames))
		self.tableWidgetCustomers.setHorizontalHeaderLabels(self.customersColumnNames)
		self.matchString = self.lineEditSearchById.text()
		if (self.matchString != ''):
			self.searchedRows = queries.matchRows(connection, cursor, 'users', 'user_id', self.matchString)
			self.tableWidgetCustomers.setRowCount(len(self.searchedRows))
			for row in range(0, len(self.searchedRows)):
				for column in range(0, len(self.customersColumnNames)):
					cell = str(self.searchedRows[row][column])
					self.tableWidgetCustomers.setItem(row, column, QtWidgets.QTableWidgetItem(cell))
			self.tableWidgetCustomers.resizeColumnsToContents()
			self.tableWidgetCustomers.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
		else:
			self.displayTable()
		
	def pushButtonProfileClicked(self):
		self.employeeProfile = QtWidgets.QMainWindow()
		self.employeeProfileUi = employeeProfile.UiEmployeeProfile()
		self.hide()

connection = sqlite3.connect('dbms_db.db')
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	window = UiEmployeeCustomers()
	app.exec_()
