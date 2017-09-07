#!/usr/bin/env python
import json, logging, time
#mysql.connector

from flask import Flask
from watson_developer_cloud import ToneAnalyzerV3
#from save import insert_data

"""Configure logging file. The program logs exceptions to an, external file, which
will be useful when scaled. Logging.ERROR indicates the program has not been able to carry out its function."""

app = Flask(__name__)

logging.basicConfig(filename='log.txt', level=logging.ERROR)

#Set password and options first
try :
	tone_analyzer = ToneAnalyzerV3(
	username='5b55cac9-1576-4669-ac69-c1d8358c0015',
	password='ec0wKSjOyZb1',
	version='2016-09-20')
except:
	print('Tone analyzer credentials failed.')
	logging.exception(time.strftime("%c")+ ". " + 'Tone analyzer credentials failed. Traceback:')

"""Set up database connections. Program uses a mysql database to store comments, choosen for its reliability.
Please run the db.py script to set up this database in Mysql, and replace the parameters below with your username
and password. This way of connecting will have to refactored for production use, but will work for development.
{
  "url": "https://gateway.watsonplatform.net/tone-analyzer/api",
  "username": "5b55cac9-1576-4669-ac69-c1d8358c0015",
  "password": "ec0wKSjOyZb1"
}"""

#try:
#	database = mysql.connector.connect(user='ENTER YOUR USERNAME HERE', password='ENTER YOUR PASSWORD HERE',
#	database='SKU')
#except:
#	print('Database connection failed.')
#	logging.exception(time.strftime("%c")+ ". " + 'Database connection failed. Traceback:')

payload = {
		'name': 'S12T-MMM-RS',
		'comment': 'I wish I was happy...really!',
	}

#Put all the above in a separate file? And don't forget to not include or clean up the log files first.

@app.route('/SKU-Retriever/api/v1.0/retrieve', methods=['GET'])
def update_sku():
	try:
		print("SKU number is:" + " " + payload['name'])
		response = tone_analyzer.tone(text=payload['comment'])
		#insert_data(payload)
		print("Comment analyzed and saved sucessfully!")
	except KeyError as e: #expand on this bit and error handling, tests for all modules and so on tomorrow.
			print ('No SKU found. Error code:', e)
			#log the error
			logging.exception(time.strftime("%c")+ ". " + 'No SKU found. Traceback:')
			return
	return jsonify(response)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
	print("Server has started!")
	app.run(debug=True)