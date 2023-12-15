from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# import time

serv_obj = Service("D:/Python Practice/SeleniumProject/recources/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver.get(url)
driver.maximize_window()

# windowid = driver.current_window_handle
# print(windowid)

driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
# windowIDS = driver.window_handles
#
# parentwindowid = windowIDS[0]
# childwindowid =  windowIDS[1]
#
# print(parentwindowid,childwindowid)
#
# driver.close()
#
#
# driver.close()
