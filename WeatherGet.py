import requests
import json
import csv

city = input("Please enter a city: ").lower()

with open("WeatherGet\worldcities.csv", newline='', encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['city'].lower() == city:
            lon = row['lng']
            lat = row['lat']


def jsonString(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

responseWeather = requests.get(f"https://www.7timer.info/bin/api.pl?lon={lon}&lat={lat}&product=civillight&output=json")

if responseWeather.status_code == 200:
    jsonString(responseWeather.json())