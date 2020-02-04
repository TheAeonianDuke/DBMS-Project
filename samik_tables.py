import mysql.connector
from mysql.connector import Error
conn = mysql.connector.connect(host='localhost',
                                        database='project',
                                        user='root',
                                        password='samik1234',
                                        auth_plugin='mysql_native_password')

cursor = conn.cursor()
cursor.execute("drop table if exists products")
product_table = '''create table products (
    product_id INT primary key,
    name  varchar(255),
    supplier_name varchar(100),
    buying_cost INT,
    selling_cost INT NOT NULL,
    offers Varchar(100),
    category varchar(100)
    
);'''
cursor.execute(product_table)

add_data = '''insert into products(product_id,name,supplier_name,buying_cost,selling_cost,offers,category)
values (1,'maggi','nestle',10,12,'','food') , (2,'coke','coca-cola',30,35,'','drinks'),
(3,'cadbury silk','cadbury',50,70,'20 percent off','food'), (4,'clinic+ shampoo','clinic+',40,50,'buy 3 get 1 free','beauty and wellness'),
(5,'axe deodrant','axe',30,60,'','beauty and wellness'), (6,'redbull','redbull',70,100,'','drinks'),(7,'motherdairy mango icecream','motherdairy',10,20,'','food'),
(8,'brittania hideandseek','brittania',20,30,'','food'),(9,'surfexcel','surfexcel',300,350,'20 percent off','cleaning and household'),(10,'borges olive oil','borges',800,1000,'','food'),
(11,'pears soap','pears',100,150,'20 percent off','hygiene'),(12,'nescafe coffee','nescafe',100,150,'','drinks'),(13,'pampers diapers','pampers',600,750,'','babycare'),
(14,'vaseline petroleum jelly','vaseline',100,200,'','beauty and wellness'),(15,'colgate active salt toothpaste','colgate',50,100,'20 percent off','hygiene'),(16,'pepsodent toothpaste','pepsodent',50,80,'','hygiene'),
(17,'pantiene anti hairfall conditioner','pantiene',100,200,'buy 3 get 1 free','beauty and wellness'),(18,'harpic toilet cleaner','harpic',100,150,'','cleaning and household'),
(19,'kellogs cornflakes','kellogs',150,200,'','food'),(20,'cadbury oreo','cadbury',20,30,'','food');'''

cursor.execute(add_data)
# cursor.execute("drop table if exists suppliers")
# supplier_table = '''create table suppliers (
#     supp_id INT primary key,
#     name VARCHAR(100),
#     product_id INT  ,
#     location varchar(100),
#     category VARCHAR(100),
#     FOREIGN KEY (product_id) REFERENCES products (product_id)
#  );  
# '''

# add_data_supp = ''' insert into 
# ('nestle', 1, 'food')
# ('coca-cola', 2, 'drinks')
# ('cadbury', 3, 'food')
# ('clinic+', 4, 'beauty and wellness')
# ('axe', 5, 'beauty and wellness')
# ('redbull', 6, 'drinks')
# ('motherdairy', 7, 'food')
# ('brittania', 8, 'food')
# ('surfexcel', 9, 'cleaning and household')
# ('borges', 10, 'food')
# ('pears', 11, 'hygiene')
# ('nescafe', 12, 'drinks')
# ('pampers', 13, 'babycare')
# ('vaseline', 14, 'beauty and wellness')
# ('colgate', 15, 'hygiene')
# ('pepsodent', 16, 'hygiene')
# ('pantiene', 17, 'beauty and wellness')
# ('harpic', 18, 'cleaning and household')
# ('kellogs', 19, 'food')
# ('cadbury', 20, 'food')
# '''
# cursor.execute(supplier_table)
cursor.execute("drop table if exists discounts")
discount_table = '''
    create table discounts(discount_id int primary key, discount_type varchar(100));
'''
cursor.execute(discount_table)
discount_data = '''
insert into discounts(discount_id,discount_type)
values (1,'buy 3 get 1 free'),(2,'buy 1 get 1 free'),(3,'20 percent off'),(4,'15 percent off'),(5,'20 percent extra'),(6,'buy 2 get 1 free'),(7,'10 rupees cashback'),
(8,'50 percent off'),(9,'5 rupees cashback'),(10,'40 percent off');
'''
cursor.execute(discount_data)
conn.commit()
conn.close()
