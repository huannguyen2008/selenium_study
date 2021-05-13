import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
WEBDRIVER = 'chromedriver'
path = os.path.join(ROOT_DIR, WEBDRIVER)

driver = webdriver.Chrome(path)

driver.get("https://www.facebook.com/")
print(driver.title)

try:
    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'email'))
    )
    username.send_keys('0338386275')
    pw = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'pass'))
    )
    pw.send_keys('')
    username.send_keys(Keys.RETURN)
except Exception as e:
    print(e)
    time.sleep(5)
    driver.quit()
