from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# import time

serv_obj = Service("D:/Python Practice/SeleniumProject/recources/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

url = "https://swisnl.github.io/jQuery-contextMenu/demo.html"
driver.get(url)
driver.maximize_window()
