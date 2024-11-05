import json
from requests import Session, Timeout, TooManyRedirects
import mysql.connector 
import os
from dotenv import load_dotenv
import pandas as pd
from init import connect_mysql, fetch_data_from_api

load_dotenv()

def insert_into_mysql(data):
    conn = connect_mysql()
    if conn is None: 
        print("Connection to MySQL failed")
        return
    
    try:
        cursor = conn.cursor()
        insert_query = (
            "INSERT INTO Cryptocurrency_Info (id, crypto_name, crypto_slug, crypto_symbol, crypto_logo_url)"
            "VALUES (%s, %s, %s, %s, %s)"
        )
		
        if "data" not in data:
            print("Key 'data' not found in the response")
            return
            
        for record in data["data"].values():
            crypto_id = record["id"]
            crypto_name = record["name"]
            crypto_slug = record["slug"]
            crypto_symbol = record["symbol"]
            crypto_logo_url = record["logo"]
		
            cursor.execute(insert_query, (crypto_id, crypto_name, crypto_slug, crypto_symbol, crypto_logo_url))
			
        conn.commit()
        print("Inserted successfully")
    except mysql.connector.Error as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        conn.close()

url = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/info"
data = fetch_data_from_api(url)
insert_into_mysql(data)
