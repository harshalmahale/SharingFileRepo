from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# import time

serv_obj = Service("D:/Python Practice/SeleniumProject/recources/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

url = "https://testautomationpractice.blogspot.com/"
driver.get(url)
driver.maximize_window()

table_rows = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
print(table_rows)
table_column = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))
print(table_column)
driver.close()