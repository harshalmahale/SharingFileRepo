from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
# import time

serv_obj = Service("D:/Python Practice/SeleniumProject/recources/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

url = "https://www.dummyticket.com/dummy-ticket-for-visa-application/"
driver.get(url)
driver.maximize_window()

driver.find_element(By.XPATH,"//*[@id='select2-billing_country-container']").click()
countrieslist = driver.find_elements(By.XPATH,"//*[@id='select2-billing_country-results']/li")
print(len(countrieslist))

for list in countrieslist:
    if list.text=="India":
        list.click()
        break
