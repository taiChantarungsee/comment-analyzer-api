import json, logging, time, mysql.connector

from urllib.request import Request, urlopen, URLError
from watson_developer_cloud import ToneAnalyzerV3
from save import insert_data

"""Configure logging file. The program logs exceptions to an, external file, which
will be useful when scaled. Logging.ERROR indicates the program has not been able to carry out its function."""
logging.basicConfig(filename='log.txt', level=logging.ERROR)

#Set password and options first
try :
	tone_analyzer = ToneAnalyzerV3(
	username='a724ff30-3000-49c2-8b93-af026b10e7c5',
	password='GIAJflppODTp',
	version='2016-05-19')
except:
	print('Tone analyzer credentials failed.')
	logging.exception(time.strftime("%c")+ ". " + 'Tone analyzer credentials failed. Traceback:')

"""Set up database connections. Program uses a mysql database to store comments, choosen for its reliability.
Please run the db.py script to set up this database in Mysql, and replace the parameters below with your username
and password. This way of connecting will have to refactored for production use, but will work for development."""
try:
	database = mysql.connector.connect(user='ENTER YOUR USERNAME HERE', password='ENTER YOUR PASSWORD HERE',
	database='SKU')
except:
	print('Database connection failed.')
	logging.exception(time.strftime("%c")+ ". " + 'Database connection failed. Traceback:')

payload = {
		'name': 'S12T-MMM-RS',
		'comment': 'I wish I was happy...really!',
	}

def main(payload):
	try:
		print("SKU number is:" + " " + payload['name'])
		print(json.dumps(tone_analyzer.tone(text=payload['comment']), indent=2))
		response = json.dumps(tone_analyzer.tone(text=payload['comment']))
		insert_data(payload)
		print("Comment analyzed and saved sucessfully!")
	except KeyError as e: #expand on this bit and error handling, tests for all modules and so on tomorrow.
			print ('No SKU found. Error code:', e)
			#log the error
			logging.exception(time.strftime("%c")+ ". " + 'No SKU found. Traceback:')

if __name__ == '__main__':
	main(payload)