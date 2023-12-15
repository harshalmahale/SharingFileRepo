from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
import time

serv_obj = Service("D:/Python Practice/SeleniumProject/recources/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

url = "https://www.selenium.dev/selenium/docs/api/java/index.html?index-all.html"
driver.get(url)
driver.maximize_window()

driver.switch_to.frame("packageListFrame")
driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")
driver.find_element(By.LINK_TEXT, "WebDriver").click()
driver.switch_to.default_content()

driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH,"/html/body/header/nav/div[1]/div[1]/ul/li[8]/a").click()

driver.close()

