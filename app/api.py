from flask import Flask, request, jsonify, render_template
import requests
import urllib.request
from urllib.request import urlopen
import json
import os
import sys

#api documentations: https://openweathermap.org/current
#returns json file with many weather data, but need to parse for weather["main"], main["temp"], main["feels_like"], main["temp_min"], main["temp_max"],
def weatherData(lat, lon):
    with open("api_keys/weatherkey.txt", "r") as file:
        api_key = file.read().strip()
    if not api_key:
        print("api key not valid")
        sys.exit(1)
    weather_data = requests.get(f'''https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=imperial&appid={api_key}''')
    #print(f'''https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}''')
    if weather_data.ok: #sucsess code
        return weather_data.json()
    else:
        weather_data.raise_for_status()

#returns lat and lon of first city with matching name as parameter, place (limit set to 1 city to avoid multiple responses)
#return json containing city name with country and state
def coordinates(place):
    with open("api_keys/weatherkey.txt", "r") as file:
        api_key = file.read().strip()
    if not api_key:
        print("api key not valid")
        sys.exit(1)
    city_data = requests.get(f'''http://api.openweathermap.org/geo/1.0/direct?q={place}&limit=1&appid={api_key}''')
    if city_data.ok:
        return city_data.json()
    else:
        city_data.raise_for_status()

#query results will be saved as json to prevent unecessary api calls for the same query
#used to obtain pictures from depop and link to item
def get_images(query):
    name = query.replace(" ", "_")
    filename = f"{name}.json"
    if not os.path.exists(filename):
        with open("api_keys/searchKey.txt", "r") as file:
            api_key = file.read().strip()
        if not api_key:
            print("api key not valid")
            sys.exit(1)
        images_data = requests.get(f'''https://serpapi.com/search.json?engine=google_images&q={query}&google_domain=google.com&gl=us&hl=en&api_key={api_key}''')
        if images_data.ok:
            with open(filename, "w") as f:
                json.dump(images_data.json(), f, indent=2)
            print(f"Saved to {filename}")
    else:
        print(f"{filename} already exists. Did not overwrite.")

