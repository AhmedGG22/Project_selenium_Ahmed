import time

from selenium.common.exceptions import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
#driver.implicitly_wait(20)--- mecanizme d'attend dynamique(attend les elements  pour afficher de   20 seconde d'attend maximuim)
MyWait=WebDriverWait(driver,20,poll_frequency=2,ignored_exceptions=2[NoSuchElementException])#--mecanizme d'attend dynamique specifique(attend l'element   specifier 20 seconde  pour  afficher )
driver.get("https://www.google.ca")
#time.sleep(4)
#driver.find_element(By.XPATH,'//input[@name="q"]').send_keys("selenium")
searchgoogle=MyWait.until(EC.presence_of_element_located((By.NAME,"q")))
#searchgoogle = driver.find_element(By.NAME,"q")
searchgoogle.send_keys("selenium")
searchgoogle.submit()
#time.sleep(2)
#resultlink=driver.find_element(By.XPATH,'//h3[text()="Selenium"]')
resultlink=MyWait.until(EC.presence_of_element_located((By.XPATH,'//h3[text()="Selenium"]')))
resultlink.click()
#time.sleep(3)



#time.sleep(2)
driver.close()
