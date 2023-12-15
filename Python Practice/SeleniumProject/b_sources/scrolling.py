from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# import time

serv_obj = Service("D:/Python Practice/SeleniumProject/recources/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

url = "https://www.countries-ofthe-world.com/flags-of-the-world.html"
driver.get(url)
driver.maximize_window()

flag = driver.find_element(By.XPATH,"//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[2]")
driver.execute_script("arguments[0].scrollIntoView();",flag)
value = driver.execute_script("return window.pageOffset;")
print("Numbers of pixel moved:", value)