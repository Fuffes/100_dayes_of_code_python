import requests

responce = requests.get(url="http://api.open-notify.org/iss-now.json")
responce.raise_for_status()
resp = responce.json()
position = (resp["iss_position"]["longitude"], resp["iss_position"]["latitude"])
print(position)
