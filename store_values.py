import json
import requests

global_url = "https://api.coinmarketcap.com/v2/global/"

request = requests.get(global_url)
results = request.json()

# print(json.dumps(results, sort_keys=True, indent=4))

active_currencies = results['data']['active_cryptocurrencies']

# print(active_cryptocurrencies)

active_markets = results['data']['active_markets']
bitcoin_percentage = results['data']['bitcoin_percentage_of_market_cap']
last_updated = results['data']['last_updated']
global_cap = 
global_volume =
