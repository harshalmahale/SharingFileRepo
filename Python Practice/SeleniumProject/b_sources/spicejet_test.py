from selenium import webdriver
driver = webdriver.Chrome("../recources/chromedriver.exe")
url = "https://www.spicejet.com/"
driver.get(url)
