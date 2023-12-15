from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# import time

serv_obj = Service("D:/Python Practice/SeleniumProject/recources/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

url = "https://text-compare.com/"
driver.get(url)
driver.maximize_window()

input1=driver.find_element(By.XPATH,"//*[@id='inputText1']").send_keys("Welcome Harshal")
input2=driver.find_element(By.XPATH,"//*[@id='inputText2']")

act = ActionChains(driver)
act.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
act.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
act.send_keys(Keys.TAB).perform()
act.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

