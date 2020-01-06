import json
import requests

global_url = "https://api.coinmarketcap.com/v2/global/"

request = requests.get(global_url)
results = request.json()

# print(json.dumps(results, sort_keys=True, indent=4))

active_currencies = results ['data']['active_cryptocurrencies']

# print(active_cryptocurrencies)

active_markets = results['data']['active_markets']
bitcoin_percentage = results['data']['bitcoin_percentage_of_market_cap']
last_updated = results['data']['last_updated']
global_cap = results['data']['quotes']['USD']['total_market_cap']
global_volume = results['data']['quotes']['USD']['total_volume_24h']
print()
print('There are ' + str(active_currencies) + 'active curencies and' + str(active_markets) + 'active markets.')
print('The global cap' + str(global_cap) + 'and global volume is' + str(global_volume) + '.')
print('Bitcoin\'s total global cap is' + str(bitcoin_percentage) + '.')
print()
print('The information was last updated on' + last_updated + '.')
