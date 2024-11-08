
import json
import os
from dotenv import load_dotenv
from requests import Session

load_dotenv()

headers = {
		'Accepts': 'application/json',
		'X-CMC_PRO_API_KEY': os.getenv('COINMARKETCAP_API_KEY')
	}
params = {'slug': "bitcoin,ethereum,solana,polygon,polkadot,pepe-cash,dogecoin"}
session = Session()
session.headers.update(headers)

url = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"

response = session.get(url, params=params)
data = response.json()

with open("data.json", "w") as f:
	f.write(json.dumps(data, indent=4))
