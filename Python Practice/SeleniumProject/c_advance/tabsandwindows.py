from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
# import time

import os
serv_obj = Service("D:/Python Practice/SeleniumProject/recources/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# url = "https://demo.nopcommerce.com/"
# driver.get(url)
driver.maximize_window()

# Open another link from one site
# regilink = Keys.CONTROL + Keys.RETURN
# driver.find_element(By.LINK_TEXT,"Register").send_keys(regilink)

# Switch to new tab

driver.get("https://www.amazon.in/")
driver.switch_to.new_window("window")
# driver.switch_to.new_window("tab")
driver.get("https://www.flipkart.com/")

