import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://bdeb.omnivox.ca")
time.sleep(2)
driver.find_element(By.NAME,"Identifiant").send_keys("6202085")
time.sleep(2)
driver.find_element(By.NAME,"Password").send_keys("Ep00330801")
time.sleep(2)
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
time.sleep(2)
