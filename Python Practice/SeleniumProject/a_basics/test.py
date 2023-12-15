from selenium import webdriver
# import time

driver = webdriver.Chrome("../recources/chromedriver.exe")
url = "http://cookbook.seleniumacademy.com/Config.html"
driver.get(url)
driver.find_element(by= 'xpath', value= 'html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Bcci")
driver.find_element(by= 'xpath', value= 'html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').submit()

