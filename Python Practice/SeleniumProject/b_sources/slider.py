from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# import time

serv_obj = Service("D:/Python Practice/SeleniumProject/recources/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

url = "https://www.jqueryscript.net/demo/touch-progressive-enhancement-range-slider/"
driver.get(url)
driver.maximize_window()

start=driver.find_element(By.XPATH,"//*[@id='demo']/div/span")
print("location of slider")
print(start.location)

act = ActionChains(driver)
act.drag_and_drop_by_offset(start,200,0).perform()