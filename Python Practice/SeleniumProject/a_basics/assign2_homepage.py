from selenium import webdriver
import time
driver = webdriver.Chrome("../recources/chromedriver.exe")
url = "https://www.google.com/"
driver.get(url)
time.sleep(2)
print(element1)