import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# import time

serv_obj = Service("D:/Python Practice/SeleniumProject/recources/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

url = "https://swisnl.github.io/jQuery-contextMenu/demo.html"
driver.get(url)
driver.maximize_window()

button = driver.find_element(By.XPATH,"/html/body/div/section/div/div/div/p/span")
act = ActionChains(driver)
act.context_click(button).perform()