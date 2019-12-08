import json
import requests

global_url = "https://api.coinmarketcap.com/v2/global/"

request = requests. get(global_url)
results = request.json()

# print(json.dumps(results, sort_keys=True, indent=4))

active_currencies = requests['data']['active_cryptocurrencies']

print(active_currencies)
