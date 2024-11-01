import json
import time
from requests import Session, Timeout, TooManyRedirects
import mysql.connector 
import os
from dotenv import load_dotenv
import schedule
from src.setup import connect_mysql, fetch_data_from_api

load_dotenv()

def insert_into_mysql(data):
	if data is None: 
		print("No data to insert into MySQL")
		return 
		
	conn = connect_mysql()
	if conn is None: 
		print("Connection to MySQL failed")
		return 
	
	try: 
		cursor = conn.cursor()
	
		insert_query_metrics = (
			"INSERT INTO Cryptocurrency_Metrics (crypto_id, cmc_rank, num_market_pairs, circulating_supply, last_updated)"
			"VALUES (%s, %s, %s, %s, %s)"
		)
		
		insert_query_quote = (
			"""
			INSERT INTO Cryptocurrency_USD_Quote 
				(crypto_id, 
				usd_current_price, 
				usd_volume_24h, 
				usd_volume_percent_change_24h, 
				usd_price_percent_change_1h, 
				usd_price_percent_change_24h, 
				usd_price_percent_change_7d, 
				usd_price_percent_change_30d, 
				usd_market_cap, 
				usd_market_cap_dominanc)
			VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
			"""
		)
		if "data" not in data: 
			print("Key 'data' not found in the response")
			return 
		
		for record in data["data"].values():
			crypto_id = record["id"]
			cmc_rank = record["cmc_rank"]
			num_market_pairs = record["num_market_pairs"]
			circulating_supply = record["circulating_supply"]
			last_updated = record["last_updated"]
			
			usd_current_price = record["quote"]["USD"]["price"]
			usd_volume_24h = record["quote"]["USD"]["volume_24h"]
			usd_volume_percent_change_24h = record["quote"]["USD"]["volume_change_24h"]
			usd_price_percent_change_1h = record["quote"]["USD"]["percent_change_1h"]
			usd_price_percent_change_24h = record["quote"]["USD"]["percent_change_24h"]
			usd_price_percent_change_7d = record["quote"]["USD"]["percent_change_7d"]
			usd_price_percent_change_30d = record["quote"]["USD"]["percent_change_30d"]
			usd_market_cap = record["quote"]["USD"]["market_cap"]
			usd_market_cap_dominance = record["quote"]["USD"]["market_cap_dominance"]
			
			cursor.execute(insert_query_metrics, (crypto_id, cmc_rank, num_market_pairs, circulating_supply, last_updated))
			cursor.execute(
				insert_query_quote, 
				(crypto_id, usd_current_price, usd_volume_24h, usd_volume_percent_change_24h, usd_price_percent_change_1h, usd_price_percent_change_24h, usd_price_percent_change_7d, usd_price_percent_change_30d, usd_market_cap, usd_market_cap_dominance
			))
			
		conn.commit()
		print("Inserted successfully")
		
	except mysql.connector.Error as e: 
		print(f"An error occurred: {e}")
	finally: 
		cursor.close()
		conn.close()


def main():
	# Schedule this script to run every 10 minutes
	url = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"
	schedule.every(15).minutes.do(insert_into_mysql(fetch_data_from_api(url)))
	
	while True: 
		schedule.run_pending()
		time.sleep(1)
		
if __name__ == "__main__":
	main()
	
	
	
