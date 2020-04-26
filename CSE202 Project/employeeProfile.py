# Ritoma Sen

from PyQt5 import QtWidgets, uic
import employeeInventory, employeeAnalytics, employeeEmployees, employeeCustomers
import sys

class UiEmployeeProfile(QtWidgets.QMainWindow):

	def __init__(self):
		super(UiEmployeeProfile, self).__init__()
		uic.loadUi('employeeProfile.ui', self)
		
		# Finding components.
		self.pushButtonInventory = self.findChild(QtWidgets.QPushButton, 'pushButtonInventory')
		self.pushButtonAnalytics = self.findChild(QtWidgets.QPushButton, 'pushButtonAnalytics')
		self.pushButtonEmployees = self.findChild(QtWidgets.QPushButton, 'pushButtonEmployees')
		self.pushButtonCustomers = self.findChild(QtWidgets.QPushButton, 'pushButtonCustomers')

		# Connecting components to methods.
		self.pushButtonInventory.clicked.connect(lambda: self.pushButtonClicked('inventory'))
		self.pushButtonAnalytics.clicked.connect(lambda: self.pushButtonClicked('analytics'))
		self.pushButtonEmployees.clicked.connect(lambda: self.pushButtonClicked('employees'))
		self.pushButtonCustomers.clicked.connect(lambda: self.pushButtonClicked('customers'))

		self.show()
	
	def pushButtonClicked(self, pushButtonName):
		if (pushButtonName == 'inventory'):
			# Open employeeInventory
			self.employeeInventory = QtWidgets.QMainWindow()
			self.employeeInventoryUi = employeeInventory.UiEmployeeInventory()
			self.hide()
		if (pushButtonName == 'analytics'):
			# Open employeeAnalytics
			self.employeeAnalytics = QtWidgets.QMainWindow()
			self.employeeAnalyticsUi = employeeAnalytics.UiEmployeeAnalytics()
			self.hide()
		if (pushButtonName == 'employees'):
			# Open employeeEmployees
			self.employeeEmployees = QtWidgets.QMainWindow()
			self.employeeEmployeesUi = employeeEmployees.UiEmployeeEmployees()
			self.hide()
		if (pushButtonName == 'customers'):
			# Open employeeCustomers
			self.employeeCustomers = QtWidgets.QMainWindow()
			self.employeeCustomersUi = employeeCustomers.UiEmployeeCustomers()
			self.hide()

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	window = UiEmployeeProfile()
	app.exec_()
