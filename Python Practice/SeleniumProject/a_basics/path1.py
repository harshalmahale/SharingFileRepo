import time

from selenium import webdriver

driver = webdriver.Chrome("../recources/chromedriver.exe")
# driver = webdriver
url = "https://www.google.co.in/"
driver.get(url)
driver.implicitly_wait(2)
driver.maximize_window()
fullpath = driver.find_element(by='xpath',value='/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[1]/a')
fullpath.click()

# time.sleep(2)
driver.back()
# time.sleep(2)
relative = driver.find_element(by='xpath',value = '//*[@id="gb"]/div/div[1]/div/div[2]/a')
relative.click()
# time.sleep(2)
