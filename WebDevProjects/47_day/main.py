
import requests
from bs4 import BeautifulSoup

URL = "https://appbrewery.github.io/instant_pot/"
target_price = 100


def send_allert():
    print("Price lower than target")


context = requests.get(url=URL).text
soup = BeautifulSoup(context, "html.parser")

full_price = soup.select_one("span.aok-offscreen").text
price = float(full_price.split("$")[1])

if target_price >= price:
    send_allert()



