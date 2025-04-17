import datetime
import os

import requests
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
TOKEN = os.getenv("TOKEN")

BASE_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
EXCEL_BASE_URL = "https://api.sheety.co/62c23b198adc2a1f97dbcea6c58660a4/myWorkouts/workouts"

query = input("Tell me which exercises you did: ")
headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY,
}

body = {"query": query}
resp = requests.post(url=BASE_URL, json=body, headers=headers).json()
print(resp)

for item in resp["exercises"]:
    print(item["user_input"])
    today = datetime.datetime.now()
    day = today.strftime('%d.%m.%Y')
    time = today.strftime("%H:%M")

    row = {
        "workout" : {
            "date": day,
            "time": time,
            "exercise": item["user_input"],
            "duration": item["duration_min"],
            "calories": item["nf_calories"],
        }
    }
    print(row)
    header = {"Authorization": f"Basic {TOKEN}"}
    sheet_response = requests.post(url=EXCEL_BASE_URL, json=row, headers=header)
    print(sheet_response.text)