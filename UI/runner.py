from PyQt5 import QtCore, QtGui, QtWidgets

import sys 
import requests
import splashscreen
import newuser


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	window = QtWidgets.QMainWindow()
	splashui = splashscreen.Ui_MainWindow()
	
	splashui.setupUi(window)

	window.show()
	sys.exit(app.exec_())