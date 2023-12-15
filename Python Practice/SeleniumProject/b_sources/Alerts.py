from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
import time

serv_obj = Service("D:/Python Practice/SeleniumProject/recources/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

url = "https://the-internet.herokuapp.com/javascript_alerts"
driver.get(url)
driver.maximize_window()

driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[3]/button").click()
time.sleep(5)

alertwindow = driver.switch_to.alert
print(alertwindow.text)
time.sleep(5)
alertwindow.send_keys("Welcome")
time.sleep(3)
alertwindow.accept()
# driver.close()

