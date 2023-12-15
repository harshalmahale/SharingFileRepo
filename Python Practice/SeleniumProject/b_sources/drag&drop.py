
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# import time

serv_obj = Service("D:/Python Practice/SeleniumProject/recources/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

url = "http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html"
driver.get(url)
driver.maximize_window()

source_ele = driver.find_element(By.XPATH,"//*[@id='box6']")
target_ele = driver.find_element(By.XPATH,"//*[@id='box106']")

act = ActionChains(driver)
act.drag_and_drop(source_ele,target_ele).perform()