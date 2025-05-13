import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

eng_lang = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#langSelect-EN"))).click()
cookie = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#bigCookie")))


timeout = time.time()+5
end = time.time()+5*60


def upgrade():
    try:
        unlocked_upgrade = driver.find_elements(By.CSS_SELECTOR, value=".product.unlocked.enabled")
        unlocked_upgrade[-1].click()
    except IndexError:
        print("there are no updates")


def get_cps():
    cps = driver.find_element(By.CSS_SELECTOR, value="#cookies")
    print(cps.text)


while True:
    cookie.click()

    if time.time() > timeout:
        upgrade()
        timeout = time.time() + 5

    if time.time() > end:
        get_cps()
        driver.quit()
        break