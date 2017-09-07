import mysql.connector, json

#functions for saving database data

def insert_data(json):	
	database = mysql.connector.connect(user='root', password='millieiscute2',
	database='SKU')
	cursor = database.cursor()

	data = json
	insert = (
		"""INSERT INTO SKU(sku,comment) VALUES (%s,%s)"""
		)
	for name , comment in data.items():
		cursor.execute(insert, (name,comment))
	database.commit()
	database.close()

	print('finished saving!')

if __name__ == '__main__':
	insert_data(payload)