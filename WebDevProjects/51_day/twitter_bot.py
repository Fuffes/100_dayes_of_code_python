import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SPEEED_TEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://x.com/i/flow/login"

load_dotenv()
ADDRESS = os.getenv("ADDRESS")
PASSWORD = os.getenv("PASSWORD")
USERNAME_TWITTER = os.getenv("USERNAME_TWITTER")


class InternetSpeedTwitterBot:
    def __init__(self, driver: webdriver, down: float, up: float):
        self.driver = driver
        self.up = float(up)
        self.down = float(down)
        self.wait = WebDriverWait(self.driver, 40)
        self.speed_test_result = ()

    def get_internet_speed(self) -> None:
        self.driver.get(SPEEED_TEST_URL)
        go_btn = self.driver.find_element(By.CSS_SELECTOR, value=".start-text").click()
        result_label = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.result-data[data-result-id='true'] a")))
        result = result_label.get_attribute("href")
        upload_speed = self.driver.find_element(By.CSS_SELECTOR, value=".upload-speed").text
        download_speed = self.driver.find_element(By.CSS_SELECTOR, value=".download-speed").text
        self.speed_test_result = (float(download_speed), float(upload_speed), result)

    def tweet_at_provider(self):
        if self.speed_test_result[0]<self.down or self.speed_test_result[1]<self.up:
            self.driver.get(TWITTER_URL)

            # Enter address
            address = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[autocomplete='username']")))
            address.send_keys(ADDRESS)
            next_btn = self.driver.find_element(By.CSS_SELECTOR, value="div > button:nth-child(6) > div").click()

            # Enter username
            username = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name = "text"]')))
            username.send_keys(USERNAME_TWITTER)
            next = self.driver.find_element(By.CSS_SELECTOR, value="div.css-175oi2r.r-1f0wa7y > div > div > div > button > div").click()

            # Enter password
            password = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="password"]')))
            password.send_keys(PASSWORD)
            login_btn = self.driver.find_element(By.CSS_SELECTOR, value="div.css-175oi2r.r-1ny4l3l.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv.r-1awozwy > div.css-175oi2r.r-1wbh5a2.r-htvplk.r-1udh08x.r-1867qdf.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1 > div > div > div.css-175oi2r.r-1ny4l3l.r-6koalj.r-16y2uox.r-kemksi.r-1wbh5a2 > div.css-175oi2r.r-16y2uox.r-1wbh5a2.r-f8sm7e.r-13qz1uu.r-1ye8kvj > div.css-175oi2r.r-1f0wa7y > div > div > div > div > button")
            login_btn.click()

            # Enter message
            post_btn = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#react-root > div > div > div.css-175oi2r.r-1f2l425.r-13qz1uu.r-417010.r-18u37iz > header > div > div > div > div:nth-child(1) > div.css-175oi2r.r-l00any.r-e7q0ms.r-1awozwy > a > div'))).click()
            message = f"Hey ___, my internet speed {self.speed_test_result[0]}down/{self.speed_test_result[1]}up when I pay for {self.down}down/{self.up}up. Here you can see speed test results {self.speed_test_result[2]}"
            message_box = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div').send_keys(message)
