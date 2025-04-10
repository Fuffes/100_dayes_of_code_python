import os

import requests
from twilio_sender import send_alert

api_key = os.getenv("API_KEY")

LAT = "52.23"
LON = "21.00"
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"
params = {
    "lat": LAT,
    "lon": LON,
    "appid" : api_key,
    "cnt": 4,
}

resp = requests.get(url=BASE_URL, params=params)
resp.raise_for_status()
full_data = resp.json()

weather_codes = [item["weather"][0]["id"] for item in full_data["list"]]


is_rain = False
for item in weather_codes:
    if item < 700:
        is_rain = True

if is_rain:
    send_alert("It's going to rain today")