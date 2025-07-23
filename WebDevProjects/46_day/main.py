import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.billboard.com/charts/hot-100"

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")



resp = requests.get(url=f"{BASE_URL}/{date}/", headers=header)
page = resp.text

soup = BeautifulSoup(page, "html.parser")
title_tags = soup.select("li h3#title-of-a-story")

titles = [title.getText(strip=True) for title in title_tags]
print(titles)
