# Ritoma Sen

import sqlite3
import re
from heapq import nlargest

def columnNames(connection, cursor, tableName):
	"""Returns the column names of the inventory table

	:param connection: The sqlite3 connection to the database.
	:type connection: sqlite3.Connection
	:param cursor: The sqlite3 cursor to execute queries.
	:type cursor: sqlite3.Cursor
	:param tableName: Name of the table for which the column names are to be returned.
	:type tableName: string
	:returns: A list of strings representing the header columns.
	:rtype: list
	"""

	try:
		query = 'SELECT * FROM ' + tableName
		table = cursor.execute(query)
		data = cursor.fetchone()
		return data.keys()
	except Exception:
		pass

def allRows(connection, cursor, tableName):
	"""Returns the rows of the table

	:param connection: The sqlite3 connection to the database.
	:type connection: sqlite3.Connection
	:param cursor: The sqlite3 cursor to execute queries.
	:type cursor: sqlite3.Cursor
	:param tableName: Name of the table for which the rows are to be returned.
	:type tableName: string
	:returns: A list of Row objects representing the rows of the table.
	:rtype: list
	"""

	try:
		query = 'SELECT * FROM ' + tableName
		table = cursor.execute(query)
		rows = []
		for i in table:
			rows.append(i)
		return rows
	except Exception:
		return []

def searchInRows(connection, cursor, tableName, columnName, searchString):
	"""Returns the rows of the table which have the given string in the designated column.

	:param connection: The sqlite3 connection to the database.
	:type connection: sqlite3.Connection
	:param cursor: The sqlite3 cursor to execute queries.
	:type cursor: sqlite3.Cursor
	:param tableName: Name of the table for which the rows are to be returned.
	:type tableName: string
	:param columnName: Name of the column where the string is searched for.
	:type columnName: string
	:param searchString: The string for which the search needs to be performed.
	:type searchString: string
	:returns: A list of Row objects representing the required rows of the table.
	:rtype: list
	"""

	try:
		query = "SELECT * FROM " + tableName + " WHERE " + columnName + " LIKE '%" + searchString + "%'"
		table = cursor.execute(query)
		rows = []
		for i in table:
			rows.append(i)
		return rows
	except Exception:
		return []

def searchInRowsTwoColumns(connection, cursor, tableName, columnNameOne, columnNameTwo, searchString):
	"""Returns the rows of the table which have the given string in the designated column.

	:param connection: The sqlite3 connection to the database.
	:type connection: sqlite3.Connection
	:param cursor: The sqlite3 cursor to execute queries.
	:type cursor: sqlite3.Cursor
	:param tableName: Name of the table for which the rows are to be returned.
	:type tableName: string
	:param columnNameOne: Name of the first column where the string is searched for.
	:type columnNameOne: string
	:param columnNameTwo: Name of the second column where the string is searched for.
	:type columnNameTwo: string
	:param searchString: The string for which the search needs to be performed.
	:type searchString: string
	:returns: A list of Row objects representing the required rows of the table.
	:rtype: list
	"""

	try:
		query = "SELECT * FROM " + tableName + " WHERE " + columnNameOne + " LIKE '%" + searchString + "%'"
		table = cursor.execute(query)
		rows = []
		for i in table:
			rows.append(i)
		query = "SELECT * FROM " + tableName + " WHERE " + columnNameTwo + " LIKE '%" + searchString + "%'"
		table = cursor.execute(query)
		for j in table:
			if j not in rows:
				rows.append(j)
		return rows
	except Exception:
		return []

def matchRows(connection, cursor, tableName, columnName, matchString):
	"""Returns the rows of the table which are an exact match for the given string in the designated column.

	:param connection: The sqlite3 connection to the database.
	:type connection: sqlite3.Connection
	:param cursor: The sqlite3 cursor to execute queries.
	:type cursor: sqlite3.Cursor
	:param tableName: Name of the table for which the rows are to be returned.
	:type tableName: string
	:param columnName: Name of the column where the string is matched.
	:type columnName: string
	:param matchString: The string for which the match needs to be performed.
	:type matchString: string
	:returns: A list of Row objects representing the required rows of the table.
	:rtype: list
	"""

	try:
		query = "SELECT * FROM " + tableName + " WHERE " + columnName + " = " + matchString
		table = cursor.execute(query)
		rows = []
		for i in table:
			rows.append(i)
		return rows
	except Exception:
		return []

