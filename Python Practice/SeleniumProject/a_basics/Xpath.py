import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("D:/Python Practice/SeleniumProject/recources/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(5)

driver.get("https://www.google.co.in/")
driver.maximize_window()
# time.sleep(2)

#Absolute path
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/a").click()
# time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys("cars")
# time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/button").click()

# time.sleep(5)
#Relative Path
driver.back()
# time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys("Iphone")
# time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/button").click()
# time.sleep(2)
