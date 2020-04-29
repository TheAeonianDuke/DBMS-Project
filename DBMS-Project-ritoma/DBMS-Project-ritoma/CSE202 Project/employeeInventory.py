# Ritoma Sen

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
import employeeProfile
import sqlite3
import queries
import sys

class UiEmployeeInventory(QtWidgets.QMainWindow):

	def __init__(self):
		super(UiEmployeeInventory, self).__init__()
		uic.loadUi('employeeInventory.ui', self)

		# Finding components.
		self.pushButtonProfile = self.findChild(QtWidgets.QPushButton, 'pushButtonProfile')
		self.tableWidgetInventory = self.findChild(QtWidgets.QTableWidget, 'tableWidgetInventory')
		self.lineEditSearchByName = self.findChild(QtWidgets.QLineEdit, 'lineEditSearchByName')
		self.lineEditSearchById = self.findChild(QtWidgets.QLineEdit, 'lineEditSearchById')

		# Doing some magic for flawless functioning.
		self.tableStyling()
		self.displayTable()

		# Connecting components to methods.
		self.pushButtonProfile.clicked.connect(self.pushButtonProfileClicked)
		self.lineEditSearchByName.returnPressed.connect(self.searchByName)
		self.lineEditSearchById.returnPressed.connect(self.searchByID)
		self.tableWidgetInventory.cellDoubleClicked.connect(self.showLocation)

		self.show()
	
	def tableStyling(self):
		css = '::section{background-color: rgb(103, 30, 189); font-family: Josefin Sans; font-size: 13px; color: rgb(151, 250, 252)}'
		self.tableWidgetInventory.horizontalHeader().setStyleSheet(css)
		self.tableWidgetInventory.verticalHeader().setStyleSheet(css)
		
	def displayTable(self):
		self.inventoryColumnNames = queries.columnNames(connection, cursor, 'inventory')
		self.tableWidgetInventory.setColumnCount(len(self.inventoryColumnNames))
		self.tableWidgetInventory.setHorizontalHeaderLabels(self.inventoryColumnNames)
		self.inventoryRows = queries.allRows(connection, cursor, 'inventory')
		self.tableWidgetInventory.setRowCount(len(self.inventoryRows))
		for row in range(0, len(self.inventoryRows)):
			for column in range(0, len(self.inventoryColumnNames)):
				cell = str(self.inventoryRows[row][column])
				self.tableWidgetInventory.setItem(row, column, QtWidgets.QTableWidgetItem(cell))
		self.tableWidgetInventory.resizeColumnsToContents()
		self.tableWidgetInventory.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
	
	def pushButtonProfileClicked(self):
		self.employeeProfile = QtWidgets.QMainWindow()
		self.employeeProfileUi = employeeProfile.UiEmployeeProfile()
		self.hide()
	
	def searchByName(self):
		self.inventoryColumnNames = queries.columnNames(connection, cursor, 'inventory')
		self.tableWidgetInventory.setColumnCount(len(self.inventoryColumnNames))
		self.tableWidgetInventory.setHorizontalHeaderLabels(self.inventoryColumnNames)
		self.searchString = self.lineEditSearchByName.text()
		if (self.searchString != ''):
			self.searchedRows = queries.searchInRows(connection, cursor, 'inventory', 'product_name', self.searchString)
			self.tableWidgetInventory.setRowCount(len(self.searchedRows))
			for row in range(0, len(self.searchedRows)):
				for column in range(0, len(self.inventoryColumnNames)):
					cell = str(self.searchedRows[row][column])
					self.tableWidgetInventory.setItem(row, column, QtWidgets.QTableWidgetItem(cell))
			self.tableWidgetInventory.resizeColumnsToContents()
			self.tableWidgetInventory.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
		else:
			self.displayTable()
	
	def searchByID(self):
		self.inventoryColumnNames = queries.columnNames(connection, cursor, 'inventory')
		self.tableWidgetInventory.setColumnCount(len(self.inventoryColumnNames))
		self.tableWidgetInventory.setHorizontalHeaderLabels(self.inventoryColumnNames)
		self.matchString = self.lineEditSearchById.text()
		if (self.matchString != ''):
			self.searchedRows = queries.matchRows(connection, cursor, 'inventory', 'product_id', self.matchString)
			self.tableWidgetInventory.setRowCount(len(self.searchedRows))
			for row in range(0, len(self.searchedRows)):
				for column in range(0, len(self.inventoryColumnNames)):
					cell = str(self.searchedRows[row][column])
					self.tableWidgetInventory.setItem(row, column, QtWidgets.QTableWidgetItem(cell))
			self.tableWidgetInventory.resizeColumnsToContents()
			self.tableWidgetInventory.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
		else:
			self.displayTable()
	
	def showLocation(self, row, column):
		location = queries.findLocation(connection, cursor, str(row + 1))
		aisle = location[0]
		shelf = location[1]
		self.messageBoxLocation = QMessageBox()
		self.messageBoxLocation.setWindowTitle('Location')
		self.messageBoxLocation.setText('Aisle: ' + aisle + '\nShelf: ' + shelf)
		self.messageBoxLocation.exec_()

connection = sqlite3.connect('dbms_db.db')
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	window = UiEmployeeInventory()
	app.exec_()
