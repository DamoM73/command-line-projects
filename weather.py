import requests
import json

city = input("Enter city name: ")

response = requests.get(f"https://goweather.herokuapp.com/weather/{{city}}")

if response.status_code == 200:
    data = response.text
    parse_data = json.loads(data)
    print(f"\nToday's weather for {city}")
    print(parse_data["description"])
    print(parse_data["temperature"])
else:
    print("Error loading API")