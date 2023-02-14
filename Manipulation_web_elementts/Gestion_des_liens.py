# selenium 4
#import selenium
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
list_link=driver.find_elements(By.TAG_NAME,"a")
print( "le nombre de lien sur le page est:",len(list_link))
time.sleep(4)
for link in list_link:
    print(link.text)
    print(link.get_attribute("href"))

driver.close()