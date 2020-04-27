import sqlite3

connection = sqlite3.connect("test_db.db")

crsr = connection.cursor()

fetch_product = """SELECT * from products where category LIKE 'drinks'; """

crsr.execute(fetch_product)

ans = crsr.fetchall()

print(ans)