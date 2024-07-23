import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


driver = webdriver.Chrome()

driver.get("https://live.euronext.com/nb/markets/oslo/equities/list")
stocks = ""
driver.implicitly_wait(10)
def scrape_page():
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    table = soup.find_all('td', class_="stocks-symbol")
    symbols = ""
    for symbol in table:
        symbols += symbol.text + '\n'
    return symbols
time.sleep(2)
num = 0
# Iterate through pages
while num < 4:
    try:
        # Find the "next page" button and click it
        next_button = driver.find_element(By.XPATH, '//a[@data-dt-idx="' + str(num) + '"]')
        driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
        next_button.click()
        
        # Wait for the next page to load
        time.sleep(1) 
        
        # Scrape the new page
        stocks +=  scrape_page()
        num += 1
    except:
        print(f"Error + {num}")
        break
f = open("stocks.txt", "w")
f.write(stocks)
f.close()
# Close the WebDriver
driver.quit()
