from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("D:/Python Practice/SeleniumProject/recources/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(5)

url = "http://cookbook.seleniumacademy.com/Config.html"
driver.get(url)

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@value,'Features')]")
print(len(checkboxes))
driver.close()