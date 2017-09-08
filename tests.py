import unittest
from save import insert_data
from main import app

"""NOTE: Runnging the test will generate a resource warning in addition to the test results. This is a problem with
Python3 and therefore can't be directly resolved yet"""    

class SKUTestCase(unittest.TestCase):

    def setUp(self): 
        self.app = app
        self.client = app.test_client()
        self.client.testing = True

    def test_sku_retrieval(self):
        response = self.client.get('/SKU-Retriever/api/v0.1/retrieve')
        self.assertEqual(response.status_code, 200)
              
if __name__ == "__main__":
    unittest.main()