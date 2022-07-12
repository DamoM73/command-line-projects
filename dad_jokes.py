import requests
import json

response = requests.get("https://api.chucknorris.io/jokes/random")

if response.status_code == 200:
    data = response.text
    parse_data = json.loads(data)
    print(parse_data["value"])
else:
    print("Error loading API")