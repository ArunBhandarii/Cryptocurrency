import json
import requests
from datetime import datetime

global_url = " https://api.coinmarketcap.com/v2/global/"

request = requests.get(global_url)
results = request.json()

# print(json.dumps(results, sort_keys=True, indent=4))

active_currencies = results['data']['active_cryptocurrencies']

# print(active_cryptocurrencies)

active_markets = results['data']['active_markets']
bitcoin_percentage = results['data']['bitcoin_percentage_of_market_cap']
last_updated = results['data']['last_updated']
global_cap = str(results['data']['quotes']['USD']['total_market_cap'])
global_volume = str(results['data']['quotes']['USD']['total_volume_24h'])

active_currencies_string = '{:,}'.format(active_currencies)
active_markets_string = '{:,}'.format(active_markets)
global_cap_string = '{:,}'.format(global_cap)
global_volume_string = '{:,}'.format(global_volume)

last_updated_string = datetime.frontimestamp(last_updated).strftime('%B %d, %Y at %I:%M%p')

print()
print('There are ' + active_currencies_string + 'active curencies and' + active_markets_string + 'active markets.')
print('The global cap' + global_cap_string + 'and global volume is' + global_volume_string + '.')
print('Bitcoin\'s total global cap is' + str(bitcoin_percentage) + '.')
print()
print('The information was last updated on' + last_updated_string + '.') 
