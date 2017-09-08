# Short script to set up the create and populate a Mysql database with examples. Enter your username
# and password below at the 'database' variable declaration.

import mysql.connector, json

try:
	database = mysql.connector.connect(user='ENTER USERNAME', password='ENTER PASSWORD',
	database='SKU')
	if not database:
		connection = mysql.connector.connect(user='ENTER USERNAME', password='ENTER PASSWORD')
		cursorA = connection.cursor()
		cursorA.execute('CREATE DATABASE SKU;')
except:
	print('Database connection failed.')

def create_data():	
	cursorA = database.cursor()
	cursorB = database.cursor()
	
	# Create a simple table to store comments by SKU
	TABLES = (
	    """CREATE TABLE SKU (
	      sku varchar(20) NOT NULL,
	      comment varchar(50) NOT NULL
	    );""")
	
	cursorA.execute(TABLES)
	
	#Load data into table
	DATA = (
		"""INSERT INTO SKU(sku, comment)
		VALUES ('S12T-Com-RS', 'I am angry'),('S12T-Com-RT','I am sad');"""
		)
	
	cursorB.execute(DATA)
	
	database.commit()
	database.close()

create_data()