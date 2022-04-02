import requests
import json

country = input("Please type the country or city you want to know how is the weather like: ")
api = "http://api.weatherapi.com/v1/current.json?key=4193824395d440f1ab7153808220204&q=" + country + "&aqi=no"

asd = requests.get(api)
location = asd.json()["location"]
current = asd.json()["current"]
if current["is_day"] == 1:
    x = "day"
else:
    x = "evening"


print(f"{location['region']}, {location['country']}\nNow in {location['name']}, it is {current['temp_c']} degrees and {current['temp_f']} Fahrenheit. Weather is {current['condition']['text']} and it's a lovely {x} in {location['region']}.")