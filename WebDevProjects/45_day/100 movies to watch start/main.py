import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


resp = requests.get(url=URL).text

soup = BeautifulSoup(resp, 'html.parser')
titles_tags = soup.select("h3.title")
titles = [tag.text for tag in titles_tags[::-1]]

with open("movies.txt", "a", encoding='utf-8') as file:
    file.writelines(f"{title}\n" for title in titles)

