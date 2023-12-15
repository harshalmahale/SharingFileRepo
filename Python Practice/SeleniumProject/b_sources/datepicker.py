from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

serv_obj = Service("D:/Python Practice/SeleniumProject/recources/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

url = "https://www.dummyticket.com/dummy-ticket-for-visa-application/"
driver.get(url)
driver.maximize_window()

driver.find_element(By.XPATH, "//*[@id='dob']").click() #opens datepicker
# time.sleep(3)

datepicker_month=Select(driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div[1]/div/select[1]"))
datepicker_month.select_by_visible_text("Aug")


time.sleep(3)

datepicker_year=Select(driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div[1]/div/select[2]"))
datepicker_year.select_by_visible_text("1999")

time.sleep(3)

dates = driver.find_elements(By.XPATH,"//*[@id='ui-datepicker-div']//table/tbody/tr/td/a")
time.sleep(3)
for ele in dates:
    if ele.text=="25":
        ele.click()
        break
