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

#driver.get("https://db-comp.eu/")
years = [1990, 2011]
for year in years:

    driver.get("https://db-comp.eu/?slotName=Slot_Main_3&Search_by_value=details&Document_type_values=1&Month_from_value=1&Year_from_value={year}&Month_to_value=1&Year_to_value=2022&Mysql_operator_value=none&Sort_results_value=relevance&page=1")
    
    # TODO: extraer numero de paginas
    num_pags = funcion_que_te_extrae_num_pags()

    for n_pag in num_pags:
        driver.get(f"https://db-comp.eu/?slotName=Slot_Main_3&Search_by_value=details&Document_type_values=1&Month_from_value=1&Year_from_value={year}&Month_to_value=1&Year_to_value=2022&Mysql_operator_value=none&Sort_results_value=relevance&page={n_pag}")

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

        def scrape_links(driver, delay, xpath_results="//div[@id='plgslt_Slot_Main_3_results']//a[@href]", attribute_str="href"):            
            lst = []
            try:
                elems = driver.find_elements(By.XPATH, xpath_results)
                print("Page is ready!")
                for elem in elems:
                    print(elem.get_attribute(attribute_str))
                    if elem.get_attribute(attribute_str) != None:
                        lst.append(elem.get_attribute(attribute_str))
            except TimeoutException:
                print("Loading took too much time!")

            return lst[:len(lst)-2]