def matchRowsTwoColumns(connection, cursor, tableName, columnNameOne, columnNameTwo, matchString):
	"""Returns the rows of the table which are an exact match for the given string in the designated column.

	:param connection: The sqlite3 connection to the database.
	:type connection: sqlite3.Connection
	:param cursor: The sqlite3 cursor to execute queries.
	:type cursor: sqlite3.Cursor
	:param tableName: Name of the table for which the rows are to be returned.
	:type tableName: string
	:param columnNameOne: Name of the first column where the string is matched.
	:type columnNameOne: string
	:param columnNameTwo: Name of the second column where the string is matched.
	:type columnNameTwo: string
	:param matchString: The string for which the match needs to be performed.
	:type matchString: string
	:returns: A list of Row objects representing the required rows of the table.
	:rtype: list
	"""

	try:
		query = "SELECT * FROM " + tableName + " WHERE " + columnNameOne + " = " + matchString
		table = cursor.execute(query)
		rows = []
		for i in table:
			rows.append(i)
		query = "SELECT * FROM " + tableName + " WHERE " + columnNameOne + " = " + matchString
		table = cursor.execute(query)
		for j in table:
			if j not in rows:
				rows.append(j)
		return rows
	except Exception:
		return []

def findLocation(connection, cursor, id):
	"""Returns the location of the product with the given id.

	:param connection: The sqlite3 connection to the database.
	:type connection: sqlite3.Connection
	:param cursor: The sqlite3 cursor to execute queries.
	:type cursor: sqlite3.Cursor
	:param id: The id of the product whose location is to be found.
	:type id: string
	:returns: A tuple of the kind (aisle, shelf)
	:rtype: tuple
	"""

	try:
		query = "SELECT * FROM map WHERE product_id = " + id
		table = cursor.execute(query)
		data = table.fetchone()
		aisle = str(data['location_aisle'])
		shelf = str(data['location_shelf'])
		return (aisle, shelf)
	except Exception:
		return ('NA', 'NA')

def findTopN(connection, cursor, tableName, columnName, n):
	"""Returns the rows of the table which have the top n values in the specified column.

	:param connection: The sqlite3 connection to the database.
	:type connection: sqlite3.Connection
	:param cursor: The sqlite3 cursor to execute queries.
	:type cursor: sqlite3.Cursor
	:param tableName: Name of the table for which the rows are to be returned.
	:type tableName: string
	:param columnName: Name of the column from where the top five values are to be found.
	:type columnName: string
	:param n: The number of top elements to be returned.
	:type n: string
	:returns: A list of Row objects representing the required rows of the table.
	:rtype: list
	"""

	try:
		query = "SELECT * FROM " + tableName + " ORDER BY " + columnName + " DESC LIMIT " + str(n)
		table = cursor.execute(query)
		rows = []
		for i in table:
			rows.append(i)
		return rows
	except Exception:
		return []
	

def calculateTotalProfit(connection, cursor):
	"""Returns the total profit so far.

	:param connection: The sqlite3 connection to the database.
	:type connection: sqlite3.Connection
	:param cursor: The sqlite3 cursor to execute queries.
	:type cursor: sqlite3.Cursor
	:returns: Total profit so far
	:rtype: int
	"""

	try:
		queryOne = "SELECT product_id, quantity, after_discount FROM  user_purchases"
		tableOne = cursor.execute(queryOne)
		dataOne = tableOne.fetchall()
		buyingCosts = []
		sellingCosts = []
		for rowNumber in range(0, len(dataOne)):
			product_id = dataOne[rowNumber]['product_id']
			quantity = dataOne[rowNumber]['quantity']
			after_discount = dataOne[rowNumber]['after_discount']
			queryTwo = "SELECT buying_cost FROM products WHERE product_id = " + str(product_id)
			tableTwo = cursor.execute(queryTwo)
			dataTwo = tableTwo.fetchone()
			buying_cost = dataTwo['buying_cost']
			buy = int(buying_cost) * int(quantity)
			sell = int(after_discount)
			buyingCosts.append(buy)
			sellingCosts.append(sell)
		return (sum(sellingCosts) - sum(buyingCosts))
	except:
		return 0

def calculateTotalExpenditure(connection, cursor, user_id):
	"""Returns the total amount spent at the store by the specified user.

	:param connection: The sqlite3 connection to the database.
	:type connection: sqlite3.Connection
	:param cursor: The sqlite3 cursor to execute queries.
	:type cursor: sqlite3.Cursor
	:param user_id: The user for whom the data is to be found.
	:type user_id: string
	:returns: Total profit so far
	:rtype: int
	"""

	try:
		query = "SELECT after_discount FROM user_purchases WHERE user_id = " + str(user_id)
		table = cursor.execute(query)
		data = table.fetchall()
		expenditure = []
		for rowNumber in range(0, len(data)):
			expenditure.append(data[rowNumber]['after_discount'])
		return sum(expenditure)
	except Exception:
		return 0

def calculateAverageProfitPerTransaction(connection, cursor):
	"""Returns the average profit per transaction.

	:param connection: The sqlite3 connection to the database.
	:type connection: sqlite3.Connection
	:param cursor: The sqlite3 cursor to execute queries.
	:type cursor: sqlite3.Cursor
	:returns: Average profit per transaction
	:rtype: int
	"""

	try:
		totalProfit = calculateTotalProfit(connection, cursor)
		query = "SELECT COUNT(*) FROM transactions"
		table = cursor.execute(query)
		data = table.fetchall()
		numberOfTransactions = data[0][0]
		return round((totalProfit / numberOfTransactions), 2)
	except Exception:
		return 0

