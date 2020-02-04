import mysql.connector
from mysql.connector import Error
conn = mysql.connector.connect(host='localhost',
                                        database='project',
                                        user='root',
                                        password='Vishesh03',
                                        auth_plugin='mysql_native_password')

cursor = conn.cursor()
cursor.execute("drop table if exists loyalty")
loyalty_table = '''create table loyalty (
    card_id INT primary key,
    user_id INT references,
    category varchar(40)
);'''


#cursor.execute(product_table)
cursor.execute(loyalty_table)

loyalty_data = '''insert into loyalty(card_id,user_id,category)
values (1,1,'PLATINUM'),(2,2,'GOLD'),(3,3,'DIAMOND'),(4,4,'SILVER'),(5,5'SILVER'),(6,6,'GOLD'),(7,7,'SILVER'),(8,8,'GOLD'),(9,9,'PLATINUM'),(10,10,'SILVER'),(11,11,'GOLD'),(12,12,'SILVER'),(13,13,'SILVER'),(14,14,'PLATINUM'),(15,15,'GOLD');'''

cursor.execute(loyalty_data)


cursor.execute("drop table if exists transactions")
transactions_table = '''
    create table transactions(transcation_id int primary key, receipt_id int, user_id int, product_id int, total_cost int , employee_id int, satisfaction numeric(3,2));
'''
cursor.execute(transactions_table)
transactions_data = '''
insert into transactions(transcation_id, receipt_id, user_id, product_id, total_cost, employee_id, satisfaction)
values (1,1,1,15,100,1,4.25),(2,2,3,15,100,1,2.50),(3,3,1,10,1000,3,3.75),(4,4,1,1,12,1,3.12),(5,5,3,2,35,3,4.85),(6,6,3,6,100,4,4.25),(7,7,9,18,20,2,3.55),
(8,8,9,20,30,3,3.85),(9,9,14,6,100,2,4.35),(10,10,9,8,30,4,4.25), (11,11,9,2,35,4,4.50), (12,12,14,17,200,2,4.65), (13,13,6,19,750,1,4.30), (14,14,4,17,200,1,4.23), (15,15,2,6,100,2,3.45);
'''
cursor.execute(transactions_data)
conn.commit()
conn.close()
