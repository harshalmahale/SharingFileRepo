import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# import time

serv_obj = Service("D:/Python Practice/SeleniumProject/recources/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

url = "https://opensource-demo.orangehrmlive.com"
driver.get(url)
driver.maximize_window()

#login

driver.find_element(By.ID, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()
time.sleep(3)

#Admin-->user management -->users

admin=driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a")
usermagn=driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span")
user=driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li/a")


# mousehover

act = ActionChains(driver)

act.move_to_element(admin).move_to_element(usermagn).move_to_element(user).click().perform()