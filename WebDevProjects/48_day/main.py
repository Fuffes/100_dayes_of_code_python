from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

titles = driver.find_elements(By.CSS_SELECTOR, value="div.event-widget li a")
times = driver.find_elements(By.CSS_SELECTOR, "div.event-widget li time")


result = {}
for index in range(len(titles)):
    result[str(index)] = {
        "time": times[index].get_attribute("datetime"),
        "name": titles[index].text
    }

print(result)
driver.close()