from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


URL="https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

driver.get(URL)
sign_in_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.sign-in-modal button")))

sign_in_btn.click()

email_in = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="session_key"]')))
password_in = driver.find_element(By.CSS_SELECTOR, 'input[name="session_password"]')
password_in.get_attribute()

email_in.send_keys("projectpyaddress@gmail.com")
password_in.send_keys("123321Nata")

submit_btn = driver.find_element(By.CSS_SELECTOR, value='div.sign-in-modal__screen button[type="submit"]').click()
