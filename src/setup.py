import json 
import os 
from dotenv import load_dotenv
from requests import Session, Timeout, TooManyRedirects, RequestException 
import mysql.connector 

def connect_mysql():
	try: 
		conn = mysql.connector.connect(
			host=os.getenv('MYSQL_HOST'),
			user=os.getenv('MYSQL_USER'),
			password=os.getenv('MYSQL_PASSWORD'),
			database=os.getenv('MYSQL_DATABASE')
		)
		
		if conn.is_connected():
			print("Connected to MySQL successfully")
			return conn
	except mysql.connector.Error as e: 
		print(e)
		return None
	
def fetch_data_from_api(api_url):
	headers = {
		'Accepts': 'application/json',
		'X-CMC_PRO_API_KEY': os.getenv('COINMARKETCAP_API_KEY')
	}
	params = {'slug': "bitcoin,ethereum,solana,polygon,polkadot,pepe-cash,dogecoin"}
	session = Session()
	session.headers.update(headers)
	
	try:
		response = session.get(api_url, params=params)
		data = json.loads(response.text)
		# Check for errors in the API response
		if "status" in data and data["status"]["error_code"] != 0:
			print(f"Error {data['status']['error_code']}: {data['status']['error_message']}")
			return None
		return data
		
	except (RequestException, Timeout, TooManyRedirects) as e: 
		print(f"An error occurred: {e}")
		return None