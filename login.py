from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
time.sleep(1)

user = driver.find_element(By.ID, 'username')
user.send_keys("rahulshettyacademy")
time.sleep(1)

password = driver.find_element(By.ID, 'password')
password.send_keys("learning")

btn = driver.find_element(By.ID, 'signInBtn')
btn.click()

try:
    new_page = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "ProtoCommerce Home"))
    )

    items = driver.find_elements(By.CLASS_NAME,"card-title")
    for item in items:
        print(item.text)
finally:
    driver.quit()

time.sleep(3)
driver.quit()
