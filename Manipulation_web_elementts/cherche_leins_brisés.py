# selenium 4
#import selenium
import time
import requests
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
list_link=driver.find_elements(By.TAG_NAME,"a")
compteur=0
for link in list_link:
    URL=link.get_attribute("href")
    try:
        response=requests.head(URL)
    except:
        None

    if response.status_code>=400:
        print(URL,"est un lien brisé")
        compteur=compteur+1
    else:
        print(URL,"est un lien valide ")

        print("le nombre de lien brisé est :",compteur)






time.sleep(2)
driver.close()