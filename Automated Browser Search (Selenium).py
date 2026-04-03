from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()

try:
    driver.get("https://www.google.com")
    # Find the search box element
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Python Automation Projects")
    search_box.send_keys(Keys.RETURN)
    
    time.sleep(5) # Let the results load
    print("Page Title:", driver.title)
finally:
    driver.quit()