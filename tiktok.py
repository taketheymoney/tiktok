import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

#THIS INITIALIZES THE DRIVER (AKA THE WEB BROWSER)
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)


link = ("https://www.tiktok.com/@gordonramsayo...")

driver.get("" + link)
time.sleep(2)

Followers = driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[2]/div[2]/div/div[1]/h2[1]/div[2]/strong').text
Following = driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[2]/div[2]/div/div[1]/h2[1]/div[1]/strong').text
Likes = driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[2]/div[2]/div/div[1]/h2[1]/div[3]/strong').text


print(Followers)
print(Following)
print(Likes)
