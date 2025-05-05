from bs4 import BeautifulSoup
import requests

URL = "https://news.ycombinator.com/"

resp = requests.get(url=URL)
web_page = resp.text

soup = BeautifulSoup(web_page, 'html.parser')

tags = soup.select(".titleline > a")
scores_tags = soup.select(".subline .score")
titles = [tag.text for tag in tags]
links = [tag.get('href') for tag in tags]
scores = [int(score.text.split()[0]) for score in scores_tags]
print(titles)
print(links)
print(scores)

