from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
# import time

import os
serv_obj = Service("D:/Python Practice/SeleniumProject/recources/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

url = "https://fireworks.com/"
driver.get(url)
driver.maximize_window()

cookies = driver.get_cookies()
print("size of cookies ",len(cookies))

for c in cookies:
    print(c)


# add cookie to browser

driver.add_cookie({"name": "Mycookie", "value" : "123456"})
cookies = driver.get_cookies()
print("size of cookies ",len(cookies))

# Delete specific cookie from browser

driver.delete_cookie("Mycookie")
cookies = driver.get_cookies()
print("size of cookies ",len(cookies))

# delete all cookie
driver.delete_all_cookies()
cookies = driver.get_cookies()
print("size of cookies ",len(cookies))


