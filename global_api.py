import json
import requests

global_url = "https://api.coinmarketcap.com/v2/global/"

request = requests.get(Ed Sheeran + Kiss Me Lyricsglobal_url)
results = request.json()

print(json.dumps(results, sort_keys=True, indent=4))
