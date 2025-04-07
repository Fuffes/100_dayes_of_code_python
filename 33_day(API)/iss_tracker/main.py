

import requests
import datetime

LAT = 52.231791
LONG = 21.006274

def is_visible():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    resp = response.json()
    iss_longitude = float(resp["iss_position"]["longitude"])
    iss_latitude = float(resp["iss_position"]["latitude"])
    if LAT-5 <= iss_latitude <= LAT+5 and LONG-5 <= iss_longitude <= LONG+5:
        return True

def is_night():
    params= {
        "lat": LAT ,
        "lng": LONG,
        "formatted": 0,
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=params)
    response.raise_for_status()
    data = response.json()
    print(data)
    sunrise = datetime.datetime.fromisoformat(data["results"]["sunrise"])
    sunset = datetime.datetime.fromisoformat(data["results"]["sunset"])

    current_time = datetime.datetime.now(datetime.timezone.utc)
    print(sunset)
    print(sunrise)
    print(current_time)
    print( not(sunrise<=current_time<=sunset))

if is_night() and is_visible():
    print("Look UP")