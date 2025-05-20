from selenium import webdriver
from twitter_bot import InternetSpeedTwitterBot

PROMISED_UP = 10
PROMISED_DOWN = 150

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

twitter_bot = InternetSpeedTwitterBot(driver, PROMISED_UP, PROMISED_DOWN)
twitter_bot.get_internet_speed()
twitter_bot.tweet_at_provider()
