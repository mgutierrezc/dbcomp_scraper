from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
import requests
import re
import pprint as pp
import urllib
import time

chromeOptions = webdriver.ChromeOptions()

# chromeOptions.add_experimental_option("prefs",{"download.default_directory":"H:\\Mi unidad\\Prueba"})

path_1 = "D:\Descargas\chromedriver_win32 (2)\chromedriver.exe"
driver = webdriver.Chrome(path_1)

driver.get("https://db-comp.eu/")

#Cerrar la wea de cookies
driver.find_element(By.CLASS_NAME, "zenario_cc_accept").click()

#Darle click a agreement
driver.find_element(By.ID, "1").click()

#Introducir la fecha

##### Mes de Inicio
start_month = driver.find_element(By.ID, "plgslt_Slot_Main_3_month_from")
start_month.click()
start_month.send_keys(Keys.ARROW_DOWN)

##### Año de Inicio
start_year = driver.find_element(By.ID, "plgslt_Slot_Main_3_year_from")
start_year.click()
start_year.send_keys(Keys.ARROW_DOWN)
start_year.send_keys(Keys.ARROW_DOWN)
start_year.send_keys(Keys.ARROW_DOWN)
start_year.send_keys(Keys.ARROW_DOWN)
start_year.send_keys(Keys.ARROW_DOWN)
start_year.send_keys(Keys.ARROW_DOWN)

#### Mes de fin
finish_month = driver.find_element(By.ID, "plgslt_Slot_Main_3_month_to")
finish_month.click()
finish_month.send_keys(Keys.ARROW_DOWN)

#### Año de fin
finish_year = driver.find_element(By.ID, "plgslt_Slot_Main_3_year_to")
finish_year.click()
finish_year.send_keys(Keys.ARROW_DOWN)


#Darle click a search
driver.find_element(By.ID, "plgslt_Slot_Main_3_search").click()
time.sleep(1)
# Dar click a una decisión, descargar, entrar a la otra pestaña, descargar, cerrar la pestaña, continuar con la que sigue, 

# lnks = driver.find_elements(By.CSS_SELECTOR, '#plgslt_Slot_Main_3_results')
#elems = driver.find_elements(By.TAG_NAME, 'a')
page_source = driver.page_source
with open("gaaaa.txt", "w+") as file:
    file.write(page_source)

# body = driver.find_element(By.TAG_NAME, "body").text
# time.sleep(5)
delay = 5
try:
    #myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//div[@id='plgslt_Slot_Main_3_results']//a[@href]")))
    elems = driver.find_elements(By.XPATH, "//div[@id='plgslt_Slot_Main_3_results']//a[@href]")
    print("Page is ready!")
    for elem in elems:
        print(elem.get_attribute("href"))
except TimeoutException:
    print("Loading took too much time!")

# soup = BeautifulSoup(page_source, 'html.parser')
# divs = soup.find_all("result")
# for div in divs:
#     print("div: ", div)

# links = []
# links_selector = soup.find_all('div', class_='result')
# print("links_selector: ", links_selector)


# elems = driver.find_elements_by_xpath("//a[@href]")
# for link in elems:
#     print("link: ", link.get_attribute("href"))


# print("link: ", lnks[0])
# print("link: ", len(lnks))

# for lnk in lnks:
#     print("link with href: ", lnk.get_attribute("href"))

# Descargar las decisiones en una carpeta

# Cuando no hayan más decisiones, darle a siguiente página
# driver.close()