from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
# import time
import os
serv_obj = Service("D:/Python Practice/SeleniumProject/recources/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

url = "https://www.jaguar.in/index.html"
driver.get(url)
driver.maximize_window()

# driver.save_screenshot("D:/Python Practice/SeleniumProject/c_advance/homepage.png")
driver.save_screenshot(os.getcwd()+ "//homepage1.png")