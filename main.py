#!/usr/bin/env python
import json, logging, time, mysql.connector

from flask import Flask, jsonify, make_response
from watson_developer_cloud import ToneAnalyzerV3
from save import insert_data

"""In order to start the server, please run the db.py script to set up the SKU database in Mysql, and you need to 
place your username and password in that script and in save.py as well. This way of connecting will have to refactored for 
production use, but will work for development. Please also insert your blue mix credentials at lines 22-23 below.

Below we configure the logging file. The program logs exceptions to an, external file, which
will be useful when scaled. Logging.ERROR indicates the program has not been able to carry out its function."""

app = Flask(__name__)

logging.basicConfig(filename='log.txt', level=logging.ERROR)

#Set up tone analyzer credentials.
try :
	tone_analyzer = ToneAnalyzerV3(
	username='USERNAME',
	password='PASSWORD',
	version='2016-09-20')
except:
	print('Tone analyzer credentials failed.')
	logging.exception(time.strftime("%c")+ ". " + 'Tone analyzer credentials failed. Traceback:')

# Example of a comment, that will be used to show the service works when a client accesses the API.
payload = {
		'name': 'F12T-MMM-RS',
		'comment': 'I am feeling down',
	}

@app.route('/SKU-Retriever/api/v0.1/retrieve', methods=['GET'])
def update_sku():
	try:
		print("SKU number is:" + " " + payload['name'])
		response = tone_analyzer.tone(text=payload['comment'])
		insert_data(payload)
		print("Comment analyzed and saved sucessfully!")
	except KeyError as e:
			print ('No SKU found. Error code:', e)
			#log the error
			logging.exception(time.strftime("%c")+ ". " + 'No SKU found. Traceback:')
			return
	return jsonify(response)

#implement error handler for displaying an error message in a 404 response.
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
	print("Server has started!")
	app.run(debug=True)