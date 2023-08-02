from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://automationintesting.com/selenium/testpage/")
print(driver.title)


search = driver.find_element(By.ID, 'firstname')
search.send_keys('Atif')

page = driver.page_source

print(page)
time.sleep(5)
driver.quit()