
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.orangehrm.com/")
time.sleep(3)
driver.get("https://www.google.ca/")
time.sleep(4)
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.refresh()
driver.back()
driver.close()