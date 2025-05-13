from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# driver.maximize_window()
#
# # num = driver.find_element(By.CSS_SELECTOR, value="#articlecount li a")
# # num.click()
#
# all_portals = driver.find_element(By.LINK_TEXT, value="Wiktionary")
# # all_portals.click()
#
# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python",Keys.ENTER)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")
driver.maximize_window()

first_name = driver.find_element(By.CSS_SELECTOR, value='input[name="fName"]')
last_name = driver.find_element(By.CSS_SELECTOR, value='input[name="lName"]')
email = driver.find_element(By.CSS_SELECTOR, value='input[name="email"]')
sign_up = driver.find_element(By.CSS_SELECTOR, value='button[type="submit"]')

first_name.send_keys("First Name")
last_name.send_keys("Last Name")
email.send_keys("Address@gmail.com")
sign_up.click()


# driver.quit()