def calculateAverageExpenditurePerTransaction(connection, cursor, user_id):
	"""Returns the average profit per transaction.

	:param connection: The sqlite3 connection to the database.
	:type connection: sqlite3.Connection
	:param cursor: The sqlite3 cursor to execute queries.
	:type cursor: sqlite3.Cursor
	:param user_id: The user for whom the data is to be found.
	:type user_id: string
	:returns: Average profit per transaction
	:rtype: int
	"""

	try:
		totalExpenditure = calculateTotalExpenditure(connection, cursor, user_id)
		query = "SELECT COUNT(*) FROM transactions WHERE user_id = " + str(user_id)
		table = cursor.execute(query)
		data = table.fetchall()
		numberOfTransactions = data[0][0]
		return round((totalExpenditure / numberOfTransactions), 2)
	except Exception:
		return 0

def findFiveMostFrequentAll(connection, cursor):
	"""Returns the rows of the product table which have the five most frequently bought products.

	:param connection: The sqlite3 connection to the database.
	:type connection: sqlite3.Connection
	:param cursor: The sqlite3 cursor to execute queries.
	:type cursor: sqlite3.Cursor
	:returns: A list of Row objects representing the required rows of the table.
	:rtype: list
	"""

	try:
		counts = {}
		queryOne = "SELECT product_id, quantity FROM user_purchases"
		tableOne = cursor.execute(queryOne)
		dataOne = tableOne.fetchall()
		for rowNumber in range(0, len(dataOne)):
			product_id = dataOne[rowNumber]['product_id']
			quantity = dataOne[rowNumber]['quantity']
			if product_id not in counts:
				counts[product_id] = quantity
			else:
				counts[product_id] += quantity
		pids = nlargest(5, counts, key = counts.get)
		pidsListString = '('
		for pid in pids:
			pidsListString += str(pid) + ', '
		pidsListString = pidsListString[0:-2] + ')'
		queryTwo = "SELECT * FROM products WHERE product_id in " + pidsListString
		tableTwo = cursor.execute(queryTwo)
		rows = []
		for i in tableTwo:
			rows.append(i)
		return rows
	except Exception:
		return []

def findFiveMostFrequentForUser(connection, cursor, user_id):
	"""Returns the rows of the product table which have the five most frequently bought products by the specified user.

	:param connection: The sqlite3 connection to the database.
	:type connection: sqlite3.Connection
	:param cursor: The sqlite3 cursor to execute queries.
	:type cursor: sqlite3.Cursor
	:param user_id: The user for whom the data is to be found.
	:type user_id: string
	:returns: A list of Row objects representing the required rows of the table.
	:rtype: list
	"""
	try:
		counts = {}
		queryOne = "SELECT product_id, quantity FROM user_purchases WHERE user_id = " + str(user_id)
		tableOne = cursor.execute(queryOne)
		dataOne = tableOne.fetchall()
		for rowNumber in range(0, len(dataOne)):
			product_id = dataOne[rowNumber]['product_id']
			quantity = dataOne[rowNumber]['quantity']
			if product_id not in counts:
				counts[product_id] = quantity
			else:
				counts[product_id] += quantity
		pids = nlargest(5, counts, key=counts.get)
		pidsListString = '('
		for pid in pids:
			pidsListString += str(pid) + ', '
		pidsListString = pidsListString[0:-2] + ')'
		queryTwo = "SELECT * FROM products WHERE product_id in " + pidsListString
		tableTwo = cursor.execute(queryTwo)
		rows = []
		for i in tableTwo:
			rows.append(i)
		return rows
	except Exception:
		return []

def findDiscountsOnOrOff(connection, cursor, user_id):
	"""Returns a true or false value based on whether any of the most frequently bought products by the specified user are on discount.

	:param connection: The sqlite3 connection to the database.
	:type connection: sqlite3.Connection
	:param cursor: The sqlite3 cursor to execute queries.
	:type cursor: sqlite3.Cursor
	:param user_id: The user for whom the discounts are to be found.
	:type user_id: string
	:returns: True if any of the products are on discount, false otherwise.
	:rtype: boolean
	"""

	try:
		rows = findFiveMostFrequentForUser(connection, cursor, user_id)
		for row in rows:
			if (len(str(row['discount_id'])) != 0):
				return True
		return False
	except Exception:
		return False

if __name__ == '__main__':
	connection = sqlite3.connect('dbms_db.db')
	connection.row_factory = sqlite3.Row
	cursor = connection.cursor()
	print(findDiscountsOnOrOff(connection, cursor, '1'))
