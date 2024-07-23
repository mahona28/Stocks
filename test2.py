from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://live.euronext.com/nb/markets/oslo/equities/euronext/list")
driver.implicitly_wait(10)
time.sleep(5)
button = driver.find_element(By.CSS_SELECTOR,'a[data-dt-idx="1"]')
try:
    button.click()
except:
    print("Error")
time.sleep(5)
driver.quit()