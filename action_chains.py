from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.maximize_window()
# driver.implicitly_wait(5)
btn = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]")
btn.click()

try:
    prompt = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "prompt"))
    )
    lang = driver.find_element(By.ID,"langSelect-EN")
    lang.click()

    driver.implicitly_wait(10)
    # time.sleep(50)
    cookie = driver.find_element(By.ID, "bigCookie")
    cookie_count = driver.find_element(By.ID, "cookies")
    items = [driver.find_element(By.ID, "productPrice"+ str(i)) for i in range(1,-1,-1)]

    actions = ActionChains(driver)

    for i in range(5000):
        actions.click(cookie)
        actions.perform()
        count = int(cookie_count.text.split(" ")[0])
        
        for item in items:
            value = int(item.text)
            if value <= count:
                upgrade_actions = ActionChains(driver)
                upgrade_actions.move_to_element(item)
                upgrade_actions.click()
                upgrade_actions.perform()
finally:
    driver.quit()