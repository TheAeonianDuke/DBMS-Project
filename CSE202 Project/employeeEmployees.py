# Ritoma Sen

from PyQt5 import QtWidgets, uic
import employeeProfile
import sqlite3
import queries
import sys

class UiEmployeeEmployees(QtWidgets.QMainWindow):

	def __init__(self):
		super(UiEmployeeEmployees, self).__init__()
		uic.loadUi('employeeEmployees.ui', self)

		# Finding components.
		self.pushButtonProfile = self.findChild(QtWidgets.QPushButton, 'pushButtonProfile')
		self.tableWidgetEmployees = self.findChild(QtWidgets.QTableWidget, 'tableWidgetEmployees')
		self.lineEditSearchByName = self.findChild(QtWidgets.QLineEdit, 'lineEditSearchByName')
		self.lineEditSearchById = self.findChild(QtWidgets.QLineEdit, 'lineEditSearchById')
		self.lineEditViewBestN = self.findChild(QtWidgets.QLineEdit, 'lineEditViewBestN')

		# Doing some magic for flawless functioning.
		self.tableStyling()
		self.displayTable()

		# Connecting components to methods.
		self.pushButtonProfile.clicked.connect(self.pushButtonProfileClicked)
		self.lineEditSearchByName.returnPressed.connect(self.searchByName)
		self.lineEditSearchById.returnPressed.connect(self.searchByID)
		self.lineEditViewBestN.returnPressed.connect(self.showTopN)

		self.show()
	
	def tableStyling(self):
		css = '::section{background-color: rgb(103, 30, 189); font-family: Josefin Sans; font-size: 13px; color: rgb(151, 250, 252)}'
		self.tableWidgetEmployees.horizontalHeader().setStyleSheet(css)
		self.tableWidgetEmployees.verticalHeader().setStyleSheet(css)
		
	def displayTable(self):
		self.employeesColumnNames = queries.columnNames(connection, cursor, 'employees')
		self.tableWidgetEmployees.setColumnCount(len(self.employeesColumnNames))
		self.tableWidgetEmployees.setHorizontalHeaderLabels(self.employeesColumnNames)
		self.employeesRows = queries.allRows(connection, cursor, 'employees')
		self.tableWidgetEmployees.setRowCount(len(self.employeesRows))
		for row in range(0, len(self.employeesRows)):
			for column in range(0, len(self.employeesColumnNames)):
				cell = str(self.employeesRows[row][column])
				self.tableWidgetEmployees.setItem(row, column, QtWidgets.QTableWidgetItem(cell))
		self.tableWidgetEmployees.resizeColumnsToContents()
		self.tableWidgetEmployees.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
	
	def searchByName(self):
		self.employeesColumnNames = queries.columnNames(connection, cursor, 'employees')
		self.tableWidgetEmployees.setColumnCount(len(self.employeesColumnNames))
		self.tableWidgetEmployees.setHorizontalHeaderLabels(self.employeesColumnNames)
		self.searchString = self.lineEditSearchByName.text()
		if (self.searchString != ''):
			self.searchedRows = queries.searchInRowsTwoColumns(connection, cursor, 'employees', 'first_name', 'last_name', self.searchString)
			self.tableWidgetEmployees.setRowCount(len(self.searchedRows))
			for row in range(0, len(self.searchedRows)):
				for column in range(0, len(self.employeesColumnNames)):
					cell = str(self.searchedRows[row][column])
					self.tableWidgetEmployees.setItem(row, column, QtWidgets.QTableWidgetItem(cell))
			self.tableWidgetEmployees.resizeColumnsToContents()
			self.tableWidgetEmployees.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
		else:
			self.displayTable()
	
	def searchByID(self):
		self.employeesColumnNames = queries.columnNames(connection, cursor, 'employees')
		self.tableWidgetEmployees.setColumnCount(len(self.employeesColumnNames))
		self.tableWidgetEmployees.setHorizontalHeaderLabels(self.employeesColumnNames)
		self.matchString = self.lineEditSearchById.text()
		if (self.matchString != ''):
			self.searchedRows = queries.matchRows(connection, cursor, 'employees', 'employees_id', self.matchString)
			self.tableWidgetEmployees.setRowCount(len(self.searchedRows))
			for row in range(0, len(self.searchedRows)):
				for column in range(0, len(self.employeesColumnNames)):
					cell = str(self.searchedRows[row][column])
					self.tableWidgetEmployees.setItem(row, column, QtWidgets.QTableWidgetItem(cell))
			self.tableWidgetEmployees.resizeColumnsToContents()
			self.tableWidgetEmployees.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
		else:
			self.displayTable()
	
	def showTopN(self):
		self.employeesColumnNames = queries.columnNames(connection, cursor, 'employees')
		self.tableWidgetEmployees.setColumnCount(len(self.employeesColumnNames))
		self.tableWidgetEmployees.setHorizontalHeaderLabels(self.employeesColumnNames)
		self.n = self.lineEditViewBestN.text()
		if (self.n != ''):
			self.searchedRows = queries.findTopN(connection, cursor, 'employees', 'peer_rating', str(self.n))
			self.tableWidgetEmployees.setRowCount(len(self.searchedRows))
			for row in range(0, len(self.searchedRows)):
				for column in range(0, len(self.employeesColumnNames)):
					cell = str(self.searchedRows[row][column])
					self.tableWidgetEmployees.setItem(row, column, QtWidgets.QTableWidgetItem(cell))
			self.tableWidgetEmployees.resizeColumnsToContents()
			self.tableWidgetEmployees.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
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
	window = UiEmployeeEmployees()
	app.exec_()
