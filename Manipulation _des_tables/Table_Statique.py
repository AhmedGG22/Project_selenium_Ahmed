
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(4)
nombre_Lignes=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr")
print(len(nombre_Lignes))
nombre_colonnes=driver.find_elements(By.XPATH,"//table[@name='BookTable']//th")
print(len(nombre_colonnes))
#recuperer la valeur d'une cellule de la table
valeur_cellule=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[3]/td[1]")
print(valeur_cellule.text)
#recuperer toutes les donneés du tableau
nb_lignes=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
nb_colonnes=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//th"))
valeur_head=driver.find_element(By.XPATH,"//table[@name='BookTable']//th")
for i in range(1,len(valeur_head+1)):
    data_head = driver.find_element(By.XPATH, "//table[@name='BookTable']//th[" + str(i) + "]").text
    print(data_head)
time.sleep(2)
for r in range(2,nb_lignes+1):
    for c in range(1,nb_colonnes+1):
        time.sleep(2)
        val_cel=val_cell=driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]/td["+str(c)+"]").text
        print(val_cel,end='           ')
print()
time.sleep(2)

for r in range (2,nb_lignes+1):
    auteur=driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]/td[2]").text
    if auteur=='Amit':
        prix=driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]/td[4]").text
        nom_livre=driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]/td[1]").text
        print(auteur,"******",nom_livre, "*******", prix)

driver.close()

