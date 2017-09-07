# test_bucketlist.py
import unittest, os, json, mysql.connector, os, warnings
from save import insert_data
from main import app

class SKUTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
 #       database = mysql.connector.connect(user='root', password='millieiscute2')
 #       TABLES = (
 #       """CREATE TABLE SKU (
 #         sku varchar(20) NOT NULL,
 #         comment varchar(50) NOT NULL
 #       );""")
 #       DATA = (
 #       """INSERT INTO SKU(sku, comment)
 #       VALUES ('ER3C-Tye-DZ', 'I am sad'),('S98H-Pol-VC','I am happy');"""
 #       )
 #       cursorA = database.cursor()
 #       cursorA.execute('CREATE DATABASE TEST;', TABLES, DATA)
     
        self.app = app
        self.client = app.test_client()
        self.client.testing = True

    def test_sku_retrieval(self):
        response = self.client.get('/SKU-Retriever/api/v1.0/retrieve')
        self.assertEqual(response.status_code, 200)

#    def tearDown(self):
#        os.remove("test.db")
              
if __name__ == "__main__":
    unittest.main()