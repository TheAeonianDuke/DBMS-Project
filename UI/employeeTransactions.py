# Ritoma Sen

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
import employeeProfile
import sqlite3
import queries
import sys

class UiEmployeeTransactions(QtWidgets.QMainWindow):

	def __init__(self):
		super(UiEmployeeTransactions, self).__init__()
		uic.loadUi('employeeTransactions.ui', self)

		# Finding components.
		self.pushButtonProfile = self.findChild(QtWidgets.QPushButton, 'pushButtonProfile')
		self.tableWidgetTransactions = self.findChild(QtWidgets.QTableWidget, 'tableWidgetTransactions')

		# Doing some magic for flawless functioning.
		self.tableStyling()
		self.displayTable()

		# Connecting components to methods.
		self.pushButtonProfile.clicked.connect(self.pushButtonProfileClicked)

		self.show()
	
	def tableStyling(self):
		css = '::section{background-color: rgb(103, 30, 189); font-family: Josefin Sans; font-size: 13px; color: rgb(151, 250, 252)}'
		self.tableWidgetTransactions.horizontalHeader().setStyleSheet(css)
		self.tableWidgetTransactions.verticalHeader().setStyleSheet(css)
	
	def displayTable(self):
		self.transactionsColumnNames = queries.columnNames(connection, cursor, 'transactions')
		self.tableWidgetTransactions.setColumnCount(len(self.transactionsColumnNames))
		self.tableWidgetTransactions.setHorizontalHeaderLabels(self.transactionsColumnNames)
		self.transactionsRows = queries.allRows(connection, cursor, 'transactions')
		self.tableWidgetTransactions.setRowCount(len(self.transactionsRows))
		for row in range(0, len(self.transactionsRows)):
			for column in range(0, len(self.transactionsColumnNames)):
				cell = str(self.transactionsRows[row][column])
				self.tableWidgetTransactions.setItem(row, column, QtWidgets.QTableWidgetItem(cell))
		self.tableWidgetTransactions.resizeColumnsToContents()
		self.tableWidgetTransactions.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
	
	def pushButtonProfileClicked(self):
		self.employeeProfile = QtWidgets.QMainWindow()
		self.employeeProfileUi = employeeProfile.UiEmployeeProfile()
		self.hide()

connection = sqlite3.connect('dbms_db.db')
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	window = UiEmployeeTransactions()
	app.exec_()
