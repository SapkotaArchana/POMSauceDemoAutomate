from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

username_field = driver.find_element(By.ID, "user-name")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")
element_double_click = driver.find_element(By.XPATH, "//h4[normalize-space()='Password for all users:']")


username_field.send_keys("standard_user")

username_field.send_keys(Keys.TAB)

# password_field.send_keys("secret_sauce")
password_field.send_keys("secret_sauce12345")

# Use backspace to remove the extra characters
for _ in range(5):
    password_field.send_keys(Keys.BACKSPACE)
time.sleep(2)

# right click
actions = ActionChains(driver)
# actions.context_click(login_button).perform()
actions.click(username_field).key_down(Keys.CONTROL).send_keys('a').send_keys('c').key_up(Keys.CONTROL).perform()

time.sleep(2)


# double-click
# actions.double_click(element_double_click).perform()
actions.click(password_field).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()


time.sleep(3)

driver.quit()
