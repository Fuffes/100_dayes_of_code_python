import os

import requests
import datetime

from dotenv import load_dotenv

from stock_data import stock
from itertools import islice


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
BASE_STOCK_API_URL = "https://www.alphavantage.co/query"
BASE_NEWS_API_URL = "https://newsapi.org/v2/top-headlines"

load_dotenv()
stock_api_key = os.getenv("STOCK_API_KEY")
news_api_key = os.getenv("NEWS_API_KEY")


def calc_price_change() -> float:
    """Return the price change in %"""
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol" : STOCK,
        "apikey" : stock_api_key,
        "outputsize":"compact",
    }
    resp = requests.get(url=BASE_STOCK_API_URL, params=params)
    resp.raise_for_status()
    data = resp.json()
    full_daily_data = data['Time Series (Daily)']
    open_values = [v["4. close"] for v in islice(full_daily_data.values(), 2)]
    new_value = float(open_values[0])
    old_value = float(open_values[1])
    change = ((old_value-new_value)/old_value)*100
    return round(change, 2)


def get_news() -> list:
    """return: list of the articles"""
    params = {
        "q": "tesla",
        "sortBy": "publishedAt",
        "apiKey": news_api_key
    }
    resp = requests.get(url=BASE_NEWS_API_URL, params=params)
    resp.raise_for_status()
    articles = resp.json()["articles"]
    return articles


price_change = calc_price_change()
if abs(price_change)>5:
    news = get_news()
    for article in news:
        message =f"{STOCK}: {price_change}% \nHeadline: {article["title"]}\nBrief: {article["description"]}"
        print(message)




