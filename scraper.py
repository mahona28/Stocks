import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


driver = webdriver.Chrome()

driver.get("https://live.euronext.com/nb/markets/oslo/equities/euronext/list")
stocks = ""
driver.implicitly_wait(10)
def scrape_page():
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    table = soup.find_all('td', class_="stocks-symbol")
    mystring = str(table)
    mystring = mystring.replace('<td class="stocks-symbol">', "")
    mystring = mystring.replace('</td>', "\n")
    mystring = mystring.replace(', ', "")
    mystring = mystring[1:-2]
    print("\n" + mystring)
    return mystring

# Scrape the first page
stocks += scrape_page()

# Iterate through pages
while True:
    try:
        # Find the "next page" button and click it
        next_button = driver.find_element(By.XPATH, '//a[@data-dt-idx="1"]')
        driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
        next_button.click()

        # Wait for the next page to load
        time.sleep(2) 
        
        # Scrape the new page
        stocks += scrape_page()
                # Find the "next page" button and click it
        next_button = driver.find_element(By.XPATH, '//a[@data-dt-idx="2"]')
        driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
        next_button.click()

        # Wait for the next page to load
        time.sleep(2)
        
        # Scrape the new page
        stocks += scrape_page()
        f = open("stocks.txt", "w")
        f.write(stocks)
        f.close()
        break
    except Exception as e:
        print(f"Error: {e}")
        break

# Close the WebDriver
driver.quit()
