from selenium import webdriver
# from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# import time
import os

location = os.getcwd()

def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("D:/Python Practice/SeleniumProject/recources/chromedriver.exe")

    #download files in desired location
    preference = {"download.default_directory":location,"plugins.always_open_pdf_externally":True}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preference)
    driver = webdriver.Chrome(service=serv_obj,options=ops)
    return driver

driver = chrome_setup()

url = "https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/"
driver.get(url)
driver.maximize_window()

driver.find_element(By.XPATH,"//*[@id='table-files']/tbody/tr[1]/td[5]/a").click()
