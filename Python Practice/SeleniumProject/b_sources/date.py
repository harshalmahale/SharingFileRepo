from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
import time

serv_obj = Service("D:/Python Practice/SeleniumProject/recources/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

url = "https://jqueryui.com/datepicker/"
driver.get(url)
driver.maximize_window()

driver.switch_to.frame(0)

# driver.find_element(By.XPATH, "//*[@id='datepicker']").send_keys("11/20/2022")

year = "2020"
month= "December"
date = "15"
driver.find_element(By.XPATH, "//*[@id='datepicker']").click()

while True:
    mon=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if mon==month and yr==year:
        break;
    else:
        # driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[2]/span").click()  #Next arrow
        driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[1]/span").click()  #Previous arrow


# Select Dates

dates=driver.find_elements(By.XPATH,"//*[@id='ui-datepicker-div']/table/tbody/tr/td/a")

for ele in dates:
    if ele.text==date:
        ele.click()
        break
